public class SharedPreferencesDemo extends Activity
{
    EditText editview;


    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

    // Récupération du fichier de préférences par défaut.
    SharedPreferences settings = getPreferences(MODE_PRIVATE);

    // Récupération de la chaîne associée à la clé nommée "text".
    // Si la clé n'existe pas, la chaîne "empty" est retournée.
    String text = settings.getString("text", "empty");

    // La chaîne récupérée est mise dans une view pour affichage.
    editview = (EditText)findViewById(R.id.editview);
    editview.setText(text);
    }

    @Override
    public void onStop()
    {
    super.onStop();

    // Récupération du fichier de préférences par défaut.
    SharedPreferences settings = getPreferences(MODE_PRIVATE);
    // Récupération de l'Editor pour modifier les entrées.
    SharedPreferences.Editor editor = settings.edit();
    // La chaîne est associée à la clé "text".
    editor.putString("text", ( editview.getText() ).toString() );
    // Effectue les modifications.
    editor.commit();
    }
}
