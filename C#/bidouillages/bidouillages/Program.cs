using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bidouillages
{
    class Program
    {
        static int CalculSommeIntersection()
        {
            List<int> multiplesDe3 = new List<int>();
            List<int> multiplesDe5 = new List<int>();

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0)
                    multiplesDe3.Add(i);
                if (i % 5 == 0)
                    multiplesDe5.Add(i);
            }

            int somme = 0;
            foreach (int m3 in multiplesDe3)
            {
                foreach (int m5 in multiplesDe5)
                {
                    if (m3 == m5)
                        somme += m3;
                }
            }
            return somme;
        }

        static void Main(string[] args)
        {
            /*int i = 200;
            short s = (short)i;*/

            /*string chaineAge = "20";
            int age = Convert.ToInt32(chaineAge); // age vaut 20
            int age = int.Parse(chaineAge); // age vaut 20

            Console.WriteLine(age);*/

            /*string chaineAge = "ab20cd";
            int age;
            if (int.TryParse(chaineAge, out age))
            {
                Console.WriteLine("La conversion est possible, age vaut " + age);
            }
            else
            {
                Console.WriteLine("Conversion impossible");
            }*/

            /*Console.WriteLine("Veuillez saisir une phrase et valider avec la touche \"Entrée\"");
            string saisie = Console.ReadLine();
            Console.WriteLine("Vous avez saisi : " + saisie);*/

            /*Console.WriteLine("Veuillez appuyer sur une touche pour démarrer le calcul ...");
            Console.ReadKey(true);
            int somme = 0;
            for (int i = 0; i <= 100; i++)
            {
                somme += i;
            }
            Console.WriteLine(somme);*/

            /*Console.WriteLine("Voulez-vous continuer (O/N) ?");
            ConsoleKeyInfo saisie = Console.ReadKey(true);

            if (saisie.Key == ConsoleKey.O)
            {
                Console.WriteLine("On continue ...");
            }
            else
            {
                Console.WriteLine("On s'arrête ...");
            }*/

            /*Console.WriteLine(CalculSommeIntersection());*/

            int noteDo = 262;
            int noteRe = 294;
            int noteMi = 330;
            int noire = 400;
            int blanche = 800;

            Console.Beep(noteDo, noire);
            Console.Beep(noteDo, noire);
            Console.Beep(noteDo, noire);
            Console.Beep(noteRe, noire);
            Console.Beep(noteMi, blanche);
            Console.Beep(noteRe, blanche);
            Console.Beep(noteDo, noire);
            Console.Beep(noteMi, noire);
            Console.Beep(noteRe, noire);
            Console.Beep(noteRe, noire);
            Console.Beep(noteDo, noire);

        }
    }
}
