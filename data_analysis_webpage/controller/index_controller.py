"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th

Description: This python Scripts is responsible for the index
page of the data analysis system.
"""

from flask import render_template, Blueprint
from model.user import User
from model.user_admin import Admin

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    """
    The method controls the index page of this web application by
    checking if there is any logged user. If there exists a logged user,
    pass the current_login_user’s role to context[‘current_user_role’],
    registering an admin and render the '01index.html' template.

    return
    --------
    '01index.html' html template and context dictionary
    """
    context = {}
    # check the class variable User.current_login_user
    if User.current_login_user is not None:
        context['current_user_role'] = User.current_login_user.role
    # manually register an admin account when open index page
    model_user = User()
    admin_dict = model_user.read_user_info('admin')
    # Iterating over each saved admin
    for each_admin in admin_dict.values():
        if each_admin['username'] == 'admin' \
                and each_admin['password'] \
                == model_user.encrypt_password('admin1111'):
            return render_template('01index.html', **context)
    # if the username 'admin' and password 'admin1111' have not been
    # registered, manually register this admin.
    Admin().register_admin()
    return render_template('01index.html', **context)
