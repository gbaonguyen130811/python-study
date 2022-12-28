def show_actions():
    print("********** STUDENT MANAGEMENT **********")
    print("0. Exit")
    print("1. Insert student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Display student list")
    print("***************************************")


def show_student_properties():
    print("********** MAIN MENU **********")
    print("0. Ignore")
    print("1. Name")
    print("2. Age")
    print("3. School name")
    print("4. Class name")
    print("*****************************")


def choice_action():
    choice = None
    while choice is None:
        choice = int(input("Choice a action: "))
        if choice < 0 or choice > 4:
            choice = None
    return choice


def choice_property():
    choice = int(input("Choice a property to update: "))
    if choice < 0 or choice > 4:
        return -1
    return choice
