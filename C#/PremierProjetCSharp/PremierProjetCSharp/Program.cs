using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PremierProjetCSharp
{
    class Program
    {
        
        static void Main(string[] args)
        {

            string message = "";

            DayOfWeek jour = DateTime.Now.DayOfWeek;

            if (jour != DayOfWeek.Saturday && jour != DayOfWeek.Sunday)
            {
                if (DateTime.Now.Hour > 9 && DateTime.Now.Hour < 18) {
                    message = "Bonjour ";
                }

                else
                {
                    message = "Bonsoir ";
                }
            }

            else
            {
                message = "Bon weekend ";
            }

            message += Environment.UserName;

            Console.WriteLine(message);
        }
    }
}
