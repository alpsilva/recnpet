using RecNPet.Models;

namespace RecNPet.Services
{
    public class PetInfoService
    {
        public List<PetsCardInfo> infos = new List<PetsCardInfo>
        {
            new PetsCardInfo
            {
                name = "Rufus",
                species = "Cachorro",
                years = "2 anos",
                race = "Não especificada",
                sex = "Macho",
                castrated = false,
            },
            new PetsCardInfo
            {
                name = "Daisy",
                species = "Cachorro",
                years = "3 anos",
                race = "Pug",
                sex = "Fêmea",
                castrated = false,
            },
            new PetsCardInfo
            {
                name = "Brutus",
                species = "Cachorro",
                years = "4 anos",
                race = "Não especificada",
                sex = "Macho",
                castrated = true,
            }
        };

        public Owner Owner { get; set; }
    }
}
