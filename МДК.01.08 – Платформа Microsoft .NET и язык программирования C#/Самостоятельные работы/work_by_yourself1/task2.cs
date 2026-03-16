using System;
using System.Collections.Generic;
using System.Text;

namespace work_by_yourself
{
    internal class task2
    {
        static Queue<string> addTask(Queue<string> queue)
        {
            Console.Write("Введите срочную задачу: ");
            string newTask = Console.ReadLine();
            queue.Enqueue(newTask);
            Console.WriteLine("Задача успешно добавлена!\n");
            return queue;
        }

        static Queue<string> completeTask(Queue<string> queue)
        {
            queue.Dequeue();
            Console.WriteLine("Первая из очереди задача выполнена!\n");
            return queue;
        }

        static void showTasks(Queue<string> queue)
        {
            Console.WriteLine("Все срочные задачи в очереди:");
            foreach (var task in queue)
            {
                Console.WriteLine(task.ToString());
            }
            Console.WriteLine("\n");
        }

        static void Main2(string[] args)
        {
            Queue<string> Tasks = new Queue<string>();

            while (true)
            {
                Console.WriteLine("====ОЧЕРЕДЬ СРОЧНЫХ ЗАДАЧ====\n1. Добавить задачу\n2. Выполнить задачу\n3. Показать все задачи\n");
                Console.Write("Введите номер действия: ");
                string action = Console.ReadLine();
                if (action == "1")
                {
                    addTask(Tasks);
                }
                else if (action == "2")
                {
                    completeTask(Tasks);
                }
                else if (action == "3")
                {
                    showTasks(Tasks);
                }
            }
        }
    }
}
