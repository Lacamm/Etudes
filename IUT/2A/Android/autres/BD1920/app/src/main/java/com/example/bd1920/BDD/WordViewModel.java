package com.example.bd1920.BDD;

//The ViewModel's role is to provide data to the UI and survive configuration changes.
// A ViewModel acts as a communication center between the Repository and the UI.
//Your activities and fragments are responsible for drawing data to the screen,
// while your ViewModel can take care of holding and processing all the data needed for the UI.

import android.app.Application;

import com.example.bd1920.MainActivity;
import com.example.bd1920.Models.Word;

import java.util.List;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

public class WordViewModel extends AndroidViewModel {

    private WordRepository mRepository;

    private LiveData<List<Word>> mAllWords;

    private LiveData<Integer> nbElem;

    public WordViewModel (Application application) {
        super(application);
        mRepository = new WordRepository(application);
        mAllWords = mRepository.getAllWordsLD();
        nbElem = mRepository.getNbElemLD();
    }

    public LiveData<List<Word>> getAllWordsLD() { return mAllWords; }

    public LiveData<Integer> getNbElemLD(){ return nbElem; }

    public void insert(Word word) { mRepository.insert(word); }

    public void deleteAll(){ mRepository.deleteAll(); }

    public Integer nbElements(){ return mRepository.getNbElements();}

}
