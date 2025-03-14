package com.example.jamian.first;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class SecondActivity extends AppCompatActivity {

    public static final String EXTRA_AUTHOR="auteur";
    public static final String EXTRA_CONTENT="contenu";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        Button valider = (Button) findViewById(R.id.valider);
    }

    public void creerMessage(View view){
        EditText author = findViewById(R.id.author);
        EditText contenu = findViewById(R.id.contenu);

        Intent intent = new Intent();
        intent.putExtra(EXTRA_AUTHOR,author.getText().toString());
        intent.putExtra(EXTRA_CONTENT, contenu.getText().toString());

        setResult(RESULT_OK, intent);
        finish();
    }
}