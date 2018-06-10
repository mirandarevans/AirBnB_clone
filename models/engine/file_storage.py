#!/usr/bin/env python3
''' contains class used to manage a JSON '''

import json
from import_classes import *
from datetime import datetime


class FileStorage():
        ''' Performs various actions with a JSON '''

        def __init__(self):
                ''' Initializes fs object '''
                self.__objects = dict()
                self.__file_path = 'file.json'

        def all(self):
                ''' Returns all objects stored in JSON '''
                return self.__objects

        def new(self, obj):
                ''' Puts new object representation into a private variable '''
                self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

        def delete(self, key):
                ''' Deletes an object from the JSON '''
                self.__objects.pop(key)
                self.save()

        def update(self, key, attribute_name, attribute_value):
                ''' Updates an object '''
                obj = self.__objects[key]
                obj.__dict__[attribute_name] = attribute_value
                obj.__dict__['updated_at'] = datetime.today()
                self.save()

        def save(self):
                ''' Saves current state of private variable holding objects
                to JSON '''
                with open(self.__file_path, 'w+') as f:
                        json.dump({key: value.to_dict() for
                                  (key, value) in self.__objects.items()}, f)

        def reload(self):
                ''' Retrieves objects from JSON '''
                try:
                        with open(self.__file_path, 'r') as f:
                                self.__objects = {key: eval('{}(**{})'.format(
                                        value['__class__'], str(value))) for
                                        (key, value) in json.load(f).items()}
                except:
                        pass