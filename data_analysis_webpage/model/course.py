"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts constructs a Course class, which
represents a specific course recorded in the data analysis system,
under a specific category and subcategory. The course can be found
by course id, instructor id and page.
"""

import json
from lib.helper import course_data_path, figure_save_path
from model.user import User
import pandas as pd
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Course:

    def __init__(self, category_title="", subcategory_id=-1,
                 subcategory_title="", subcategory_description="",
                 subcategory_url="", course_id=-1,
                 course_title="", course_url="", num_of_subscribers=0,
                 avg_rating=0.0, num_of_reviews=0):
        """
        The constructor of the Course class, for initiating a new Course
        object.

        parameter
        --------
        category_title: A String representing the category title.
        subcategory_id: An integer representing the id of the category.
        subcategory_title: A String representing the subcategory title.
        subcategory_description: A String representing the subcategory
        description.
        subcategory_url: A String representing the url of the subcategory.
        course_id: An integer representing the id of the course.
        course_title: A String representing the course title.
        course_url: A String representing the course url.
        num_of_subscribers: An integer representing the number of
        subscribers.
        avg_rating: An integer representing the average rating of the
        course.
        num_of_reviews: An integer representing the number of reviews
        for the course.
        """
        self.category_title = category_title
        self.subcategory_id = subcategory_id
        self.subcategory_title = subcategory_title
        self.subcategory_description = subcategory_description
        self.subcategory_url = subcategory_url
        self.course_id = course_id
        self.course_title = course_title
        self.course_url = course_url
        self.num_of_subscribers = num_of_subscribers
        self.avg_rating = avg_rating
        self.num_of_reviews = num_of_reviews

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the Course object.
        """
        return f'{self.category_title};;;{self.subcategory_id};;;' \
               f'{self.subcategory_title};;;' \
               f'{self.subcategory_description};;;' \
               f'{self.subcategory_url};;;{self.course_id};;;' \
               f'{self.course_title};;;{self.course_url};;;' \
               f'{self.num_of_subscribers};;;' \
               f'{self.avg_rating};;;{self.num_of_reviews}'

    def get_courses(self):
        """
        This method will extract course information from the given
        course data file, convert them into formatted String and
        save into the course.txt file.
        """
        util_user = User()
        source_file_path_list = util_user.get_source_file_path()
        course_str = ""
        # iterating over the path of each json file
        for each_path in source_file_path_list:
            file_reader = open(each_path, "r")
            file_txt = file_reader.read()
            file_dict = json.loads(file_txt)
            category_title = file_dict['unitinfo']['category']
            sub_cat = file_dict['unitinfo']['source_objects'][0]
            subcategory_id = sub_cat['id']
            subcategory_title = sub_cat['title']
            subcategory_description = sub_cat['description']
            subcategory_url = sub_cat['url']
            course_list = file_dict['unitinfo']['items']
            # Iterating over each course in the values of 'items'
            for each_course_dict in course_list:
                course_id = each_course_dict['id']
                course_title = each_course_dict['title']
                course_url = each_course_dict['url']
                num_of_subscribers = each_course_dict['num_subscribers']
                avg_rating = each_course_dict['avg_rating']
                num_of_reviews = each_course_dict['num_reviews']
                # save the information of each course into a formatted
                # String.
                course_str += f'{category_title};;;{subcategory_id};;;' \
                              f'{subcategory_title};;;' \
                              f'{subcategory_description};;;' \
                              f'{subcategory_url};;;{course_id};;;' \
                              f'{course_title};;;{course_url};;;' \
                              f'{num_of_subscribers};;;' \
                              f'{avg_rating};;;{num_of_reviews}\n'
        file_writer = open(course_data_path, 'w')
        file_writer.write(course_str)
        file_writer.close()

    def clear_course_data(self):
        """
        This method will remove all the content in the course.txt file.
        """
        file_writer = open(course_data_path, 'w')
        file_writer.write("")
        file_writer.close()

    def generate_page_num_list(self, page, total_pages):
        """
        This method uses the current page number and total pages to
        generate a list of integers as viewable page numbers.

        parameter
        --------
        page: An integer representing the page number to retrieve the
        courses on this page.
        total_pages: An integer representing the total page number.

        return
        --------
        A list of integers as viewable page numbers.
        """

        # If the total page is less than 9, only generate pages
        # from 1 up to the total_pages.
        if total_pages < 9:
            page_num_list = list(range(1, total_pages))
        # If the current page number is less than or equal to 5,
        # the generated page number list is always [1,2,3,4,5,6,7,8,9]
        elif page <= 5:
            page_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # If the current page is greater than or equal to total pages
        # minus 4, the list of numbers changes to range between total
        # pages minus 8 until total pages.
        elif page >= total_pages - 4:
            page_num_list = list(range(total_pages - 8, total_pages + 1))
        # If the current page number is greater than 5 and less than
        # total pages minus 4, the page number list will be integers
        # from current page number minus 4 until current page number
        # plus 4
        else:
            page_num_list = list(range(page - 4, page + 5))
        return page_num_list

    def get_courses_by_page(self, page):
        """
        This method retrieves all the course information from saved file,
        and generates a list of course objects on the input page.

        parameter
        --------
        page: An integer representing the page number to retrieve the
        courses on this page.

        return
        --------
        A tuple containing the list of courses on the page, total page
        number and the total number of courses.
        """
        page_max = 20
        course_dict = self.read_course_info()
        # Calculating the total number of courses and pages.
        total_course = len(course_dict)
        total_page = math.ceil(total_course / 20)
        course_list = list(course_dict.values())
        # Dividing the course list into chunks, each containing a
        # max number (page_max) of courses.
        course_list = [course_list[i:i + page_max] for i
                       in range(0, len(course_list), page_max)]
        # Trying retrieving the course list based on the page number.
        try:
            course_page = course_list[int(page) - 1]
        # If an error occurs, set the course_page to an empty list.
        except Exception:
            course_page = []
        # Converting the dictionary items of course information into
        # a list of course objects.
        course_obj_list = [Course(each['category_title'],
                                  each['subcategory_id'],
                                  each['subcategory_title'],
                                  each['subcategory_description'],
                                  each['subcategory_url'],
                                  each['course_id'],
                                  each['course_title'],
                                  each['course_url'],
                                  each['num_of_subscribers'],
                                  each['avg_rating'],
                                  each['num_of_reviews']) for each
                           in course_page]
        return course_obj_list, total_page, total_course

    def delete_course_by_id(self, course_id):
        """
        This method deletes a course item from the course.txt file
        based on the given id.

        parameter
        --------
        id: An integer representing the id of the course.

        return
        --------
        A boolean representing whether the deletion was successful.
        """
        course_dict = self.read_course_info()
        course_id = int(course_id)
        if course_id not in course_dict.keys():
            return False
        # deleting the course info if the id can be found in
        # the saved course info file.
        else:
            del course_dict[course_id]
            all_course_str = ""
            for each_course in course_dict.values():
                all_course_str += f"{each_course['category_title']};;;" \
                                  f"{str(each_course['subcategory_id'])};;;" \
                                  f"{each_course['subcategory_title']}" \
                                  f";;;" \
                                  f"{each_course['subcategory_description']}" \
                                  f";;;" \
                                  f"{each_course['subcategory_url']};;;" \
                                  f"{str(each_course['course_id'])};;;" \
                                  f"{each_course['course_title']};;;" \
                                  f"{each_course['course_url']};;;" \
                                  f"{str(each_course['num_of_subscribers'])};;;" \
                                  f"{str(each_course['avg_rating'])};;;" \
                                  f"{str(each_course['num_of_reviews'])}\n"

            file_writer = open(course_data_path, 'w')
            file_writer.write(all_course_str)
            file_writer.close()

            util_user = User()
            user_dict = util_user.read_user_info('all')
            for uid, user_info in user_dict.items():
                # if an instructor in the user.txt file teaches this course,
                # the course id should also be removed from the instructor’s
                # course_id_list
                if user_info['role'] == 'instructor' \
                        and str(course_id) in user_info['course']:
                    user_dict[uid]['course'].remove(str(course_id))
                    util_user.write_user_into_file(user_dict, 'w')
                    break
            return True

    def get_course_obj(self, course_id, course_dict):
        """
        This method generates a course object based on a course_id,
        which can be used to retrieve course information from
        a course_dict.

        parameter
        --------
        course_id: An integer representing the id of the course.
        course_dict: A dictionary storing the information of all
        courses.

        return
        --------
        A course object found based on the course_id, or None if
        the id cannot be found in the dictionary.
        """
        course_id = int(course_id)
        for cid, course_info in course_dict.items():
            # If the course id can be found in the dictionary,
            # generates a course object using the retrieved
            # course information.
            if cid == course_id:
                course_obj = Course(course_info['category_title'],
                                    course_info['subcategory_id'],
                                    course_info['subcategory_title'],
                                    course_info['subcategory_description'],
                                    course_info['subcategory_url'],
                                    course_info['course_id'],
                                    course_info['course_title'],
                                    course_info['course_url'],
                                    course_info['num_of_subscribers'],
                                    course_info['avg_rating'],
                                    course_info['num_of_reviews'])
                return course_obj

    def get_course_by_course_id(self, course_id):
        """
        This method gets a course object based on a course_id,
        and generates a comment of the course based on its ratings
        subscribers and reviews.

        parameter
        --------
        course_id: An integer representing the id of the course.

        return
        --------
        A course object found based on the course_id, and a String
        representing the comment of the course.
        """
        course_dict = self.read_course_info()
        course_id = int(course_id)
        course_obj = self.get_course_obj(course_id, course_dict)
        # Generating different comments based on the ratings,
        # subscribers and reviews.
        if course_obj.num_of_subscribers > 100000 \
                and course_obj.avg_rating > 4.5 \
                and course_obj.num_of_reviews > 10000:
            comment = "Top Courses"
        elif course_obj.num_of_subscribers > 50000 \
                and course_obj.avg_rating > 4.0 \
                and course_obj.num_of_reviews > 5000:
            comment = "Popular Courses"
        elif course_obj.num_of_subscribers > 10000 \
                and course_obj.avg_rating > 3.5 \
                and course_obj.num_of_reviews > 1000:
            comment = "Good Courses"
        else:
            comment = "General Courses"

        return course_obj, comment

    def get_course_by_instructor_id(self, instructor_id):
        """
        This method gets a list of course object and the
        total number of courses taught by an
        instructor, based on an instructor_id.


        parameter
        --------
        instructor_id: An integer representing the id of the
        instructor.

        return
        --------
        A list  of course objects found based on the instructor_id,
        and an integer representing the total number of courses
        """
        util_user = User()
        instructor_dict = util_user.read_user_info('instructor')
        instructor_id = int(instructor_id)
        course_list = []
        total_courses = 0
        # Iterating over each instructor saved in the dictionary,
        # if the instructor_id can be found, retrieve the course ids
        # taught by the instructor.
        for iid, instructor_info in instructor_dict.items():
            if iid == instructor_id:
                course_list = instructor_info['course']
                total_courses = len(course_list)
                # only display the first 20 courses if total greater
                # than 20.
                if total_courses > 20:
                    course_list = course_list[:21]
                break
        course_dict = self.read_course_info()
        course_obj_list = []
        # Iterating over each course id in the list and generating
        # a course object respectively.
        for each in course_list:
            course_obj_list.append(self.get_course_obj(each,
                                                       course_dict))
        return course_obj_list, total_courses

    def generate_course_figure1(self):
        """
        This method generates a graph to show the top 10 subcategories
        with the most subscribers.

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure1.png')
            return "No data to make the chart."

        subcat_df = course_df.groupby(['subcategory_title']).sum()
        subcat_df = subcat_df.sort_values(by=['num_of_subscribers'],
                                          ascending=False)
        top_subcat_list = list(subcat_df.index)[:10]
        top_subscribers_list = list(subcat_df.num_of_subscribers)[:10]

        plt.figure(figsize=(13, 5))
        plt.bar(top_subcat_list, top_subscribers_list, width=0.7,
                color='#7eb54e', edgecolor='pink')
        plt.xlabel('Subcategory title')
        plt.ylabel('Number of subscribers')
        plt.title("The Top 10 subcategories with the Most Subscribers")
        plt.xticks(rotation=65)
        plt.tight_layout()
        plt.savefig(figure_save_path + 'course_figure1.png')
        plt.close()

        understanding = "The bar chart shows that the most popular " \
                        "subcategories are directly relevant " \
                        "to programming, such as web development and " \
                        "programming languages. Subcategories" \
                        "that are related to data analysis, computer " \
                        "networks and app developments are the second" \
                        "popular, followed by subcategories that are " \
                        "relevant to business and commence."
        return understanding

    def generate_course_figure2(self):
        """
        This method generates a graph to show the top 10 courses
        that have lowest avg rating and over 50000 reviews..

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        # If there are no saved course information, generates a
        # blank image and returns a message.
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure2.png')
            return "No data to make the chart."

        course_with_reviews = course_df[course_df['num_of_reviews']
                                        > 50000]
        course_with_reviews = \
            course_with_reviews.sort_values(by=['avg_rating'],
                                            ascending=True)
        top_course_list = list(course_with_reviews.course_title)[:10]
        for title in top_course_list:
            if len(title.split(' ')) > 3:
                top_course_list[top_course_list.index(title)] \
                    = ' '.join(title.split(' ')[:3])
        rating_list = list(course_with_reviews.avg_rating)[:10]

        plt.figure(figsize=(10, 5))
        plt.bar(top_course_list, rating_list, width=0.7,
                color='#7eb54e', edgecolor='pink')
        plt.xlabel('Course title')
        plt.ylabel('Average rating')
        plt.title('Average Ratings of the Top 10 Lowest Rated Courses')
        plt.ylim(4.4, 4.6)
        plt.xticks(rotation=65)
        plt.tight_layout()
        plt.savefig(figure_save_path + 'course_figure2.png')
        plt.close()

        understanding = "The bar chart shows that among courses " \
                        "with over 5000 reviews," \
                        " the Agile Project Management course has " \
                        "the lowest average" \
                        "rating, and many of the programming " \
                        "courses such as " \
                        "machine earning, python, java, web development" \
                        "courses also received the top 10 lowest " \
                        "rating from student reviews. "

        return understanding

    def generate_course_figure3(self):
        """
        This method generates a graph to show all the courses avg rating
        distribution that has subscribers between 100000 and 10000
        (scatter chart)

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure3.png')
            return "No data to make the chart."

        course_with_subscribers = \
            course_df[course_df['num_of_subscribers'] >= 10000]
        course_with_subscribers = \
            course_with_subscribers[
                course_with_subscribers['num_of_subscribers']
                <= 100000]

        plt.figure(figsize=(13, 5))
        y = list(course_with_subscribers.avg_rating)
        x = list(course_with_subscribers.num_of_subscribers)
        plt.scatter(x, y, s=5, c='pink', edgecolors='black',
                    linewidths=.5)
        plt.xlabel('Number of subscribers')
        plt.ylabel('Average rating')
        plt.title('Average Ratings Against Number of '
                  'Subscribers of Courses')
        plt.savefig(figure_save_path + 'course_figure3.png')
        plt.close()
        understanding = "The scatter plot shows that among courses" \
                        " with between 10000-100000 reviews," \
                        " most courses have 10000-30000 reviews," \
                        " and the average ratings for " \
                        "courses that have less reviews are more" \
                        " disperse and tend to contain " \
                        "more outliers with very low ratings."

        return understanding

    def generate_course_figure4(self):
        """
        This method generates a graph to show number of courses
        for all categories and sort in ascending order (pie chart)

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure4.png')
            return "No data to make the chart."

        cat_series = \
            course_df['category_title'].value_counts(ascending=True)
        labels = list(cat_series.index)
        sizes = list(cat_series.values)

        explode = [0] * (len(labels) - 2) + [300, 0]

        fig1, ax1 = plt.subplots(figsize=(15, 8))
        ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
                labels=None, shadow=True,
                startangle=90, radius=1000,
                textprops={'fontsize': 6})
        plt.legend(labels, bbox_to_anchor=(1, 0.5),
                   loc="center right", fontsize=5, edgecolor='m')
        plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
        ax1.axis('equal')
        plt.title("The Number of Courses (Percentage) for All Categories")
        plt.savefig(figure_save_path + 'course_figure4.png')
        plt.close()

        understanding = "The pie chart shows that mobile " \
                        "development courses is the category with" \
                        "the greatest number of courses, " \
                        "with Database Design & Development being" \
                        " the second largest category."
        return understanding

    def generate_course_figure5(self):
        """
        This method generates a graph to show how many courses have
        reviews and how many courses do not have reviews.(bar chart)

        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure5.png')
            return "No data to make the chart."

        course_with_reviews = \
            course_df[course_df['num_of_reviews'] != 0]
        course_without_reviews = \
            course_df[course_df['num_of_reviews'] == 0]
        y = [len(course_with_reviews), len(course_without_reviews)]
        x = ['course with reviews', 'course without reviews']

        plt.figure(figsize=(10, 5))
        plt.bar(x, y, width=0.7, color='#7eb54e', edgecolor='pink')
        plt.ylabel('Number of courses')
        plt.title('The Number of Courses with and without Reviews')
        plt.tight_layout()
        plt.savefig(figure_save_path + 'course_figure5.png')
        plt.close()

        understanding = "The bar chart shows that the majority of" \
                        " courses have reviews," \
                        "while only very few courses have no reviews."
        return understanding

    def generate_course_figure6(self):
        """
        This method generates a graph to show the top 10 subcategories
         with the least courses (any chart)


        return
        --------
        A string explanation about the interpretation of the graph.
        """
        course_df = self.read_course_df()
        if len(course_df) == 0:
            plt.savefig(figure_save_path + 'course_figure6.png')
            return "No data to make the chart."

        subcat_series = course_df['subcategory_title'].value_counts(ascending=True)
        labels = list(subcat_series.index)[:10]
        sizes = list(subcat_series.values)[:10]

        plt.figure(figsize=(10, 5))
        plt.bar(labels, sizes, width=0.7, color='#7eb54e', edgecolor='pink')
        plt.ylabel('Number of courses')
        plt.title('The Top 10 Subcategories with the Least Courses ')
        plt.xticks(rotation=65)
        plt.tight_layout()
        plt.savefig(figure_save_path + 'course_figure6.png')
        plt.close()

        understanding = "The bar chart shows that the IT certification subcategory is " \
                        "less popular, which has the least courses, followed by " \
                        "subcategories such as bookkeeping, communication and " \
                        "compliance. "
        return understanding

    def read_course_df(self):
        """
        This method reads course.txt into a dataframe.

        return
        --------
        A dataframe contains the information of each course, with the
        columns containing all course info.
        """
        df = pd.read_csv(course_data_path, sep=';;;',
                         names=['category_title', 'subcategory_id', 'subcategory_title',
                                'subcategory_description', 'subcategory_url', 'course_id',
                                'course_title', 'course_url', 'num_of_subscribers',
                                'avg_rating', 'num_of_reviews'],
                         engine='python')
        return df

    def read_course_info(self):
        """
        The method reads the saved course info (course.txt) file,
        converts it into a dictionary, and return the dictionary of all
        courses.

        return
        --------
        A dictionary contains the information of each course, with the key
        being course_id and values containing all course info.
        """
        # reads course.txt into a dataframe, adjusting the columns.
        df = self.read_course_df()
        df = df.set_index('course_id')
        df['course_id'] = df.index
        df = df[['category_title', 'subcategory_id', 'subcategory_title',
                 'subcategory_description', 'subcategory_url', 'course_id',
                 'course_title', 'course_url', 'num_of_subscribers',
                 'avg_rating', 'num_of_reviews']]
        # converting dataframe to a dictionary
        course_dict = df.to_dict('index')

        return course_dict
