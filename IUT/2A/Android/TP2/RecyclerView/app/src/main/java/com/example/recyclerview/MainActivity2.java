package com.example.recyclerview;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.example.recyclerview.Model.Prof;

public class MainActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
    }

    @Override
    public void finish(){
        EditText nom = findViewById(R.id.edtNomProf);
        EditText mat = findViewById(R.id.edtMatier);
        Prof p = new Prof(nom.getText().toString(), mat.getText().toString());
        Intent intent = new Intent();
        intent.putExtra("prof", p);
        setResult(Activity.RESULT_OK, intent);
        super.finish();
    }

    public void saisirProf(View view) {
        finish();
    }
}