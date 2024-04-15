#!/usr/bin/python3
"""
console module
"""

import cmd


class BNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
