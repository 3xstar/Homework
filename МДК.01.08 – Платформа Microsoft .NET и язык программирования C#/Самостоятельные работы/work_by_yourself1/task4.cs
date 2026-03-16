namespace work_by_yourself
{
    internal class task4
    {
        static HashSet<string> addTag(HashSet<string> tags)
        {
            Console.Write("Введите название нового тега: ");
            string tag = Console.ReadLine();
            tags.Add(tag);
            Console.WriteLine("Тег успешно добавлен!\n");
            return tags;
        }

        static void showTags(HashSet<string> tags)
        {
            Console.WriteLine("Все существующие теги:");
            foreach (string tag in tags)
            {
                Console.WriteLine(tag);
            }
            Console.WriteLine("\n");
        }

        static bool checkTag(HashSet<string> tags, string tag)
        {

            if (tags.Contains(tag))
            {
                Console.WriteLine("Такой тег существует! :)");
                return true;
            }
            else
            {
                Console.WriteLine("Такого тега не существует :(");
                return false;
            }
        }

        static Dictionary<string, Dictionary<string, string>> addTask(Dictionary<string, Dictionary<string, string>> dict, HashSet<string> tags)
        {
            Console.Write("Введите название задачи: ");
            string title = Console.ReadLine();

            Console.Write("Введите приоритет задачи (от 1 до 3): ");
            string priority = Console.ReadLine();

            showTags(tags);
            Console.Write("Введите тег из списка для присваивания задаче: ");
            string user_tag = Console.ReadLine();

            if (checkTag(tags, user_tag))
            {
                Dictionary<string, string> priority_tag = new Dictionary<string, string>();
                priority_tag.Add(user_tag, priority);

                dict.Add(title, priority_tag);
            }

            Console.WriteLine("Задача успешно добавлена!\n");
            return dict;
        }

        static void showTasksByPriority(Dictionary<string, Dictionary<string, string>> dict)
        {
            Console.Write("Введите приоритет (low или middle или high): ");
            string priority = Console.ReadLine();
            if (priority == "high")
            {
                Console.WriteLine($"Все задачи с приоритетом {priority}: ");
                foreach (var task in dict)
                {
                    if (task.Value.ContainsValue(priority))
                    {
                        Console.WriteLine(task);
                    }
                }
                Console.WriteLine("\n");
            }

            else if (priority == "middle")
            {
                Console.WriteLine($"Все задачи с приоритетом {priority}: ");
                foreach (var task in dict)
                {
                    if (task.Value.ContainsValue(priority))
                    {
                        Console.WriteLine(task);
                    }
                }
                Console.WriteLine("\n");
            }

            else if (priority == "low")
            {
                Console.WriteLine($"Все задачи с приоритетом {priority}: ");
                foreach (var task in dict)
                {
                    if (task.Value.ContainsValue(priority))
                    {
                        Console.WriteLine(task);
                    }
                }
                Console.WriteLine("\n");
            }

            else
            {
                Console.WriteLine("Задач с таким приоритетом не существует\n");
            }
        }

        static void showTasks(Dictionary<string, Dictionary<string, string>> dict)
        {
            Console.WriteLine("Все задачи: ");
            foreach (var task in dict)
            {
                Console.WriteLine(task);
            }
            Console.WriteLine("\n");
        }

        static Dictionary<string, Dictionary<string, string>> changeTag(Dictionary<string, Dictionary<string, string>> dict, HashSet<string> tags)
        {
            showTasks(dict);
            Console.Write("Введите название задачи для изменения тега: ");
            string title = Console.ReadLine();
            foreach (var task in dict)
            {
                if (task.Key.Contains(title))
                {
                    showTags(tags);
                    Console.Write("Введите тег из списка для присваивания задаче: ");
                    string user_tag = Console.ReadLine();

                    if (checkTag(tags, user_tag))
                    {
                        string old_tag = string.Empty;
                        foreach (var tag in task.Value)
                        {
                            old_tag = tag.Key;
                        }

                        Dictionary<string, string> tag_priority = new Dictionary<string, string>();
                        tag_priority.Add(user_tag, task.Value[old_tag]);
                        dict.Remove(task.Key);
                        dict.Add(task.Key, tag_priority);
                    }
                }
            }
            Console.WriteLine("Тег задачи успешно изменен!\n");
            return dict;
        }

        static void Main(string[] args)
        {
            Dictionary<string, Dictionary<string, string>> Tasks = new Dictionary<string, Dictionary<string, string>>();
            HashSet<string> tags = new HashSet<string>();

            while (true)
            {
                Console.WriteLine("====ЗАДАЧИ И ПРИОРИТЕТЫ====\n1. Добавить задачу\n2. Показать задачи по приоритету\n3. Показать все задачи\n4. Показать все теги\n5. Добавить тег\n6. Изменить тег задачи");
                Console.Write("Введите номер действия: ");
                string action = Console.ReadLine();
                if (action == "1")
                {
                    addTask(Tasks, tags);
                }
                else if (action == "2")
                {
                    showTasksByPriority(Tasks);
                }

                else if (action == "3")
                {
                    showTasks(Tasks);
                }
                else if (action == "4")
                {
                    showTags(tags);
                }
                else if (action == "5")
                {
                    addTag(tags);
                }
                else if (action == "6")
                {
                    changeTag(Tasks, tags);
                }
            }
        }
    }
}
