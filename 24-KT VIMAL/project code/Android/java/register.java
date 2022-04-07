package com.example.ocrappnew;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Patterns;
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

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class register extends Activity {
EditText firstname,lastname,phone,place,email,uname,pwd;
Button register;
String fname,lname,gen,ph,place1,post1,pin1,email1,username,password;
    String url="";
    String ip="";
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        firstname=findViewById(R.id.fname);
        lastname=findViewById(R.id.lname);


        phone=findViewById(R.id.Phone);
        place=findViewById(R.id.place);


        email=findViewById(R.id.email);
        uname=findViewById(R.id.uname);
        pwd=findViewById(R.id.pwd);
        register=findViewById(R.id.button6);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        ip=sh.getString("ip","");

        url="http://"+ip+":5000/register";

        register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fname=firstname.getText().toString();
                lname=lastname.getText().toString();


                ph=phone.getText().toString();
                place1=place.getText().toString();


                email1=email.getText().toString();
                username=uname.getText().toString();
                password=pwd.getText().toString();

                if(fname.equalsIgnoreCase(""))
                {
                    firstname.setError("enter your firstname");
                    firstname.requestFocus();
                }

                else if(!fname.matches("^[a-zA-Z]*$"))
                {
                    firstname.setError("characters allowed");
                    firstname.requestFocus();
                }


                else if(lname.equalsIgnoreCase(""))
                {
                        lastname.setError("enter your lastname");
                        lastname.requestFocus();
                }

                else if(!lname.matches("^[a-zA-Z]*$"))
                {
                    lastname.setError("characters allowed");
                    lastname.requestFocus();
                }
                else if(ph.equalsIgnoreCase(""))
                {
                    phone.setError("Enter contact");
                    phone.requestFocus();
                }
                else if(ph.length()!=10)
                {
                    phone.setError("Invalid phoneno");
                    phone.requestFocus();
                }
                else if(email1.equalsIgnoreCase(""))
                {
                    email.setError("enter email");
                }
                else if(!Patterns.EMAIL_ADDRESS.matcher(email1).matches())
                {
                    email.setError("Enter Valid Email");
                    email.requestFocus();
                }

                else if(username.equalsIgnoreCase(""))
                {
                    uname.setError("enter your username");
                    uname.requestFocus();
                }
                else if(password.equalsIgnoreCase(""))
                {
                    pwd.setError("enter your password");
                    pwd.requestFocus();
                }
                else {


                    // Instantiate the RequestQueue.
                    RequestQueue queue = Volley.newRequestQueue(register.this);

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.

                            try {
                                JSONObject jo = new JSONObject(response);
                                String status = jo.getString("task");

                                if (status.equalsIgnoreCase("success")) {
                                    Toast.makeText(getApplicationContext(), "Registered ", Toast.LENGTH_SHORT).show();
//
                                    startActivity(new Intent(getApplicationContext(),MainActivity.class));


                                } else {
                                    Toast.makeText(register.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
                                }
                            } catch (Exception e) {

                                Toast.makeText(register.this, "" + e, Toast.LENGTH_SHORT).show();

                            }

                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(register.this, error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {
                            Map<String, String> params = new HashMap<>();
                            params.put("username", username);
                            params.put("password", password);
                            params.put("fname", fname);
                            params.put("lname", lname);

                            params.put("Phone", ph);
                            params.put("Place", place1);


                            params.put("Email", email1);


                            return params;
                        }
                    };
                    // Add the request to the RequestQueue.
                    queue.add(stringRequest);


                }
            }
        });


    }
}