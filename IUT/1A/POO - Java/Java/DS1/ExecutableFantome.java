public class ExecutableFantome{
    public static void main(String [] args){
        Fantome lemure = new Fantome("Lémure", "romain", 5);
        Fantome willis = new Fantome("Willis", "slave", 2);
        Fantome mau = new Fantome("Mau", "égyptien");
        Fantome casper = new Fantome("Casper","américain", 1);
        Fantome davyjones = new Fantome("Davy Jones", "hollandais", 5);
        Fantome sleepyhollow = new Fantome("Sleepy Hollow", "amériacain");

        System.out.println(lemure); //aff1
        System.out.println(mau); //aff2
        System.out.println("Niveau de nuissance de Willis: "+ willis.getNuisance());

        Armee armeeFantomes = new Armee();
        armeeFantomes.enrole(lemure);
        armeeFantomes.enrole(willis);
        armeeFantomes.enrole(mau);

        System.out.println(armeeFantomes); //aff3
        System.out.println("Fantome le moins nuisible: "+armeeFantomes.leMoinsNuisible()); //aff4

        Armee armeeFantomes2 = new Armee();
        armeeFantomes2.enroleSpecial(lemure);
        armeeFantomes2.enroleSpecial(willis);
        armeeFantomes2.enroleSpecial(mau);
        armeeFantomes2.enroleSpecial(casper);
        armeeFantomes2.enroleSpecial(davyjones);
        armeeFantomes2.enroleSpecial(sleepyhollow);

        System.out.println(armeeFantomes2); //aff3
    }
}