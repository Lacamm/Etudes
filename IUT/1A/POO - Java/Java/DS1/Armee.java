import java.util.ArrayList;

public class Armee{
    private ArrayList<Fantome> armeeFantomes;

    public Armee(){
        this.armeeFantomes = new ArrayList<>();
    }

    public void enrole(Fantome fantome){
        this.armeeFantomes.add(fantome);
    }

    public void enroleSpecial(Fantome fantome){
        boolean puissanceExistente;
        puissanceExistente = false;
        for (Fantome f:armeeFantomes){
            if (f.getNuisance() == fantome.getNuisance()){
                puissanceExistente = true;
            }
        }
        if (!puissanceExistente){
            this.armeeFantomes.add(fantome);
        }
    }

    public String toString(){
        String res;
        res = "Armee de Fantôme: ";
        for (Fantome f:armeeFantomes){
            res += f;
        }
        return res;
    }

    public Fantome leMoinsNuisible(){
        Fantome fant = null;
        for (Fantome f:armeeFantomes){
            if ((fant == null || f.getNuisance() < fant.getNuisance()) && f.getNuisance() != -1){
                fant = f;
            }
        }
        return fant;
    }
}