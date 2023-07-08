#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    class initialization
    """
    prompt = "(hbnb) "

    def arg_checker(self, arg):
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
        # if len(args) == 0:
        #     print('** class name missing **')
        # else:
        #     class_name = args[0]
        #     if class_name not in models.dict_class:
        #         print('** class doesn\'t exist **')
        if arg_checker(args):
            instance = models.dict_class[class_name]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance

        Args:
            arg (str): class & id.
        """
        args = arg.split()
        # if len(args) == 0:
        #     print('** class name missing **')
        # else:
        #     class_name = args[0]
        #     if class_name not in models.dict_class:
        #         print('** class doesn\'t exist **')
        if arg_checker(args):
            if len(args) < 2:
                print('** instance id missing **')
            else:
                instance_id = args[1]
                instance = models.storage.get(class_name, instance_id)
                if instance is None:
                    print('** no instance found **')
                else:
                    print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance

        Args:
            arg (str): class & id
        """
        args = arg.split()
        # if len(args) == 0:
        #     print('** class name missing **')
        # else:
        #     class_name = args[0]
        #     if class_name not in models.dict_class:
        #         print('** class doesn\'t exist **')
        if arg_checker(args):
            if len(args) < 2:
                print('** instance id missing **')
            else:
                instance_id = args[1]
                # Deletes the instance of the specified class
                # and id and saves the changes to the JSON file
                instance = models.storage.get(class_name, instance_id)
                if instance is None:
                    print('** no instance found **')
                else:
                    instance.delete()
                    models.storage.save()

    def do_update(self, arg):
        """
        Updates an instance

        Args:
            arg (str): class & id
        """
        args = arg.split()
        # if len(args) == 0:
        #     print('** class name missing **')
        # else:
        #     class_name = args[0]
        #     if class_name not in models.dict_class:
        #         print('** class doesn\'t exist **')
        if arg_checker(args):
            if len(args) < 2:
                print('** instance id missing **')
            else:
                instance_id = args[1]
                instance = models.storage.get(class_name, instance_id)
                if instance is None:
                    print('** no instance found **')
                elif len(args) < 3:
                    print('** attribute name missing **')
                elif len(args) < 4:
                    print('** value missing **')
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    # Updates the instance attribute with the
                    # specified value and saves the changes to the JSON file
                    setattr(instance, attr_name, attr_value)
                    instance.save()

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
            instances = models.storage.all(class_name)
        for instance in instances.values():
            print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
