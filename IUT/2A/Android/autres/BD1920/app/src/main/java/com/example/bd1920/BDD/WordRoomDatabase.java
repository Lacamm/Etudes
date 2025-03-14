package com.example.bd1920.BDD;

import android.content.Context;
import android.os.AsyncTask;

import com.example.bd1920.Models.Word;

import androidx.annotation.NonNull;
import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;
import androidx.sqlite.db.SupportSQLiteDatabase;


//On indique les entites utilisees dans la BD
@Database(entities = {Word.class}, version = 1)
public abstract class WordRoomDatabase extends RoomDatabase {

    //utilisation du pattern singleton
    public abstract WordDao wordDao();

    private static WordRoomDatabase INSTANCE;


    static WordRoomDatabase getDatabase(final Context context) {
        if (INSTANCE == null) {
            synchronized (WordRoomDatabase.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context.getApplicationContext(),
                            WordRoomDatabase.class, "word_database")
                            .build();

                }
            }
        }
        return INSTANCE;
    }
}
