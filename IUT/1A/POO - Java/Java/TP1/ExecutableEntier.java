class ExecutableEntier {
   public static void main(String [] args) {
       CoupleEntiers couple = new CoupleEntiers();
       CoupleEntiers autreCouple = new CoupleEntiers(); // 5)  //

       couple.setPrem(-16);
       couple.setSec(-6);
       couple.affiche(); // (1)
       System.out.println(couple.fraction()); // (2)
       
       System.out.println(couple.getPrem()+" "+couple.getSec());
       System.out.println(couple.somme()); // affiche -22
       System.out.println(couple.plus(autreCouple)); // affiche le résulat de la somme de 2 couples     // 5)  //
       couple.affiche();
   }
}

// 3) La division par 0 est impossible, il faut rajouter une condition pour 0 //

// 2) Le couple ne s'affiche pas, il faut créer un méthode d'affichage //

// 4) Il faut rajouter les méthodes: getPrem, getSec et somme //

// 5)  //