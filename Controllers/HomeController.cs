using CrashVisualizer.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.IO;

namespace CrashVisualizer.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(string stateName)
        {
            StateViewModel model = new StateViewModel(stateName, StatesInfo.NewYork.Population, StatesInfo.NewYork.Area, StatesInfo.NewYork.CrashesPerYear);
            return View("StateInfo", model);
        }

        public async Task<IActionResult> Visualise(string id)
        {
            if (id == "New York")
            {
                return this.File(await System.IO.File.ReadAllBytesAsync("./wwwroot/local.html"), "text/html");
            }
            return this.View("Index");
        }

        public async Task<IActionResult> Prediction(string id)
        {
            if (id == "New York")
            {
                return this.File(await System.IO.File.ReadAllBytesAsync("./wwwroot/local1.html"), "text/html");
            }
            return this.View("Index");
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}