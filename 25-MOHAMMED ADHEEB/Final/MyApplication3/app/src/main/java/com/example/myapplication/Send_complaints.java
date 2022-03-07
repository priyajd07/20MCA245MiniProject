package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

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

public class Send_complaints extends AppCompatActivity {
    EditText e1;
    Button b1;
    SharedPreferences sh;
    ListView l1;
    ArrayList<String>com,date,reply;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_complaints);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.editText4);
        b1=(Button)findViewById(R.id.button3);
        l1=findViewById(R.id.list);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String complaints=e1.getText().toString();
                if(complaints.equalsIgnoreCase(""))
                {
                    e1.setError("Enter Complaint");
                }
                else if(!complaints.matches("^[a-zA-Z ]*$"))
                {
                    e1.setError("characters allowed");
                }
                else {
                    RequestQueue queue = Volley.newRequestQueue(Send_complaints.this);
                    String url = "http://" + sh.getString("ip", "") + ":5000/send_complaints";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("success")) {

                                    Toast.makeText(Send_complaints.this, "Success", Toast.LENGTH_SHORT).show();
                                    Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                    startActivity(ik);

                                } else {


                                    Toast.makeText(Send_complaints.this, "Failed", Toast.LENGTH_SHORT).show();


                                    Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                    startActivity(ik);


                                }
                            } catch (JSONException e) {
                                Toast.makeText(Send_complaints.this, "error" + e, Toast.LENGTH_SHORT).show();
                                e.printStackTrace();
                            }


                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {


                            Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {
                            Map<String, String> params = new HashMap<String, String>();
                            params.put("complaints", complaints);
                            params.put("lid", sh.getString("lid", ""));


                            return params;
                        }
                    };
                    queue.add(stringRequest);
                }

            }
        });





        String url ="http://"+sh.getString("ip", "") + ":5000/viewcomreply";
        RequestQueue queue = Volley.newRequestQueue(Send_complaints.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    com= new ArrayList<>();
                    date= new ArrayList<>();
                    reply=new ArrayList<>();



                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        com.add(jo.getString("complaint"));
                        date.add(jo.getString("date"));
                        reply.add(jo.getString("reply"));






                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new Custom3(Send_complaints.this,com,date,reply));
//                    l1.setOnItemClickListener(Send_complaints.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(Send_complaints.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("uid", sh.getString("lid",""));




                return params;
            }
        };
        queue.add(stringRequest);



    }
}
