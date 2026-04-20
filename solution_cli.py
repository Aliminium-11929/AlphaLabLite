import argparse

from execute import execute
from view import view


def execute_runner(args):
    scriptlines: list[str] = []
    try:
        newLine = input()
        while True:
            scriptlines.append(newLine.strip())
            newLine = input()
    except EOFError:
        clean_scriptlines = []
        for line in scriptlines:
            if line != "":
                clean_scriptlines.append(line)
        print(execute(script=scriptlines))


def view_runner(args):
    objectID = args.id
    objectVarnames = args.varnames
    print(view(id=objectID, varnames=objectVarnames))


def main():
    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers()
    parser_execute = subparsers.add_parser(
        "execute", help="Read entire stdin as input script"
    )
    parser_execute.set_defaults(func=execute_runner)
    parser_view = subparsers.add_parser("view", help="View items by ID")
    parser_view.add_argument("--id", type=str)
    parser_view.add_argument("varnames", nargs="*")
    parser_view.set_defaults(func=view_runner)
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()


if __name__ == "__main__":
    main()
