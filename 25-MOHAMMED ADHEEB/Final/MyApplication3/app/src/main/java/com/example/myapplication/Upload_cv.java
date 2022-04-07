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

public class Upload_cv extends AppCompatActivity {
    EditText e1,e2,e3,e4,e5;
    Button b1;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload_cv);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1=(EditText)findViewById(R.id.editText11);
        e2=(EditText)findViewById(R.id.editText12);
        e3=(EditText)findViewById(R.id.editText13);
        e4=(EditText)findViewById(R.id.editText14);
        e5=(EditText)findViewById(R.id.editText15);
        b1=(Button)findViewById(R.id.button8);
         b1.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View view) {
                 final String education=e1.getText().toString();
                 final String institution=e2.getText().toString();
                 final String year=e3.getText().toString();
                 final String regno=e4.getText().toString();
                 final String percentage=e5.getText().toString();
                 if(education.equalsIgnoreCase(""))
                 {
                     e1.setError("Enter your education details");
                 }
                 else if(institution.equalsIgnoreCase(""))
                 {
                     e2.setError("Enter institution");
                 }
                 else if(year.equalsIgnoreCase(""))
                 {
                     e3.setError("Enter year");
                 }
                 else if(regno.equalsIgnoreCase(""))
                 {
                     e4.setError("Enter your name");
                 }
                 else if(percentage.equalsIgnoreCase(""))
                 {
                     e5.setError("Enter your name");
                 }
                 else {
                     RequestQueue queue = Volley.newRequestQueue(Upload_cv.this);
                     String url = "http://" + sh.getString("ip", "") + ":5000/uploadcv";

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

                                     Toast.makeText(Upload_cv.this, "success", Toast.LENGTH_SHORT).show();


                                     Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                     startActivity(ik);

                                 } else {
                                     Toast.makeText(Upload_cv.this, "Failed", Toast.LENGTH_SHORT).show();


                                     Intent ik = new Intent(getApplicationContext(), Candidate_home.class);
                                     startActivity(ik);


                                 }
                             } catch (JSONException e) {
                                 Toast.makeText(Upload_cv.this, "error" + e, Toast.LENGTH_SHORT).show();
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
                             params.put("education", education);
                             params.put("institution", institution);
                             params.put("year", year);
                             params.put("regno", regno);

                             params.put("percentage", percentage);
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
