using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using MudBlazor.Services;
using RecNPet;
using RecNPet.Services;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri("http://127.0.0.1:8000") });
builder.Services.AddSingleton<PetInfoService>();
builder.Services.AddScoped<ApiService>();
builder.Services.AddMudServices();
await builder.Build().RunAsync();
