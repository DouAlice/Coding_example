"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts is responsible for user login,
registration, deletion and student information presentation.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result
from model.course import Course
from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
from model.user_student import Student

user_page = Blueprint("user_page", __name__)

model_user = User()
model_course = Course()
model_student = Student()


@user_page.route("/login", methods=['GET'])
def login():
    """
    The method controls the login page by returning the
    '00login.html' template to the front end.

    return
    --------
    '00login.html' html template
    """
    return render_template('00login.html')


@user_page.route("/login", methods=['POST'])
def login_post():
    """
    The method posts “username”, “password” values from the request.values
    to back end, perform validations on username and password, followed by
    an authentication.

    return
    --------
    A user string containing the user info if successful authentication,
    otherwise an error message.
    """
    username = request.values['username']
    password = request.values['password']

    if model_user.validate_username(username) \
            and model_user.validate_password(password):
        authentication_result, user_info_string \
            = model_user.authenticate_user(username, password)
        if authentication_result:
            # If authentication success, generate a corresponding user object
            # using the generate_user() method and assign this user to the
            # User.current_login_user class variable.
            login_user = generate_user(user_info_string)
            User.current_login_user = login_user
            return render_result(msg=str(login_user))
    # returning error messages if login failed
    return render_err_result(msg="Login failed. Invalid username or password.")


def generate_user(login_user_str):
    """
    The method converts the given user string to an object.

    return
    --------
    the converted object, representing the login user.
    """
    user_info_list = login_user_str.split(";;;")
    role = user_info_list[4]
    login_user = User()
    # Creating objects of different classes based on the login user role.
    if role == "admin":
        login_user = Admin(user_info_list[0], user_info_list[1], user_info_list[2],
                           user_info_list[3], user_info_list[4])
    elif role == "student":
        login_user = Student(user_info_list[0], user_info_list[1], user_info_list[2],
                             user_info_list[3], user_info_list[4], user_info_list[5])
    elif role == "instructor":
        login_user = Instructor(user_info_list[0], user_info_list[1], user_info_list[2],
                                user_info_list[3], user_info_list[4], user_info_list[5],
                                user_info_list[6], user_info_list[7],
                                user_info_list[8].split('--'))

    return login_user


@user_page.route("/logout", methods=['GET'])
def logout():
    """
    The method controls the logout page by returning the
    '01index.html' template to the front end.

    return
    --------
    '01index.html' html template
    """
    User.current_login_user = None
    return render_template('01index.html')


@user_page.route("/register", methods=['GET'])
def register():
    """
    The method controls the register page by returning the
    '00register.html' template to the front end.

    return
    --------
    '00register.html' html template
    """
    return render_template('00register.html')


@user_page.route("/register", methods=['POST'])
def register_post():
    """
    The method posts user info values to the back end and performs validations
    on them. If all valid, register this user.

    return
    --------
    A string representing the messages about registration outcomes for the user.
    """
    username = request.values['username']
    password = request.values['password']
    email = request.values['email']
    register_time = request.values['register_time']
    role = request.values['role']

    # register the user if the inout username, password and email are all valid.
    if model_user.validate_username(username) \
            and model_user.validate_password(password) \
            and model_user.validate_email(email):
        result = model_user.register_user(username, password,
                                          email, int(register_time), role)
        if result:
            return render_result(msg="Successful registration.")
        else:
            return render_err_result(
                msg="Registration failed because username already exist.")
    return render_err_result(
        msg="Registration failed because of invalid username, password or email.")


@user_page.route("/student-list", methods=['GET'])
def student_list():
    """
    The method creates a table to show the information of students.

    return
    --------
    '10student_list.html' html template to show student list, or
    returning to the index page when errors occur
    """
    if User.current_login_user.role == 'admin':
        req = request.values
        if 'page' in req:
            page = int(req['page'])
        else:
            page = 1
        context = {}
        # get values for one_page_student_list, total_pages, total_num
        student_obj_list, total_page, total_student \
            = model_student.get_students_by_page(page)
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(page, total_page)
        # check one_page_student_list, make sure this variable not be None, if None, assign it to []
        if student_obj_list is None:
            student_obj_list = []

        context['one_page_user_list'] = student_obj_list
        context['total_pages'] = total_page
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_student
        context['current_user_role'] = User.current_login_user.role
        # add "current_user_role" to context
    else:
        return redirect(url_for("index_page.index"))

    return render_template("10student_list.html", **context)


@user_page.route("/student-info", methods=['GET'])
def student_info():
    """
    The method finds a student based on the “id” attribute
    in the request.values. If not exist, return a new student
    and set all instance variables with default values.

    return
    --------
    '11student_info.html' html template to show student info,
    and context dictionary.
    """
    context = {}
    if 'id' not in request.values:
        student_obj = None
    else:
        student_obj = model_student.get_student_by_id(request.values['id'])
    context['student_obj'] = student_obj if student_obj else User.current_login_user
    context['current_user_role'] = User.current_login_user.role

    return render_template('11student_info.html', **context)


@user_page.route("/student-delete", methods=['GET'])
def student_delete():
    """
    The method Delete student according to the “id” attribute in the request.values.

    return
    --------
    redirecting to show student_list ot index page
    """
    student_id = request.values['id']
    result = model_student.delete_student_by_id(student_id)
    if result:
        return redirect(url_for('user_page.student_list'))
    else:
        return redirect(url_for('index_page.index'))
