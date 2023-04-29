using RecNPet.Models;
using System.Net.Http;
using System.Net.Http.Json;

namespace RecNPet.Services
{
    public class ApiService
    {
        private HttpClient http;

        class Reports
        {
            public Dictionary<string, ReportsInner>[] reports { get; set; }
        }

        class ReportsInner
        {
            Coordinates coordinates { get; set; }
            string date { get; set; }
            string type { get; set; }
        }

        class Coordinates
        {
            float x;
            float y;
        }

        class News
        {
            NewsData[] news { get; set; }
        }
        class NewsData
        {
            string active { get; set;}
            string register_date { get; set;}
            string text { get; set;}
            string title { get; set;}
        }

        public ApiService(HttpClient _http) 
        {
            http = _http;
        }

        public async Task GetReports()
        {
            var x = await http.GetFromJsonAsync<News>("news");
        }

        public async Task<Owner> GetOwners(string CPF)
        {
            var x = await http.GetFromJsonAsync<Owner>($"owner/{CPF}");
            return x;
        }
    }
}
