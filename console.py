#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""
import cmd
import models
# from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    class initialization
    """
    prompt = "(hbnb) "
    storage = models.storage
    storage.reload()

    def arg_checker(self, args):
        if len(args) == 0:
            print('** class name missing **')
            return False
        else:
            class_name = args[0]
            if class_name not in models.dict_class:
                print('** class doesn\'t exist **')
                return False
        return True

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

    def do_create(self, arg):
        """
        Creates a new instance

        Args:
            arg (str): Creates a new instance of the specified
            class and saves it to the JSON file
        """
        args = arg.split()
        if self.arg_checker(args):
            instance = models.dict_class[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in models.dict_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance

        Args:
            arg (str): class & id
        """
        args = arg.split()
        if self.arg_checker(args):
            if len(args) < 2:
                print('** instance id missing **')
            else:
                # Deletes the instance of the specified class
                # and id and saves the changes to the JSON file
                key = f"{args[0]}.{args[1]}"
                temp = models.storage.all()  # temp is self.__object
                if key in temp:
                    del (temp[key])
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance

        Args:
            arg (str): class & id
        """
        args = arg.split()
        if self.arg_checker(args):
            if len(args) < 2:
                print('** instance id missing **')
            else:
                instance_id = args[1]
                key = "{}.{}".format(args[0], args[1])
                temp = models.storage.all()  # temp is self.__object
                if key not in temp:
                    print('** no instance found **')
                elif len(args) < 3:
                    print('** attribute name missing **')
                elif len(args) < 4:
                    print('** value missing **')
                else:
                    new_obj = temp.get(key)
                    setattr(new_obj, args[2], args[3])
                    models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances

        Args:
            arg (str): class & id
        """
        args = arg.split()
        if len(args) == 0:
            # Print the string representation of all instances in general
            instances = models.storage.all()
        else:
            class_name = args[0]
            if class_name not in models.dict_class:
                print('** class doesn\'t exist **')
                return
            # Prints the string representation
            # of all instances of the specified class
            instances = models.storage.all()
            for instance in instances.values():
                print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()