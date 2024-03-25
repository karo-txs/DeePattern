from re import finditer
import importlib
import inspect
import pkgutil


def camel_case_split(identifier):
    matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return "_".join([m.group(0) for m in matches])


def load_classes_in_package(package, endswith):
    class_map = {}
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
        module = importlib.import_module(modname)
        for name, obj in inspect.getmembers(module):

            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                if name.endswith(endswith):
                    simple_name = camel_case_split(name.replace(endswith, "")).lower()
                    class_map[simple_name] = obj
    return class_map


def get_class(class_map: dict, selected_class_name: str, *args) -> any:
    selected_class = class_map[selected_class_name]
    return selected_class(args)
