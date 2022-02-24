package com.example.image_story_teller;

import java.util.HashMap;
import java.util.Map;

import org.json.JSONException;
import org.json.JSONObject;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import android.os.Bundle;
import android.preference.PreferenceManager;
import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class SIGN_UP extends Activity {
	EditText e1,e2,e3,e4,e5;
	Button b1;
	String name,phone,email,password,username;
    SharedPreferences sh;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_sign__up);
		e1=(EditText)findViewById(R.id.editText1);
		e2=(EditText)findViewById(R.id.editText2);
	    e3=(EditText)findViewById(R.id.editText3);
		e5=(EditText)findViewById(R.id.editText5);
		e4=(EditText)findViewById(R.id.editText4);
		b1=(Button)findViewById(R.id.button1);
		sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
	    b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				name=e1.getText().toString();
				phone=e2.getText().toString();
				
				email=e3.getText().toString();
			
				username=e4.getText().toString();
				password=e5.getText().toString();
				 
				if (name.equalsIgnoreCase("")) {
	                    e1.setError("Enter Your name");
	                } 
				if (phone.equalsIgnoreCase("")) {
                    e2.setError("Enter Your phone no");
                }
				 
				 else if (email.equalsIgnoreCase("")) {
	                    e3.setError("Enter Your email");
	                } 
				
				 else if (username.equalsIgnoreCase("")) {
	                    e4.setError("Enter Your username");
	                } 
				 else if (password.equalsIgnoreCase("")) {
	                    e5.setError("Enter Your password");
	                } 
				  
//				 else if(password.length()!=6)
//				 {
//					 e4.setError("Invalid Password");
//				 }
				 else{

				  RequestQueue queue = Volley.newRequestQueue(SIGN_UP.this);
		           String url = "http://" + sh.getString("ip", "") + ":5000/reg";

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
		                    	  
		                 Toast.makeText(SIGN_UP.this,"success", Toast.LENGTH_SHORT).show();

		                          
		                          Intent ik = new Intent(getApplicationContext(), LOGIN.class);
		                          startActivity(ik);

		                      } else {
		                   	 
		                Toast.makeText(SIGN_UP.this,"Invalid", Toast.LENGTH_SHORT).show();                          
		                      }
		                  } catch (JSONException e) {
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
		                
		                  params.put("nm",name);
		                  params.put("ph", phone);
		                  params.put("em", email);
		                  params.put("un",username);
		                  params.put("pw",password);
		                 
//		         

		                  return params;
		              }
		          };
		          queue.add(stringRequest);
				 }
				
				
				
				
				
				
			}

			private boolean isValidphone(String phone) {
				// TODO Auto-generated method stub
				if (phone != null && phone.length() > 9 && phone.length()<=12) {
					return true;
				}
				return false;
			}
		});
		
	
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.sign__u, menu);
		return true;
	}

}
