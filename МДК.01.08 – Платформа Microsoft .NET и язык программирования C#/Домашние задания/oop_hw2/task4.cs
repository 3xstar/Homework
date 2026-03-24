using System.Collections.Specialized;
using System.Numerics;

namespace hw2
{
    internal class task4
    {
        static void Main4(string[] args)
        {
            Website website = new Website();
            website.SetData("YouTube", "https://youtube.com", "Site for watching", "192.168.0.0");
            website.ShowData();
        }
    }

    class Website
    {
        public string title;
        public string path;
        public string description;
        private string ip_adress;

        public void SetData(string t, string p, string d, string ip)
        {
            title = t;
            path = p;
            description = d;
            ip_adress = ip;
        }

        public void ShowData()
        {
            Console.WriteLine("Название сайта: " + title);
            Console.WriteLine("Путь к сайту: " + path);
            Console.WriteLine("Описание сайта: " + description);
            Console.WriteLine("IP адрес сайта: " + ip_adress);
        }

        public string GetTitle()
        {
            return title;
        }
        public string GetPath()
        {
            return path;
        }
        public string GetDescription()
        {
            return description;
        }
        public string GetIP()
        {
            return ip_adress;
        }
    }
}
