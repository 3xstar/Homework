using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Text;

namespace work_by_yourself
{
    internal class task3
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

        static void checkTag(HashSet<string> tags)
        {
            Console.WriteLine("Введите имя тега для проверки: ");
            string tag = Console.ReadLine();

            if (tags.Contains(tag))
            {
                Console.WriteLine("Такой тег существует! :)");
            }
            else
            {
                Console.WriteLine("Такого тега не существует :(");
            }

            Console.WriteLine("\n");
        }

        static void Main3(string[] args)
        {
            HashSet<string> Tags = new HashSet<string>();

            while (true)
            {
                Console.WriteLine("=====УПРАВЛЕНИЕ ТЕГАМИ=====\n1. Добавить тег\n2. Показать все теги\n3. Проверить существование тега\n");
                Console.Write("Введите номер действия: ");
                string action = Console.ReadLine();

                if (action == "1")
                {
                    addTag(Tags);
                }

                else if (action == "2")
                {
                    showTags(Tags);
                }

                else if (action == "3")
                {
                    checkTag(Tags);
                }
            }
        }
    }
}
