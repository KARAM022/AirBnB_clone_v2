#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

# Sample usage:

if __name__ == "__main__":
    fs = FileStorage()

    # All States
    all_states = fs.all(State)
    print("All States:", len(all_states))
    for state in all_states.values():
        print(state)

    # Create a new State
    new_state = State()
    new_state.name = "California"
    fs.new(new_state)
    fs.save()
    print("New State:", new_state)

    # All States
    all_states = fs.all(State)
    print("All States:", len(all_states))
    for state in all_states.values():
        print(state)

    # Create another State
    another_state = State()
    another_state.name = "Nevada"
    fs.new(another_state)
    fs.save()
    print("Another State:", another_state)

    # All States
    all_states = fs.all(State)
    print("All States:", len(all_states))
    for state in all_states.values():
        print(state)

    # Delete the new State
    fs.delete(new_state)

    # All States
    all_states = fs.all(State)
    print("All States:", len(all_states))
    for state in all_states.values():
        print(state)
