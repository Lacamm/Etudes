public class ExeDI{
    public static void main(String [] args){
        Vaisseau v = new Vaisseau();

        for(int i=0; i<=20; i++){
            try{v.deplacer(-1);}
            catch(DeplacementImpossible DI){
                System.out.println("Le vaisseau est déjà tout à gauche !");
            }
        }

        for(int i=0; i<=20; i++){
            try{v.tirer();}
            catch(PlusDeProjectilesException PE){
                System.out.println("A court de munition !");
            }


        }
    }
}