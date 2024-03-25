#!/usr/bin/python3

from cmd import Cmd


class HBNBCommand(Cmd):
  """Simple command interpreter for the HBnb application."""

  prompt = "(hbnb) "
  intro = "Welcome to the HBNB command interpreter!"

  def do_quit(self, arg):
    """Quit the command interpreter."""
    print("Exiting HBNB command interpreter")
    exit()

  def emptyline(self):
    """Handle empty lines by passing."""
    pass

  def do_help(self, arg):
    """Provides help information on available commands."""
    print("Documented commands (type help <command> for more info):")
    super().do_help(arg)


if __name__ == '__main__':
  HBNBCommand().cmdloop()
