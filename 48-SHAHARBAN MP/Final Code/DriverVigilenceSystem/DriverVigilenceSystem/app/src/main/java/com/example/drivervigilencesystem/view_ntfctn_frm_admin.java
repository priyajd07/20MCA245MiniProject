package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.ListView;

public class view_ntfctn_frm_admin extends AppCompatActivity {

    EditText ed1;
    ListView lv1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_ntfctn_frm_admin);
        ed1=(EditText)findViewById(R.id.e1);
        lv1=(ListView) findViewById(R.id.l1);
    }
}