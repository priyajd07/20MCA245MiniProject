package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
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

public class Apply extends AppCompatActivity {
    TextView t1,t2,t3,t4,t5;
    Button b1;
    SharedPreferences sh;
    String id;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_apply);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        t1=(TextView)findViewById(R.id.textView31);
        t2=(TextView)findViewById(R.id.textView32);
        t3=(TextView)findViewById(R.id.textView33);
        t4=(TextView)findViewById(R.id.textView34);
        t5=(TextView)findViewById(R.id.textView35);
        t1.setText(getIntent().getStringExtra("post"));
        t2.setText(getIntent().getStringExtra("skill"));
        t3.setText(getIntent().getStringExtra("qualification"));
        t4.setText(getIntent().getStringExtra("descrption"));
        t5.setText(getIntent().getStringExtra("experence"));
        id=getIntent().getStringExtra("jobid");
        b1=(Button)findViewById(R.id.button10);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                RequestQueue queue = Volley.newRequestQueue(Apply.this);
                String url = "http://" + sh.getString("ip","") + ":5000/apply_for_job";

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

                                Toast.makeText(Apply.this, "Success", Toast.LENGTH_SHORT).show();
                                Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                startActivity(ik);

                            } else {




                                Toast.makeText(Apply.this, "Failed", Toast.LENGTH_SHORT).show();


                                Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                startActivity(ik);


                            }
                        } catch (JSONException e) {
                            Toast.makeText(Apply.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                        params.put("jobid", id);
                        params.put("lid", sh.getString("lid",""));



                        return params;
                    }
                };
                queue.add(stringRequest);






            }
        });

    }
}
