using System.Collections.Specialized;
using System.Numerics;

namespace hw2
{
    internal class task3
    {
        static void Main3(string[] args)
        {
            int[] arr = new int[] { 1, 2, 6, -1, 88, 7, 6 };
            int[] filter_arr = new int[] { 6, 88, 7};
            foreach (int i in filter(arr, filter_arr))
            {
                Console.WriteLine(i);
            }
        }

        static int[] filter(int[] array, int[] filter_array)
        {

            List<int> list = array.ToList();

            for (int i = list.Count - 1; i >= 0; i--)
            {
                for(int j = 0; j < filter_array.Length; j++)
                {
                    if(array[i] == filter_array[j])
                    {
                        list.RemoveAt(i);
                    }
                }
            }

            return list.ToArray();
        }
    }
}
