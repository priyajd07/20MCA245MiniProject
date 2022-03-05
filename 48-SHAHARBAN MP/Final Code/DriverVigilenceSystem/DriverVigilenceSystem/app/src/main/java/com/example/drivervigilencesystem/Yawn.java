package com.example.drivervigilencesystem;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class Yawn extends AppCompatActivity implements View.OnClickListener {
ImageView I;
Button alert;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_yawn);
        I=(ImageView)findViewById(R.id.imageView2);
        alert=(Button)findViewById(R.id.btn_alert);
        alert.setOnClickListener(this)
        ;
    }

    @Override
    public void onClick(View view) {

    }
}
