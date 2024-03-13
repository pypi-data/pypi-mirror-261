import inspect
from .context import SnakeNest, SnakeConfiguration, SnakeParameters


class Snake:
    def __init__(self, **kwargs):
        self.__snake_parameters = SnakeParameters(**kwargs)

    def __call__(self, class_definition):
        self.__snake_parameters.name = class_definition.__name__
        SnakeNest.add_definition(class_definition, self.__snake_parameters)
        return class_definition


class Poisoned:

    def __init__(self, **kwargs):
        self.__config = kwargs

    def __call__(self, snake_method):
        def serpe(*args, **kwargs):
            spec = inspect.getfullargspec(snake_method)

            args_list = spec[0]
            annotations = spec[6]
            real_args = [args[0]]
            for i in range(len(args_list)):
                arg = args_list[i]
                if arg == 'self':
                    continue
                if self.__config.get(arg) is not None:
                    bean = SnakeNest.bite(self.__config.get(arg), annotations.get(arg))
                else:
                    bean = SnakeNest.bite(arg, annotations.get(arg))

                if len(args) > i and args[i] is not None:
                    real_args.append(args[i])
                else:
                    real_args.append(bean)
            return snake_method(*real_args, **kwargs)

        return serpe


__all__ = ['SnakeNest', 'SnakeConfiguration', 'Snake', 'Poisoned']
