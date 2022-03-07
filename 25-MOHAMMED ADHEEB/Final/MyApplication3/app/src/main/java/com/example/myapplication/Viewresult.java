package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListView;
import android.widget.Spinner;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.StrictMode;
import android.preference.PreferenceManager;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
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
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
public class Viewresult extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    ListView l1;
    Spinner s;
    String url;
    SharedPreferences sh;
    ArrayList<String> post,pid,userdtls,postt,rank;
    String postid;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewresult);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        s=findViewById(R.id.spinner3);
        l1=findViewById(R.id.list);


        url ="http://"+sh.getString("ip","")+":5000/viewpost";
        s.setOnItemSelectedListener(Viewresult.this);
        RequestQueue queue = Volley.newRequestQueue(Viewresult.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);

                    post= new ArrayList<>(ar.length());
                    pid= new ArrayList<>(ar.length());
                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        post.add(jo.getString("job_name"));
                        pid.add(jo.getString("job_id"));


                    }

                    ArrayAdapter<String> ad=new ArrayAdapter<String>(Viewresult.this,android.R.layout.simple_spinner_item,post);
                    s.setAdapter(ad);

                    // l1.setAdapter(new custom2(Monitoring_signal.this,notification,date));

                } catch (JSONException e) {
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(),"Error",Toast.LENGTH_LONG).show();
            }
        });
        // Add the request to the RequestQueue.
        queue.add(stringRequest);









    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        postid=pid.get(i);



        String url ="http://"+sh.getString("ip", "") + ":5000/viewresult";
        RequestQueue queue = Volley.newRequestQueue(Viewresult.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    userdtls= new ArrayList<>();
                    postt= new ArrayList<>();
                    rank=new ArrayList<>();



                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        userdtls.add(jo.getString("candidate_name")+"   "+jo.getString("email")+"   "+jo.getString("contact_01"));
                        postt.add(jo.getString("job_name"));
                        rank.add((i+1)+"");






                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new Custom3(Viewresult.this,userdtls,postt,rank));
//                    l1.setOnItemClickListener(Viewresult.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(Viewresult.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("pid",postid);



                return params;
            }
        };
        queue.add(stringRequest);






    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }
}