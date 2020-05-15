using System;
using Foodery.Recipes.Application.Interfaces;
using Foodery.Recipes.Integration.Adapters;

namespace Foodery.Recipes.Integration
{
    public class RecipeAdapterFactory : IRecipeAdapterFactory
    {
        public IRecipeAdapter Create(string language)
        {
            switch (language)
            {
                case "en":
                    return new EnglishRecipeAdapter();
                case "es":
                    return new SpanishRecipeAdapter();
                case "ua":
                    return new UkranianRecipeAdapter();
                default:
                    throw new NotImplementedException($"Not implemented for {language}");
            }
        }
    }
}