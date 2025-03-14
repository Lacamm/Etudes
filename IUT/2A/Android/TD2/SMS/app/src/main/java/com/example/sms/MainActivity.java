package com.example.sms;

import android.app.Activity;
import android.os.Bundle;
import android.telephony.gsm.SmsManager;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

class MainActivity extends Activity {

    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d("mesLogs", "Passgage onCreate");

        Button btnEnvoie = (Button)findViewById(R.id.envoyer);
        final EditText numero =(EditText)findViewById(R.id.numero);
        final EditText message = (EditText)findViewById(R.id.message);
        btnEnvoie.setOnClickListener(new OnClickListener() {

            @SuppressWarnings("deprecation")
            public void onClick(View v) {
                String num = numero.getText().toString();
                String msg = message.getText().toString();

                if(num.length()== 10 && msg.length() > 0){
                    SmsManager.getDefault().sendTextMessage(num, null, msg, null, null);
                    numero.setText("");
                    message.setText("");
                    Log.d("mesLogs", "Passgage conditionnelle");
                }
                else{
                    Toast.makeText(MainActivity.this, "Enter un numero correct et/ou le message", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
    public void onStop() {
        super.onStop();
        Log.d("mesLogs", "Passgage onStop");
    }
}