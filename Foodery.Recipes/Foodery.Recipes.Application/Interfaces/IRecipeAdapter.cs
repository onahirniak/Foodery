using System.Threading.Tasks;
using Foodery.Recipes.Application.Models;

namespace Foodery.Recipes.Application.Interfaces
{
    public interface IRecipeAdapter
    {
        Task<IngredientResult[]> GetIngredients(string query);
    }
}