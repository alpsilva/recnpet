using System.Text.Json.Serialization;

namespace RecNPet.Models
{
    public class News
    {
        [JsonPropertyName("news")]
        public List<NewsData> news { get; set; }
    }
    public class NewsData
    {
        [JsonPropertyName("text")]
        public string text { get; set; }
        [JsonPropertyName("active")]
        public bool active { get; set; }
        [JsonPropertyName("register_date")]
        public string register_date { get; set; }
        [JsonPropertyName("title")]
        public string title { get; set; }
    }
}
