namespace CrashVisualizer.Models
{
    public class StateViewModel
    {
        public StateViewModel(string name, int population, int area, int crashesPerYear)
        {
            Name=name;
            Population=population;
            Area=area;
            CrashesPerYear=crashesPerYear;
        }

        public string Name { get; set; }

        public int Population { get; set; }

        public int Area { get; set; }

        public int CrashesPerYear { get; set; }
    }
}
