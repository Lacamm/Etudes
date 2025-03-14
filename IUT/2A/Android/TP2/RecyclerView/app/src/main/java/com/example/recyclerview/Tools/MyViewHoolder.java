package com.example.recyclerview.Tools;

import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.recyclerview.Model.Prof;
import com.example.recyclerview.R;

public class MyViewHoolder extends RecyclerView.ViewHolder {

    private TextView tvName;
    private TextView tvMat;

    public MyViewHoolder(View intenView) {
        super(intenView);
        tvName = intenView.findViewById(R.id.tvNomCells);
        tvMat = intenView.findViewById(R.id.tvMatCells);
    }

    public void display(Prof p){
        tvName.setText(p.getNom());
        tvMat.setText(p.getMatiere());
    }
}
