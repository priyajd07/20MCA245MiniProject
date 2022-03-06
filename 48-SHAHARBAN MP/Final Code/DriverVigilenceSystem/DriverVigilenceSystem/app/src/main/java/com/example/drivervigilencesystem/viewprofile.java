package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class viewprofile extends AppCompatActivity implements View.OnClickListener {

    TextView tv_name,tv_addr,tv_phn,tv_email;
    Button bt1;
    ImageView im1;

    @Override
    public void onBackPressed() {
        Intent ij=new Intent(getApplicationContext(), driverhome.class);
        startActivity(ij);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewprofile);
        tv_name=(TextView)findViewById(R.id.tv_name);
        tv_addr=(TextView)findViewById(R.id.tv_addr);
        tv_phn=(TextView)findViewById(R.id.tv_phone);
        tv_email=(TextView)findViewById(R.id.tv_eml);
        bt1=(Button) findViewById(R.id.button2);
        im1=(ImageView)findViewById(R.id.im);
        bt1.setOnClickListener(this);

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip = sh.getString("ip", "");
        String url = "http://" + ip + ":5000/and_view_profile_driver";

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            String sucs = jsonObj.getString("status");
                            if (sucs.equalsIgnoreCase("ok")) {
                                String name = jsonObj.getString("name");
                                String email = jsonObj.getString("email");
                                String phone = jsonObj.getString("phone");
                                String photo = jsonObj.getString("photo");
                                String address = jsonObj.getString("house");
                                address=address + "\n" + jsonObj.getString("place");
                                address=address + "\n" + jsonObj.getString("post");
                                address=address + "\n" + jsonObj.getString("pin");


                                tv_addr.setTextColor(Color.BLACK);
//                                tv_name.setTextColor(Color.BLACK);
                                tv_email.setTextColor(Color.BLACK);
//                                tv_phn.setTextColor(Color.BLACK);

                                tv_name.setText(name);
                                tv_addr.setText(address);
                                tv_email.setText(email);
                                tv_phn.setText(phone);

                                String url1="http://"+ip+":5000"+photo;
                                Picasso.with(getApplicationContext()).load(url1).transform(new CircleTransform()).into(im1);

                            } else {

                                Toast.makeText(getApplicationContext(), "Invalid username or password...", Toast.LENGTH_SHORT).show();



                            }
                        } catch (Exception e) {


                            Toast.makeText(getApplicationContext(), "eeeee" + e.toString(), Toast.LENGTH_LONG).show();

                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() {
                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<>();

                params.put("lid", sh.getString("lid", ""));


                return params;
            }
        };
        int MY_SOCKET_TIMEOUT_MS = 100000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);
    }


    @Override
    public void onClick(View v) {
        if(v==bt1) {
            Intent ij=new Intent(getApplicationContext(), editprofile.class);
            startActivity(ij);
        }
    }
}