##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from app.api import *
from flask import *
from datetime import datetime

class Controller(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
        self.task = Task(app, conn)

    def index_action(self):
        tasks = self.task.get_tasks_by_user_id(1)
        for task in tasks:
            print(task)
        return render_template("index.html")

class AuthController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.api = API(app, conn)

    def register_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.user_create(username, password)
        flash(result)
        return redirect(url_for('route_home'))

    def signin_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.user_login(username, password)
        flash(result)
        return redirect(url_for('route_home'))

    def signout_action(self, request):
        result = self.api.user_logout()
        flash(result)
        return redirect(url_for('route_home'))

class UserController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
        if len(session) < 1:
            dct = {}
            dct['error'] = "you must be logged in"
            ret = json.dumps(dct)
            flash(ret)

    def view_user_info_action(self):
        if len(session) < 1:
            print("ouais")
            return redirect(url_for('route_home'))
        return render_template("profile.html")

    def view_user_all_task_action(self):
        return render_template("index.html")

    def view_user_special_task_action(self):
        return render_template("index.html")

    def update_task_action(self, request):
        return redirect(url_for('route_user_all_task'))

    def create_task_action(self, request):
        return redirect(url_for('route_user_all_task'))

    def delete_task_action(self, request):
        return redirect(url_for('route_user_all_task'))
