#!/usr/bin/python3
"""
console module
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage

class BNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create an instance of of a class then save it to json file"""
        if args:
            if args == "BaseModel":
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")
    
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        all_obj = storage.all()
        list_object = []
        for obj_id in all_obj.keys():
            obj = all_obj[obj_id]
            list_object.append(str(obj))
        print(list_object)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        print(end="")

    def do_EOF(self, line):
        """Handle End-of-File (EOF) condition to exit the program gracefully"""
        print()
        return True


if __name__ == '__main__':
    BNBCommand().cmdloop()
