"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs a Student class inherited from the
User class, which represents a student who can either view courses enrolled
by himself/herself or view reviews written by himself/herself .
"""


from Course import Course
from Review import Review
from User import User


class Student(User):

    def __init__(self, id=-1, username="", password="", user_title = "",
                 user_image_50x50="", user_initials="",
                 review_id=-1):
        """
        The constructor of the Student class, for initiating a new Student
        object.

        parameter
        --------
        id: An integer representing the id of the student.
        username: A String representing the username of the student.
        password: A String representing the password of the student.
        user_title = A String representing the title of the student.
        user_image_50x50 = A String representing the image of the student.
        user_initials = A String representing the initials of the student
        review_id: An integer representing the id of the review written
        by the student.

        """
        self.id = id
        self.username = username
        self.password = password
        self.user_title = user_title
        self.user_image_50x50 = user_image_50x50
        self.user_initials = user_initials
        self.review_id = review_id

    def view_courses(self, args=[]):
        """
        The view_courses function will find the course registered by the student
        using the Student object's review id, and print the course.

        parameter
        --------
        input_password: the password string that needs to be encrypted.

        """
        util_review = Review()
        # find the course id according to review id.
        stu_course_id = \
            str(util_review.find_review_by_id(self.review_id).course_id).strip()
        util_course = Course()

        # find the course enrolled by the student according to course id.
        stu_course_obj = util_course.find_course_by_id(stu_course_id)
        print('The course registered by the student:\n')
        print(stu_course_obj)

    def view_reviews(self, args=[]):
        """
        The view_reviews function will find the review written by the
        student using the Student object's review id, and print the review.

        parameter
        --------
        input_password: the password string that needs to be encrypted.

        """
        util_review = Review()

        # find the review written by the student according to review id.
        review_obj = str(util_review.find_review_by_id(self.review_id)).strip()
        print('The review written by the student:\n')
        print(review_obj)

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the Student object.

        """
        return super().__str__() + f';;;{self.user_title};;;{self.user_image_50x50};;;{self.user_initials};;;' \
                                   f'{self.review_id}'
