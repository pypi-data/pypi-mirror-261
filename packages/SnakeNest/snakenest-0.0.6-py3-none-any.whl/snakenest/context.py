import inspect, types


class Nest:
    nest = None

    def __init__(self):
        Nest.__init()

    @staticmethod
    def __init():
        if Nest.nest is None:
            Nest.nest = {"byQualifier": {}, "byType": {}, "definitions": {}}

    @staticmethod
    def __register_by_name(name, inst):
        Nest.nest['byQualifier'][name] = inst

    @staticmethod
    def __register_by_type(inst):
        type_list = inspect.getmro(type(inst))
        for type_name in type_list:
            if type_name is type(object()):
                continue

            if Nest.nest['byType'].get(type_name, None) is None:
                Nest.nest['byType'][type_name] = []

            Nest.nest['byType'][type_name].append(inst)

    @staticmethod
    def __get_class_by_name(name):
        return Nest.nest['byQualifier'].get(name, None)

    @staticmethod
    def __get_class_by_type(the_type):
        return Nest.nest['byType'].get(the_type, None)

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
        snake_args = snake_obj[1]

        if type(snake_class) is not types.FunctionType:
            inst = self.__create_from_class(snake_class, snake_args)
            self.__register_by_name(snake_name, inst)
            self.__register_by_type(inst)

    def initialize(self):
        for snake_name, snake_value in Nest.nest['definitions'].items():
            self.__create_from_name(snake_name, snake_value)

    @staticmethod
    def clear():
        if Nest.nest is not None:
            Nest.nest.clear()
            del Nest.nest
            Nest.nest = None
            Nest.__init()

    @staticmethod
    def add_definition(bean_definition, args=None):
        Nest.nest['definitions'][bean_definition.__snake_name__] = (bean_definition, args)

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
            if inst is None and Nest.nest['definitions'].get(name, None) is not None:
                return self.__create_from_name(name, Nest.nest['definitions'].get(name))
            else:
                return inst


SnakeNest = Nest()
