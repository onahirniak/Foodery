import requests
from flask import current_app

def search_ingredients(query):
    apiKey = current_app.config["SPOONACULAR_API_KEY"]
    baseUrl = current_app.config["SPOONACULAR_BASE_URL"]
    response = requests.get(f"{baseUrl}/food/ingredients/autocomplete?query={query}&number=40&apiKey={apiKey}");
    return response.json();

def search_recipes_by_ingredients(query):
    apiKey = current_app.config["SPOONACULAR_API_KEY"]
    baseUrl = current_app.config["SPOONACULAR_BASE_URL"]
    response = requests.get(f"{baseUrl}/recipes/findByIngredients?ingredients={query}&ranking=1&number=40&apiKey={apiKey}");
    return response.json();

def get_recipe_by_id(recipe_id):
    apiKey = current_app.config["SPOONACULAR_API_KEY"]
    baseUrl = current_app.config["SPOONACULAR_BASE_URL"]
    response = requests.get(f"{baseUrl}/recipes/{recipe_id}/information?apiKey={apiKey}");
    return response.json();




