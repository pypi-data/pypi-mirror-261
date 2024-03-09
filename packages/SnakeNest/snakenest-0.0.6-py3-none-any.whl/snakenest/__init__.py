import inspect
from .context import SnakeNest


class Snake:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.init_args = kwargs.get("args", None)

    def __call__(self, class_definition):
        name = self.name if self.name != "" else class_definition.__name__
        class_definition.__snake_name__ = name

        SnakeNest.add_definition(class_definition, self.init_args)
        return class_definition

    @classmethod
    def to_define_name(cls, class_definition, **kwargs):
        init_args = kwargs.get("args", None)
        name = kwargs.get("name", "")
        name = name if name is not None else class_definition.__name__

        def get_instance():
            return class_definition

        get_instance.__snake_name__ = name

        SnakeNest.add_definition(get_instance, init_args)


class Poisoned:

    def __init__(self, **kwargs):
        self.config = kwargs

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
                if self.config.get(arg) is not None:
                    bean = SnakeNest.bite(self.config.get(arg), annotations.get(arg))
                else:
                    bean = SnakeNest.bite(arg, annotations.get(arg))

                if len(args) > i and args[i] is not None:
                    real_args.append(args[i])
                else:
                    real_args.append(bean)
            return snake_method(*real_args, **kwargs)

        return serpe


__all__ = ['SnakeNest', 'Snake', 'Poisoned']
