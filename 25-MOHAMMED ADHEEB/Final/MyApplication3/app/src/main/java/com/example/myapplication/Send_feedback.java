package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

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

public class Send_feedback extends AppCompatActivity {
    EditText e1;
    Button b;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_feedback);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=findViewById(R.id.editTextTextMultiLine);
        b=findViewById(R.id.button19);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                final String feed=e1.getText().toString();

                RequestQueue queue = Volley.newRequestQueue(Send_feedback.this);
                String url = "http://" + sh.getString("ip", "") + ":5000/sendfeed";

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

                                Toast.makeText(Send_feedback.this, "success", Toast.LENGTH_SHORT).show();


                                Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                startActivity(ik);

                            } else {
                                Toast.makeText(Send_feedback.this, "Failed", Toast.LENGTH_SHORT).show();


                                Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                startActivity(ik);


                            }
                        } catch (JSONException e) {
                            Toast.makeText(Send_feedback.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                        params.put("feed", feed);
                        params.put("lid", sh.getString("lid",""));

                        return params;
                    }
                };
                queue.add(stringRequest);



            }
        });

    }
}