from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__                                                # Tип объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))] # Атрибуты объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]  # Методы объекта
    module = obj.__class__.__module__                                            # принадлежномть объекта
    info = {                                                                     # Создание словаря с информацией об объекте
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }
    return info


# Интроспекция числа.
number_info = introspection_info(42)
pprint(number_info)

# Интроспекция функции.
func_info = introspection_info(introspection_info)
pprint(func_info)
