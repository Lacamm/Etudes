class Animal {
  private String nom;
  private Habitat monHabitat;

  public String getNom() {
    return nom;
  }

  public void nourrir() {
    this.monHabitat.manger();
  }

  public void setMonHabitat(Habitat habitat){this.monHabitat = habitat;}

}
