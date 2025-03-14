package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    val TAG="MainActivity"
    var rota = 0
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.d(TAG, "Création de l'activité")

        val btn:Button = findViewById(R.id.monbouton)
        val img:ImageView = findViewById(R.id.monImage)


        btn.setOnClickListener {
            Log.d(TAG, "On clique sur le bouton")
            Toast.makeText(this, "Click !", Toast.LENGTH_SHORT).show()

            Log.d(TAG, "Changement pour activité secondaire")
            val intent = Intent(this, MainActivity2::class.java)
            startActivity(intent)

        }

        img.setOnClickListener {
            Log.d(TAG, "On clique sur l'image")
            //Toast.makeText(this, "Click Image !", Toast.LENGTH_SHORT).show()
            Toast.makeText(this, rota.toString(), Toast.LENGTH_SHORT).show()
            
        }
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "Démarrage de l'activité principale")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "Mise en pause de l'activité principale")
    }

    override fun onResume() {
        super.onResume()

        val cpt:TextView = findViewById(R.id.monCPT)
        cpt.text = (rota.toString())

        Log.d(TAG, "Reprise de l'activité principale")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "Arret de l'activité principale")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "Redémarrage de l'activité principale")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "Destruction de l'activité principale")
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        Log.d(TAG, "Sauvegarde de l'activité principale")
        rota ++
        outState.putInt( "rotation",rota)

    }

    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        Log.d(TAG, "Restoration de l'activité principale")
        rota = savedInstanceState.getInt("rotation")
    }

}

