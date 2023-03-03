#!/usr/bin/python3
"""
Module Name:
console

Module Description:
This module contains only one Class

Module Classes:
- HBNBCommand

Module Attributes:
- None
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class_names_str = ["BaseModel", "User", "Place", "State",
                 "City", "Amenity", "Review"]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    """Command-line interface for the AIRBNB project."""

    #intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        """Quit command to exit the program.

        Args:
            args (str): The arguments passed with the command.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, args: str) -> bool:
        """Handle the end-of-file event (Ctrl+D).

        Args:
            args (str): The arguments passed with the command.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_create(self, args: str) -> None:
        """Create a new instance of a given class.

        Args:
            args (str): The arguments passed with the command.
                        It should contain the class name.

        Returns:
            None
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return

        # Process
        new_instance = eval(class_name)()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args: str) -> None:
        """Show the string representation of an instance.

        Args:
            args (str): The arguments passed with the command.
                        It should contain the class name and the instance ID.

        Returns:
            None
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        model = all_data.get(f"{class_name}.{instance_id}", None)

        if model is None:
            print("** no instance found **")
            return

        print(model)

    def do_all(self, args: str) -> None:
        """Show the string representation of all instances of a given class.

        Args:
            args (str): The arguments passed with the command.
                        It may contain the class name.

        Returns:
            None
        """
        arg_list = args.split()
        if arg_list and arg_list[0] not in class_names_str:
            print("** class doesn't exist **")
            return

        # Process
        objects = [str(obj) for obj in all_data.values()  # if only write all
                   if args == "" or str(obj).startswith(f"[{args}]")]

        print(objects)

    def do_destroy(self, args: str) -> None:
        """Delete an instance based on the class name and ID.

        Args:
            args (str): The arguments passed with the command.
                        It should contain the class name and the instance ID.

        Returns:
            None
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        try:
            all_data.pop(f"{class_name}.{instance_id}")
        except KeyError:
            print("** no instance found **")
            return

        storage.save()

    def do_update(self, args: str) -> None:
        """Update an instance based on the class name and ID.

        Args:
            args (str): The arguments passed with the command.
                        It should contain the class name, instance ID,
                        attribute name, and attribute value.

        Returns:
            None
        """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        instance = all_data.get(f"{class_name}.{instance_id}", None)

        if instance is None:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_name = arg_list[2]
        attribute_value = arg_list[3]

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** this attribute can't be change **")
            return

        setattr(instance, attribute_name, attribute_value)

        instance.save()

    def complete_add(self, text, line, start_index, end_index) -> str:
        """Provide auto-completion for some commands.

        Args:
            text (str): The current word being completed.
            line (str): The whole command line being completed.
            start_index (int): The start index of the current word.
            end_index (int): The end index of the current word.

        Returns:
            str: A list of possible completions.
        """
        options = ['quit', 'help', 'all', 'show', 'destroy', 'update']
        if text:
            return [option for option in options if option.startswith(text)]
        else:
            return options

    def default(self, line: str) -> None:
        """Handle unknown commands.

        Args:
            line (str): The unknown command.

        Returns:
            None
        """
        print_string = f"Command '{line}' not found, "
        print_string += f"please type help to display the commands availables"
        print(print_string)

    def emptyline(self) -> None:
        """
        Handle empty lines
        """
        pass

    def do_count(self, args: str) -> None:
        """ Retrieve the number of instances of a class.
            """
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list and arg_list[0] not in class_names_str:
            print("** class doesn't exist **")
            return
        class_count = 0
        for key in all_data.keys():
            to_compare = key.split('.')[0]
            if to_compare == arg_list[0]:
                class_count += 1
        print(class_count)

    def do_BaseModel(self, arguments):
        """ Retrieve an instance based on BaseModel.
            """
        method = arguments.split('(')[0].strip('.')
        raw_args = arguments.split('(')[1].strip(')')
        args = (raw_args.replace('",', '')).replace('"', '')
        if args != "":
            internal_args = "BaseModel " + args
        else:
            internal_args = "BaseModel"
        eval("self.do_{}".format(method))(internal_args)

    def do_User(self, arguments):
        """ Retrieve an instance based on User.
            """
        method = arguments.split('(')[0].strip('.')
        raw_args = arguments.split('(')[1].strip(')')
        args = (raw_args.replace('",', '')).replace('"', '')
        if args != "":
            internal_args = "User " + args
        else:
            internal_args = "User"
        eval("self.do_{}".format(method))(internal_args)

    def do_Place(self, arguments):
        """ Retrieve an instance based on Place.
            """
        method = arguments.split('(')[0].strip('.')
        raw_args = arguments.split('(')[1].strip(')')
        args = (raw_args.replace('",', '')).replace('"', '')
        if args != "":
            internal_args = "Place " + args
        else:
            internal_args = "Place"
        eval("self.do_{}".format(method))(internal_args)

        #### Hola, adalanté un poquito. Para las demás clases sería el mismo bloque de código, espero que puedas ayudarme con lo de las comillas 
        #### en los argumentos y el mecanismo de qué hacer cuando hay argumentos en exceso

if __name__ == '__main__':
    HBNBCommand().cmdloop()
