import java.util.List;
import java.util.ArrayList;

class Donjon {
  private String nom;
  private List<Piece> listePieces;
  private List<Objet> recompenses;
  private boolean reussi;

  public Donjon(String nom)
  {
    this.nom = nom;
    this.listePieces = new ArrayList<>();
    this.recompenses = new ArrayList<>();
    this.reussi = false;
  }

  public List<Piece> getListePieces() {
    return listePieces;
  }

  public Piece get_piece(int i)
  {
    return this.listePieces.get(i);
  }
  public void add_piece(Piece piece){ this.listePieces.add(piece);}
  public void add_loot(Objet objet) { this.recompenses.add(objet);}

  public String getNom() {
    return nom;
  }

  public boolean isReussi() {
    return reussi;
  }

  public void setReussi(boolean reussi) {
    this.reussi = reussi;
  }

  public int getNbPiece()
  {
    return this.listePieces.size();
  }

  public List<Objet> getRecompenses() {
    return recompenses;
  }

  public void save()
  {
    for(Piece p: this.listePieces)
      p.save();
  }
}
