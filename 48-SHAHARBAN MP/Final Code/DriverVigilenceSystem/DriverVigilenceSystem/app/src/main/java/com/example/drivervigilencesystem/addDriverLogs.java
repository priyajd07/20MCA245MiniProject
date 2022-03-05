package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class addDriverLogs extends AppCompatActivity implements View.OnClickListener {
    EditText ed1,ed2,ed3,ed4;
    TextView tv1,tv2,tv3,tv4;
    Button bt1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_driver_logs);
        ed1=(EditText)findViewById(R.id.e1);
        ed2=(EditText)findViewById(R.id.e2);
        ed3=(EditText)findViewById(R.id.e3);
        ed4=(EditText)findViewById(R.id.e4);
        tv1=(TextView)findViewById(R.id.t3);
        tv2=(TextView)findViewById(R.id.t3);
        tv3=(TextView)findViewById(R.id.t3);
        tv4=(TextView)findViewById(R.id.t4);
        bt1=(Button) findViewById(R.id.b1);
        bt1.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {
        if(v==bt1) {
            String date = ed1.getText().toString();
            String time = ed2.getText().toString();
            String angle = ed3.getText().toString();
            String speed = ed4.getText().toString();
        }

    }
}