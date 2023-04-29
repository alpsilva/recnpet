namespace RecNPet.Models
{
    public class Address
    {
        public string address { get; set; }
        public string cep { get; set; }
        public string city { get; set; }
        public string neighborhood { get; set; }
        public string number { get; set; }
    }

    public class Disease
    {
        public string description { get; set; }
        public string diagonostic_date { get; set; }
        public int incubation_period_days { get; set; }
        public string name { get; set; }
        public string register_date { get; set; }
        public bool spreads_by_contact { get; set; }
        public string symptoms { get; set; }
        public string veterinary_id { get; set; }
    }

    public class OwnerData
    {
        public Address address { get; set; }
        public string cpf { get; set; }
        public string email { get; set; }
        public string name { get; set; }
        public List<Pet> pets { get; set; }
        public string phone { get; set; }
        public string register_date { get; set; }
    }

    public class Pet
    {
        public string breed { get; set; }
        public bool castrated { get; set; }
        public object chip { get; set; }
        public string description { get; set; }
        public List<Disease> diseases { get; set; }
        public string fur { get; set; }
        public string gender { get; set; }
        public string name { get; set; }
        public string register_date { get; set; }
        public string species { get; set; }
        public string stature { get; set; }
    }

    public class Owner
    {
        public string key { get; set; }
        public OwnerData owner { get; set; }
    }


    public class LoginOwner
    {
        public string CPF { get; set; }
    }
}
