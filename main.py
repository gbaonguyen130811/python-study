import os
import student_management as std_func
import menu
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu.show_actions()
    while True:
        choice = menu.choice_action()
        if choice == 0:
            print("Exit...")
            break
        elif choice == 1:
            std_func.insert_student()
        elif choice == 2:
            std_func.update_student()
        elif choice == 3:
            std_func.delete_student()
        elif choice == 4:
            std_func.display_students()

        if choice is not None:
            input("Press any key to continue....")
            clear_screen()
            menu.show_actions()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
