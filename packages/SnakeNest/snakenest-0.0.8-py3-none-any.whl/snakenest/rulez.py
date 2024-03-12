from re import findall
import yaml
from os.path import exists
from yaml import full_load as load_yaml_file


# https://matthewpburruss.com/post/yaml/
# https://pyyaml.org/wiki/PyYAMLDocumentation
class Rulez:
    def __init__(self, file_):
        self.__prop = {}
        self.__rulez = {}
        if exists(file_):
            with open(file_) as f:
                self.__rulez = load_yaml_file(f)

    def __get(self, val, name):
        _max = len(val)
        obj = self.__rulez
        for i in range(_max):
            if val[i] in obj:
                if i == _max - 1:
                    a = obj[val[i]]
                    self.__prop[name] = a
                    return a
                else:
                    obj = obj[val[i]]
        return ''

    def get(self, item, default=None):
        search = item
        matches = findall('\\${(.*?)}', item)
        if len(matches) > 0:
            search = matches[0]

        if search in self.__prop:
            return self.__prop[search]

        val = search.split('.')
        value = self.__get(val, search)
        if value != '':
            return value

        return default
