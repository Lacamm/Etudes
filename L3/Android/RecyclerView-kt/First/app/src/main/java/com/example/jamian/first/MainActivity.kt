package com.example.jamian.first

import androidx.appcompat.app.AppCompatActivity
import com.example.jamian.first.MessagesFragment.OnListFragmentInteractionListener
import android.os.Bundle
import android.content.Intent
import android.util.Log
import android.view.View
import android.widget.Button

class MainActivity : AppCompatActivity(), OnListFragmentInteractionListener {
    var messagesFragmaent: MessagesFragment? = null
    var messageDetailFragment: MessageDetailFragment? = null
    var selectedMessage: Message? = null

    val TAG="MainActivity"
    val creer: Button = findViewById(R.id.Créer)
    val supprimer: Button = findViewById(R.id.Supprimer)


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        messageDetailFragment = supportFragmentManager.findFragmentById(R.id.mainNoteDetailFrag) as MessageDetailFragment?
        messagesFragmaent = supportFragmentManager.findFragmentById(R.id.mainNoteFrag) as MessagesFragment?
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
    }

    fun onSendPressed(view: View?) {}
    override fun onListFragmentInteraction(item: Message?) {
        Log.d("MsgCallback", (item?.date.toString()) + (item?.author ?: "(null)") + " - " + (item?.msg ?: "(null)"))
        //TODO

        supprimer.setOnClickListener(View.OnClickListener({messagesFragmaent.deleteMessage("toto")}))
    }

    creer.setOnClickListener(View.OnClickListener(messagesFragmaent.addMessage(item)))
}