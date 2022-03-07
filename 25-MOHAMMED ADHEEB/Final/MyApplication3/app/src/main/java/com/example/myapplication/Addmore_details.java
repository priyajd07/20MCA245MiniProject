package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Addmore_details extends AppCompatActivity {
    EditText e1,e2;
    Button b1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_addmore_details);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.editText16);
        e2=(EditText)findViewById(R.id.editText17);
        b1=(Button)findViewById(R.id.button11);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String skill=e1.getText().toString();
                final String experience=e2.getText().toString();
                if(skill.equalsIgnoreCase(""))
                {
                    e1.setError("Enter your skills");
                }
                else if(experience.equalsIgnoreCase(""))
                {
                    e2.setError("Enter your experience");
                }
                else {


                    RequestQueue queue = Volley.newRequestQueue(Addmore_details.this);
                    String url = "http://" + sh.getString("ip", "") + ":5000/more_qualification_details";

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

                                    Toast.makeText(Addmore_details.this, "Success", Toast.LENGTH_SHORT).show();
                                    Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                    startActivity(ik);

                                } else {


                                    Toast.makeText(Addmore_details.this, "Failed", Toast.LENGTH_SHORT).show();


                                    Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                    startActivity(ik);


                                }
                            } catch (JSONException e) {
                                Toast.makeText(Addmore_details.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                            params.put("skill", skill);
                            params.put("experience", experience);
                            params.put("lid", sh.getString("lid", ""));


                            return params;
                        }
                    };
                    queue.add(stringRequest);

                }

            }
        });

    }
}
