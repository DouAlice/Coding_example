"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs a User class, which represents a
general user with a unique user id, a username and a password, who can log in
but have no permission to view, extract or remove data.

"""

import random


class User:

    def __init__(self, id=-1, username="", password=""):
        """
        The constructor of the User class, for initiating a new User object.

        parameter
        --------
        id: An integer representing the id of the user.
        username: A String representing the username of the user.
        password: A String representing the password of the user.

        """
        self.id = id
        self.username = username
        self.password = password

    def generate_unique_user_id(self):
        """
        The generate_user_id function will extract existing student, instructor
        and admin ids to randomly generate a unique user id for the user.

        return
        --------
        new_id: A 10-digit integer, the new, unique id that has been generated.
        """

        # Extract the stored student, instructor and admin info, store them in
        # dictionaries. Extract the IDs (keys in the dictionaries) and store
        # them in lists respectively.
        stu_id_list = list(self.extract_student_dict().keys())
        ins_id_list = list(self.extract_instructor_dict().keys())
        admin_id_list = list(self.extract_admin_dict().keys())

        # Append the student, instructor and admin id lists.
        all_id_list = stu_id_list + ins_id_list + admin_id_list

        # Randomly generate a 10-digit integer. Convert the integer to String
        # to compare if it already exists in the id lists. If it does,
        # regenerate a new id until the id is unique.
        new_id = random.randint(1000000000, 9999999999)
        while str(new_id) in all_id_list:
            new_id = random.randint(1000000000, 9999999999)

        return new_id

    def encryption(self, input_password):
        """
        The encryption function will encrypt the user passwords.

        parameter
        --------
        input_password: the password string that needs to be encrypted.

        return
        --------
        encrypted_str: The user password string after encryption.
        """

        # Characters of all_puntuation will be used in encryption.
        all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

        # Finding the character of all_punctuation that will be
        # used to encrypt every first, second and third characters
        # in the input user password.
        # Store the 3 characters into a list.
        first_char = all_punctuation[len(input_password) % len(all_punctuation)]
        second_char = all_punctuation[len(input_password) % 5] * 2
        third_char = all_punctuation[len(input_password) % 10] * 3
        char_list = [first_char, second_char, third_char]

        encrypted_str = "^^^"  # Adding the start characters.

        # For each character in the input user password,
        # every first, second and third characters will
        # be encrypted with the first, second and third
        # elements in the char_list respectively.
        for i in range(len(input_password)):
            encrypted_str += char_list[i % 3]
            encrypted_str += input_password[i]
            encrypted_str += char_list[i % 3]
        encrypted_str += "$$$"  # Adding the end characters.

        return encrypted_str

    def extract_admin_dict(self):
        """
        The extract_admin_dict function will extract all the stored admin data
        and save in a dictionary.

        return
        --------
        stu_dict: the dictionary in which admin data is stored in.
        """

        try:
            # Try opening the user_admin.txt, reading the information as String
            # and splitting the String into a list, separated by line.
            file_handler = open(
                './data/result/user_admin.txt',
                'r', encoding="utf-8")
            admin_str = file_handler.read()
            admin_list = admin_str.splitlines()

            # For each item (representing a single admin) in the list,
            # store the admin id as the key in the dictionary admin_dict.
            # The value for each key is also a dictionary, storing the
            # full admin information.
            admin_dict = {}
            for one_admin in admin_list:
                one_admin_list = one_admin.split(";;;")
                admin_id = one_admin_list[0]
                admin_username = one_admin_list[1]
                admin_password = one_admin_list[2]
                admin_dict[admin_id] = {'id': admin_id,
                                        'username': admin_username,
                                        'password': admin_password}

        # If the user_admin.txt could not be found, create an empty dictionary.
        except FileNotFoundError:
            admin_dict = {}
        else:
            file_handler.close()

        return admin_dict

    def extract_student_dict(self):
        """
        The extract_student_dict function will extract all the stored student
        data and save as a dictionary.

        return
        --------
        stu_dict: the dictionary in which student data is stored in.
        """
        try:
            # Try opening the user_student.txt, reading the information as
            # String and splitting the String into a list, separated by line.
            file_student = open(
                './data/result/user_student.txt'
                , 'r', encoding="utf-8")
            stu_str = file_student.read()
            stu_list = stu_str.splitlines()

            # For each item (representing a single student) in the list,
            # store the student id as the key in the dictionary admin_dict.
            # The value for each key is also a dictionary, storing the
            # full student information.
            stu_dict = {}
            for one_stu in stu_list:
                stu_info_list = one_stu.split(";;;")
                student_id = stu_info_list[0]
                student_username = stu_info_list[1]
                student_password: str = stu_info_list[2]
                student_title = stu_info_list[3]
                student_image = stu_info_list[4]
                student_initial = stu_info_list[5]
                review_id = stu_info_list[6]
                stu_dict[student_id] = {'id': student_id,
                                        'username': student_username,
                                        'password': student_password,
                                        'title': student_title,
                                        'image': student_image,
                                        'initial': student_initial,
                                        'review_id': review_id}

        # If the user_student.txt could not be found, create an
        # empty dictionary.
        except FileNotFoundError:
            stu_dict = {}
        else:
            file_student.close()

        return stu_dict

    def extract_instructor_dict(self):
        """
        The extract_instructor_dict function will extract all the stored
        instructor data and save as a dictionary.

        return
        --------
        stu_dict: the dictionary in which instructor data is stored in.
        """
        try:
            # Try opening the user_instructor.txt, reading the information
            # as Stringand splitting the String into a list, separated
            # by line.
            file_instructor = open(
                './data/result/user_instructor.txt',
                'r', encoding="utf-8")
            instructor_str = file_instructor.read()
            instructor_list = instructor_str.splitlines()

            # For each item (representing a single instructor) in the list,
            # store the instructor id as the key in the dictionary admin_dict.
            # The value for each key is also a dictionary, storing the
            # full instructor information.
            instructor_dict = {}
            for each_instructor in instructor_list:
                instructor_info_list = each_instructor.split(";;;")
                instructor_id = instructor_info_list[0]
                instructor_username = instructor_info_list[1]
                instructor_password = instructor_info_list[2]
                instructor_dis_name = instructor_info_list[3]
                instructor_job = instructor_info_list[4]
                instructor_image = instructor_info_list[5]
                instructor_course = instructor_info_list[6]
                instructor_dict[instructor_id] = {
                    'id': instructor_id,'username': instructor_username,
                    'password': instructor_password,
                    'display_name': instructor_dis_name,
                    'job': instructor_job,'image': instructor_image,
                    'course': instructor_course}

        # If the user_instructor.txt could not be found, create an
        # empty dictionary.
        except FileNotFoundError:
            instructor_dict = {}
        else:
            file_instructor.close()
        return instructor_dict

    def login(self):
        """
        The login function checks if the User object's username and password
        match with any of the existing record of student, instructor or
        admin information.

        return
        --------
        A tuple which contains the login_result(bool), login_user_role(str)
        and user info (dictionary).
        """

        # Extract the stored student, instructor and admin info, store them in
        # dictionaries.
        stu_dict = self.extract_student_dict()
        ins_dict = self.extract_instructor_dict()
        admin_dict = self.extract_admin_dict()

        # in each stored value in the dictionary (the value represents the
        # full student information), if the username of the current object
        # matches with the value of the username stored in the dictionary,
        # the password also matches with the store password, return the
        # login result as True and return the student role and student
        # information.
        for student_info in stu_dict.values():
            # If the object username and password match with one of
            # the stored student info, return "Student" as the
            # login_user_role.
            if student_info['username'] == self.username and \
                    student_info['password'] == self.encryption(self.password):
                return True, "Student", student_info

        for instructor_info in ins_dict.values():
            # If the object username and password match with one of
            # the stored instructor info, return "Instructor" as the
            # login_user_role.
            if instructor_info['username'] == self.username and \
                    instructor_info['password'] == self.encryption(self.password):
                return True, "Instructor", instructor_info

        for admin_info in admin_dict.values():
            # If the object username and password match with one of
            # the stored admin info, return "Admin" as the
            # login_user_role.
            if admin_info['username'] == self.username and \
                    admin_info['password'] == self.encryption(self.password):
                return True, "Admin", admin_info

        # If the object username and password match with no stored
        # info, return the login result as False, login_user_role
        # as an empty String and user info as an empty dictionary.
        return False, "", {}

    def extract_info(self):
        """
        The extract_info function will print a message, warning the user that there is no permission
        to extract information.

        """
        print("You have no permission to extract information.")

    def view_courses(self):
        """
        The view_courses function will print a message, warning the user that there is no permission
        to view courses.

        """
        print("You have no permission to view course.")

    def view_users(self):
        """
        The view_users function will print a message, warning the user that there is no permission
        to extract view users.

        """
        print("You have no permission to view users.")

    def view_reviews(self):
        """
        The view_reviews function will print a message, warning the user that there is no permission
        to extract view reviews.

        """
        print("You have no permission to view reviews.")

    def remove_data(self):
        """
        The remove_data function will print a message, warning the user that there is no permission
        to extract remove data.

        """
        print("You have no permission to remove data.")

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes (id, username, password) of the object.

        """
        return f'{self.id};;;{self.username};;;{self.password}'
