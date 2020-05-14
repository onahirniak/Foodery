using System;
using System.Threading.Tasks;
using Foodery.Recipes.Application.Interfaces;
using Foodery.Recipes.Application.Models;

namespace Foodery.Recipes.Application
{
    public class RecipeService
    {
        private readonly IRecipeAdapterFactory _factory;

        public RecipeService(IRecipeAdapterFactory factory)
        {
            _factory = factory;
        }

        public async Task<IngredientResult[]> GetIngredients(string language, string query)
        {
            var adapter = _factory.Create(language);

            return await adapter.GetIngredients(query);
        }
    }
}