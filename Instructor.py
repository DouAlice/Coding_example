"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs an Instructor class inherited from
the User class, which represents an instructor who can either view the courses
taught by himself/herself or view reviews of those courses.
"""

import os
import re

from Course import Course
from Review import Review
from User import User


class Instructor(User):

    def __init__(self, id=-1, username="", password="", display_name="",
                 job_title="", image_100x100="", course_id_list=[]):
        """
        The constructor of the Instructor class, for initiating a new Instructor
        object.

        parameter
        --------
        id: An integer representing the id of the instructor.
        username: A String representing the username of the instructor.
        password: A String representing the password of the instructor.
        display_name = A String representing the display name of the instructor.
        job_title = A String representing the job title of the instructor.
        image_100x100 = A String representing the image of the instructor.
        course_id_list = A list with items being the id of the courses
        taught by the instructor.

        """
        self.id = id
        self.username = username
        self.password = password
        self.display_name = display_name
        self.job_title = job_title
        self.image_100x100 = image_100x100
        self.course_id_list = course_id_list

    def view_courses(self, args=[]):
        """
        The view_courses function will find the courses taught by the instructor
        using the Instructor object's id, and print the courses.

        parameter
        --------
        args: A list by default is [] which does not need to be entered here.

        return
        --------
        course_obj_list: The list contains all the Course objects that has been
        found according to the instructor id.
        """
        util_courses = Course()
        course_obj_list = util_courses.find_course_by_instructor_id(self.id)

        # If the number of reviews is greater than 10, only print 10 reviews.
        if len(course_obj_list) > 10:
            print(f'==========================================================='
                  f'=================================\n'
                  f"There are {len(course_obj_list)} courses in total, "
                  f"only the first 10 will be printed.")
            for i in range(10):
                print(course_obj_list[i])
        else:
            print(f"There are {len(course_obj_list)} courses in total: ")
            for course_obj in course_obj_list:
                print(course_obj)
        return course_obj_list

    def view_reviews(self, args=[]):
        """
        The view_reviews function will find the reviews for the courses taught
        by the instructor using the Instructor object's id, and print the reviews.

        parameter
        --------
        args: A list by default is [] which does not need to be entered here.
        """
        course_obj_list = self.view_courses()
        util_review = Review()
        for each_course in course_obj_list:
            review_obj_list = \
                util_review.find_review_by_course_id(each_course.course_id)
            # If no reviews can be found for the course, print a message.
            if review_obj_list is None:
                print(f'==================================================='
                      f'=========================================\n'
                      f'\nThe course "{each_course.course_title}" '
                      f'with id {each_course.course_id} has no reviews.')
            # If the number of reviews is greater than 10, only print 10 reviews.
            elif len(review_obj_list) > 10:
                print(f'===================================================='
                      f'========================================\n'
                      f'\nThe total number of reviews: {len(review_obj_list)}.'
                      f'\nAs there are more than 10 reviews for'
                      f'this course, only the first 10 will be displayed.\n'
                      f' Below are the reviews for course '
                      f'"{each_course.course_title}" '
                      f'with id {each_course.course_id}:'
                      )
                for i in range(10):
                    print(review_obj_list[i].content)
            else:
                print(f'==================================================='
                      f'=========================================\n'
                      f'\nThe total number of reviews: {len(review_obj_list)}.'
                      f'\nBelow are the reviews for course '
                      f'"{each_course.course_title}" '
                      f'with id {each_course.course_id}:\n')

                for each_review in review_obj_list:
                    print(each_review.content)

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the instructor object.

        """
        instructor_info = super().__str__() + \
                          f';;;{self.display_name};;;{self.job_title};;;' \
                          f'{self.image_100x100}'
        for each_course in self.course_id_list:
            instructor_info += ";;;"
            instructor_info += each_course

        return instructor_info