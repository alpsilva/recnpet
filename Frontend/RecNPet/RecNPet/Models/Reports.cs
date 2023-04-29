using Newtonsoft.Json;

namespace RecNPet.Models
{
    // Root myDeserializedClass = JsonConvert.DeserializeObject<Root>(myJsonResponse);
    public class Coordinates
    {
        public int x { get; set; }
        public int y { get; set; }
    }
    public class ReportsData
    {
        public Coordinates coordinates { get; set; }
        public string date { get; set; }
        public string type { get; set; }
    }

    public class Reports
    {
        public List<ReportsData> reports { get; set; }
    }
}
