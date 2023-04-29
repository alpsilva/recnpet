using RecNPet.Models;
using System.Net.Http;
using System.Net.Http.Json;

namespace RecNPet.Services
{
    public class ApiService
    {
        private HttpClient http;

        public ApiService(HttpClient _http) 
        {
            http = _http;
        }

        public async Task<News> GetReports()
        {
            return await http.GetFromJsonAsync<News>("news");
        }

        public async Task<Owner> GetOwners(string CPF)
        {
            var x = await http.GetFromJsonAsync<Owner>($"owner/{CPF}");
            return x;
        }
    }
}
