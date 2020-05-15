using System.Threading.Tasks;
using Foodery.Recipes.Application.Interfaces;
using Foodery.Recipes.Application.Models;

namespace Foodery.Recipes.Integration.Adapters
{
    public class EnglishRecipeAdapter : IRecipeAdapter
    {
        public Task<IngredientResult[]> GetIngredients(string query)
        {
            throw new System.NotImplementedException();
        }
    }
}