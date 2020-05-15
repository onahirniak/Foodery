using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace Foodery.Recipes.Application
{
    public static class ApplicationSetup
    {
        public static IServiceCollection AddApplicationServices(this IServiceCollection services)
        {
            services.TryAddScoped<RecipeService>();
            return services;
        }
    }
}