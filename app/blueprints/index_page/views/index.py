from flask import request, current_app, render_template, Response
from flask.views import View


class IndexView(View):
    methods = ["GET"]

    def dispatch_request(self) -> str:
        # current_app.config.get("MY_CONFIG_VARIABLE")
        return render_template("index.jinja2")
