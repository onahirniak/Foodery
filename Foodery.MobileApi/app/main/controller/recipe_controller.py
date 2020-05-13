from flask import request
from flask_restx import Resource

from ..util.dto import RecipeDto
from ..service.receipt_service import *
from ..util.decorator import token_required, admin_token_required

api = RecipeDto.api

@api.route('/ingredients')
@api.param('query', 'The query')
class IngredientsList(Resource):
    @api.doc()
    @api.marshal_list_with(RecipeDto.ingredient)
    @token_required
    def get(self):
        """Search ingredients for recipe"""
        query = request.args.get('query')
        return search_ingredients(query)

@api.route('/')
@api.param('query', 'The query')
class RecipesList(Resource):
    @api.doc()
    @api.marshal_list_with(RecipeDto.recipe_search)
    @token_required
    def get(self):
        """Search recipes by ingredients"""
        query = request.args.get('query')
        return search_recipes_by_ingredients(query)


@api.route('/<recipe_id>')
@api.param('recipe_id', 'The recipe identifier')
class Recipe(Resource):
    @api.doc()
    #@api.marshal_list_with(RecipeDto.recipe)
    @token_required
    def get(self, recipe_id):
        """Get recipe by id"""
        return get_recipe_by_id(recipe_id)