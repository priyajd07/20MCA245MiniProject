package com.example.drivervigilencesystem;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.MenuItem;
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
import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;


import com.squareup.picasso.Picasso;

import org.jetbrains.annotations.NotNull;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class partner_home extends AppCompatActivity {
    ImageView im;
    TextView tv_name, tv_phone, tv_email, tv_addr;
    Button edt;

//    private ActivityPartnerHomeBinding binding;


    @Override
    public void onBackPressed() {
        return;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

//        binding = ActivityPartnerHomeBinding.inflate(getLayoutInflater());
        setContentView(R.layout.activity_partner_home);

        im=(ImageView) findViewById(R.id.im);
        tv_name=(TextView) findViewById(R.id.tv_name);
        tv_phone=(TextView) findViewById(R.id.tv_phone);
        tv_email=(TextView) findViewById(R.id.tv_eml);
        tv_addr=(TextView) findViewById(R.id.tv_addr);
        edt=(Button)findViewById(R.id.button2);
        edt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent ij=new Intent(getApplicationContext(), editprofile_partner.class);
                startActivity(ij);
            }
        });

        profile_load();
        BottomNavigationView navView = findViewById(R.id.nav_view);
        navView.setItemIconTintList(null);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        navView.setOnNavigationItemSelectedListener(mobj);
    }
    public void profile_load(){
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip = sh.getString("ip", "");
        String url = "http://" + ip + ":5000/and_view_profile_partner";

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
                                address=address + ", " + jsonObj.getString("place");
                                address=address + ",\n" + jsonObj.getString("post");
                                address=address + ", " + jsonObj.getString("pin");


                                tv_addr.setTextColor(Color.BLACK);
//                                tv_name.setTextColor(Color.BLACK);
                                tv_email.setTextColor(Color.BLACK);
//                                tv_phone.setTextColor(Color.BLACK);

                                tv_name.setText(name);
                                tv_addr.setText(address);
                                tv_email.setText(email);
                                tv_phone.setText(phone);

                                String url1="http://"+ip+":5000"+photo;
                                Picasso.with(getApplicationContext()).load(url1).transform(new CircleTransform()).into(im);

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

    private BottomNavigationView.OnNavigationItemSelectedListener mobj
            = new BottomNavigationView.OnNavigationItemSelectedListener() {
        @Override
        public boolean onNavigationItemSelected(@NonNull @NotNull MenuItem item) {
            switch (item.getItemId()){
                case R.id.navigation_home:
                    Intent ij=new Intent(getApplicationContext(), changepassword_partner.class);
                    startActivity(ij);
                    return true;
                case R.id.navigation_dashboard:
                    Intent ik=new Intent(getApplicationContext(), partner_view_driver.class);
                    startActivity(ik);
                    return true;
                case R.id.navigation_notifications:
                    Intent il=new Intent(getApplicationContext(), partner_view_notifications.class);
                    startActivity(il);
                    return true;
                case R.id.navigation_logout:
                    Intent im=new Intent(getApplicationContext(), login.class);
                    startActivity(im);
                    return true;

                case R.id.navhome:
                    Intent ims=new Intent(getApplicationContext(), partner_home.class);
                    startActivity(ims);
                    return true;
            }
            return false;
        }
    };
}