using System.Collections.Specialized;
using System.Numerics;

namespace hw2
{
    internal class task2
    {
        static void Main2(string[] args)
        {
            Console.WriteLine("Введите число для проверки на палиндром: ");
            int numb = Convert.ToInt32(Console.ReadLine());
            palindrom(numb);
        }

        static void palindrom(int numb)
        {
            string str_numb = numb.ToString();
            string reverse_numb = "";
            for(int i = str_numb.Length - 1; i >= 0; i--)
            {
                reverse_numb += str_numb[i];
            }
            if(str_numb == reverse_numb)
            {
                Console.WriteLine("Число является палиндромом!");
            }
            else
            {
                Console.WriteLine("Число не является палиндромом!");
            }
        }
    }
}
