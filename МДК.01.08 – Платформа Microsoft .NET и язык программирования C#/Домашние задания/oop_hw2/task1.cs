namespace hw2
{
    internal class task1
    {
        static void Main1(string[] args)
        {
            Console.WriteLine("Введите символ для создания квадрата: ");
            char a = Convert.ToChar(Console.ReadLine());
            Console.WriteLine("Введите длину стороны квадрата: ");
            double b = Convert.ToInt32(Console.ReadLine());
            square(a, b);
        }

        static void square(char symbol, double side)
        {
            for (int i = 0; i < side; i++)
            {
                for (int j = 0; j < side; j++)
                {
                    Console.Write(symbol + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
