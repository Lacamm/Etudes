
import java.util.*;

public class Main {
  public static void main(String[] args){
    Monde m = new Monde();
    m.addPrairies(new Prairie(0, 0, 1));
    m.addPrairies(new Prairie(1, 0, 1));
    m.addPrairies(new Prairie(0, 1, 1));
    m.addPrairies(new Prairie(1, 1, 1));

  }
}