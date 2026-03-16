namespace work_by_yourself
{
    internal class task1
    {
        static Dictionary<string, int> addTask(Dictionary<string, int> dict)
        {
            Console.Write("Введите название задачи: ");
            string title = Console.ReadLine();

            Console.Write("Введите приоритет задачи (от 1 до 3): ");
            int priority = Convert.ToInt32(Console.ReadLine());
            
            dict.Add(title, priority);
            Console.WriteLine("Задача успешно добавлена!\n");
            return dict;

        }

        static void showTasksByPriority(Dictionary<string, int> dict)
        {
            Console.Write("Введите приоритет (от 1 до 2): ");
            int priority = Convert.ToInt32(Console.ReadLine());
            if (priority < 3)
            {
                Console.WriteLine($"Все задачи с приоритетом выше {priority}: ");
                foreach (var task in dict)
                {
                     if(task.Value > priority)
                     {
                         Console.WriteLine(task);
                     }
                }
                Console.WriteLine("\n");
            }
            else
            {
                Console.WriteLine("Задач выше максимального приоритета не существует\n");
            }
        }

        static void showMaxPriorityTasks(Dictionary<string, int> dict)
        {
             Console.WriteLine($"Все задачи с максимальным приоритетом: ");
            foreach (var task in dict)
            {
                int maxPriority = dict.Values.Max();
                if(task.Value == maxPriority)
                {
                    Console.WriteLine(task);
                }
                Console.WriteLine("\n");
            }

        }

        static void showTasks(Dictionary<string, int> dict)
        {
            Console.WriteLine("Все задачи: ");
            foreach (var task in dict)
            {
                Console.WriteLine(task);
            }
            Console.WriteLine("\n");
        }

        static void Main1(string[] args)
        {
            Dictionary<string, int> Tasks = new Dictionary<string, int>();
            while (true)
            {
                Console.WriteLine("====ЗАДАЧИ И ПРИОРИТЕТЫ====\n1. Добавить задачу\n2. Показать задачи по приоритету\n3. Показать задачи с максимальным приоритетом\n4. Показать все задачи\n");
                Console.Write("Введите номер действия: ");
                string action = Console.ReadLine();
                if (action == "1")
                {
                    addTask(Tasks);
                }
                else if (action == "2")
                {
                    showTasksByPriority(Tasks);
                }

                else if (action == "3")
                {
                    showMaxPriorityTasks(Tasks);
                }
                else if (action == "4")
                {
                    showTasks(Tasks);
                }
            }
        }
    }
}
