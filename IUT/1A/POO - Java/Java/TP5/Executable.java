public class Executable{

    public static void main (String [] args){
        Lettre lettre1 = new Lettre('a');
        Lettre lettre2 = new Lettre('z');

        System.out.println(lettre1.toAscii());
        System.out.println(lettre2.toAscii());
        System.out.println();

        System.out.println(lettre1.toMorse());
        System.out.println(lettre2.toMorse());

        System.out.println((char)97);
    }
}