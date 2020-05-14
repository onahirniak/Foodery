using Foodery.Recipes.Application;
using Foodery.Recipes.Application.Interfaces;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace Foodery.Recipes.Integration
{
    public static class IntegrationSetup
    {
        public static IServiceCollection AddIntegrationServices(this IServiceCollection services)
        {
            services.TryAddScoped<IRecipeAdapterFactory, RecipeAdapterFactory>();
            return services;
        }
    }
}