from flask import Blueprint

from app.blueprints.resources.views.resources import ResourcesView

# do not rename "blueprint" variable if you want to use auto import
blueprint: Blueprint = Blueprint(
    'resources',
    __name__,
    template_folder='templates'
)

blueprint.add_url_rule('/resources', view_func=ResourcesView.as_view('resources_page'))
