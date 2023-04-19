from flask import Blueprint, make_response, render_template, current_app, Response

from app.blueprints.index_page.views.index import IndexView

blueprint: Blueprint = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/', view_func=IndexView.as_view('index_route'))
