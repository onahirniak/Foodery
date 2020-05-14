namespace Foodery.Recipes.Application.Interfaces
{
    public interface IRecipeAdapterFactory
    {
        IRecipeAdapter Create(string language);
    }
}