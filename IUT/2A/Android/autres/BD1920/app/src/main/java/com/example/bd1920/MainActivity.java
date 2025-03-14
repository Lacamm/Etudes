package com.example.bd1920;

import android.content.Intent;
import android.os.Bundle;

import com.example.bd1920.BDD.WordViewModel;

import androidx.lifecycle.ViewModelProvider;
import androidx.lifecycle.ViewModelProviders;
import com.example.bd1920.Models.Word;
import com.example.bd1920.Tools.WordListAdapter;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.lifecycle.Observer;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

public class MainActivity extends AppCompatActivity {
    public static final int NEW_WORD_ACTIVITY_REQUEST_CODE = 1;

    //Use ViewModelProviders to associate your ViewModel with your UI controller.
    // When your app first starts, the ViewModelProviders will create the ViewModel.
    // When the activity is destroyed, for example through a configuration change, the ViewModel persists.
    // When the activity is re-created, the ViewModelProviders return the existing ViewModel
    private WordViewModel mWordViewModel;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //Code necessaire pour le menu, pas utilise dans cette appli
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        //gestion du bouton permettant de lancer l'activite qui ajoute des mots a la BD
        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, NewWordActivity.class);
                startActivityForResult(intent, NEW_WORD_ACTIVITY_REQUEST_CODE);
            }
        });


        //gestion de la recyclerview
        RecyclerView recyclerView = findViewById(R.id.recyclerview);
        final WordListAdapter adapter = new WordListAdapter(this);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        //mWordViewModel = ViewModelProviders.of(this).get(WordViewModel.class); deprecated!!
        mWordViewModel = new WordViewModel(this.getApplication());

        //add an observer for the LiveData returned by getAllWordsLD().
        //The onChanged() method fires when the observed data changes and the activity is in the foreground.
        mWordViewModel.getAllWordsLD().observe(this, new Observer<List<Word>>() {
            @Override
            public void onChanged(@Nullable final List<Word> words) {
                // Update the cached copy of the words in the adapter.
                adapter.setWords(words);
                TextView textView = findViewById(R.id.textView3);
                textView.setText("nb elements via getAllWords : "+words.size());
            }
        });
        mWordViewModel.getNbElemLD().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(@Nullable Integer integer) {
                TextView textView = findViewById(R.id.textView4);
                textView.setText("nb elements via observer : "+integer);
            }
        });
    }

    //pour le menu, pas utilise
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    //idem
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == NEW_WORD_ACTIVITY_REQUEST_CODE && resultCode == RESULT_OK) {
            Word word = new Word(data.getStringExtra(NewWordActivity.EXTRA_REPLY));
            mWordViewModel.insert(word);
        } else {
            Toast.makeText(
                    getApplicationContext(),
                    R.string.empty_not_saved,
                    Toast.LENGTH_LONG).show();
        }
    }

    public void deleteAll(View view){
        mWordViewModel.deleteAll();
    }

    //pas d'utilisation des LiveData, il faut cliquer sur le bouton pour mettre a jour le nb d'elements
    public void nbElements(View view){
        TextView textView = findViewById(R.id.textView2);
        textView.setText(mWordViewModel.nbElements().toString());
    }



}
