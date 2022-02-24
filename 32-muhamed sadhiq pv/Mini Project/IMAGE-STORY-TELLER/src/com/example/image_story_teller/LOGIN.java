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
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class LOGIN extends Activity {
	Button b1,b2;
	EditText e1,e2;
	String url="",ip="";
	SharedPreferences sh;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_login);
		b1=(Button)findViewById(R.id.button1);
		 b2=(Button)findViewById(R.id.button2);

	        e1=(EditText)findViewById(R.id.editText1);
	        e2=(EditText)findViewById(R.id.editText2);
	        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
	     
	        b2.setOnClickListener(new View.OnClickListener() {
				
				@Override
				public void onClick(View arg0) {
					// TODO Auto-generated method stub
					Intent ik = new Intent(getApplicationContext(), SIGN_UP.class);
                   startActivity(ik);
				}
			});
	        b1.setOnClickListener(new View.OnClickListener() {
				
				@Override
				public void onClick(View arg0) {
					// TODO Auto-generated method stub
				final	String un=e1.getText().toString();
				final	String passwd=e2.getText().toString();
				if (un.equalsIgnoreCase("")) {
	                e1.setError("Enter Your username");
	            } else if (passwd.equalsIgnoreCase("")) {
	                e2.setError("Enter Your Password");
	            }
	            else {
					
					RequestQueue queue = Volley.newRequestQueue(LOGIN.this);
	                url = "http://" + sh.getString("ip", "") + ":5000/login";
	                
	                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
	                    @Override
	                    public void onResponse(String response) {
	                        // Display the response string.
	                        Log.d("+++++++++++++++++", response);
	                        Toast.makeText(getApplicationContext(), "resp" + response, Toast.LENGTH_LONG).show();

	                        try {
	                            JSONObject json = new JSONObject(response);
	                            String res = json.getString("task");

	                            if (res.equalsIgnoreCase("invalid")) {
	                               
	                            	 Toast.makeText(LOGIN.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

	                            } else {
	                            	
//	                            	String []aa=res.split("#");

	                                SharedPreferences.Editor edp = sh.edit();
	                                edp.putString("id", res);
	                                edp.commit();
	               
	                                 Intent ik = new Intent(getApplicationContext(), USER_HOME.class);
	                                 startActivity(ik);
	                            	}
	                            
	                        } catch (JSONException e) {
		                        Toast.makeText(getApplicationContext(), "exp" + e, Toast.LENGTH_LONG).show();

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
	                        params.put("username", un);
	                        params.put("password", passwd);

	                        return params;
	                    }
	                };
	                queue.add(stringRequest);
	            }

				}
	        
	        });
		}
		
		public void onBackPressed() {
	        // TODO Auto-generated method stub
	        AlertDialog.Builder ald=new AlertDialog.Builder(LOGIN.this);
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
	        al.show();
		
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.login, menu);
		return true;
	}

}
