using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using NUnit.Framework;

namespace Foodery.Recipes.Tests
{
    public class RecipeApiTests
    {
        private readonly ApiTestsFixture _fixture;

        public RecipeApiTests()
        {
            _fixture = new ApiTestsFixture();
        }
        
        [Test]
        public async Task ShouldReturnEnglishIngridients()
        {
            var client = _fixture.Server.CreateClient();

            var response = await client.GetAsync("api/recipe");

            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
        }
    }
}