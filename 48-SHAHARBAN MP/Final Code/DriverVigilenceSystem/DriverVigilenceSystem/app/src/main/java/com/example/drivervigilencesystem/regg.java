package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.ImageView;

public class regg extends AppCompatActivity {
    ImageView im_drv, im_usr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_regg);
        im_drv=(ImageView)findViewById(R.id.imageView3);
        im_usr=(ImageView)findViewById(R.id.imageView7);

        im_drv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("reg_type", "driver");
                ed.commit();
                Intent ij = new Intent(getApplicationContext(),signup.class);
                startActivity(ij);
            }
        });

        im_usr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("reg_type", "user");
                ed.commit();
                Intent ij = new Intent(getApplicationContext(),signup.class);
                startActivity(ij);
            }
        });
    }
}