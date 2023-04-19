"""
https://flask.palletsprojects.com/en/2.2.x/templating/#context-processors
"""
import os
from flask import Flask


def register_context_processor(app: Flask) -> None:

    @app.context_processor
    def inject_is_production() -> dict:
        return dict(
            app_name="Flask-Backbone",
            app_config=os.environ.get('APP_CONFIG')
        )
