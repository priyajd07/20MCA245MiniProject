package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.util.Patterns;
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

public class Registration extends AppCompatActivity {
    EditText e1,e2,e3,e4,e5,e6;
    Button b1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.editText5);
        e2=(EditText)findViewById(R.id.editText6);
        e3=(EditText)findViewById(R.id.editText7);
        e4=(EditText)findViewById(R.id.editText8);
        e5=(EditText)findViewById(R.id.editText9);
        e6=(EditText)findViewById(R.id.editText10);
        b1=(Button)findViewById(R.id.button4);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String name=e1.getText().toString();
                final String email=e2.getText().toString();
                final String contact1=e3.getText().toString();
                final String contactr2=e4.getText().toString();
                final String username=e5.getText().toString();
                final String password=e6.getText().toString();

                if(name.equalsIgnoreCase(""))
                {
                    e1.setError("Enter your name");
                }
                else if(!name.matches("^[a-zA-Z]*$"))
                {
                    e1.setError("characters allowed");
                }
                else if(email.equalsIgnoreCase(""))
                {
                    e2.setError("Enter your Email");
                }
                else if(!Patterns.EMAIL_ADDRESS.matcher(email).matches())
                {
                    e2.setError("Enter Valid Email");
                    e2.requestFocus();
                }
                else if(contact1.equalsIgnoreCase(""))
                {
                    e3.setError("Enter your number");
                }
                else if(contact1.length()!=10)
                {
                    e3.setError("Invalid phoneno");
                }
                else if(contactr2.equalsIgnoreCase(""))
                {
                    e4.setError("Enter extra contact");
                }
                else if(contactr2.length()!=10)
                {
                    e4.setError("Invalid phoneno");
                }
                else if(username.equalsIgnoreCase(""))
                {
                    e5.setError("Enter your username");
                }
                else if(password.equalsIgnoreCase(""))
                {
                    e6.setError("Enter your password");
                }
                else {


                    RequestQueue queue = Volley.newRequestQueue(Registration.this);
                    String url = "http://" + sh.getString("ip", "") + ":5000/registration";

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

                                    Toast.makeText(Registration.this, "Registration success", Toast.LENGTH_SHORT).show();


                                    Intent ik = new Intent(getApplicationContext(), Login.class);
                                    startActivity(ik);

                                } else {
                                    Toast.makeText(Registration.this, "Registration Failed", Toast.LENGTH_SHORT).show();


                                    Intent ik = new Intent(getApplicationContext(), Login.class);
                                    startActivity(ik);


                                }
                            } catch (JSONException e) {
                                Toast.makeText(Registration.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                            params.put("name", name);
                            params.put("email", email);
                            params.put("contact1", contact1);
                            params.put("contact2", contactr2);

                            params.put("uname", username);
                            params.put("password", password);

                            return params;
                        }
                    };
                    queue.add(stringRequest);


                }




            }
        });
    }
}
