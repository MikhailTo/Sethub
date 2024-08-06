from functools import singledispatch
import inspect

class Debug:

    @singledispatch
    @staticmethod
    def print(arg):
        raise NotImplementedError("Не реализовано")

    @staticmethod
    @print.register
    def _(arg: dict):
        for key, value in arg.items():
            print(f"{key}: {value}")

    @staticmethod
    @print.register
    def _(arg: tuple):
        for value in arg:
            print(value)
    @classmethod
    def print_args_class(self, title, obj):
        print(title)
        for key, value in obj.__dict__.items():
            print(f"{key}: {value}")
    @classmethod
    def print_methods_class(self, title, obj):
        print(title)
        # Получаем список методов и атрибутов класса
        methods = [name for name in dir(obj) if callable(getattr(obj, name))]

        # Печатаем информацию о каждом методе
        for method_name in methods:
            method = getattr(obj, method_name)
            signature = inspect.signature(method)
            print(f"Метод: {method_name}")
            print(f"Аргументы: {signature}")
            print()

# # Example for dict:
# db_settings = {
#     "DB_USER": "user",
#     "DB_PASSWORD": "password",
#     "DB_HOST": "host",
#     "DB_PORT": "port",
#     "DB_NAME": "name"
# }
# Debug.print(db_settings)

# # Example for tuple:
# db_settings = ("user", "password", "host", "port", "name")
# Debug.print(db_settings)