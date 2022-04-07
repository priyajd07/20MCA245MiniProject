package com.example.ocrappnew;



import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
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

public class MainActivity extends Activity {

    EditText username,password;
    Button login,register;
    String uname,pwd;
    String url="";
    String ip="";
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username=findViewById(R.id.uname);
        password=findViewById(R.id.editTextTextPassword);
        login=findViewById(R.id.button5);
        register=findViewById(R.id.button6);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        ip=sh.getString("ip","");

        url="http://"+sh.getString("ip","")+":5000/logincode";


        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                uname=username.getText().toString();
                pwd=password.getText().toString();

                if (uname.equalsIgnoreCase("")) {
                    username.setError("Enter Your Usename");
                    username.requestFocus();
                } else if (pwd.equalsIgnoreCase("")) {
                    password.setError("Enter your password");
                    password.requestFocus();
                } else {


                    // Instantiate the RequestQueue.
                    RequestQueue queue = Volley.newRequestQueue(MainActivity.this);

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.

                            try {
                                JSONObject jo = new JSONObject(response);
                                String status = jo.getString("task");

                                if (status.equalsIgnoreCase("success")) {
                                    String lid = jo.getString("lid");

                                    SharedPreferences.Editor edt = sh.edit();
                                    edt.putString("lid", lid);
                                    edt.commit();

                                    String type=jo.getString("type");
                                    if(type.equalsIgnoreCase("user"))
                                    {
                                        Intent in = new Intent(getApplicationContext(), home.class);
                                        startActivity(in);
                                    }


//


                                } else
                                {
                                    Toast.makeText(getApplicationContext(), "Invalid username or password", Toast.LENGTH_SHORT).show();
                                }
                            } catch (Exception e) {

                                Toast.makeText(MainActivity.this, ""+e, Toast.LENGTH_SHORT).show();

                            }

                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(MainActivity.this, error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }) {
                        @Override
                        protected Map<String, String> getParams() {
                            Map<String, String> params = new HashMap<>();
                            params.put("username", uname);
                            params.put("password", pwd);

                            return params;
                        }
                    };
                    // Add the request to the RequestQueue.
                    queue.add(stringRequest);
                }


            }


        });
        register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent in = new Intent(getApplicationContext(), register.class);
                startActivity(in);

            }
        });


    }
    public void onBackPressed() {
        // TODO Auto-generated method stub
        AlertDialog.Builder ald=new AlertDialog.Builder(MainActivity.this);
        ald.setTitle("Do you want to Exit")
                .setPositiveButton(" YES ", new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface arg0, int arg1) {
                        Intent in=new Intent(Intent.ACTION_MAIN);
                        in.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                        in.addCategory(Intent.CATEGORY_HOME);
                        startActivity(in);
                    }
                })
                .setNegativeButton(" NO ", new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface arg0, int arg1) {

                    }
                });

        AlertDialog al=ald.create();
        al.show();}

}