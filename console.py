#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    intro = "Welcome to the AIRBNB console command"
    prompt = "(hbnb) "

    def do_quit(self, args: str) -> bool:
        return True

    def do_EOF(self, args: str) -> bool:
        return True
    
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