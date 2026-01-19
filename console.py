#!/usr/bin/python3
"""Console module for AirBnB clone."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = self.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show string representation of an instance.

        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id.

        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances.

        Usage: all [class name]
        """
        all_objs = storage.all()
        obj_list = []

        if not arg:
            # Print all instances
            for obj in all_objs.values():
                obj_list.append(str(obj))
        else:
            # Print instances of specific class
            class_name = arg.split()[0]

            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            for key, obj in all_objs.items():
                if key.startswith(class_name + "."):
                    obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        # Don't update id, created_at, updated_at
        if attribute_name in ['id', 'created_at', 'updated_at']:
            return

        obj = all_objs[key]

        # Try to cast to the correct type
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            try:
                attribute_value = attr_type(attribute_value)
            except (ValueError, TypeError):
                pass
        else:
            # Try to infer type
            try:
                attribute_value = int(attribute_value)
            except ValueError:
                try:
                    attribute_value = float(attribute_value)
                except ValueError:
                    pass  # Keep as string

        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
