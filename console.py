#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The comman
    """

    prompt = "(hbnb)"

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "Review": Review,
        "City": City,
        "Amenity": Amenity
    }

    def default(self, line):

        if '.' in line and '(' in line and ')' in line:
            try:
                class_name, method_call = line.split('.', 1)
                method, args = method_call.split('(', 1)
                args = args.rstrip(')')

                if args.startswith('"') and args.endswith('"'):
                    args = args[1:-1]

                if method == "all":
                    return self.do_all(class_name)
                elif method == "count":
                    return self.do_count(class_name)
                elif method == "show":
                    return self.do_show(f"{class_name} {args}")
                elif method == "destroy":
                    return self.do_destroy(f"{class_name} {args}")
                elif method == "update":

                    id_obj, dic_part = args.split(",", 1)
                    id_obj = id_obj.strip().strip('"')
                    dic_part = dic_part.strip()

                    if dic_part.startswith('{') and dic_part.endswith('}'):
                        try:
                            import ast
                            pyth_obj = ast.literal_eval(dic_part)

                        except Exception as e:
                            print("invalid dictitionary")
                            return

                        for k, v in pyth_obj.items():

                            update_str = f'{class_name} {id_obj} {k} "{v}"'
                            self.do_update(update_str)

                    else:

                        parts = [a.strip().strip('"') for a in args.split(",")]
                        if len(parts) < 3:
                            print("the arguments are few")
                            return

                        obj_id, attr_name, attr_value = parts

                        return self.do_update(
                            f'{class_name} {obj_id} {attr_name} "{attr_value}"'
                            )

            except Exception as e:
                print("** unkown classname or something went wrong**")
                return
        else:
            print("**unkown classname**")

    def emptyline(self):
        """overriding defaul`emptyline` method
        so that an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """quit: to exit the program when user writes `quit` command"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program when user writes `EOF` command"""
        return True

    def help_quit(self):
        print("Usage:it exit the program when user writes `quit` command")
        print(" write `quit` to exit the commandline ")

    def help_EOF(self):
        print("Usage:it exit the program when user writes `EOF` command")
        print(" write `EOF` to exit the commandline ")

    def do_create(self, arg):
        arg = arg.split()
        parameter = {}
        if not arg:
            print("please provide class and object attribute")
            return
        class_name = arg[0]
        if class_name not in self.classes:
            print("class name doesn't exist")
            return
        cleared_value = None
        for param in arg[1:]:
            if "=" not in param:
                print("invalid key-pair parameter")
                return
            key, value = param.split("=",1)
            if value.startswith('"') and value.endswith('"'):
                value = value.replace('\\"', '"')
                value = value.replace("_", " ")
                cleared_value = value
            elif "." in value:
                try:
                    value = float(value)
                    cleared_value = value
                except ValueError:
                    return

            else:
                try:
                    value = int(value)
                    cleared_value = value
                except value:
                    return 
            parameter[key] = cleared_value
        new_obj = self.classes[class_name]()
        for k, v in parameter.items():
            setattr(new_obj, k, v)
        print(new_obj)

    def do_show(self, arg):
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"

            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"

            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        results = []
        objects = storage.all()
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return

            for key, obj in objects.items():
                if key.startswith(arg + '.'):
                    results.append(str(obj))
        else:
            for obj in objects.values():
                results.append(str(obj))
        print(results)

    def do_count(self, arg):
        results = 0
        if arg:
            if arg not in self.classes:
                print("**class doesn't exist**")
                return
            all_objects = storage.all()
            for key, v in all_objects.items():

                if key.startswith(arg + '.'):
                    results += 1
            print(results)

    def do_update(self, arg):
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                atrr_name = args[2]
                atrr_value = args[3].strip('"')
                try:
                    if '.' in atrr_value:
                        atrr_value = float(atrr_value)
                    else:
                        atrr_value = int(atrr_value)
                except ValueError:
                    pass
                setattr(obj, atrr_name, atrr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
