import sys
import os
from view import JsonView

if __name__ == '__main__':
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    arg = sys.argv
    if arg[1] == "j":
        if len(arg) != 3:
            print("Please specify a JSON File Sir")
        else:
            file_path = os.path.join(THIS_FOLDER, arg[2])
            json_view = JsonView(file_path=file_path)
            json_view.process_file()
            json_view.print_result()
    elif arg[1] == "c":
        print("Belum implemen hehe")
    else:
        print("HELLO")
