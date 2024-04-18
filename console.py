#!/usr/bin/python3
"""
console module
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
import os

class BNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create an instance of a class then save it to json file"""
        if args:
            arguments = args.split()
            class_name = arguments[0]
            if hasattr(globals().get(class_name), '__bases__') and issubclass(globals().get(class_name), BaseModel):
                my_model = globals()[arguments[0]]()
                my_model.save()
                print(my_model.id)           
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show instance base on id and class name"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        all_class_name = []
        my_id_dict = {}
                
        for obj_key in all_objects.keys():
            class_name, obj_id = obj_key.split('.')
            all_class_name.append(class_name)
            
            if class_name in my_id_dict.keys():
                my_id_dict[class_name].append(obj_id)
            else:
                my_id_dict[class_name] = [obj_id]

            if class_name == arguments[0] and obj_id == arguments[1]:
                print(all_objects[obj_key])
                return
        
        if arguments[0] not in all_class_name:
            print("** class doesn't exist **")
            return
        
        
        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return

        
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        all_class_name = []
        my_id_dict = {}
        
        
        try:
            for obj_key in all_objects.keys():
                class_name, obj_id = obj_key.split('.')
                all_class_name.append(class_name)
                
                if class_name in my_id_dict.keys():
                    my_id_dict[class_name].append(obj_id)
                else:
                    my_id_dict[class_name] = [obj_id]
            
                if class_name == arguments[0] and obj_id == arguments[1]:
                    del all_objects[obj_key]
                storage.save()

        except RuntimeError:
            return
        
        if arguments[0] not in all_class_name:
            print("** class doesn't exist **")

        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return


    def do_update(self, args):
        """update an instance base class name and id"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        if len(arguments) < 3:
            print("** attribute name missing ** ")
            return
    
        if len(arguments) < 4:
            print("** value missing **")
            return

        all_class_name = []
        my_id_dict = {}
        
        try:
            for obj_key in all_objects.keys():
                class_name, obj_id = obj_key.split('.')
                all_class_name.append(class_name)
                
                if class_name in my_id_dict.keys():
                    my_id_dict[class_name].append(obj_id)
                else:
                    my_id_dict[class_name] = [obj_id]
            
                if class_name == arguments[0] and obj_id == arguments[1]:
                    setattr(all_objects[obj_key], arguments[2], arguments[3])
                storage.save()
        except RuntimeError:
            return

        if arguments[0] not in all_class_name:
            print("** class doesn't exist **")

        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return
            

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        arguments = args.split()
        all_obj = storage.all()
        all_class_name = []

        for obj_key in all_obj.keys():
            class_name, obj_id = obj_key.split('.')
            all_class_name.append(class_name)

        if args:
            if arguments[0] not in all_class_name:
                print("** class doesn't exist **")
                return
            
            list_object = []
            for obj_id in all_obj.keys():
                cls_name, o_id = obj_key.split('.')
                if arguments[0] == cls_name:
                    obj = all_obj[obj_id]
                    list_object.append(str(obj))
            print(list_object)
        
        else:
            list_object = []
            for obj_id in all_obj.keys():
                obj = all_obj[obj_id]
                list_object.append(str(obj))
            print(list_object)

    def default(self, line):
        print("Not implemented yet")

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
