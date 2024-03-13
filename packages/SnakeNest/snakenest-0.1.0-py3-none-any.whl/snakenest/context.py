import inspect, types
from .configuration import Configuration


class SnakeParameters:
    def __init__(self, **kwargs):
        self.__name = kwargs.get("name", None)
        self.__args = kwargs.get("args", None)
        self.__condition = kwargs.get("condition", None)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if self.__name is None:
            self.__name = name

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args):
        self.__args = args

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition):
        self.__condition = condition


class Context:
    nest = None

    def __init__(self):
        Context.__init()

    @staticmethod
    def __init():
        if Context.nest is None:
            Context.nest = {'byQualifier': {}, 'byType': {}, 'definitions': {}}

    @staticmethod
    def __register_by_name(name, inst):
        Context.nest['byQualifier'][name] = inst

    @staticmethod
    def __register_by_type(inst):
        type_list = inspect.getmro(type(inst))
        for type_name in type_list:
            if type_name is type(object()):
                continue

            if Context.nest['byType'].get(type_name, None) is None:
                Context.nest['byType'][type_name] = []

            Context.nest['byType'][type_name].append(inst)

    @staticmethod
    def __get_class_by_name(name):
        return Context.nest['byQualifier'].get(name, None)

    @staticmethod
    def __get_class_by_type(the_type):
        return Context.nest['byType'].get(the_type, None)

    @staticmethod
    def __create_from_class(snake_class, snake_args):
        tmp_args = []
        args_spec = inspect.getfullargspec(snake_class.__init__)[0]
        for i in range(len(args_spec)):
            if args_spec[i] == "self" or args_spec[i] == "cls":
                continue

            if snake_args.get(args_spec[i]) is not None:
                tmp_args.append(snake_args.get(args_spec[i]))
            else:
                tmp_args.append(None)

        return snake_class(*tmp_args)

    def __create_from_name(self, snake_name, snake_obj):
        snake_class = snake_obj[0]
        snake_args = snake_obj[1].args

        # update value from config
        if snake_args:
            for name, value in snake_args.items():
                snake_args[name] = Configuration.rulez.get(value, value)

        if type(snake_class) is not types.FunctionType:
            inst = self.__create_from_class(snake_class, snake_args)
            self.__register_by_name(snake_name, inst)
            self.__register_by_type(inst)

    def __initialize_snakes(self):
        for snake_name, snake_value in Context.nest['definitions'].items():
            self.__create_from_name(snake_name, snake_value)

    @staticmethod
    def clear():
        if Context.nest is not None:
            Context.nest.clear()
            del Context.nest
            Context.nest = None
            Context.__init()

    @staticmethod
    def add_definition(bean_definition, parameters: SnakeParameters):
        if not parameters.condition:
            Context.nest['definitions'][parameters.name] = (bean_definition, parameters)
            return

        if Configuration.rulez.get(parameters.condition['key']) == parameters.condition['value']:
            Context.nest['definitions'][parameters.name] = (bean_definition, parameters)

    def bite(self, name, the_type):
        inst = self.__get_class_by_name(name)
        if inst is not None:
            return inst
        else:
            inst_array = self.__get_class_by_type(the_type)
            if inst_array is not None and len(inst_array) > 1:
                raise Exception(f'too many instances of {str(the_type)}')

            elif inst_array is not None:
                inst = inst_array[0]
            if inst is None and Context.nest['definitions'].get(name, None) is not None:
                return self.__create_from_name(name, Context.nest['definitions'].get(name))
            else:
                return inst

    def initialize(self):
        self.__initialize_snakes()


SnakeConfiguration = Configuration()
SnakeNest = Context()
