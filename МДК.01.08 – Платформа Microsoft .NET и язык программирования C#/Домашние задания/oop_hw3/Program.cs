using System.Diagnostics.Metrics;

namespace hw3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book("Преступление и наказание", "Боря");
            Book b2 = new Book("Война и мир", "Ваня");
            Console.WriteLine("=== УЧЕТ СТУДЕНТОВ ===");
            Console.WriteLine($"Начальное количество студентов в системе: {Student.GetCounter()}");
            Console.WriteLine("\n");

            Console.WriteLine("Создан студент Саша");
            Student Sasha = new Student("Саша", b1);
            Console.WriteLine($"Текущее количество студентов в системе: {Student.GetCounter()}");
            Console.WriteLine("Создан студент Андрей");
            Student Andrew = new Student("Андрей", b2);
            Console.WriteLine($"Текущее количество студентов в системе: {Student.GetCounter()}");
            Console.WriteLine("\n");

            Console.WriteLine("=== КОПИРОВАНИЕ ===");
            Console.WriteLine($"Оригинальный студент: {Andrew.name}, его любимая книга: \"{Andrew.favorite_book.title}\" " +
                $"автора {Andrew.favorite_book.author}");
            Student Copy_of_Student = Andrew;
            Book Copy_of_Book = Andrew.favorite_book;

            Console.WriteLine("Копирование данных и внесение изменений...");
            Copy_of_Student.name = "Петя";
            Console.WriteLine($"Изменение имени копии студента на: {Copy_of_Student.name}");

            Book b3 = new Book("Колобок", "Пушкин");
            Copy_of_Student.favorite_book = b3;
            Console.WriteLine($"Изменение названия книги студента на: {Copy_of_Student.favorite_book.title}");
            Console.WriteLine("\n");
            Console.WriteLine("=== РЕЗУЛЬТАТ ===");
            Console.WriteLine($"Имя оригинального студента: {Andrew.name}\nЛюбимая книга оиргинального студента: {Andrew.favorite_book.title}");


        }

        struct Book{
            public string title;
            public string author;

            public Book(string t, string a)
            {
                title = t;
                author = a;
            }
        }

        class Student
        {
            private static int counter = 0;

            public string name;
            public Book favorite_book;

            public Student(string n, Book f_b)
            {
                favorite_book = f_b;
                name = n;
                counter += 1;
            }

            public static int GetCounter() => counter;
        }
    }
}
