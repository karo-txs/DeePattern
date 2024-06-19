from __future__ import annotations
import toml


class ConfigSingleton(object):

    def __init__(self, name: str = "base_conf"):
        self.name = name
    
    def load_config(self, filepath: str = None) -> ConfigSingleton:
        config_data = toml.load(filepath)
        current_section = None

        for section, entries in config_data.items():
            parts = section.split(".")
            current_section = parts[0] if len(parts) > 1 else None

            for key, value in entries.items():
                if isinstance(value, str) and value.endswith(".toml"):
                    attr_name = f"{current_section}_{key}" if current_section else key
                    subconfig_instance = ConfigSingleton(value.split("/")[-1].replace(".toml", "")).load_config(value)
                    setattr(self, attr_name, subconfig_instance)

                elif isinstance(value, list) and isinstance(value[0], str) and value[0].endswith(".toml"):
                    attr_name = f"{current_section}_{key}" if current_section else key
                    subconfig_instances = []
                    for v in value:
                        subconfig_instances.append(ConfigSingleton(v.split("/")[-1].replace(".toml", "")).load_config(v))
                    setattr(self, attr_name, subconfig_instances)

                else:
                    attr_name = f"{current_section}_{key}" if current_section else f"{section}_{key}"
                    setattr(self, attr_name, value)
        return self
    
    def create_attr(self, attr_name, value) -> ConfigSingleton:
        setattr(self, attr_name, value)
        return self

    def create_attrs_from_dict(self, dict_values) -> ConfigSingleton:
        for key in dict_values.keys():
            setattr(self, key, dict_values[key])
        return self
    
    def __repr__(self, level=0):
        indent = '  ' * level
        result = ''
        for attr, value in sorted(self.__dict__.items()):
            if isinstance(value, ConfigSingleton):
                result += f'{indent}{attr}:\n{value.__repr__(level+1)}'
            else:
                result += f'{indent}{attr}: {value}\n'
        return result

    def to_dict(self):
        return {
            name: getattr(self, name) for name in dir(self) if not name.startswith("_") \
                and name not in ["create_attr", "create_attrs_from_dict", "load_config", "to_dict"]
        }
