import java.sql.*;

public class ConnexionBD {
	private Connection mysql;
	private boolean connecte=false;
	public ConnexionBD() throws ClassNotFoundException{
		try{
			Class.forName("com.mysql.jdbc.Driver");
		}
		catch(ClassNotFoundException ex){
			System.out.println("Driver introuvable");
		}

}

	public void connecter(String nomServeur, String nomBase, String nomLogin, String motDePasse) throws SQLException {
		try{
			this.mysql = DriverManager.getConnection("jdbc:mysql://servinfo-mariadb:3306/"+nomBase,nomLogin,motDePasse);
			this.connecte = true;
		}
		catch(SQLException ex){
			System.out.println("Msg"+ex.getMessage()+ex.getErrorCode());
		}
	}
	public void close() throws SQLException {
		this.mysql.close();
		this.connecte = false;
	}

  public boolean isConnecte(){ return this.connecte;}

  public Blob createBlob()throws SQLException{
		return this.mysql.createBlob();
	}
	public Statement createStatement() throws SQLException {
		return this.mysql.createStatement();
	}

	public PreparedStatement prepareStatement(String requete) throws SQLException{
		return this.mysql.prepareStatement(requete);
	}

}
