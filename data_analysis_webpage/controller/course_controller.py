"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts is responsible for extraction,
analysis, deletion and presentation of instructor information.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result
from model.user import User
from model.course import Course
from model.user_instructor import Instructor
from flask import render_template, Blueprint

course_page = Blueprint("course_page", __name__)

model_course = Course()
model_instructor = Instructor()
model_user = User()


@course_page.route("/reset-database", methods=['POST'])
def reset_database():
    """
    The method removes all the content in the user.txt and course.txt
    files by calling methods in User and Course class.

    return
    --------
    Reminding messages for the user regarding reseting outcomes.
    """
    try:
        model_user.clear_user_data()
        model_course.clear_course_data()
        return render_result(msg="The database has been reset, all data have been removed.")
    except Exception:
        return render_err_result(msg="Exception happened.")


@course_page.route("/course-list", methods=['GET'])
def course_list():
    """
    The method creates a table to show the information of courses.

    return
    --------
    '02course_list.html' html template to show course list, or
    returning to the index page when errors occur
    """
    if User.current_login_user:
        req = request.values
        page = int(req['page']) if "page" in req else 1
        context = {}
        # get values for one_page_course_list, total_pages, total_num
        course_obj_list, total_page, total_course = model_course.get_courses_by_page(page)
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(page, total_page)
        # check one_page_course_list, make sure this variable not be None, if None, assign it to []
        if course_obj_list is None:
            course_obj_list = []

        context['one_page_course_list'] = course_obj_list
        context['total_pages'] = total_page
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_course
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))
    return render_template("02course_list.html", **context)


@course_page.route("/process-course", methods=["POST"])
def process_course():
    """
    The method extracts all the course information from the given data
    files and store course info into the course.txt file

    return
    --------
    Reminding messages for the user regarding processing outcomes.
    """
    try:
        model_course.get_courses()
    except Exception as e:
        print(e)
        return render_err_result(msg="error in process course")

    return render_result(msg="process course finished successfully")


@course_page.route("/course-details")
def course_details():
    """
    The method creates a table to show the information of courses.

    return
    --------
    '03course_details.html' html template to show course details,
    and context dictionary containing course info.
    """
    overall_comment = ""
    context = {}
    if User.current_login_user:
        req = request.values
        course_id = req['id'] if "id" in req else -1

        if course_id == -1:
            course = None
        else:
            course, overall_comment = model_course.get_course_by_course_id(int(course_id))

        if not course:
            context["course_error_msg"] = "Error, cannot find course"
        else:
            context['course'] = course
            context['overall_comment'] = overall_comment
        context['current_user_role'] = User.current_login_user.role

    return render_template("03course_details.html", **context)


@course_page.route("/course-delete")
def course_delete():
    """
    The method Delete course according to the “id” attribute
    in the request.values.

    return
    --------
    redirecting to show course_list or providing error messages
    """
    req = request.values
    course_id = req['id'] if "id" in req else -1
    print("course delete:", course_id)
    if course_id == -1:
        return render_err_result(msg="course cannot find")
    result = model_course.delete_course_by_id(int(course_id))
    print("course delete:", result)
    if result:
        return redirect(url_for("course_page.course_list"))
    else:
        return render_err_result(msg="course delete error")


@course_page.route("/course-analysis")
def course_analysis():
    """
    The method creates and displays figures showing the depicting
    course information / characteristics, and the figure interpretations.

    return
    --------
    '04course_analysis.html' html template to show the figures, and
    the context dictionary containing the figure explanations.
    """
    context = {}
    if User.current_login_user:
        explain1 = model_course.generate_course_figure1()
        explain2 = model_course.generate_course_figure2()
        explain3 = model_course.generate_course_figure3()
        explain4 = model_course.generate_course_figure4()
        explain5 = model_course.generate_course_figure5()
        explain6 = model_course.generate_course_figure6()

        context['explain1'] = explain1
        context['explain2'] = explain2
        context['explain3'] = explain3
        context['explain4'] = explain4
        context['explain5'] = explain5
        context['explain6'] = explain6
        context['current_user_role'] = User.current_login_user.role
    else:
        return redirect(url_for("course_page.course_list"))

    return render_template("04course_analysis.html", **context)
