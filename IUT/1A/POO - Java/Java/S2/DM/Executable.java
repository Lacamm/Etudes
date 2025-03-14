public class Executable{
    public static void main(String [] args) {
        //Oeufs oeufLait;

        Oeufs oeufsLait = new Oeufs("au lait",15,3);
        Oeufs oeufsNoir = new Oeufs("noir",15);
        System.out.println(oeufsLait.toString());
        System.out.println(oeufsNoir.toString());
    }
}