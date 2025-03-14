package com.example.bd1920.BDD;

import com.example.bd1920.Models.Word;

import java.util.List;

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Query;

//In the DAO (data access object), you specify SQL queries and associate them with method calls.
// The compiler checks the SQL and generates queries from convenience annotations for common queries, such as @Insert.
// The DAO must be an interface or abstract class.By default, all queries must be executed on a separate thread.
// Room uses the DAO to create a clean API for your code.


    //Annotate the class with @Dao to identify it as a DAO class for Room.
    @Dao
    public interface WordDao {


        //You don't have to provide any SQL! (There are also @Delete and @Update annotations
        // for deleting and updating a row, but you are not using them in this app.)
        @Insert
        void insert(Word word);


        //There is no convenience annotation for deleting multiple entities,
        // so annotate the method with the generic @Query.
        @Query("DELETE FROM word_table")
        void deleteAll();

        @Query("SELECT * from word_table ORDER BY word ASC")
        List<Word> getAllWords();

        @Query("SELECT * from word_table ORDER BY word ASC")
        LiveData<List<Word>> getAllWordsLD();

        //create an Observer of the data in the onCreate() method of MainActivity and
        // override the observer's onChanged() method.
        // When the LiveData changes, the observer is notified and onChanged() is executed.
        // You will then update the cached data in the adapter, and the adapter will update what the user sees.

        @Query("SELECT count(*) from word_table")
        int nbElements();

        @Query("SELECT count(*) from word_table")
        LiveData<Integer> nbElementsLD();
    }


