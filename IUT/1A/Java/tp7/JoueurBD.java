import java.sql.*;
import java.util.ArrayList;

public class JoueurBD {
	public ConnexionMySQL laConnexion;

	public JoueurBD(ConnexionMySQL laConnexion){
		this.laConnexion=laConnexion;
	}

	public int maxNumJoueur() throws SQLException{
		Statement stat = laConnexion.createStatement();
		ResultSet res = stat.executeQuery("select max(numJoueur) max from JOUEUR");
		res.next();
		return res.getInt("max");
	}

	public int insererJoueur( Joueur j) throws  SQLException{
		PreparedStatement ps = laConnexion.prepareStatement("insert into JOUEUR values(?,?,?,?,?,?,?);");
        ps.setInt(1,maxNumJoueur()+1);
        ps.setString(2,j.getPseudo());
        ps.setString(3,j.getMotdepasse());
        ps.setInt(6,j.getNiveau());
        ps.setString(4,(""+j.getSexe()+""));
        ps.setBoolean(5,j.isAbonne());
        Blob blob = laConnexion.createBlob();
        blob.setBytes(1,j.getAvatar());
        ps.setBlob(7,blob);
        ps.executeUpdate();
        return this.maxNumJoueur()+1;
	}

	public void effacerJoueur(int num) throws SQLException {
		Statement stat = laConnexion.createStatement();
		stat.executeUpdate("delete from JOUEUR where numJoueur = " + num );
	}

    public void majJoueur(Joueur j)throws SQLException{
		PreparedStatement ps=laConnexion.prepareStatement("update JOUEUR set numJoueur=?, pseudo=?, motdepasse=?, sexe=?, abonne=?, niveau=?, avatar=? where numJoueur=?");
		ps.setInt(1, j.getIdentifiant());
		ps.setString(2,j.getPseudo());
		ps.setString(3,j.getMotdepasse());
		ps.setString(4, ""+j.getSexe());
		String abo;
		if (j.isAbonne()){abo="O";}
		else{abo = "N";} 
		ps.setString(5,abo);
		ps.setInt(6, j.getNiveau());
		Blob b=laConnexion.createBlob();
		b.setBytes(1,j.getAvatar());
		ps.setBlob(7,b);
		ps.setInt(8, j.getIdentifiant());
    }

    public Joueur rechercherJoueurParNum(int num)throws SQLException{
			Statement stat = laConnexion.createStatement();
			ResultSet res = stat.executeQuery("select * from JOUEUR where numJoueur = " + num );
			try {
				res.next();
				int numJ = res.getInt("numJoueur");
				String pseudo = res.getString("pseudo");
				String mdp = res.getString("motdepasse");
				char sexe = res.getString("sexe").charAt(0);
				boolean abdo = res.getString("abonne").charAt(0) == 'O';
				int love = res.getInt("niveau");
				byte[] png = res.getBytes("avatar");

				return new Joueur(numJ, pseudo, mdp, love, sexe, abdo, png);
			}
			catch(Exception zetta){throw new SQLException("Joueur non trouvé");}
    }

    ArrayList<Joueur> listeDesJoueurs() throws SQLException{
		ArrayList<Joueur> resultat = new ArrayList<Joueur>();
		Statement stat = laConnexion.createStatement();
		ResultSet rs=stat.executeQuery("select * from JOUEUR");
		while (rs.next()){
			Joueur j=new Joueur(rs.getInt("numJoueur"),rs.getString("pseudo"),
					rs.getString("motdepasse"),  rs.getInt("niveau"),rs.getString("sexe").charAt(0),
					rs.getString("abonne").charAt(0)=='O',  rs.getBytes("avatar"));
			resultat.add(j);
		}
		rs.close();
		return resultat;
    }

    public String rapportMessage() throws SQLException{
        Statement stat = laConnexion.createStatement();
	    ResultSet rs=stat.executeQuery(
	            "select j2.pseudo pseudoRec, dateMsg, j1.pseudo pseudoExp, contenuMsg "+
                        "from MESSAGE, JOUEUR j1, JOUEUR j2 " +
                        "where j1.numJoueur=idUt1 and j2.numJoueur=idUt2 "+
                        "order by j2.pseudo, dateMsg");
	    String pseudoPrec="", pseudo="111";
	    int cpt=0;
	    String res="";
	    while (rs.next()){
	        pseudo=rs.getString(1);
	        if (! pseudo.equals(pseudoPrec)){
	            if (!pseudoPrec.equals("")){
	                res+="Le nombre total de messages est : "+cpt+"\n\n";
                }
                cpt=0;
	            res+="Messages reçus par"+pseudo+"\n";
	            pseudoPrec=pseudo;
            }
            cpt+=1;
	        res+=rs.getTimestamp(2)+": de "+rs.getString(3)+": "+rs.getString(4)+"\n";
        }
        if (!pseudoPrec.equals("")) {
	        res += "Le nombre total de messages est : " + cpt + "\n\n";
	    }
	    rs.close();
	    return res;
    }
}
