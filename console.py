#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class_names = [BaseModel]
class_names_str = ["BaseModel"]

class HBNBCommand(cmd.Cmd):

    intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        return True

    def do_EOF(self, args: str) -> bool:
        return True

    def do_create(self, args: str) -> str:
        new_instance = None
        # Vallidation
        if args == "":
            print("** class name missiong **")
            return
        if not args in class_names_str:
            print("** class doesn't exist **")
            return

        for number, class_to_create in enumerate(class_names_str):
            if args == class_to_create:
                new_instance = class_names[number]()

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args: str):
        # Vallidations
        args = args.split(' ')
        lenght = len(args)

        if args[0] == "":
            print("** class name missing **")
            return
        if not args[0] in class_names_str:
            print("** class doesn't exist **")
            return
        if lenght == 1:
            print("** instance id missing **")
            return

        all_data = storage.all()
        new_dictionary = {}

        for key, value in all_data.items():
            if key.startswith(f"{args[0]}.{args[1]}"):
                new_dictionary[key] = value
        
        if new_dictionary == {}:
            print("** no instance found **")
            return
        else:
            model = storage.all()[f"{args[0]}.{args[1]}"]
            print(model)
        

    def do_all(self, args):
        for obj in storage.all():
            print(storage.all()[obj].__str__())
        return
    
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
