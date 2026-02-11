namespace hw3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Виселица");
            Console.WriteLine();
            List<string> elements = [ "стойка", "перекладина",
                "распорка", "веревка", "голова", "туловище",
                "левая рука", "правая рука", "левая нога",
                "правая нога" ];

            Console.WriteLine();
            Console.Write("Введите загадываемое слово: ");
            string word = Console.ReadLine();
            Console.WriteLine();
            List<string> wordArray = word.Select(c => c.ToString()).ToList();

            List<string> user_letters = [];
            while (true)
            {
                if (elements.Count == 0)
                {
                    Console.WriteLine();
                    Console.WriteLine("Поражение - вы повесились!");
                    break;
                }
                if (string.Join("", user_letters.OrderBy(l => word.IndexOf(l))) == word)
                {
                    Console.WriteLine("Поздравляем! Вы угадали слово!");
                    break;
                }

                Console.WriteLine("Оставшиеся элементы виселицы:");
                foreach(string e in elements)
                {
                    Console.WriteLine(e);
                }

                Console.WriteLine();
                Console.WriteLine("Слово состоит из: " + wordArray.Count + " букв");
                Console.WriteLine("Количество угаданных букв: " + user_letters.Count);
                Console.Write("Текущее слово: ");
                foreach (char c in word)
                {
                    if (user_letters.Contains(c.ToString()))
                        Console.Write(c + " ");
                    else
                        Console.Write("_ ");
                }
                Console.WriteLine();
                Console.WriteLine();

                Console.Write("Угадайте букву из слова: ");
                string letter = Console.ReadLine();

                if (wordArray.Contains(letter))
                {
                    Console.WriteLine("Ты угадал/а букву!");
                    wordArray.RemoveAll(x => x == letter);
                    Console.WriteLine("Оставшееся количество букв: " + wordArray.Count);
                    user_letters.Add(letter);
                }
                else
                {
                    Console.WriteLine("Ты не угадал/а букву!");
                    elements.RemoveAt(elements.Count - 1);
                }

            }
        }
    }
}
