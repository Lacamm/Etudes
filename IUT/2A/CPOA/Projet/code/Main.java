import java.util.*;

public class Main {
    public static void main(String [] args){
      Planete planete1 = new Planete();

      Biome biomePrairie = new Biome();

      Prairies prairie1 = new Prairies(3,0,0);
      Prairies prairie2 = new Prairies(5,1,0);
      Prairies prairie3 = new Prairies(1,0,1);
      Prairies prairie4 = new Prairies(8,1,1);

      Lapin lapin1 = new Lapin("mâle",10,0);
      Lapin lapin2 = new Lapin("femelle",10,0);

      biomePrairie.addPrairies(prairie1);
      biomePrairie.addPrairies(prairie2);
      biomePrairie.addPrairies(prairie3);
      biomePrairie.addPrairies(prairie4);


      biomePrairie.addAnimal(lapin1, prairie1);
      biomePrairie.addAnimal(lapin2, prairie1);
      

    int rep=-1;
    Scanner sc=new Scanner(System.in);
    while(rep!=0){

      for(Prairies p : biomePrairie.getPrairie()){
        System.out.println(p);
      }
        System.out.println("0. Quitter");
        System.out.println("1. Continuer");

        rep=sc.nextInt();
        sc.nextLine();

        switch(rep){
          case 1: {
            for(Prairies p : biomePrairie.getPrairie()){
              p.croissanceCarotte();

              for(Animal a : p.getLapin()){
                Integer age = a.getAge();
                a.setAge(age+1);
              }
            }
          break;
        }
      }
    }



  
  }
}
