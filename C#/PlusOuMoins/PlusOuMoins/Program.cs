using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlusOuMoins
{
    class Program
    {
        static void Main(string[] args)
        {
            int valeurATrouver = new Random().Next(0, 100);
            int valeur = -1;
            int compteur = 1;
            while (valeur != valeurATrouver)
            {
                Console.WriteLine("Saisir une valeur entre 0 et 99");
                Console.WriteLine();
                string saisie = Console.ReadLine();

                if (int.TryParse(saisie, out valeur))
                {
                    if (0 <= valeur && valeur < 100)
                    {
                        if (valeur < valeurATrouver)
                        {
                            Console.WriteLine("C'est plus");
                            Console.WriteLine();
                            compteur += 1;
                        }
                        else if (valeur > valeurATrouver)
                        {
                            Console.WriteLine("C'est moins");
                            Console.WriteLine();
                            compteur += 1;
                        }
                        else
                        {
                            Console.WriteLine("Vous avez trouvé en " + compteur + " coups");                            
                        }
                    }
                    else
                    {
                        Console.WriteLine("Le nombre n'est pas das l'intervalle");
                        Console.WriteLine();
                    }
                }
                else
                {
                    Console.WriteLine("Vous n'avez pas saisit un entier");
                    Console.WriteLine();
                }

                
            }
        }
    }
}
