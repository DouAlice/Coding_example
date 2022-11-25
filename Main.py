"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs a main test file to show menu
to the user and process user operations.

"""

from Admin import Admin
from Instructor import Instructor
from Student import Student
from User import User


def show_menu(login_user_role):
    """
    The show_menu function will print out the available options that
    the user can choose.

    parameter
    --------
    login_user_role: The role of the user, can be either Student,
    Instructor or Admin.

    """
    print(f'Please enter {login_user_role} command for further service:'
          f'\n1. EXTRACT_DATA\n2. VIEW_COURSES\n3. VIEW_'
          f'USERS\n4. VIEW_REVIEWS\n5. REMOVE_DATA')


def process_operations(user_object):
    """
    The process_operations function will ask the users to input commands,
    display instructions messages and execute the user commands accordingly,
    including performing data extraction, removal, view.

    parameter
    --------
    user_object: An object of either Student, Instructor or Admin class.

    """
    exit_command = False
    while not exit_command:
        # print different instruction messages for Admin and other users.
        if type(user_object).__name__ == "Admin":
            print('\nAdmin can take commands “1”, “2”, “3”, “4”, “5”.\n'
                  'For command “2” and “4”, please enter'
                  ' “TITLE_KEYWORD/ID/INSTRUCTOR_ID” and “ID/KEYWORD/COURSE_ID” '
                  'as a second command, followed by a value.\n'
                  'For example, input “2 TITLE_KEYWORD web”(the value after '
                  'the second command can only be one word).\n'
                  'Please make sure that each command or value is separated '
                  'by ONE space only.\n'
                  'If you enter no other arguments for command “2” and “4”, '
                  'a default overview output will be '
                  'displayed.\n')
        else:
            print('\nInstructor and Student can take command “2”, “4” '
                  'and no other arguments are allowed.\n')

        # prompts the user to enter commands if the command is blank,
        # until the user enters a non-blank command or 'exit'.
        commands = input("Please enter your commands: ").strip().split(" ")
        while commands == [''] and commands[0].lower() != 'exit':
            commands = \
                input("Please either enter your non-empty commands or"
                      " enter 'exit' to exit the "
                      "system: ").strip().split(" ")
        option = commands[0]
        if option.lower() == 'exit':
            exit_command = True

        # if commands have no arguments following the first command(option),
        # set args as an empty list.
        try:
            args = commands[1:]
        except:
            args = []

        # executing data extraction, data view or data removal according to
        # the option (first command) input by the user.
        if option == '1':
            print("========================================"
                  "You have chosen to extract data.==========================="
                  "=============\n"
                  "-------------------------"
                  "Please wait while the system is processing"
                  "--------------------------")
            user_object.extract_info()
            if type(user_object).__name__ == "Admin":
                print("========================================"
                      "Extraction finish.==========================="
                      "=============\n")
        elif option == '2':
            print("========================================"
                  "You have chosen to view courses.============================"
                  "============\n")
            user_object.view_courses(args)
            print("========================================"
                  "View finished.========================================\n")
        elif option == '3':
            print("========================================"
                  "You have chosen to view users.==========================="
                  "=============\n")
            user_object.view_users()
            if type(user_object).__name__ == "Admin":
                print("========================================View finished."
                      "================================"
                      "========\n")
        elif option == '4':
            print("========================================"
                  "You have chosen to view reviews."
                  "=========================="
                  "==============\n")
            user_object.view_reviews(args)
            print("========================================View finished."
                  "========================================\n")
        elif option == '5':
            print("========================================"
                  "You have chosen to remove data.=========================="
                  "==============\n")
            choice = input("Please confirm if you wish to continue removing data,"
                           " this will delete or stored data.\n"
                           "Enter Y if you wish to continue,"
                           " enter anything else to discontinue: \n")
            if choice == 'Y':
                user_object.remove_data()
                if type(user_object).__name__ == "Admin":
                    print("========================================"
                          "All data have been removed.======================="
                          "=================\n")
            else:
                print("========================================"
                      "Data removal was not executed.======================="
                      "=================\n")
        # print a warning message is the first command is not one of
        # 1, 2, 3, 4, 5.
        else:
            if not exit_command:
                print("\nPlease enter a valid first command. Your first command"
                      " must be one of 1/2/3/4/5. No other options"
                      " are accepted.")

    print("\nYou have successfully exited the system!")


# juan_moran jm22081600jm
# eduonix_learning_solutions 598757

def main():
    """
    The main function will ask the user to enter username, password to login,
    records user role and information, and call the process_operations method
    to allow user to enter and execute commands.

    parameter
    --------
    user_object: An object of either Student, Instructor or Admin class.

    """

    login_result = False
    login_user_role = ""
    login_user_info = {}
    username_password = [""]

    # Ask the user to input username and password.
    # If the user does not enter 'exit', keep asking the user to input
    # if the input is not exactly two word separated by a space.
    while username_password[0].lower() != 'exit' \
            and (len(username_password) != 2 or not login_result):
        username_password = \
            input('Please enter both username and password in the correct'
                  ' format e.g., "adcde 12345", also make sure they are '
                  'separated by one space only and '
                  'they are not empty: \n').strip().split(" ")
        try:
            temp_user = \
                User(username=username_password[0], password=username_password[1])
        except:
            temp_user = \
                User(username="", password="")

        login_result, login_user_role, login_user_info = temp_user.login()
        # if the login_result is False, prints a message.
        if not login_result and username_password[0].lower() != 'exit':
            print("========================================"
                  "Login failed.========================================")
            print('Incorrect username or password.\n'
                  'Please re-enter username and password in '
                  'format “username password” '
                  'e.g., "adcde 12345". \n')

        if username_password[0].lower() == 'exit':
            print("You have exited the program")

        # Creating an object of Admin, Instructor or Student class,
        # according to the login_user_role.
        else:
            user_object = None
            if login_user_role == 'Admin':
                user_object = Admin(int(login_user_info['id']),
                                    login_user_info['username'],
                                    login_user_info['password'])

            elif login_user_role == 'Instructor':
                user_object = Instructor(int(login_user_info['id']),
                                         login_user_info['username'],
                                         login_user_info['password'],
                                         login_user_info['display_name'],
                                         login_user_info['job'],
                                         login_user_info['image'],
                                         login_user_info['course'])

            elif login_user_role == 'Student':
                user_object = Student(int(login_user_info['id']),
                                      login_user_info['username'],
                                      login_user_info['password'],
                                      login_user_info['title'],
                                      login_user_info['image'],
                                      login_user_info['initial'],
                                      int(login_user_info['review_id']))

            if login_user_role in ['Admin', 'Instructor', 'Student']:
                print(f'========================================'
                      f'{type(user_object).__name__} '
                      f'login successfully================'
                      f'========================')
                print(f'Welcome {type(user_object).__name__}, '
                      f'your role is {type(user_object).__name__}')
                show_menu(login_user_role)
                process_operations(user_object)


if __name__ == "__main__":
    # print a welcome message
    print("========================================"
          "Welcome to our system========================================")

    # manually creates an admin object and register the admin.
    admin = Admin(111, 'Dou1', '222')
    admin.register_admin()
    print("======================================="
          "Admin has been registered=======================================")
    main()
