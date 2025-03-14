package com.example.recyclerview.Tools;

import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.recyclerview.Model.Prof;
import com.example.recyclerview.R;

import java.util.ArrayList;

public class MyAdapter extends RecyclerView.Adapter<MyViewHoolder>{
    private static ArrayList<Prof> profs;

    public MyAdapter(ArrayList<Prof> list){
        profs = list;
    }

    @NonNull
    @Override
    // crée des nouvelles vues pour recyclerView
    public MyViewHoolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
        View view = layoutInflater.inflate(R.layout.cells,parent, false);
        MyViewHoolder myViewHoolder = new MyViewHoolder(view);
        return myViewHoolder;
    }

    @Override
    // remplace contenu d'une vue
    public void onBindViewHolder(@NonNull MyViewHoolder holder, int position) {
        Prof prof = profs.get(position);
        holder.display(prof);
    }

    //nb elem à afficher dans recyclerVieww
    @Override
    public int getItemCount() {
        return profs.size();
    }

    public void setProfs(ArrayList<Prof> profs) {
        this.profs = profs;
    }
}
