using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.TestHost;

namespace Foodery.Recipes.Tests
{
    public class ApiTestsFixture
    {
        public TestServer Server { get; set; }

        public ApiTestsFixture()
        {
            Server = new TestServer(new WebHostBuilder()
                .UseStartup<Startup>());
        }
    }
}