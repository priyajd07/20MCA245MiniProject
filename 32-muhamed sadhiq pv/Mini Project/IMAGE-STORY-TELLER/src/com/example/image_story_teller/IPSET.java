package com.example.image_story_teller;

import android.os.Bundle;
import android.preference.PreferenceManager;
import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class IPSET extends Activity {
	Button b1;
	EditText e1;
	String url="",ip="";
	SharedPreferences sh;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_ipset);
		 b1=(Button)findViewById(R.id.button1);

	        e1=(EditText)findViewById(R.id.editText1);
	        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
	      
	        b1.setOnClickListener(new View.OnClickListener() {
				
				@Override
				public void onClick(View arg0) {
					// TODO Auto-generated method stub
				 ip=e1.getText().toString();
					  SharedPreferences.Editor ed = sh.edit();
				        ed.putString("ip", ip);
				        ed.commit();
				Intent ik = new Intent(getApplicationContext(), LOGIN.class);
                startActivity(ik);
				}
			});		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.ipset, menu);
		return true;
	}

}
