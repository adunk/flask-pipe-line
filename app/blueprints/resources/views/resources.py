from flask import request, current_app, render_template, Response
from flask.views import View


class ResourcesView(View):
    methods = ["GET"]

    def dispatch_request(self) -> str:
        return render_template("resources.jinja2")
