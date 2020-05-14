using System.Linq;
using Foodery.Recipes.Application.Models;
using Foodery.Recipes.Models;

namespace Foodery.Recipes.Mappings
{
    public static class RecipeMappings
    {
        public static IngredientResponse[] ToIngredientResponse(this IngredientResult[] results)
        {
            return results.Select(i => new IngredientResponse
            {
                Name = i.Name,
                ImageUrl = i.ImageUrl
            }).ToArray();
        }
    }
}