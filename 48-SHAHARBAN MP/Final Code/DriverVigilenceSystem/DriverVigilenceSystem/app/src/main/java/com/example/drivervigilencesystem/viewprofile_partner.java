package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class viewprofile_partner extends AppCompatActivity implements View.OnClickListener {

    TextView tv1,tv2,tv3,tv4,tv5,tv6,tv7,tv8;
    Button bt1;
    ImageView im1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewprofile_partner);

        tv1=(TextView)findViewById(R.id.t3);
        tv2=(TextView)findViewById(R.id.t3);
        tv3=(TextView)findViewById(R.id.t3);
        tv4=(TextView)findViewById(R.id.t3);
        tv5=(TextView)findViewById(R.id.t3);
        tv6=(TextView)findViewById(R.id.t3);
        tv7=(TextView)findViewById(R.id.t7);
        tv8=(TextView)findViewById(R.id.t8);
        bt1=(Button) findViewById(R.id.b1);
        im1=(ImageView)findViewById(R.id.i1);
        bt1.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if(v==bt1) {
            String name = tv5.getText().toString();
            String adrs = tv6.getText().toString();
            String phn = tv7.getText().toString();
            String email = tv8.getText().toString();
        }

    }
}