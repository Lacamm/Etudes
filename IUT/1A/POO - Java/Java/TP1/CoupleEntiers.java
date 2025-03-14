public class CoupleEntiers {
   private int premier, second;
   public CoupleEntiers() {
       this.premier = 0;
       this.second = 0;
   }
   public void setPrem(int premier) {this.premier = premier;}
   public void setSec(int second) {this.second = second;}
   public int getPrem() {return this.premier;}
   public int getSec() {return this.second;}
   public void permute() {
       int aux;
       aux = this.premier;
       this.premier = this.second;
       this.second = aux;
   }
   public int fraction() {
       if (this.second != 0)
            return this.premier / this.second;
        else 
            return 0;    
   }
   public int somme(){
       return this.premier + this.second;
   }
   public CoupleEntiers plus(CoupleEntiers autreCouple){
       CoupleEntiers res = new CoupleEntiers();
       res.setPrem(this.getPrem()+autreCouple.getPrem());
       res.setSec(this.getSec()+autreCouple.getSec());
       return res;
   }
   public void affiche(){
       System.out.println("("+this.premier+","+this.second+")"); 
   }
   public void affiche2(){
       System.out.println(res)
   }
}