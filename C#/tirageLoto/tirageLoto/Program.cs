using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tirageLoto
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] loto = new int[7];

            int i = 0;
            while (i < 7)
            {
                int nombreA = new Random().Next(1, 50);

                if (!dejaPresent(loto, i, nombreA))
                {
                    loto[i] = nombreA;
                    i++;
                }
            }
            AfficheLeTableau(loto);
        }
        private static bool dejaPresent(int[] Tloto, int indice, int nbA)
        {               
            for (int j = 0; j < indice; j++)
            {
                if (Tloto[j] == nbA)
                {
                    return true;
                }
            }
            return false;
        }
        private static void AfficheLeTableau(int[] tabLoto)
        {
            Console.Write("Tirage utilisateur : ");
            for (int k = 0; k < tabLoto.Length; k++)
            {
                Console.Write(tabLoto[k] + " ");
            }
            Console.WriteLine();
        }
    }
}
