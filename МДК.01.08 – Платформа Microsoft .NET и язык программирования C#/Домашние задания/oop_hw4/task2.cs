
namespace hw4
{
    internal class task2
    {
        static void Main(string[] args)
        {
            DatabaseConnector connector = new DatabaseConnector();
            connector.Connect();

            Console.WriteLine("\n");

            DatabaseConnector connector2 = new DatabaseConnector();
            connector2.Connect();
        }
    }
}

class DatabaseConnector
{
    static string connectionString;

    static DatabaseConnector()
    {
        connectionString = "Server=localhost;DB=Test";
        Console.WriteLine("Static constructor called.");
    }

    public DatabaseConnector()
    {
        Console.WriteLine("Instance created");
    }

    public void Connect()
    {
        if (connectionString != null)
        {
            Console.WriteLine($"Connected to database:\n{connectionString}");
        }
        else
        {
            Console.WriteLine("Connection is null");
        }
    }
}
