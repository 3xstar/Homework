using System.Collections.Specialized;
using System.Net;
using System.Numerics;

namespace hw2
{
    internal class task5
    {
        static void Main5(string[] args)
        {
            Journal ninjago = new Journal();
            ninjago.SetData("Ниндзяго", 2007, "Journal LEGO Ninjago", 88005553535, "lego@gmail.com");
            ninjago.ShowData();
        }
    }

    class Journal
    {
        public string title;
        public int year;
        public string description;
        public long number;
        public string email;
     

        public void SetData(string t, int y, string d, long n, string e)
        {
            title = t;
            year = y;
            description = d;
            number = n;
            email = e;
        }

        public void ShowData()
        {
            Console.WriteLine("Название журнала: " + title);
            Console.WriteLine("Год основания: " + year);
            Console.WriteLine("Описание журнала: " + description);
            Console.WriteLine("Контактный телефон: " + number);
            Console.WriteLine("Контактный email: " + email);
        }

        public string GetTitle()
        {
            return title;
        }
        public int GetYear()
        {
            return year;
        }
        public string GetDescription()
        {
            return description;
        }
        public long GetNumber()
        {
            return number;
        }
        public string GetEmail()
        {
            return email;
        }
    }
}
