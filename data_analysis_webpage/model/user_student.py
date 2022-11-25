"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts constructs a Student class inherited from the
User class, which represents a student who has an email and can be found by
 page or student id.
"""

from model.user import User
import math


class Student(User):

    def __init__(self, uid=-1, username="", password="",
                 register_time="yyyy-MM-dd_HH:mm:ss.SSS",
                 role="", email=""):
        """
        The constructor of the Student class, for initiating a new Student
        object.

        parameter
        --------
        uid: An integer representing the id of the user.
        username: A String representing the username.
        password: A String representing the user password.
        register_time: A String representing the time of registration.
        role: A String representing the role of the user.
        email: A String representing the Student email.
        """
        super().__init__(uid, username, password, register_time, role)
        self.email = email

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the Student object.
        """
        return f'{self.uid};;;{self.username};;;{self.password};;;' \
               f'{self.register_time};;;{self.role};;;{self.email}'

    def get_students_by_page(self, page):
        """
        This method retrieves all the student information from saved file,
        and generates a list of student objects on the input page.

        parameter
        --------
        page: An integer representing the page number to retrieve the
        students on this page.

        return
        --------
        A tuple containing the list of students on the page, total page
        number and the total number of students.
        """
        page_max = 20
        student_dict = self.read_user_info('student')
        # Calculating the total number of students and pages.
        total_student = len(student_dict)
        total_page = math.ceil(total_student / 20)
        student_list = list(student_dict.values())
        # Dividing the student list into chunks, each containing a
        # max number (page_max) of students.
        student_list = [student_list[i:i + page_max] for
                        i in range(0, len(student_list), page_max)]
        # Trying retrieving the student list based on the page number.
        try:
            student_page = student_list[page - 1]
        # If an error occurs, set the student_page to an empty list.
        except Exception:
            student_page = []
        # Converting the dictionary items of student information into
        # a list of student objects.
        student_obj_list = [Student(each['uid'], each['username'],
                                    each['password'],
                                    each['register_time'],
                                    each['role'], each['email']) for
                            each in student_page]
        return student_obj_list, total_page, total_student

    def get_student_by_id(self, id):
        """
        This method returns a student object by retrieving the id
        from the user.txt file.

        id
        --------
        id: An integer representing the id of the student.

        return
        --------
        A student object found according to the provided object, or
        none in error conditions.
        """
        id = int(id)
        student_dict = self.read_user_info('student')
        # If the id can be found in the saved user file, generating
        # and return the Student object.
        if id in student_dict.keys():
            info = student_dict[id]
            return Student(info['uid'], info['username'],
                           info['password'],
                           info['register_time'], info['role'],
                           info['email'])
        # Else returning None.
        else:
            return None

    def delete_student_by_id(self, id):
        """
        This method deletes a student item from the user.txt file
        based on the given id.

        id
        --------
        id: An integer representing the id of the student.

        return
        --------
        A boolean representing whether the deletion was successful.
        """
        student_dict = self.read_user_info('student')
        id = int(id)
        # deleting the student info if the id can be found in
        # the saved user info file.
        if id in student_dict.keys():
            user_dict = self.read_user_info('all')
            del user_dict[id]
            self.write_user_into_file(user_dict, 'w')
            return True
        # returning false if the id cannot be found
        return False
