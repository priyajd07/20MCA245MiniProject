package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class viewresults extends AppCompatActivity {

    ListView l1;


    String url;
    SharedPreferences sh;
    ArrayList<String> post,pid,tmark,postt,amark;
    String postid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewresults);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1=findViewById(R.id.list);


        String url ="http://"+sh.getString("ip", "") + ":5000/viewresult1";
        RequestQueue queue = Volley.newRequestQueue(viewresults.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    tmark= new ArrayList<>();
                    postt= new ArrayList<>();
                    amark=new ArrayList<>();



                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        tmark.add(jo.getString("tmark"));
                        postt.add(jo.getString("post"));
                        amark.add(jo.getString("amark"));






                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new Custom3(viewresults.this,postt,tmark,amark));
//                    l1.setOnItemClickListener(Viewresult.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(viewresults.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid",sh.getString("lid",""));



                return params;
            }
        };
        queue.add(stringRequest);


    }
}