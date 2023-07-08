#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class initialization
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Command to quit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command to quit the program by pressing EOF (Ctrl+D)
        """
        return True

    def emptyline(self):
        """
        Do nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
