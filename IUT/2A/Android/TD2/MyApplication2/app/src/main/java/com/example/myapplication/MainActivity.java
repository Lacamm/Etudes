package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onPause(){
        super.onPause();
    }

    @Override
    protected void onStart(){
        super.onStart();
    }

    @Override
    protected void onRestart(){
        super.onRestart();
    }

    public void appeler(View view){
        EditText editText = findViewById(R.id.edtphone);
        String phoneNumber = editText.getText().toString();
        Intent intent  = new Intent(Intent.ACTION_DIAL);
        if (intent.resolveActivity(getPackageManager()) != null){
            startActivity(intent);
        }
    }

    public void openURL(View view){
        EditText editText = findViewById(R.id.edtURL);
        String URL = "http://"+editText.getText().toString();
        Uri webpage = Uri.parse(URL);
        Intent intent  = new Intent(Intent.ACTION_VIEW, webpage);
        if (intent.resolveActivity(getPackageManager()) != null){
            startActivity(intent);
        }
    }

    public void doToActivity2(View view){
        startActivity(new Intent(this,MainActivity2));
    }

}