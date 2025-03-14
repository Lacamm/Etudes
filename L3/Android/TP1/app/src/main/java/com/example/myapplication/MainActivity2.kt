package com.example.myapplication

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.widget.ImageView

class MainActivity2 : AppCompatActivity() {
    val TAG="SecondActivity"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        val img:ImageView = findViewById(R.id.img_dogo)

        img.setOnClickListener() {
            Log.d(TAG, "Changement pour activité principale")
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "Démarrage de l'activité secondaire")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "Mise en pause de l'activité secondaire")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "Reprise de l'activité secondaire")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "Arret de l'activité secondaire")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "Redémarrage de l'activité secondaire")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "Destruction de l'activité secondaire")
    }

    override fun onSaveInstanceState(outState: Bundle, outPersistentState: PersistableBundle) {
        super.onSaveInstanceState(outState, outPersistentState)
        Log.d(TAG, "Sauvegarde de l'activité secondaire")
    }

    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        Log.d(TAG, "Restoration de l'activité secondaire")
    }
}