package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText e1,e2;
    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1=(findViewById(R.id.editTextTextPersonName));
        e2=(findViewById(R.id.editTextTextPersonName2));
        b1=(findViewById(R.id.button));
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username=e1.getText().toString();
                String password=e2.getText().toString();
            }
        });
    }
}