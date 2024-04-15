#!/usr/bin/python3
"""
console module
"""
import cmd

class BNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def help_quit(self):
        print("Quit command to exit the program")

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print()
        return True




if __name__ == '__main__':
    BNBCommand().cmdloop()