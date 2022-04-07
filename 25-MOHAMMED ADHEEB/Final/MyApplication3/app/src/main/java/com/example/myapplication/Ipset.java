package com.example.myapplication;


import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class Ipset extends AppCompatActivity {
    EditText e1;
    Button b;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ipset);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.editText2);
        b=(Button)findViewById(R.id.button);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String ip=e1.getText().toString();
                if(ip.equals(""))
                {
                    e1.setError("enter ip");
                }
                else {
                    SharedPreferences.Editor ed = sh.edit();
                    ed.putString("ip", ip);
                    ed.commit();

                    startActivity(new Intent(getApplicationContext(), Login.class));
                }

            }
        });
    }
}
