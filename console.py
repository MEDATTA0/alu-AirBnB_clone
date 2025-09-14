#!/usr/bin/env python3
"""Console for HBNB project."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit program with EOF (Ctrl+D)."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances, or all instances of a class."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        else:
            cls_name = args[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(cls_name + "."):
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance.
        Usage:
            update <ClassName> <id> <attribute_name> <value>
            update <ClassName> <id> <dictionary>
        """
        args = arg.split(maxsplit=2)
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]

        # If a dictionary is provided
        if len(args) == 3:
            try:
                attr_dict = eval(args[2])
                if isinstance(attr_dict, dict):
                    for k, v in attr_dict.items():
                        setattr(obj, k, v)
                    obj.save()
                    return
            except Exception:
                pass

        # Single attribute update
        parts = args[2].split() if len(args) == 3 else []
        if len(parts) < 2:
            print("** attribute name missing **")
            return
        attr_name = parts[0]
        attr_value = parts[1].strip('"').strip("'")
        try:
            if "." in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except Exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
