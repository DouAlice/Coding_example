"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs a Course class, which represents
a course that can be found by title keyword, course id and instructor id.

"""

from User import User


class Course:

    def __init__(self, course_id=-1, course_title="",
                 course_image_100x100="", course_headline="",
                 course_num_subscribers=-1, course_avg_rating=-1.0,
                 course_content_length=-1.0):
        """
        The constructor of the Course class, for initiating a new Course
        object.

        parameter
        --------
        course_id: An integer representing the id of the course.
        course_title: A String representing the title of the course.
        course_image_100x100: A String representing the image of the course.
        course_headline: A String representing the headline of the course.
        course_num_subscribers: An integer representing the number of
        subscribers of the course.
        course_avg_rating: An float representing the average rating
        of the course.
        course_content_length: An float representing the content length
        of the course.
        """

        self.course_id = course_id
        self.course_title = course_title
        self.course_image_100x100 = course_image_100x100
        self.course_headline = course_headline
        self.course_num_subscribers = course_num_subscribers
        self.course_avg_rating = course_avg_rating
        self.course_content_length = course_content_length

    def find_course_by_title_keyword(self, keyword):
        """
        The find_course_by_title_keyword function will find the courses
        that contain the input keyword in the title.

        parameter
        --------
        keyword: A string representing the title keyword.

        return
        --------
        course_obj_list: The list contains all the Course objects that
        has been found according to the title keyword.
        """
        file_handler = open(
            './data/result/course.txt', 'r', encoding="utf-8")
        course_list = file_handler.readlines()
        file_handler.close()
        course_obj_list = []

        # Iterate over each course in the course_list, if the keyword
        # can be found in the course_content of a course, use the info
        # of this course to create a course object. Add this object
        # into the course_obj_list.
        for each_course in course_list:
            stored_course_info = each_course.split(";;;")
            stored_course_content = stored_course_info[1]
            if keyword in stored_course_content:
                course_obj = Course(stored_course_info[0],
                                    stored_course_info[1],
                                    stored_course_info[2],
                                    stored_course_info[3],
                                    stored_course_info[4],
                                    stored_course_info[5],
                                    stored_course_info[6])
                course_obj_list.append(course_obj)
        return course_obj_list

    def find_course_by_id(self, course_id):
        """
        The find_course_by_id function will find the course according
        to the course id.

        parameter
        --------
        course_id: A string or an int representing the course id.

        return
        --------
        course_obj: The Course object that has been found according
        to the course id.
        """
        file_handler = open(
            './data/result/course.txt', 'r', encoding="utf-8")
        course_list = file_handler.readlines()
        file_handler.close()

        # Iterate over each course in the course_list, if the course id
        # matches with the id of a course, use the info
        # of this course to create a course object. Add this object
        # into the course_obj_list.
        for each_course in course_list:
            stored_course_info = each_course.split(";;;")
            stored_course_id = stored_course_info[0]
            if str(course_id) in stored_course_id:
                course_obj = Course(stored_course_info[0],
                                    stored_course_info[1],
                                    stored_course_info[2],
                                    stored_course_info[3],
                                    stored_course_info[4],
                                    stored_course_info[5],
                                    stored_course_info[6])
                return course_obj
        return None

    def find_course_by_instructor_id(self, instructor_id):
        """
        The find_course_by_instructor_id function will find the course
        according to the instructor id.

        parameter
        --------
        instructor_id: A string or an int representing the instructor id.

        return
        --------
        course_obj_list: The list contains all the Course objects that
        has been found according to the instructor id.
        """
        util_user = User()
        ins_dict = util_user.extract_instructor_dict()
        course_obj_list = []
        course_id_list = []

        # Iterate over each item in the instructor info dictionary,
        # if the instructor id matches with the id of a course, store
        # the id of all courses taught by this instructor in the
        # course_id_list.
        for stored_instructor_id, stored_instructor_info in ins_dict.items():
            if stored_instructor_id == str(instructor_id):
                course_id_list = stored_instructor_info['course'].split("--")
                break
        # Iterate over each course in the course_id_list, find
        # each course according to the course id and create an object.
        # append this oject to the course_obj_list.
        for each_course in course_id_list:
            course_obj_list.append(self.find_course_by_id(each_course))
        return course_obj_list

    def course_overview(self):
        """
        The course_overview function will print the total number of courses.

        return
        --------
        A String that displays the total number of courses.

        """
        file_handler = open(
            './data/result/course.txt', 'r', encoding="utf-8")
        course_str = file_handler.read()

        # Determine the number of courses by the number of lines in
        # the course_str.
        course_list = course_str.splitlines()
        return f'The total number of course is: {len(course_list)}.'

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the course object.

        """
        return f'course id: {self.course_id}\ncourse title: {self.course_title}\ncourse image: ' \
               f'{self.course_image_100x100}\ncourse headline: {self.course_headline}\n' \
               f'number of subscribers: {self.course_num_subscribers}\n average rating: {self.course_avg_rating}' \
               f'\ncourse content length: {self.course_content_length}\n'
