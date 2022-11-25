"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th


Description: This python Scripts constructs an Instructor class inherited from
the User class, which represents an instructor who can view the courses
taught by himself/herself.
"""

import math
import json

import matplotlib.pyplot as plt
from lib.helper import figure_save_path
from model.user import User


class Instructor(User):
    def __init__(self, uid=-1, username="", password="",
                 register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="instructor",
                 email="", display_name="", job_title="",
                 course_id_list=[]):
        """
        The constructor of the Instructor class, for initiating a new Admin
        object.

        parameter
        --------
        uid: An integer representing the id of the instructor.
        username: A String representing the instructor username.
        password: A String representing the instructor password.
        register_time: A String representing the time of registration.
        role: A String representing the role of the instructor.
        email: A String representing the Instructor email.
        display_name: A String representing the display name of the instructor.
        job_title: A String representing the job title of the instructor.
        course_id_list: A list representing the courses taught by the
        instructor.
        """
        super().__init__(uid, username, password, register_time, role)
        self.email = email
        self.display_name = display_name
        self.job_title = job_title
        self.course_id_list = course_id_list

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the Instructor object.
        """
        course_str = "--".join(self.course_id_list)
        return f'{self.uid};;;{self.username};;;{self.password};;;' \
               f'{self.register_time};;;{self.role};;;{self.email};;;' \
               f'{self.display_name};;;{self.job_title};;;{course_str}'

    def get_instructors(self):
        """
        This method will extract instructor information from the given
        course data files, convert the info into formatted string and
        save them into the user.txt file.

        """
        source_file_path_list = self.get_source_file_path()
        instructor_info_dict = self.read_user_info('instructor')
        # iterating over the path of each json file
        for each_path in source_file_path_list:
            file_reader = open(each_path, "r")
            file_txt = file_reader.read()
            # reading json file into a dictionary
            file_dict = json.loads(file_txt)
            course_list = file_dict['unitinfo']['items']
            # Iterating over each course in the values of 'items'
            for each_course_dict in course_list:
                course_id = str(each_course_dict['id'])
                instructor_list = each_course_dict['visible_instructors']
                # Iterating over each instructor in the values of the
                # 'visible_instructors' key
                for each_instructor in instructor_list:
                    instructor_id = each_instructor['id']
                    # If an instructor is not in the saved user info,
                    # adding the instructor info into the dictionary.
                    if instructor_id not in instructor_info_dict.keys():
                        instructor_display_name = \
                            each_instructor['display_name']
                        instructor_info_dict[instructor_id] = {
                            'uid': str(instructor_id),
                            'username':
                                instructor_display_name.lower().replace(' ',
                                                                        '_'),
                            'password':
                                self.encrypt_password(str(instructor_id)),
                            'register_time': "yyyy-MM-dd_HH:mm:ss.SSS",
                            'role': 'instructor',
                            'email':
                                instructor_display_name.lower().replace(' ',
                                                                        '_')
                                + '@gmail.com',
                            'display_name': instructor_display_name,
                            'job_title': each_instructor['job_title'],
                            'course': [course_id]
                        }
                    # If an instructor is already in the saved user info,
                    # and the course id has not been saved in the course
                    # list taught by this instructor, update the
                    # course_id_list which saves this new course that
                    # the instructor teaches.
                    elif course_id \
                            not in \
                            instructor_info_dict[instructor_id]['course']:
                        instructor_info_dict[instructor_id]['course'].append(
                            course_id)
            file_reader.close()
        # Appending the information in the instructor_info_dict into the
        # user.txt file.
        self.write_user_into_file(instructor_info_dict, 'a')

    def get_instructors_by_page(self, page):
        """
        This method retrieves all the instructor information from saved file,
        and generates a list of Instructor objects on the input page.

        parameter
        --------
        username: An integer representing the page number to retrieve the
        instructors on this page.

        return
        --------
        A tuple containing the list of instructors on the page, total page
        number and the total number of instructors.
        """
        page_max = 20
        instructor_dict = self.read_user_info('instructor')
        # Calculating the total number of instructors and pages.
        total_instructor = len(instructor_dict)
        total_page = math.ceil(total_instructor / page_max)
        instructor_list = list(instructor_dict.values())
        # Dividing the instructor list into chunks, each containing a
        # max number (page_max) of instructors.
        instructor_list = [instructor_list[i:i + page_max] for i
                           in range(0, len(instructor_list), page_max)]
        # Trying retrieving the instructor list based on the page number.
        try:
            instructor_page = instructor_list[page - 1]
        # If an error occurs, set the instructor_page to an empty list.
        except Exception:
            instructor_page = []
        # Converting the dictionary items of instructor information into
        # a list of instructor objects.
        instructor_obj_list = [Instructor(each['uid'], each['username'],
                                          each['password'],
                                          each['register_time'],
                                          each['role'], each['email'],
                                          each['display_name'],
                                          each['job_title'],
                                          each['course']) for each
                               in instructor_page]
        return instructor_obj_list, total_page, total_instructor

    def generate_instructor_figure1(self):
        """
        This method generates a graph that shows the top 10 instructors
        who teach the most courses.

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        instructor_dict = self.read_user_info('instructor')
        # If there are no saved instructor information, generates a
        # blank image and returns a message.
        if len(instructor_dict) == 0:
            plt.savefig(figure_save_path + 'instructor_figure1.png')
            return "No data to make the chart."

        # sort the dictionary based on descending order of the number
        # of courses in the course_list taught by the instructors.
        instructor_dict = {k: v for k, v
                           in sorted(instructor_dict.items(),
                                     key=lambda item: len(item[1]['course']),
                                     reverse=True)}
        # Getting the title and the course number of top 10 instructors.
        top_10_list = list(instructor_dict.values())[:10]
        instructor_title = []
        course_num = []
        for each in top_10_list:
            name_words = each['display_name'].split(' ')
            if len(name_words) > 3:
                each['display_name'] = ' '.join(name_words[:3])
            instructor_title.append(each['display_name'])
            course_num.append(len(each['course']))

        # Making a bar chart and adjusting formats.
        plt.figure(figsize=(10, 5))
        plt.bar(instructor_title, course_num, width=0.7,
                color='#7eb54e', edgecolor='pink')
        plt.xlabel('Instructor title')
        plt.ylabel('Number of courses')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.ylim(20, 32)
        plt.title("The Top 10 Instructors Who Teach the Most Courses", x=0.6, y=0.9)
        plt.savefig(figure_save_path + 'instructor_figure1.png')
        plt.close()

        # Adding an interpretation of the chart.
        understanding = "The bar chart shows that the top 10 instructors who teach the most courses" \
                        " teach around 20-30 courses. Jude Coffey is the instructor who teaches the" \
                        " most courses."
        return understanding
