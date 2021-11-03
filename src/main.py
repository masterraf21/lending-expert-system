import sys
import os
from view import JsonView, CLIView

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
        try:
            print("Selamat datang di Expert System Peminjaman")
            cli_view = CLIView()
            cli_view.process_data()
            cli_view.print_result()
        except KeyboardInterrupt:
            print("\n")
            sys.exit("Byebye")

    else:
        print("HELLO")
