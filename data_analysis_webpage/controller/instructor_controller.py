"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts is responsible for extraction,
analysis and presentation of instructor information.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result
from model.user import User
from model.course import Course
from flask import render_template, Blueprint
from model.user_instructor import Instructor

instructor_page = Blueprint("instructor_page", __name__)

model_instructor = Instructor()
model_course = Course()


@instructor_page.route('/instructor-list', methods=['GET'])
def instructor_list():
    """
    The method creates a table to show the information of instructors.

    return
    --------
    '07instructor_list.html' html template to show student list, or
    returning to the index page when errors occur
    """
    if User.current_login_user:
        req = request.values
        page = int(req['page']) if "page" in req else 1
        context = {}
        # get values for one_page_instructor_list, total_pages, total_num
        instructor_obj_list, total_page, total_instructor \
            = model_instructor.get_instructors_by_page(page)
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(page, total_page)
        # check one_page_instructor_list, make sure this variable
        # not be None, if None, assign it to []
        if instructor_obj_list is None:
            instructor_obj_list = []

        context['one_page_instructor_list'] = instructor_obj_list
        context['total_pages'] = total_page
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_instructor
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))

    return render_template("07instructor_list.html", **context)


@instructor_page.route('/teach-courses', methods=['GET'])
def teach_courses():
    """
    The method creates a table to show the information of courses
    taught by the instructor.

    return
    --------
    '10student_list.html' html template to show student list, or
    returning to the index page when errors occur
    """
    context = {}
    if User.current_login_user:
        # get instructor id
        instructor_id = User.current_login_user.uid
        if 'id' in request.values:
            instructor_id = request.values['id']
        # get values for course_list, total_num
        course_obj_list, total_courses \
            = model_course.get_course_by_instructor_id(instructor_id)
        if course_obj_list is None:
            course_obj_list = []

        context['course_list'] = course_obj_list
        context['total_num'] = total_courses
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role
    else:
        return redirect(url_for("index_page.index"))
    return render_template("09instructor_courses.html", **context)


@instructor_page.route("/instructor-analysis")
def instructor_analysis():
    """
    The method creates and displays a figure showing the top 10 instructors
    who teach the most courses, and the figure interpretation.

    return
    --------
    '08instructor_analysis.html' html template to show the figure, and
    the context dictionary containing the figure explanation.
    """
    explain1 = model_instructor.generate_instructor_figure1()
    context = {}
    context['explain1'] = explain1

    return render_template("08instructor_analysis.html", **context)


@instructor_page.route("/process-instructor", methods=["POST"])
def process_instructor():
    """
    The method extracts all the instructor information from the given data
    files and store instructor info into the user.txt file

    return
    --------
    Reminding messages for the user regarding processing outcomes.
    """
    try:
        model_instructor.get_instructors()
    except Exception as e:
        print(e)
        return render_err_result(msg="error in process instructors")

    return render_result(msg="process instructors finished successfully")
