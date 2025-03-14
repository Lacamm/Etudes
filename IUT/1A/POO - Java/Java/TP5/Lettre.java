public class Lettre{
    private char lettre;
    private String morse;

    public Lettre(char lettre){this.lettre = lettre;}
    public Lettre(String morse){this.morse = morse;}

    public int toAscii(){
        int code = (int) this.lettre;
        code -= (int) 'a';
        return code;
    }

    public String toMorse() {
        String [] morses = new String [] {"=_===", "===_=_=_=", "===_=_===_=", "===_=_=", "=", "=_=_===_=", "===_===_=", "=_=_=_=", "=_=", "=_===_===_===", "===_=_===", "=_===_=_=", "===_===", "===_=", "===_===_===", "=_===_===_=", "===_===_=_===", "=_===_=", "=_=_=", "===", "=_=_===", "=_=_=_===", "=_===_===", "===_=_=_===", "===_=_==_===", "===_===_=_="};
        if (this.lettre == ' '){
            return "_______";
        }
        else{
            return morses[toAscii()];
        }
    }

    public char toChar(){
        int code = 32;
        String [] morses = new String [] {"=_===", "===_=_=_=", "===_=_===_=", "===_=_=", "=", "=_=_===_=", "===_===_=", "=_=_=_=", "=_=", "=_===_===_===", "===_=_===", "=_===_=_=", "===_===", "===_=", "===_===_===", "=_===_===_=", "===_===_=_===", "=_===_=", "=_=_=", "===", "=_=_===", "=_=_=_===", "=_===_===", "===_=_=_===", "===_=_==_===", "===_===_=_="};
        for (String cd: morses){
            if(cd == this.morse){code = morses[toAscii()];}
        }
        if(code == 32){return (char) code;}
        else{return (char) code+(int)'a';}
    }

}