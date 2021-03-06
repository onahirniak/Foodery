from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.recipe_controller import api as recipe_ns

blueprint = Blueprint('api', __name__, url_prefix='/mobile')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='Foodery MobileApi ',
          version='1.0',
          description='Foodery MobileApi documentation',
          authorizations=authorizations,
          security='apikey',
          prefix='/mobile'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(recipe_ns, path='/recipe')
