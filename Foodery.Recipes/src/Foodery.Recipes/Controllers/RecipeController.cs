using System;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Foodery.Recipes.Application;
using Foodery.Recipes.Mappings;
using Foodery.Recipes.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Foodery.Recipes.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class RecipeController : ControllerBase
    {
        private readonly RecipeService _recipes;
        
        public RecipeController(RecipeService recipes)
        {
            _recipes = recipes;
        }
        
        [HttpGet]
        public async Task<ActionResult<RecipeResponse[]>> GetRecipes(
            [FromQuery]string query = null,
            [FromQuery]string language = null)
        {
            return new RecipeResponse[]{};
        }
        
        [HttpGet("ingredientId")]
        public async Task<ActionResult<RecipeResponse>> GetRecipeById(int ingredientId, [FromQuery]string language = null)
        {
            return new RecipeResponse();
        }

        [HttpGet("ingredients")]
        public async Task<ActionResult<IngredientResponse[]>> GetIngredients(
            [FromQuery]string language = null,
            [FromQuery]string query = null)
        {
            var ingredients = await _recipes.GetIngredients(language, query);

            return ingredients.ToIngredientResponse();
        }
    }
}