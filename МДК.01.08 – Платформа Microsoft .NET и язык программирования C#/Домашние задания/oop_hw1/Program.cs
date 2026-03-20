namespace hw1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Rectangle r1 = new Rectangle(10, 20);
            Rectangle r2 = new Rectangle(20, 30);
            double r1_area = r1.GetArea();
            double r1_perimeter = r1.GetPerimeter();
            double r2_area = r2.GetArea();
            double r2_perimeter = r2.GetPerimeter();

            Console.WriteLine("=====ИНФОРМАЦИЯ О ПРЯМОУГОЛЬНИКАХ=====\n");
            Console.WriteLine("Первый прямоугольник:\n");
            Console.WriteLine($"Ширина: {r2.width} \nВысота: {r2.height}");
            Console.WriteLine($"Площадь: {r2_area}");
            Console.WriteLine($"Периметр: {r2_perimeter}");

            Console.WriteLine("Второй прямоугольник:\n");
            Console.WriteLine($"Ширина: {r2.width} \nВысота: {r2.height}");
            Console.WriteLine($"Площадь: {r2_area}");
            Console.WriteLine($"Периметр: {r2_perimeter}");
        }
    }

    class Rectangle
    {
        public double width;
        public double height;

        public Rectangle(double Width, double Height)
        {
            width = Width;
            height = Height;
        }

        public double GetArea()
        {
            return width * height;
        }

        public double GetPerimeter()
        {
            return 2 * (width + height);
        }
    }

}
