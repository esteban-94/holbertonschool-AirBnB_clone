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
from typing import Tuple, Optional
import inspect


class_names_str = [
    "BaseModel", "User", "Place", "State",
    "City", "Amenity", "Review"
    ]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    """Command-line interface for the AIRBNB project."""

    # intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        """
        Quit command to exit the program.

        Args:
            args (str): The arguments passed with the command.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, args: str) -> bool:
        """
        Handle the end-of-file event (Ctrl+D).

        Args:
            args (str): The arguments passed with the command.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_create(self, args: str) -> None:
        """
        Create a new instance of a given class.

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
        """
        Show the string representation of an instance.

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

    def do_all(self, args: Optional[str]) -> None:
        """
        Show the string representation of all instances of a given class.

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
        try:  # if only write all
            class_name = arg_list[0]
        except Exception:
            pass

        # Process
        objects = [str(obj) for obj in all_data.values()  # if only write all
                   if args == "" or str(obj).startswith(f"[{class_name}]")]

        print(objects)

    def do_destroy(self, args: str) -> None:
        """
        Delete an instance based on the class name and ID.

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
        """
        Update an instance based on the class name and ID.

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

        is_dict = False
        for i in args:
            if i == '{':
                is_dict = True

        if is_dict:
            dicty = "".join(arg_list[2:])
            dictionary = eval(dicty)

            if (isinstance(dictionary, dict)):
                for key, value in dictionary.items():
                    setattr(instance, key, value)

                instance.save()
                return

        attribute_name = arg_list[2]
        attribute_value = eval(arg_list[3])

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** this attribute can't be change **")
            return

        setattr(instance, attribute_name, attribute_value)

        instance.save()

    def complete_add(self, text: str) -> str:
        """
        Provide auto-completion for some commands.

        Args:
            text (str): The current word being completed.
            line (str): The whole command line being completed.
            start_index (int): The start index of the current word.
            end_index (int): The end index of the current word.

        Returns:
            str: A list of possible completions.
        """
        options = [
            'quit', 'help', 'all', 'show', 'destroy', 'update', 'BaseModel',
            'User', 'Place', 'State', 'City', 'Amenity', 'Review'
            ]
        if text:
            return [option for option in options if option.startswith(text)]
        else:
            return options

    def default(self, line: str) -> None:
        """
        Handle unknown commands.

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
        """
        Retrieve the number of instances of a class.

        Args:
            args (str): the class.

        Returns:
            None
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

    def _parse_args(self, arguments: str) -> Tuple[str, str]:
        """
        Parse the line enter by the user.

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            The specific method, and the args passed
        """
        # Parse the arguments
        try:
            method = arguments.split('(')[0].strip('.')
            raw_args = arguments.split('(')[1].strip(')')

            is_dict = False
            for i in raw_args:
                if i == '{':
                    is_dict = True
            if is_dict:
                line_parse = raw_args.split('{')
                id_string = line_parse[0].replace('"', '').replace(",", "")
                dict = "{" + line_parse[1]
                args = f"{id_string} {dict}"
            else:
                ag_lt = raw_args.split(", ")
                if len(ag_lt) == 3:
                    if isinstance(eval(ag_lt[2]), int):
                        args = (raw_args.replace(',', '')).replace('"', '')
                    else:
                        arg = (ag_lt[0] + " " + ag_lt[1]).replace('"', '')
                        args = arg + " " + ag_lt[2]
                else:
                    args = (raw_args.replace(',', '')).replace('"', '')
        except Exception as e:
            print("Syntax Error")
            print("Error: ", e)
            return

        # Finding the function where was called
        # gets information about the framework of the above function
        callerframerecord = inspect.stack()[1]
        # gets the frame of the above function
        frame = callerframerecord[0]
        # gets information about the framework of the above function
        info = inspect.getframeinfo(frame)

        # assign the name of the above function
        name_function = info.function.strip("do_")

        # Obtaining the internal args
        if args != "":
            internal_args = f"{name_function} {args}"
        else:
            internal_args = f"{name_function}"

        return (method, internal_args)

    def _execute(self, method: str, internal_args: str) -> None:
        """
        Execute the command specified

        Args:
            method (str): the method to be executed.
            internal_args (str): the arguments of its method

        Returns:
            None
        """
        try:
            eval("self.do_{}".format(method))(internal_args)
        except Exception:
            print("Be sure that the argument is valid")

    def do_BaseModel(self, arguments: str) -> None:
        """
        Handle all methods of BaseModel that are enter in this way:

        >>> BaseModel.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_User(self, arguments: str) -> None:
        """
        Handle all methods of User that are enter in this way:

        >>> User.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_Place(self, arguments: str) -> None:
        """
        Handle all methods of Place that are enter in this way:

        >>> Place.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_Amenity(self, arguments: str) -> None:
        """
        Handle all methods of Amenity that are enter in this way:

        >>> Amenity.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_City(self, arguments: str) -> None:
        """
        Handle all methods of City that are enter in this way:

        >>> City.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_Review(self, arguments: str) -> None:
        """
        Handle all methods of Review that are enter in this way:

        >>> Review.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)

    def do_State(self, arguments: str) -> None:
        """
        Handle all methods of State that are enter in this way:

        >>> State.method(args)

        Args:
            arguments (str): the arguments enter by the user.

        Returns:
            None
        """
        method, internal_args = self._parse_args(arguments)
        self._execute(method, internal_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
