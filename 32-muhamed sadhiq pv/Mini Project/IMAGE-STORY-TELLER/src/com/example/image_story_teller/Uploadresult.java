package com.example.image_story_teller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.util.Log;
import android.view.Menu;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

public class Uploadresult extends Activity {
	  ListView l1;
	    SharedPreferences sp;
	    String url="",imgs;
	    TextView t1;
		ArrayList<String> img,txt;

	

	@SuppressLint("NewApi")
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_uploadresult);
		l1=(ListView)findViewById(R.id.listView1);
//		t1=(TextView)findViewById(R.id.textView1);
//		
		imgs=getIntent().getStringExtra("img");
		
		  try {
			  
			                      JSONArray ar=new JSONArray(imgs);
			  
			                     
			                      img=new ArrayList<String>();
			                      txt=new ArrayList<String>();
			  
			  
			  
			                      for(int i=0;i<ar.length();i++)
			                      {
			                          JSONObject jo=ar.getJSONObject(i);
			               
			                          img.add(jo.getString("image"));
			                          txt.add(jo.getString("text"));
			  
			                      }
			                      l1.setAdapter(new Custom(Uploadresult.this, img,txt));
			                     
			  
			                  } catch (JSONException e) {
			                      Toast.makeText(getApplicationContext(),"e"+e,Toast.LENGTH_LONG).show();
			  
			                      e.printStackTrace();
			                  }
		
//		txt=getIntent().getStringExtra("txt");
//		t1.setText(txt);
		sp=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
		
		 // Instantiate the RequestQueue.
//        RequestQueue queue = Volley.newRequestQueue(Uploadresult.this);
//        // Request a string response from the provided URL.
////        String url ="http://"+sp.getString("ip","")+":5000/story";
//
//        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
//            @Override
//            public void onResponse(String res) {
//                // Display the response string.
//                Log.d("+++++++++++++++++",res);
//               
//
//                try {
//
//                    JSONArray ar=new JSONArray(res);
//
//                   
//                    img=new ArrayList<String>();
//                    txt=new ArrayList<String>();
//
//
//
//                    for(int i=0;i<ar.length();i++)
//                    {
//                        JSONObject jo=ar.getJSONObject(i);
//             
//                        img.add(jo.getString("image"));
//                        txt.add(jo.getString("text"));
//
//                    }
//                    l1.setAdapter(new Custom(Uploadresult.this, img,txt));
//                   
//
//                } catch (JSONException e) {
//                    Toast.makeText(getApplicationContext(),"e"+e,Toast.LENGTH_LONG).show();
//
//                    e.printStackTrace();
//                }
//
//
//            }
//        }, new Response.ErrorListener() {
//            @Override
//            public void onErrorResponse(VolleyError error) {
//
//                Toast.makeText(getApplicationContext(),"Error"+error,Toast.LENGTH_LONG).show();
//            }
//        }){
//        	@Override
//            protected Map<String, String> getParams()
//            {
//                Map<String, String>  params = new HashMap<String, String>();
//                
//			
//
//                return params;
//            }
//        };
//        // Add the request to the RequestQueue.
//        queue.add(stringRequest);
//		 
			
	
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.uploadresult, menu);
		return true;
	}

}
