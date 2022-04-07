package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class sendfeedback extends AppCompatActivity implements View.OnClickListener {
    EditText ed1;
    Button bt1;

    @Override
    public void onBackPressed() {
        Intent ij=new Intent(getApplicationContext(), driverhome.class);
        startActivity(ij);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sendfeedback);
        ed1=(EditText)findViewById(R.id.editText5);
        bt1=(Button) findViewById(R.id.button13);
        bt1.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        String fdbk = ed1.getText().toString();
        if(fdbk.length()==0){
            ed1.setError("Feedback cannot be empty...");
        }
        else{
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String ip = sh.getString("ip", "");
            String url = "http://" + ip + ":5000/and_driver_send_feedback";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {
                                    Toast.makeText(getApplicationContext(), "Feedback sent...", Toast.LENGTH_SHORT).show();
                                    ed1.setText("");

                                } else {

                                    Toast.makeText(getApplicationContext(), "Failed", Toast.LENGTH_SHORT).show();
                                }
                            } catch (Exception e) {


                                Toast.makeText(getApplicationContext(), "eeeee" + e.toString(), Toast.LENGTH_LONG).show();

                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // error
                            Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() {
                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    Map<String, String> params = new HashMap<>();

                    params.put("feed", fdbk);
                    params.put("lid", sh.getString("lid", ""));


                    return params;
                }
            };
            int MY_SOCKET_TIMEOUT_MS = 100000;

            postRequest.setRetryPolicy(new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
            requestQueue.add(postRequest);
        }

    }
}