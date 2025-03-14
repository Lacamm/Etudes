package com.example.bd1920.BDD;

//A Repository is a class that abstracts access to multiple data sources.
// The Repository is not part of the Architecture Components libraries,
// but is a suggested best practice for code separation and architecture.
// A Repository class handles data operations. It provides a clean API to the rest of the app for app data.


import android.app.Application;
import android.os.AsyncTask;
import android.util.Log;

import com.example.bd1920.Models.Word;

import java.util.List;

import androidx.lifecycle.LiveData;

public class WordRepository {
//ici, nous n'avons pas utilise la methode getAllWords de WordDao.


    private WordDao mWordDao;
    private LiveData<List<Word>> mAllWords;
    private LiveData<Integer> nbElem;

    WordRepository(Application application) {
        WordRoomDatabase db = WordRoomDatabase.getDatabase(application);
        mWordDao = db.wordDao();
        mAllWords = mWordDao.getAllWordsLD();
        nbElem = mWordDao.nbElementsLD();
    }


    //Pour les LiveData, inutile d'utiliser les AsyncTask, Android se debrouille seul.
    LiveData<List<Word>> getAllWordsLD() {
        return mAllWords;
    }

    LiveData<Integer> getNbElemLD() { return nbElem; }


    public void insert (Word word) {
        new insertAsyncTask(mWordDao).execute(word);
    }

    //AsyncTask obligatoire pour pouvoir manipuler la BD
    private static class insertAsyncTask extends AsyncTask<Word, Void, Void> {

        private WordDao mAsyncTaskDao;

        insertAsyncTask(WordDao dao) {
            mAsyncTaskDao = dao;
        }

        @Override
        protected Void doInBackground(final Word... params) {
            mAsyncTaskDao.insert(params[0]);
            return null;
        }
    }

    public void deleteAll(){
        new deleteAllAsyncTask(mWordDao).execute();
    }

    private static class deleteAllAsyncTask extends AsyncTask<Void,Void,Void> {
        private WordDao mAsyncTaskDao;

        deleteAllAsyncTask(WordDao dao){ mAsyncTaskDao = dao;}

        @Override
        protected Void doInBackground(Void... params){
            mAsyncTaskDao.deleteAll();
            return null;
        }
    }

    public Integer getNbElements(){
        try {
            //la methode get permet de recuperer le resultat calcule par l'AsyncTask dans la methode doInBackground
            return new getNbElementsAsync(mWordDao).execute().get();
        }catch (Exception e) {
            Log.d("test", "pb getNbElements");
        }
        return null;
    }

    private static class getNbElementsAsync extends AsyncTask<Void,Void,Integer>{
        private WordDao mAsyncTaskDao;

        getNbElementsAsync(WordDao dao){mAsyncTaskDao = dao;}

        @Override
        protected Integer doInBackground(Void... params){
            return  new Integer(mAsyncTaskDao.nbElements());
        }
    }
}
