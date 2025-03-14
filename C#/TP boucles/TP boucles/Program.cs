using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP_boucles
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Console.WriteLine(calculSomme(1, 10));

            List<double> liste = new List<double> { 1.0, 5.5, 9.9, 2.8, 9.6 };
            Console.WriteLine(CalculMoyenne(liste));
            Console.WriteLine(CalculMoyenne2(liste));*/

            Console.WriteLine(SommeMultiples());
        }

        static int calculSomme(int a, int b)
        {
            int res = 0;
            for (int i = a; i<=b ; i++)
            {
                res += i;
            }
            return res;
        }

        static double CalculMoyenne(List<double> list)
        {
            double res = 0.0;
            int tailleListe = list.Count;
            for (int i =0; i<tailleListe; i++)
            {
                res += list[i];
            }
            return res / tailleListe;
        }

        static double CalculMoyenne2(List<double> list)
        {
            double res = 0.0;
            foreach (double valeur in list)
            {
                res += valeur;
            }
            return res / list.Count;
        }

        static int SommeMultiples()
        {
            List<int> trois = new List<int> ();
            List<int> cinq = new List<int> ();
            int res = 0;

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0)
                {
                    trois.Add(i);
                }
                if (i % 5 == 0)
                {
                    cinq.Add(i);
                }
            }

            /*for (int i=3; i<=100; i += 3)
            {
                trois.Add(i);
            }

            for (int i = 5; i <= 100; i += 5)
            {
                cinq.Add(i);
            }*/

            foreach (int valeur in trois)
            {
                foreach (int valeur2 in cinq)
                {
                    if (valeur == valeur2)
                    {
                        res += valeur*2;
                    }
                }
            }

            return res;
        }
    }
}
