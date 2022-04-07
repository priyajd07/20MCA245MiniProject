package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.app.NotificationManager;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class ip_connect extends AppCompatActivity implements View.OnClickListener {
    EditText ed1;
    Button bt1;


    @Override
    public void onBackPressed() {

        Intent ins= new Intent(Intent.ACTION_MAIN);
        ins.addCategory(Intent.CATEGORY_HOME);
        ins.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(ins);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ip_connect);
        ed1=(EditText)findViewById(R.id.e1);
        bt1=(Button) findViewById(R.id.b1);
        bt1.setOnClickListener(this);



        SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        ed1.setText(sh.getString("ip",""));

        NotificationManager notificationManager =
                (NotificationManager) getApplicationContext().getSystemService(getApplicationContext().NOTIFICATION_SERVICE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M
                && !notificationManager.isNotificationPolicyAccessGranted()) {

            Intent intent = new Intent(
                    android.provider.Settings
                            .ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS);

            startActivity(intent);
        }
    }



    @Override
    public void onClick(View v) {
        if(v==bt1) {


        String ipaddress=ed1.getText().toString();


            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            SharedPreferences.Editor ed = sh.edit();
            ed.putString("ip", ipaddress);
            ed.commit();


            Intent ij = new Intent(getApplicationContext(),login.class);
            startActivity(ij);






        }
    }
}