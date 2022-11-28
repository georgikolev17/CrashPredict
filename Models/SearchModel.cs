using System.ComponentModel.DataAnnotations;

namespace CrashVisualizer.Models
{
    public class SearchModel
    {
        [Display(Name = "Select USA state")]
        public UsaStateName UsaStateName { get; set; }
    }
}
