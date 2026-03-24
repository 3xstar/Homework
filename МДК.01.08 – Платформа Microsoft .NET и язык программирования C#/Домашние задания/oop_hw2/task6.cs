namespace hw2
{
    internal class task6
    {
        static void Main(string[] args)
        {
            Shop ashan = new Shop();
            ashan.SetData("Ашан", "12 мкр. дом 7", "Магазин для повседневных товаров", 88005553535, "ashan@gmail.com");
            ashan.ShowData();
        }
    }

    class Shop
    {
        public string title;
        public string street;
        public string description;
        public long number;
        public string email;


        public void SetData(string t, string s, string d, long n, string e)
        {
            title = t;
            street = s;
            description = d;
            number = n;
            email = e;
        }

        public void ShowData()
        {
            Console.WriteLine("Название магазина: " + title);
            Console.WriteLine("Адрес магазина: " + street);
            Console.WriteLine("Профиль магазина: " + description);
            Console.WriteLine("Контактный телефон: " + number);
            Console.WriteLine("Контактный email: " + email);
        }

        public string GetTitle()
        {
            return title;
        }
        public string GetStreet()
        {
            return street;
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
