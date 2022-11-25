"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts constructs a User class, which represents a
general user with a unique user id, a username, a password, a registration
time and a by-default empty role.
"""

import os
import pandas as pd
import random
import re
from lib.helper import get_day_from_timestamp, user_data_path


class User:
    # the current user object that has logged in, by default is none.
    current_login_user = None

    def __init__(self, uid=-1, username="", password="",
                 register_time="yyyy-MM-dd_HH:mm:ss.SSS",
                 role=""):
        """
        The constructor of the User class, for initiating a new User
        object.

        parameter
        --------
        uid: An integer representing the id of the user.
        username: A String representing the username.
        password: A String representing the user password.
        register_time: A String representing the time of registration.
        role: A String representing the role of the user.
        """
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the User object.
        """
        return f'{self.uid};;;{self.username};;;{self.password};;;' \
               f'{self.register_time};;;{self.role}'

    def authenticate_user(self, username, password):
        """
        Checking whether username and password can be matched with users saved
        in data file.

        parameter
        --------
        username: A String representing the username.
        password: A String representing the user password.

        return
        --------
        A tuple contains a boolean (indicating whether authentication passed),
        and the string representing the user information.
        """
        user_dict = self.read_user_info('all')
        # iterating over the info of each user saved in the file
        for user_info in user_dict.values():
            # check if the given username and password matched
            if user_info['username'] == username and \
                    user_info['password'] == self.encrypt_password(password):
                # the course string needs to be split into list for
                # instructors
                if user_info['role'] == 'instructor':
                    user_info['course'] = '--'.join(user_info['course'])
                # converting user infor values in the dictionary into String
                user_info_values = [str(i) for i in user_info.values()]
                # filtering the nan in order to join all strings together
                filter1 = filter(lambda x: x != "nan", user_info_values)
                filtered_user_info = filter(None, list(filter1))
                return True, ";;;".join(list(filtered_user_info))
        return False, ""

    def check_username_exist(self, username):
        """
        Checking whether username has already existed in users saved
        in data file.

        parameter
        --------
        username: A String representing the username.

        return
        --------
        A boolean indicating whether the username already existed.
        """
        user_dict = self.read_user_info('all')
        # iterating over each user saved in the dictionary
        for user_info in user_dict.values():
            # check if the given username already exists
            if user_info['username'] == username:
                return True
        return False

    def generate_unique_user_id(self):
        """
        Generating a 6 digit unique user id which is not in the saved file.

        return
        --------
        A String representing the generated id.
        """
        stored_id_list = []
        user_dict = self.read_user_info('all')
        # iterating over each user saved in the dictionary,
        # retrieving the user ids
        for user_info in user_dict.values():
            stored_id_list.append(str(user_info['uid']))
        new_id = str(random.randint(100000, 999999))
        # keep generating a new id until the id does not
        # overlap with any existing records
        while new_id in stored_id_list:
            new_id = str(random.randint(100000, 999999))
        return new_id

    def encrypt_password(self, password):
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
        first_char = all_punctuation[len(password) % len(all_punctuation)]
        second_char = all_punctuation[len(password) % 5] * 2
        third_char = all_punctuation[len(password) % 10] * 3
        char_list = [first_char, second_char, third_char]

        encrypted_str = "^^^"  # Adding the start characters.

        # For each character in the input user password,
        # every first, second and third characters will
        # be encrypted with the first, second and third
        # elements in the char_list respectively.
        for i in range(len(password)):
            encrypted_str += char_list[i % 3]
            encrypted_str += password[i]
            encrypted_str += char_list[i % 3]
        encrypted_str += "$$$"  # Adding the end characters.

        self.password = encrypted_str
        return encrypted_str

    def register_user(self, username, password, email, register_time, role):
        """
        Registering a user using the input user information.

        parameter
        --------
        username: A String representing the username.
        password: A String representing the user password.
        email: A String representing the input email.
        register_time: A String representing the time of registration.
        role: A String representing the role of the user.

        return
        --------
        A boolean indicating whether registration was successful.
        """
        if self.check_username_exist(username):
            return False
        uid = self.generate_unique_user_id()
        time = self.date_conversion(register_time)
        password = self.encrypt_password(password)

        # save user info into different formats based on the user role
        registration_str = ''
        if role == 'student':
            registration_str = f'{uid};;;{username};;;{password}' \
                               f';;;{time};;;' \
                               f'{role};;;{email}\n'
        elif role == 'instructor':
            registration_str = f'{uid};;;{username};;;{password}' \
                               f';;;{time};;;' \
                               f'{role};;;{email};;;;;;;;;\n'
        elif role == 'admin':
            registration_str = f'{uid};;;{username};;;{password}' \
                               f';;;{time};;;' \
                               f'{role}\n'

        file_appender = open(user_data_path, 'a')
        file_appender.write(registration_str)
        file_appender.close()
        return True

    def date_conversion(self, register_time):
        """
        Converting the given unix epoch timestamp (milliseconds) to format
        “year-month-day_hour:minute:second.milliseconds”.

        parameter
        --------
        register_time: nix epoch timestamp in milliseconds.

        return
        --------
        A String representing the registration time in format
        “year-month-day_hour:minute:second.milliseconds”.
        """
        msec = register_time % 1000
        sec = register_time // 1000
        minute = (sec % 3600) // 60
        hour = (sec % 86400) // 3600 + 11
        day = get_day_from_timestamp(sec)
        month = (sec % 31556926) // 2629743 + 1
        year = sec // 31556926 + 1970
        return f'{year}-{month}-{day}_{hour}:{minute}:{(sec % 3600) % 60}.{msec}'

    def validate_username(self, username):
        """
        Checking whether username consists of letters or underscore only.

        parameter
        --------
        username: A String representing the username.

        return
        --------
        A boolean indicating whether the username is valid.
        """
        if bool(re.match("^[A-Za-z_]*$", username)):
            return True
        return False

    def validate_password(self, password):
        """
        Checking whether the password length is greater than or equal to 8.

        parameter
        --------
        password: A String representing the user password.

        return
        --------
        A boolean indicating whether the password is valid.
        """
        if len(password) >= 8:
            return True
        return False

    def validate_email(self, email):
        """
        Checking whether the email ends with “.com”, contain “@”, and have length
        greater than 8.

        parameter
        --------
        email: A String representing the input email.

        return
        --------
        A boolean indicating whether the email is valid.
        """
        if bool(re.match(".*@.*.com$", email)) and len(email) > 8:
            return True
        return False

    def clear_user_data(self):
        """
        Removing all the data in the saved user.txt file.
        """
        file_writer = open(user_data_path, 'w')
        file_writer.write("")
        file_writer.close()

    def read_user_info(self, user_role):
        """
        The method reads the saved user info (user.txt) file, converts it into
        a dictionary, and return the dictionary of all users, or just one user
        role based on the input user_role.

        parameter
        --------
        user_role: A String representing the required user_role of information
        extraction.

        return
        --------
        A dictionary contains the information of each user, with the key being
        uid and values containing all user info.
        """

        # read user.txt into a dataframe.
        df = pd.read_csv(user_data_path, sep=';;;',
                         names=['uid', 'username', 'password', 'register_time',
                                'role', 'email', 'display_name', 'job_title',
                                'course'],
                         engine='python')
        df = df.set_index('uid')
        df['uid'] = df.index
        df = df[['uid', 'username', 'password', 'register_time', 'role',
                 'email', 'display_name', 'job_title', 'course']]
        df = df.drop_duplicates(keep='first')
        user_dict = df.to_dict('index')

        for uid, user_info in user_dict.items():
            user_info['uid'] = str(uid)
            # the course string needs to be split into list for
            # instructors
            if user_info['role'] == 'instructor':
                user_info['course'] = user_info['course'].split('--')
            user_dict[uid] = user_info

        # returning a dictionary of either all users, or just one specific
        # user role based on the user_role requirement.
        if user_role == 'all':
            return user_dict
        else:
            final_user_dict = {}
            for uid, user_info in user_dict.items():
                if user_role == 'student' and user_info['role'] == 'student':
                    final_user_dict[uid] = user_info
                elif user_role == 'instructor' \
                        and user_info['role'] == 'instructor':
                    final_user_dict[uid] = user_info
                elif user_role == 'admin' and user_info['role'] == 'admin':
                    final_user_dict[uid] = user_info

            return final_user_dict

    def write_user_into_file(self, user_dict, mode):
        """
        The method writes the user information saved in the user_dict into
        the user.txt file.

        parameter
        --------
        user_dict: A dictionary contains the information of each user,
        with the key being uid and values containing all user info.
        mode: A string representing the file editing mode.
        """
        all_user_str = ""
        for each_user in user_dict.values():
            # Converting the user information string into different formats
            # based on the role of the user.
            if each_user['role'] == 'admin':
                each_user_str = f"{each_user['uid']};;;" \
                                f"{each_user['username']};;;" \
                                f"{each_user['password']};;;" \
                                f"{each_user['register_time']};;;" \
                                f"{each_user['role']}\n"
                all_user_str += each_user_str
            elif each_user['role'] == 'student':
                each_user_str = f"{each_user['uid']};;;" \
                                f"{each_user['username']};;;" \
                                f"{each_user['password']};;;" \
                                f"{each_user['register_time']};;;" \
                                f"{each_user['role']};;;" \
                                f"{each_user['email']}\n"
                all_user_str += each_user_str
            elif each_user['role'] == 'instructor':
                course_list_str = '--'.join(each_user['course'])
                each_user_str = f"{each_user['uid']};;;" \
                                f"{each_user['username']};;;" \
                                f"{each_user['password']};;;" \
                                f"{each_user['register_time']};;;" \
                                f"{each_user['role']};;;" \
                                f"{each_user['email']};;;" \
                                f"{each_user['display_name']};;;" \
                                f"{each_user['job_title']};;;" \
                                f"{course_list_str}\n"
                all_user_str += each_user_str
        file_writer = open(user_data_path, mode)
        file_writer.write(all_user_str)
        file_writer.close()

    def get_source_file_path(self):
        """
        The method finds and saves the path of each json file in the
        sub-folders of the source_course_files folder.

        return
        --------
        source_file_path_list: The list containing the paths of all
        json files, each element representing the path of one json
        file.
        """
        source_file_path_list = []
        source_course_path = os.getcwd() + '/data/source_course_files'
        course_cat_list = os.listdir(source_course_path)
        # Iterating over all categories under the source_course_files folder
        for category in course_cat_list:
            category_path = source_course_path + f'/{category}'
            sub_category_list = os.listdir(category_path)
            # Iterating over all sub_categories under the categories
            for sub_category in sub_category_list:
                sub_category_path = category_path + f'/{sub_category}'
                file_list = os.listdir(sub_category_path)
                # Iterating over each json file under the sub_categories
                for file in file_list:
                    file_path = sub_category_path + f'/{file}'
                    # save the path of each json file to the list
                    source_file_path_list.append(file_path)
        return source_file_path_list
