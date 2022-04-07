package com.example.myapplication;

import android.app.AlertDialog;
import android.content.DialogInterface;
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

public class Login extends AppCompatActivity {
    EditText e1,e2;
    Button b,b1;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=findViewById(R.id.editText);
        e2=findViewById(R.id.editText3);
        b=findViewById(R.id.button2);
        b1=findViewById(R.id.button5);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String username=e1.getText().toString();
                final String password=e2.getText().toString();
                if(username.equalsIgnoreCase(""))
                {
                    e1.setError("Enter username");
                }
                else if(password.equalsIgnoreCase(""))
                {
                    e2.setError("Enter password");
                }
                else {

                    RequestQueue queue = Volley.newRequestQueue(Login.this);
                    String url = "http://" + sh.getString("ip", "") + ":5000/login";

                    // Request a string response from the provided URL.
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++", response);
                            try {
                                JSONObject json = new JSONObject(response);
                                String res = json.getString("task");

                                if (res.equalsIgnoreCase("invalid")) {

                                    Toast.makeText(Login.this, "Invalid username or password", Toast.LENGTH_SHORT).show();
                                } else {


                                    SharedPreferences.Editor edp = sh.edit();
                                    edp.putString("lid", res);
                                    edp.commit();
                                    Toast.makeText(Login.this, "success", Toast.LENGTH_SHORT).show();


                                    Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                    startActivity(ik);


                                }
                            } catch (JSONException e) {
                                Toast.makeText(Login.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                            params.put("uname", username);
                            params.put("pass", password);

                            return params;
                        }
                    };
                    queue.add(stringRequest);
                }


            }
        });


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i=new Intent(getApplicationContext(), Registration.class);
                startActivity(i);
            }
        });
    }
    public void onBackPressed() {
        // TODO Auto-generated method stub
        AlertDialog.Builder ald=new AlertDialog.Builder(Login.this);
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

