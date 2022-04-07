package com.example.ocrappnew;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class ipset extends Activity {

    EditText ip;
    Button submit;
    String ip1;
    SharedPreferences sp;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ipset);


        submit=findViewById(R.id.button6);
        ip=findViewById(R.id.uname);

        sp= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());



        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                ip1=ip.getText().toString();
                if(ip1.equalsIgnoreCase(""))
                {
                    ip.setError("Enter your IP address");
                    ip.requestFocus();
                }
                else {

                    SharedPreferences.Editor ed = sp.edit();
                    ed.putString("ip", ip1);
                    ed.commit();
                    startActivity(new Intent(getApplicationContext(), MainActivity.class));
                }
            }
        });
    }
}