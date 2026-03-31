namespace hw4
{
    internal class task1
    {
        static void Main1(string[] args)
        {
            Order o1 = new Order();
            Order.DisplayInfo();
            Order o2 = new Order();
            Order.DisplayInfo();
            Order o3 = new Order();
            Order.DisplayInfo();
            Order o4 = new Order();
            Order.DisplayInfo();

        }
    }
}

class Order
{
    static int nextId = 0;
    static int OrderId;

    public Order()
    {
        nextId++;
        OrderId = nextId;
    }

    public static void DisplayInfo()
    {
        Console.WriteLine("Order #" + OrderId);
    }
}