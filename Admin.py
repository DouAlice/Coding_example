"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Script constructs an Admin class inherited from the
User class, which represents an administrator who have permission to extract,
remove and view information of students, instructors, reviews and courses.

"""

import os
import re

from Course import Course
from Review import Review
from User import User


class Admin(User):

    def register_admin(self):
        """
        The register_admin function will check if the admin info has been
        registered already, if not, it will register the admin.

        """
        # extract admin information and store in a dictionary.
        admin_dict = self.extract_admin_dict()

        # iterate over each admin stored in the dictionary, if the current
        # username matches with the stored username, change the is_registered
        # boolean variable to True, otherwise stays False.
        is_registered = False
        for each_admin in admin_dict.values():
            if each_admin['username'] == self.username:
                is_registered = True

        # If is_registered is False, store the admin information as a
        # String, append this to the stored user_admin.txt.
        if not is_registered:
            admin_str = f'{self.id};;;{self.username};;;' \
                        f'{self.encryption(self.password)}\n'
            file_writer = open(
                './data/result/user_admin.txt',
                'a', encoding="utf-8")
            file_writer.write(admin_str)
            file_writer.close()

    def extract_course_info(self):
        """
        The extract_course_info function will extract all course information
        from the raw.data.txt and store them in course.txt.

        """
        print("The system is extracting course information...")

        # Read raw_data.txt as a String, split the String into a list,
        # separated by '{"unit":'.
        file_handler = open(
            './data/course_data/raw_data.txt', encoding="utf-8")
        course_data_str = file_handler.read()
        course_data_list = course_data_str.split('{"unit":')[1:]

        # Create empty lists to store each course information attribute.
        course_id_list = []
        course_title_list = []
        course_image_list = []
        course_headline_list = []
        course_num_sub_list = []
        course_avg_rating_list = []
        course_content_len_list = []

        # Iterate over each unit in the list, truncate the part of
        # the unit that is relevant to the course items. Use regular
        # expressions to find course_id, course_title, course_image,
        # course_headline, course_num_sub, course_avg_rating and
        # course_content_len. Append this information to the lists
        # storing the course info.
        for unit in course_data_list:
            item = unit.split('"items":[')[1].split(
                '"remaining_item_count":')[0]

            id_pattern = r'"course","id":(\d+)'
            course_id = re.findall(id_pattern, item)
            course_id_list.append(course_id)

            title_pattern = \
                r'"_class":"course","id":\d+,"title":"(.*?)","url":'
            course_title = re.findall(title_pattern, item)
            course_title_list.append(course_title)

            image_pattern = r'"image_100x100":([^,]*),"image_304x171":'
            course_image = re.findall(image_pattern, item)
            course_image_list.append(course_image)

            headline_pattern = r'"headline":"(.*?)","num_subscribers":'
            course_headline = re.findall(headline_pattern, item)
            course_headline_list.append(course_headline)

            num_sub_pattern = r'"num_subscribers":([^,]*),"caption_locales":'
            course_num_sub = re.findall(num_sub_pattern, item)
            course_num_sub_list.append(course_num_sub)

            avg_rating_pattern = r'"avg_rating":([^,]*),"avg_rating_recent":'
            course_avg_rating = re.findall(avg_rating_pattern, item)
            course_avg_rating_list.append(course_avg_rating)

            content_len_pattern = r'"content_info":"(.*?) '
            course_content_len = re.findall(content_len_pattern, item)
            course_content_len_list.append(course_content_len)

        saved_course = ""
        # Iterate over the length of course_id_list.
        for i in range(len(course_id_list)):
            # Iterate over the length of each item in the course_id_list.
            for j in range(len(course_id_list[i])):
                # Concat the information for each course.
                saved_course += f'{course_id_list[i][j]};;;' \
                                f'{course_title_list[i][j]};;;' \
                                f'{course_image_list[i][j]};;;' \
                                f'{course_headline_list[i][j]};;;' \
                                f'{course_num_sub_list[i][j]};;;' \
                                f'{course_avg_rating_list[i][j]};;;' \
                                f'{course_content_len_list[i][j]}\n'

        # Open a file course.txt to store the course information String.
        file_writer = open(
            './data/result/course.txt', 'w', encoding="utf-8")
        file_writer.write(saved_course)
        file_writer.close()
        file_handler.close()

    def extract_review_info(self):
        """
        The extract_review_info function will extract all review information
        from all files in the review_data folder and store them in review.txt.

        """
        print("The system is extracting review information...")

        file_writer = open(
            './data/result/review.txt', 'w', encoding="utf-8")
        # Create a list containing the names of the files in the review_data
        # folder.
        all_review_files = os.listdir(
            './data/review_data')

        # Create empty lists to store each review information attribute.
        course_id_list = []
        review_id_list = []
        review_content_list = []
        review_rating_list = []
        i = 0

        # Iterate over each review file in the review_data folder,
        # Find course_id in the name of the review file.
        # Use regular expressions to find review_id, review_content,
        # review_rating. Append this information to the lists
        # storing the review info.
        for review_file in all_review_files:
            file_handler = open(
                f"./data/review_data/{review_file}",
                'r', encoding="utf-8")

            course_id = review_file.split(".json")[0]
            course_id_list.append(course_id)

            review_str = file_handler.read()

            id_pattern = \
                r'\"_class\": \"course_review\", \"id\": (\d+), "content":'
            review_id = re.findall(id_pattern, review_str)
            review_id_list.append(review_id)

            content_pattern = \
                r'\"_class\": \"course_review\", \"id\": \d+, \"content\": "(.*?)",'
            review_content = re.findall(content_pattern, review_str)
            review_content_list.append(review_content)

            rating_pattern = \
                r'\"rating\": (.*?), \"created\":'
            review_rating = re.findall(rating_pattern, review_str)
            review_rating_list.append(review_rating)

        saved_review = ""
        # Iterate over the length of review_id_list.
        for i in range(len(review_id_list)):
            # Iterate over the length of each item in the review_id_list.
            for j in range(len(review_id_list[i])):
                # Concat the information for each review.
                saved_review += f'{review_id_list[i][j]};;;' \
                                f'{review_content_list[i][j]};;;' \
                                f'{review_rating_list[i][j]};;;' \
                                f'{course_id_list[i]}\n'

        # Open a file review.txt to store the course information String.
        file_writer = open(
            './data/result/review.txt',
            'w', encoding="utf-8")
        file_writer.write(saved_review)
        file_handler.close()
        file_writer.close()

    def extract_students_info(self):
        """
        The extract_review_info function will extract all student
        information from all files in the review_data folder and store them
        in student.txt.

        """
        print("The system is extracting student information...")
        file_writer = open(
            './data/result/user_student.txt',
            'w', encoding="utf-8")
        # Create a list containing the names of the files in the review_data
        # folder.
        all_review_files = os.listdir(
            './data/review_data')

        saved_student = ""

        # Iterate over each review file in the review_data folder,
        # read the file as a String, split the String into a list,
        # separated by '"_class": "course_review",'.
        for review_file in all_review_files:
            file_handler = open(
                f"./data/review_data/{review_file}",
                'r', encoding="utf-8")
            review_str = file_handler.read()
            review_list = review_str.split('"_class": "course_review",')[1:]

            # iterating over each review in the review_list, use regular
            # expressions to find review_id, student_id, student_title,
            # student_image, student_initial. Append this information to the
            # lists storing the student info.
            for each_review in review_list:
                id_pattern = r'"id": (\d+),'
                review_id = re.findall(id_pattern, each_review)[0]

                student_pattern = r'"_class": "user"(.*?)."response":'
                each_student = re.findall(student_pattern, each_review)[0]

                # try finding a student id. If the id could not be found,
                # generate a unique id for the student.
                try:
                    student_id_pattern = r'"id": (\d+),'
                    student_id = \
                        re.findall(student_id_pattern, each_student)[0]
                except:
                    student_id = self.generate_unique_user_id()

                student_title_pattern = r'"title": "(.*?)",'
                student_title = \
                    re.findall(student_title_pattern, each_student)[0]

                student_image_pattern = r'"image_50x50": "(.*?)"'
                student_image = \
                    re.findall(student_image_pattern, each_student)[0]

                student_initial_pattern = r'"initials": "(.*?)"'
                student_initial = \
                    re.findall(student_initial_pattern, each_student)[0]

                # Concat the information for each student.
                saved_student += \
                    f'{student_id};;;' \
                    f'{student_title.lower().replace(" ", "_")}' \
                    f';;;' \
                    + self.encryption(f'{student_initial.lower()}{student_id}' \
                                      f'{student_initial.lower()}') + \
                    f';;;{student_title}' \
                    f';;;{student_image}' \
                    f';;;{student_initial}' \
                    f';;;{review_id}\n'

        file_writer.write(saved_student)
        file_writer.close()
        file_handler.close()

    def extract_instructor_info(self):
        """
        The extract_instructor_info function will extract all instructor
        information from the raw.data.txt file and store them in course.txt.

        """
        print("The system is extracting instructor information...")

        file_handler = open(
            './data/course_data/raw_data.txt',
            'r', encoding="utf-8")
        instructor_data_str = file_handler.read()

        # Use regular expressions to find instructor id, display_name,
        # job_title, image and course, store them in seperate lists.
        id_pattern = r'"visible_instructors".*?"id":(\d+)'
        instructor_id_list = re.findall(id_pattern, instructor_data_str)

        name_pattern = r'"visible_instructors".*?"display_name":"(.*?)"'
        instructor_display_name_list = \
            re.findall(name_pattern, instructor_data_str)

        job_pattern = r'"visible_instructors".*?"job_title":"(.*?)"'
        instructor_job_title_list = \
            re.findall(job_pattern, instructor_data_str)

        image_pattern = r'"visible_instructors".*?"image_100x100":"(.*?)"'
        instructor_image_list = \
            re.findall(image_pattern, instructor_data_str)

        course_pattern = r'"_class":"course","id":(\d*)'
        instructor_course_list = \
            re.findall(course_pattern, instructor_data_str)

        file_handler.close()

        file_writer = open(
            './data/result/user_instructor.txt',
            'w+', encoding="utf-8")

        saved_instructor = file_writer.read()

        # Iterate over the length of instructor_id_list.
        for index in range(len(instructor_id_list)):
            # If the instructor id cannot be found in the saved instructor info
            # , create a new String of the instructor information and concat it
            # to the saved instructor info.
            if not bool(re.findall(instructor_id_list[index] +
                                   r';;;?', saved_instructor)):
                saved_instructor += \
                    f'{instructor_id_list[index]};;;' \
                    f'{instructor_display_name_list[index].lower().replace(" ", "_")}' \
                    f';;;' + \
                    self.encryption(instructor_id_list[index]) + \
                    f';;;{instructor_display_name_list[index]};;;' \
                    f'{instructor_job_title_list[index]};;;' \
                    f'{instructor_image_list[index]};;;' \
                    f'{instructor_course_list[index]}\n'

            # If the instructor id is already in the saved instructor info, find
            # the line contains this instructor id, append the new course to the
            # end of the String.
            else:
                instructor_pattern = r';;;.*?\n'
                existing_instructor = re.findall(instructor_id_list[index] +
                                                 instructor_pattern,
                                                 saved_instructor)[0]
                existing_instructor_add = \
                    existing_instructor.replace("\n", "") + \
                    f"--{instructor_course_list[index]}\n"
                saved_instructor = \
                    saved_instructor.replace(existing_instructor,
                                             existing_instructor_add)

        file_writer.write(saved_instructor)
        file_writer.close()

    def extract_info(self):
        """
        The extract_info function will extract all course, student, review and
        instructor information.

        """
        self.extract_course_info()
        self.extract_review_info()
        self.extract_instructor_info()
        self.extract_students_info()

    def remove_data(self):
        """
        The remove_data function will remove all stored course, student, review
        and instructor information.

        """
        review_writer = open(
            './data/result/review.txt', 'w+', encoding="utf-8")
        stu_writer = open(
            './data/result/user_student.txt',
            'w+', encoding="utf-8")
        ins_writer = open(
            './data/result/user_instructor.txt',
            'w+', encoding="utf-8")
        course_writer = open(
            './data/result/course.txt', 'w+', encoding="utf-8")

        # remove data by write replace the file content with empty String.
        review_writer.write("")
        stu_writer.write("")
        ins_writer.write("")
        course_writer.write("")

        review_writer.close()
        stu_writer.close()
        ins_writer.close()
        course_writer.close()

    def view_courses(self, args):
        """
        The view_courses function will find the courses according to the
        provided title keyword, course id or instructor id and print the
        courses, or print a course overview.

        parameter
        --------
        args: An empty list or a list with two elements. The first element
        is the command (can only be “TITLE_KEYWORD/ID/INSTRUCTOR_ID”) and
        the second element is the value (could be title keyword, course id
        or instructor id).

        return
        --------
        A list containing course objects, a single course object or None.

        """

        util_course = Course()
        # Do a course overview if args is an empty list.
        if not args:
            print("========================================course overview"
                  "========================================")
            print(util_course.course_overview())

        # Search relevant courses according to the command and the value
        # in args. Display warning messages if the length or content of
        # the provided command and value are invalid.
        else:
            if args[0] == "TITLE_KEYWORD":
                if len(args) == 1:
                    print("Please provide a valid title keyword to search "
                          "for after the 'TITLE_KEYWORD' command. "
                          "The keyword cannot be empty.")
                    return None
                course_obj_list = \
                    util_course.find_course_by_title_keyword(args[1])
                print("========================================view courses"
                      " by keyword================================"
                      "========")
                if not course_obj_list:
                    print(f'No courses were found according to the title '
                          f'keyword "{args[1]}" provide by you.')
                else:
                    for each_course in course_obj_list:
                        print(each_course)
                return course_obj_list
            elif args[0] == "ID":
                if len(args) == 1:
                    print("Please provide a valid ID to search for after "
                          "the 'ID' command. "
                          "The ID cannot be empty.")
                    return None
                elif not args[1].isdigit():
                    print("Invalid ID input. The input must contain digits"
                          " only.")
                    return None
                course_obj = util_course.find_course_by_id(args[1])
                print("========================================view courses"
                      " by ID====================================="
                      "===")
                if not course_obj:
                    print(f'No course were was according to the course ID'
                          f' "{args[1]}" provide by you.')
                else:
                    print(course_obj)
                return course_obj
            elif args[0] == "INSTRUCTOR_ID":
                if len(args) == 1:
                    print("Please provide a valid ID to search for after "
                          "the 'INSTRUCTOR_ID' command. "
                          "The ID cannot be empty.")
                    return None
                elif not args[1].isdigit():
                    print("Invalid INSTRUCTOR_ID input. The INSTRUCTOR_ID "
                          "input must contain digits only.")
                    return None
                course_obj_list = \
                    util_course.find_course_by_instructor_id(args[1])
                print("========================================view courses"
                      " by instructor ID==========================="
                      "=============")
                if not course_obj_list:
                    print(f'No courses were found according to the instructor'
                          f' ID "{args[1]}" provide by you.')
                else:
                    for each_course in course_obj_list:
                        print(each_course)
                return course_obj_list
            else:
                print('Please provide a valid second command. For option 2, '
                      'the second command can only be one of '
                      '“TITLE_KEYWORD", "ID" or "INSTRUCTOR_ID"')

    def view_users(self):
        """
        The view_users function will find the total number for each type of
        users and display a message.

        """
        admin_reader = open(
            './data/result/user_admin.txt', 'r', encoding="utf-8")
        stu_reader = open(
            './data/result/user_student.txt',
            'r', encoding="utf-8")
        ins_reader = open(
            './data/result/user_instructor.txt',
            'r', encoding="utf-8")
        admin_str = admin_reader.read()
        stu_str = stu_reader.read()
        ins_str = ins_reader.read()

        # find the number of lines in each of String to determine the
        # number of admin, students, and isntructors.
        num_admin = len(admin_str.splitlines())
        num_stu = len(stu_str.splitlines())
        num_ins = len(ins_str.splitlines())
        print(f"The total number for each type of users: \nThere are"
              f" {num_admin} administrators in total.\n"
              f"There are {num_ins} instructors in total.\nThere are"
              f" {num_stu} students in total.")

    def view_reviews(self, args):
        """
        The view_reviews function will find the reviews according to
        the provided keyword, review id or course id and print the
        reviews, or print a review overview.

        parameter
        --------
        args: An empty list or a list with two elements. The first
        element is the command (can only be “ID/KEYWORD/COURSE_ID”)
        and the second element is the value (could be review id,
        review keyword or course id).

        return
        --------
        A list containing review objects, a single review object or None.

        """
        util_review = Review()

        # Do a review overview if args is an empty list.
        if not args:
            print("========================================"
                  "review overview========================================")
            print(util_review.review_overview())

        # Search relevant reviews according to the command and the value
        # in args. Display warning messages if the length or content of
        # the provided command and value are invalid.
        else:
            if args[0] == "KEYWORD":
                if len(args) == 1:
                    print("Please provide a valid title keyword to search "
                          "for after the 'KEYWORD' command. "
                          "The keyword cannot be empty.")
                    return None
                print("========================================"
                      "view reviews by keyword================================"
                      "========")
                review_obj_list = util_review.find_review_by_keywords(args[1])
                if not review_obj_list:
                    print(f'No reviews were found according to the keyword'
                          f' "{args[1]}" provide by you.')
                else:
                    for each_course in review_obj_list:
                        print(each_course)
                return review_obj_list
            elif args[0] == "ID":
                if len(args) == 1:
                    print("Please provide a valid ID to search for after the"
                          " 'ID' command. "
                          "The ID cannot be empty.")
                    return None
                elif not args[1].isdigit():
                    print("Invalid ID value. "
                          "The ID value must contain digits only.")
                    return None
                print("========================================view reviews by "
                      "id========================================")
                review_obj = util_review.find_review_by_id(args[1])
                if not review_obj:
                    print(f'No review was found according to '
                          f'the ID "{args[1]}" provide by you.')
                else:
                    print(review_obj)
                return review_obj
            elif args[0] == "COURSE_ID":
                if len(args) == 1:
                    print("Please provide a valid ID to search for after "
                          "the 'COURSE_ID' command. "
                          "The ID cannot be empty.")
                    return None
                elif not args[1].isdigit():
                    print("Invalid COURSE_ID input. The COURSE_ID input "
                          "must contain digits only.")
                    return None
                print("========================================"
                      "view reviews by course "
                      "id========================================")
                review_obj_list = util_review.find_review_by_course_id(args[1])
                if not review_obj_list:
                    print(f'No reviews were found according to the course '
                          f'ID "{args[1]}" provide by you.')
                else:
                    for each_course in review_obj_list:
                        print(each_course)
                return util_review.find_review_by_course_id(args[1])
            else:
                print('Please provide a valid second command. '
                      'For option 4, the second command can only '
                      'be one of “KEYWORD", "ID" or "COURSE_ID"')
