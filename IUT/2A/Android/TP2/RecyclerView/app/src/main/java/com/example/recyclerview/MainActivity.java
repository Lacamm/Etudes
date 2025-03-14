package com.example.recyclerview;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Parcelable;
import android.view.View;
import android.widget.Toast;

import com.example.recyclerview.Model.Prof;
import com.example.recyclerview.Tools.MyAdapter;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private ArrayList<Prof> profs = new ArrayList<Prof>();
    private LinearLayoutManager linearLayoutManager;
    private MyAdapter myAdapter;
    private Object MainActivity2;
    private Parcelable recyclerState;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ajouterProf();
        RecyclerView recyclerView = findViewById(R.id.recyclerview);
        linearLayoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(linearLayoutManager);
        myAdapter = new MyAdapter(profs);
        recyclerView.setAdapter(myAdapter);

    }

    void ajouterProf(){
        for(int i=0;i<20;i++){
            Prof prof =new Prof("Prof"+i,"matiere"+i);
            profs.add(prof);
        }
    }

    public void addProf(View view) {
        startActivityForResult(new Intent(this, MainActivity2.class), 1);
    }

    @Override
    public void onActivityResult(int requestcode,int resultcode,Intent intent) {

        super.onActivityResult(requestcode, resultcode, intent);
        if(requestcode == 1){
            if(resultcode == Activity.RESULT_OK){
                Prof p = intent.getParcelableExtra("prof");
                profs.add(p);
                myAdapter.notifyDataSetChanged();
            }else{
                Toast.makeText(this,"pb recup prof", Toast.LENGTH_LONG).show();
            }
        }
    }

    protected void onSaveInstanceState(Bundle state) {
        super.onSaveInstanceState(state);
        recyclerState = linearLayoutManager.onSaveInstanceState();
        state.putParcelable("infos",recyclerState);
        state.putParcelableArrayList("donnes",profs);
    }

    protected void onRestoreInstanceState(Bundle state){
        super.onRestoreInstanceState(state);
        if(state != null){
            recyclerState = state.getParcelable("infos");
            profs = state.getParcelableArrayList("donnes");
            myAdapter.setProfs(profs);
            myAdapter.notifyDataSetChanged();
        }
    }
}