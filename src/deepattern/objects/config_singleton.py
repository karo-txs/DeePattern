from __future__ import annotations
from deepattern.patterns.singleton.singleton_meta import SingletonMeta
from deepattern.objects.logger import LoggerSingleton
import toml


class ConfigSingleton(metaclass=SingletonMeta):
    
    def load_config(self, filepath: str = None) -> ConfigSingleton:
        config_data = toml.load(filepath)
        current_section = None

        for section, entries in config_data.items():
            parts = section.split(".")
            if len(parts) > 1:
                current_section = parts[0]

            if current_section:
                for key, value in entries.items():
                    attr_name = f"{current_section}_{section}_{key}"
                    setattr(self, attr_name, value)
            else:
                for key, value in entries.items():
                    attr_name = f"{section}_{key}"
                    setattr(self, attr_name, value)
        return self
    
    def create_attr(self, attr_name, value) -> ConfigSingleton:
        setattr(self, attr_name, value)
        return self

    def to_dict(self):
        return {
            name: getattr(self, name) for name in dir(self) if not name.startswith("_")
        }
    
    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())
