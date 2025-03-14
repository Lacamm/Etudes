class ExecutableWeekEnd{
    public static void main(String [] args){
        Personne Pierre = new Personne("ROCHER","Pierre");
        Personne Paul = new Personne("LENON","Paul");
        Personne Marie = new Personne("COLA","Marie");
        Personne Anna = new Personne("TATION","Anna");

        Depense DePierre1 = new Depense(Pierre,12.00,"Pain");
        Depense DePierre2 = new Depense(Pierre,70.00,"Essence");
        Depense DePaul1 = new Depense(Paul,100.00,"Pizza");
        Depense DePaul2 = new Depense(Paul,10.00,"Vin");
        Depense DeMarie1 = new Depense(Marie,15.00,"Vin");

        WeekEnd WE1 = new WeekEnd();
        
        WE1.ajouterPersonne(Pierre);
        WE1.ajouterPersonne(Paul);
        WE1.ajouterPersonne(Marie);
        WE1.ajouterPersonne(Anna);
        WE1.ajouterDepense(DePierre1);
        WE1.ajouterDepense(DePierre2);
        WE1.ajouterDepense(DePaul1);
        WE1.ajouterDepense(DePaul2);
        WE1.ajouterDepense(DeMarie1);

        System.out.println("Depenses totales: "+WE1.totalDepenses()+"€");
        System.out.println("Depenses totales pour Pierre: "+WE1.totalDepensesPersonne(Pierre)+"€");
        System.out.println("Depenses moyenne pour Paul: "+WE1.depensesMoyenne()+"€");
        System.out.println("Depenses pour Le pain: "+WE1.depenseProduit("Pain")+"€");
        System.out.println("Avoir de Anna pour le WeekEnd: "+WE1.avoirPersonne(Anna)+"€");
    }
}