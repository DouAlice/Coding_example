"""

Name: Dou Hong
Start date: June 15th
Last modified date: June 15th


Description: This python Script constructs an Admin class inherited from the
User class, which represents an administrator who can be manually registered.
"""

from lib.helper import user_data_path
from model.user import User


class Admin(User):
    def __init__(self, uid=-1, username="", password="",
                 register_time="yyyy-MM-dd_HH:mm:ss.SSS", role="admin"):
        """
        The constructor of the Admin class, for initiating a new Admin
        object.

        parameter
        --------
        uid: An integer representing the id of the user.
        username: A String representing the username.
        password: A String representing the user password.
        register_time: A String representing the time of registration.
        role: A String representing the role of the user.
        """
        super(Admin, self).__init__(uid, username, password,
                                    register_time, role)

    def register_admin(self, username='admin', password='admin1111', register_time="yyyy-MM-dd_HH:mm:ss.SSS"):
        """
        Registering an admin using the input or default admin information.

        parameter
        --------
        uid: An integer representing the id of the user.
        username: A String representing the username.
        password: A String representing the user password.
        register_time: A String representing the time of registration.
        role: A String representing the role of the user.
        """
        registration_str = f'{self.generate_unique_user_id()};;;{username};;;' \
                           f'{self.encrypt_password(password)};;;' \
                           f'{register_time};;;admin\n'
        file_appender = open(user_data_path, 'a')
        file_appender.write(registration_str)
        file_appender.close()

    def __str__(self):
        """
        Converting the object to a String representation.

        return
        --------
        A String showing the attributes of the Admin object.
        """
        return f'{self.uid};;;{self.username};;;{self.password};;;' \
               f'{self.register_time};;;{self.role}'
