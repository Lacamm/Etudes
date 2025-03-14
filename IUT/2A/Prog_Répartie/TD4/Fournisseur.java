public class Fournisseur extends Thread{
    int type;
    Stock stock;

    public Fournisseur(int type, Stock stock){
        this.type = type;
        this.stock = stock;
    }

    public void run(){
        while(true){
            if(type==1){
                stock.addCarrosserie();
            }
            else if(type==2){
                stock.addMoteur();
            }
            else if (type==3){
                stock.addRoues();
            }
        }        
    }
}
