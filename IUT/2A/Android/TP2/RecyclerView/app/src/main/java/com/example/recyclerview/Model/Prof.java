package com.example.recyclerview.Model;

import android.os.Parcel;
import android.os.Parcelable;

public class Prof implements Parcelable {
    private String nom;
    private String matiere;

    public Prof(String nom, String matiere) {
        this.nom = nom;
        this.matiere = matiere;
    }

    public Prof(Parcel parcel){
        this.nom = parcel.readString();
        this.matiere = parcel.readString();
    }

    public String getNom() {
        return nom;
    }

    public String getMatiere() {
        return matiere;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setMatiere(String matiere) {
        this.matiere = matiere;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int flags) {
        parcel.writeString(nom);
        parcel.writeString(matiere);
    }

    public static Creator<Prof> CREATOR = new Creator<Prof>() {
        @Override
        public Prof createFromParcel(Parcel parcel) {
            return new Prof(parcel);
        }

        @Override
        public Prof[] newArray(int size) {
            return new Prof[1];
        }
    };
}
