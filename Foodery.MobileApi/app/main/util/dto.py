from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class RecipeDto:
    api = Namespace('recipe', description='recipe related operations')
    ingredient = api.model('ingredient', {
        'name': fields.String(required=True),
        'image': fields.String()
    })
    recipe_search = api.model('recipe_search', {
        'id': fields.String(required=True),
        'title': fields.String(),
        'missed': fields.List(fields.Raw,attribute='missedIngredients'),
        'used': fields.List(fields.Raw,attribute='usedIngredients'),
        'unused': fields.List(fields.Raw,attribute='unusedIngredients')
    })
    recipe = api.model('recipe_search', {
        'id': fields.String(required=True),
        'title': fields.String()
    })
