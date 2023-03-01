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
        if len(args.split()) >= 1:
            # Desestructuring the args
            class_name, *_ = args.split()
            # Vallidations
            if not class_name in class_names_str:
                print("** class doesn't exist **")
                return
        else:
            # Vallidation
            if not args:
                print("** class name missiong **")
                return

        # Process
        for number, class_to_create in enumerate(class_names_str):
            if class_name == class_to_create:
                new_instance = class_names[number]()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args: str) -> None:
        if len(args.split()) >= 2:
            # Desestructuring the args
            class_name, instance_id, *_ = args.split()

            # Vallidations
            if not class_name in class_names_str:
                print("** class doesn't exist **")
                return
        else:
            # Vallidations
            if not args:
                print("** class name missing **")
                return
            if len(args.split()) < 2:
                print("** instance id missing **")
                return

        # Process
        model = all_data.get(f"{class_name}.{instance_id}", {})
        
        if model == {}:
            print("** no instance found **")
            return

        print(model)

    def do_all(self, args: str) -> None:
        if args:
            # Desestructuring the args
            class_name, *_ = args.split()

             # Validation
            if class_name and class_name not in class_names_str:
                print("** class doesn't exist **")
                return

        # Process
        objects = [str(obj) for obj in all_data.values() # if only write all
                   if args == "" or str(obj).startswith(f"[{args}]")]

        print(objects)

    def do_destroy(self, args: str) -> None:
        if len(args.split()) >= 2:
            # Desestructuring the args
            class_name, instance_id, *_ = args.split()
        else:
            # Vallidations
            if not args:
                print("** class name missing **")
                return
            if not args.split()[0] in class_names_str:
                print("** class doesn't exist **")
                return
            if len(args.split()) == 1:
                print("** instance id missing **")
                return
        
        # Process
        try:
            all_data.pop(f"{class_name}.{instance_id}")
        except KeyError:
            print("** no instance found **")
            return

        print(instance_id)


    def complete_add(self, text, line, start_index, end_index) -> str:
        options = ['quit', 'help', 'all', 'show', 'add']
        if text:
            return [option for option in options if option.startswith(text)]
        else:
            return options

    def default(self, line: str) -> None:
        print(f"Command '{line}' not found, please type help to display the commands availables")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
