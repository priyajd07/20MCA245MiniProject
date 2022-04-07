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
import android.widget.RatingBar;
import android.widget.Toast;

public class SENDFEEDBACK extends Activity {
	EditText e1;
	Button b1;
	SharedPreferences sh;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_sendfeedback);
		e1=(EditText)findViewById(R.id.editText1);
		b1=(Button)findViewById(R.id.button1);
		sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
	    b1.setOnClickListener(new View.OnClickListener() {
			
				@Override
				public void onClick(View arg0) {
					// TODO Auto-generated method stub
					
					 final String sug = e1.getText().toString();
		              if (sug.equalsIgnoreCase("")) {
		                    e1.setError("Enter suggesions");
		                } 
		             
		                else
		                {



		                RequestQueue queue = Volley.newRequestQueue(SENDFEEDBACK.this);
		                String url ="http://"+sh.getString("ip","")+":5000/fdbk";

		                // Request a string response from the provided URL.
		                StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
		                    @Override
		                    public void onResponse(String response) {
		                        // Display the response string.
		                        Log.d("+++++++++++++++++",response);
		                        try {
		                            JSONObject json=new JSONObject(response);
		                            String res=json.getString("task");

		                            if(res.equalsIgnoreCase("invalid"))
		                            {
		                                Toast.makeText(getApplicationContext(),"invalid",Toast.LENGTH_LONG).show();
		                            }
		                            else
		                            {
		                                Toast.makeText(getApplicationContext(),"success.......",Toast.LENGTH_LONG).show();
		                                
		                                Intent ik = new Intent(getApplicationContext(),USER_HOME.class);
	                                    startActivity(ik);

		                              
		                            }
		                        } catch (JSONException e) {
		                            e.printStackTrace();
		                        }


		                    }
		                }, new Response.ErrorListener() {
		                    @Override
		                    public void onErrorResponse(VolleyError error) {


		                        Toast.makeText(getApplicationContext(),"Error"+error,Toast.LENGTH_LONG).show();
		                    }
		                }){
		                    @Override
		                    protected Map<String, String> getParams()
		                    {
		                        Map<String, String>  params = new HashMap<String, String>();
		                    
								params.put("sug", sug);
		                  
								params.put("id", sh.getString("id", ""));

		                        return params;
		                    }
		                };
		                // Add the request to the RequestQueue.
		                queue.add(stringRequest);
		                }
				}
				
	    });
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.sendfeedback, menu);
		return true;
	}

}
