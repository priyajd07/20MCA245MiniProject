package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

public class Candidate_home extends AppCompatActivity {
    Button i1,i2,i3,i4,i5,i6,i7,i8,i9,i11;
    Button b6,b7;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_candidate_home);
//        i1=(ImageButton)findViewById(R.id.imageButton16);
//        i2=(ImageButton)findViewById(R.id.imageButton);
//        i3=(ImageButton)findViewById(R.id.imageButton2);
        b7=findViewById(R.id.bt);
        i4=(Button)findViewById(R.id.Button17);
//        i5=(ImageButton)findViewById(R.id.imageButton3);
//        i6=(ImageButton)findViewById(R.id.imageButton18);
//        i7=(ImageButton)findViewById(R.id.imageButton4);
        i8=(Button)findViewById(R.id.Button5);
        i11=(Button)findViewById(R.id.Button);
        b6=(Button)findViewById(R.id.button6);

        b7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(getApplicationContext(),Upload_cv.class);
                startActivity(i);

            }
        });


        b6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(getApplicationContext(),recommender.class);
                startActivity(i);

            }
        });
//        i9=(ImageButton)findViewById(R.id.imageButton19);
//        i10=(Button)findViewById(R.id.imageButton21);

//
//        i9.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Intent i=new Intent(getApplicationContext(),Viewresult.class);
//                startActivity(i);
//
//            }
//        });
//
//        i10.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Intent i=new Intent(getApplicationContext(),viewresults.class);
//                startActivity(i);
//
//            }
//        });
//
//        i1.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),Upload_cv.class);
//                startActivity(i);
//            }
//        });
//        i2.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),add_more_personal_details.class);
//                startActivity(i);
//            }
//        });
//        i3.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),Addmore_details.class);
//                startActivity(i);
//            }
//        });
        i4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(getApplicationContext(),View_company.class);
                startActivity(i);
            }
        });


        i11.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(getApplicationContext(),Send_feedback.class);
                startActivity(i);

            }
        });


//        i5.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),common_test_intro.class);
//                startActivity(i);
//            }
//        });
//        i6.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),Examintro.class);
//                startActivity(i);
//            }
//        });
//        i7.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                Intent i=new Intent(getApplicationContext(),Send_complaints.class);
//                startActivity(i);
//            }
//        });
        i8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(getApplicationContext(),Login.class);
                startActivity(i);
            }
        });






    }
}