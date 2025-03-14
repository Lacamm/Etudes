package com.example.jamian.first;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity implements MessagesFragment.OnListFragmentInteractionListener {

    MessagesFragment messagesFragment;
    MessageDetailFragment messageDetailFragment;
    Message selectedMessage;
    int nextId=0;
    boolean isResumed=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        messageDetailFragment = (MessageDetailFragment) getSupportFragmentManager().findFragmentById(R.id.mainNoteDetailFrag);
        messagesFragment = (MessagesFragment) getSupportFragmentManager().findFragmentById(R.id.mainNoteFrag);

        Button creer = (Button) findViewById(R.id.Creer);
        Button supprimer = (Button) findViewById(R.id.Supprimer);

        creer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this,SecondActivity.class);
                startActivityForResult(intent,1);
            }
        });
    }

    @Override
    public void onListFragmentInteraction(Message item) {
        Log.d("NoteCallback",item.getAuthor()+" - "+item.getContenu());
        selectedMessage = item;
        messageDetailFragment.update(item);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == Activity.RESULT_OK) {
            String auteur = data.getStringExtra(SecondActivity.EXTRA_AUTHOR);
            String contenu = data.getStringExtra(SecondActivity.EXTRA_CONTENT);
            Message message = new Message(nextId++, auteur, contenu, Calendar.getInstance().getTime());
            messagesFragment.addMessage(message);
            new Thread(() -> {
                ListeMessages ws = null;
                try {
                    ws = new ListeMessages(auteur,contenu);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                boolean ok = ws.call();
                if (!ok)
                    runOnUiThread(() -> Toast.makeText(this,"Erreur dans l'envoi du message",Toast.LENGTH_LONG).show());
                else {
                    runOnUiThread(() ->
                            {
                                if (isResumed)
                                    raffaichirMessages();
                            }
                    );
                }
            }).start();

        }
    }

    public void onSendPressed(View view) {
    }

    @Override
    public void onResume() {
        super.onResume();
        isResumed=true;
        raffaichirMessages();
    }

//    public void nouveauMessage(View vue){
//        //Message message = new Message(70,"moi","blabla", Calendar.getInstance().getTime());
//        messagesFragment.addMessage(message);
//    }

    public void supprimerMessage(View vue){
        messagesFragment.deleteMessageFromID(selectedMessage.getId());
        //messagesFragment.deleteMessage("moi");
    }

    private void raffaichirMessages() {
        new Thread(() -> {
            ListeMessages ws = null;
            try {
                ws = new ListeMessages();
            } catch (IOException e) {
                e.printStackTrace();
            }
            ArrayList<Message> aAjouter = ws.call();
            try {
                runOnUiThread(() -> {
                    messagesFragment.deleteMessage;
                    for (Message m : aAjouter)
                    {
                        messagesFragment.addMessage(m.getId(),m.getVraieDate(),m.getTitre(),m.getContenu());
                    }
                });
            }
            catch (Exception e)
            {
                e.printStackTrace();
            }

        }).start();

    }

}
