"""

Name: Dou Hong
Student ID: 32347995
Start date: April 29th
Last modified date: May 6th

Description: This python Scripts constructs a Review class, which represents
a review of a course written by a student, which can be found by review id,
review keyword and course id.

"""


class Review:
    def __init__(self, id=-1, content="", rating=-1.0, course_id=-1):
        """
        The constructor of the Review class, for initiating a new Review
        object.

        parameter
        --------
        id: An integer representing the id of the review.
        content: A String representing the content of the review.
        rating: An float representing the rating of the review.
        course_id: An integer representing the id of the course.
        """
        self.id = id
        self.content = content
        self.rating = rating
        self.course_id = course_id

    def find_review_by_id(self, review_id):
        """
        The find_review_by_id function will find the review according
        to the review id.

        parameter
        --------
        course_id: A string or an int representing the review id.

        return
        --------
        review_obj: The Review object that has been found according to
        the review id.
        """
        file_handler = open(
            './data/result/review.txt', 'r', encoding="utf-8")
        review_list = file_handler.readlines()
        file_handler.close()

        # Iterate over each review in the review_list, if the review id
        # matches with the id of a review, use the info
        # of this review to create a review object. Add this object
        # into the review_obj_list.
        for each_review in review_list:
            stored_review_info = each_review.split(";;;")
            stored_review_id = stored_review_info[0]
            if stored_review_id == str(review_id):
                review_obj = Review(stored_review_info[0],
                                    stored_review_info[1],
                                    stored_review_info[2],
                                    stored_review_info[3])
                return review_obj
        return None

    def find_review_by_keywords(self, keyword):
        """
        The find_review_by_keywords function will find the review
        according to the review content keywords.

        parameter
        --------
        keyword: A string representing the review keyword.

        return
        --------
        review__obj_list: The list contains all the Review objects
        that has been found according to
        the review keyword.
        """
        file_handler = open(
            './data/result/review.txt', 'r', encoding="utf-8")
        review_list = file_handler.readlines()
        file_handler.close()
        review_obj_list = []

        # Iterate over each review in the review_list, if the keyword
        # can be found in the review_content of a review, use the info
        # of this review to create a review object. Add this object
        # into the review_obj_list.
        for each_review in review_list:
            stored_review_info = each_review.split(";;;")
            stored_review_content = stored_review_info[1]
            if keyword in stored_review_content:
                review_obj = Review(stored_review_info[0],
                                    stored_review_info[1],
                                    stored_review_info[2],
                                    stored_review_info[3])
                review_obj_list.append(review_obj)
        return review_obj_list

    def find_review_by_course_id(self, course_id):
        """
        The find_review_by_course_id function will find the
        review according to the course id.

        parameter
        --------
        course_id: A string or an int representing the course id.

        return
        --------
        review__obj_list: The list contains all the Review objects
        that has been found according to
        the course id.
        """
        file_handler = open(
            './data/result/review.txt', 'r', encoding="utf-8")
        review_str = file_handler.read()
        review_list = review_str.splitlines()
        file_handler.close()
        review_obj_list = []

        # Iterate over each review in the review_list, if the course id
        # matches with the store course id of a review, use the info
        # of this review to create a review object. Add this object
        # into the review_obj_list.
        for each_review in review_list:
            stored_review_info = each_review.split(";;;")
            stored_course_id = stored_review_info[3]
            if stored_course_id == str(course_id):
                review_obj = Review(stored_review_info[0],
                                    stored_review_info[1],
                                    stored_review_info[2],
                                    stored_review_info[3])
                review_obj_list.append(review_obj)
                return review_obj_list
        return None

    # review = Review()
    # for each in review.find_review_by_course_id("1565998"):
    #     print(each)

    def review_overview(self):
        """
        The review_overview function will print the total number
        of reviews.

        return
        --------
        A String that displays the total number of reviews.

        """
        file_handler = open(
            './data/result/review.txt', 'r', encoding="utf-8")
        review_list = file_handler.readlines()
        file_handler.close()

        # Determine the total number of the reviews by the
        # number of items in the review_list.
        return f'the total number of reviews: {len(review_list)}'

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the review object.

        """
        return f'review id: {self.id}\nreview content: ' \
               f'{self.content}\nreview rating: {self.rating}\n' \
               f'course id: {self.course_id}\n'
