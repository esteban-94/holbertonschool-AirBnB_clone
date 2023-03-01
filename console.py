#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class_names = [BaseModel]
class_names_str = ["BaseModel"]
all_data = storage.all()

class HBNBCommand(cmd.Cmd):

    intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        return True

    def do_EOF(self, args: str) -> bool:
        return True

    def do_create(self, args: str) -> None:
        class_name, *_ = args.split()
        new_instance = None
        # Vallidation
        if not class_name:
            print("** class name missiong **")
            return
        if not class_name in class_names_str:
            print("** class doesn't exist **")
            return

        for number, class_to_create in enumerate(class_names_str):
            if args == class_to_create:
                new_instance = class_names[number]()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args: str) -> None:
        # Vallidations
        class_name, instance_id, *_ = args.split()

        if not class_name:
            print("** class name missing **")
            return
        if not class_name in class_names_str:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return

        model = all_data.get(f"{args[0]}.{args[1]}", {})
        
        if model == {}:
            print("** no instance found **")
            return

        print(model)

    def do_all(self, args: str) -> None:
        # Vallidations
        if not args in class_names_str and args != "":
            print("** class doesn't exist **")
            return

        objects = [str(obj) for obj in all_data.values()
                   if args == "" or str(obj).startswith(f"[{args}]")]

        print(objects)


    def complete_add(self, text, line, start_index, end_index) -> str:
        options = ['quit', 'help']
        if text:
            return [option for option in options if option.startswith(text)]
        else:
            return options

    def default(self, line: str) -> None:
        print(f"Command '{line}' not found, please type help to display the commands availables")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
