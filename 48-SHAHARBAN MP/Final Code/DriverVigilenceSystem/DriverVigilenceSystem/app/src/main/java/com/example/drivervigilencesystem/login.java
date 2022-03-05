package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class login extends AppCompatActivity implements View.OnClickListener {
    EditText ed1, ed2;
    TextView  tv3, tv4;
    Button b1;

    @Override
    public void onBackPressed() {
        Intent ins= new Intent(getApplicationContext(),ip_connect.class);
        startActivity(ins);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        ed1 = (EditText) findViewById(R.id.atvEmailLog);
        ed2 = (EditText) findViewById(R.id.atvPasswordLog);
//        tv3 = (TextView) findViewById(R.id.t3);
        tv4 = (TextView) findViewById(R.id.tvSignIn);
        b1 = (Button) findViewById(R.id.btnSignIn);
//        tv3.setOnClickListener(this);
        tv4.setOnClickListener(this);
        b1.setOnClickListener(this);

        ed1.setText("noob@gmail.com");
        ed1.setText("sathyan@gmail.com");
        ed2.setText("123");

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {

            Intent intent = new Intent(android.provider.Settings.ACTION_MANAGE_WRITE_SETTINGS);

            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(intent);

        }

    }
    @Override
    public void onRequestPermissionsResult(
            int requestCode,
            String permissions[],
            int[] grantResults) {
        switch (requestCode) {
            case 101:
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    Toast.makeText(login.this, "Permission Granted!", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(login.this, "Permission Denied!", Toast.LENGTH_SHORT).show();
                }
        }
    }

    @Override
    public void onClick(View v) {
        if(v==tv4){



            Intent ij = new Intent(getApplicationContext(),regg.class);
            startActivity(ij);
        }

        if (v == b1) {


            if (ContextCompat.checkSelfPermission(login.this,
                    Manifest.permission.MODIFY_PHONE_STATE)
                    != PackageManager.PERMISSION_GRANTED) {

                ActivityCompat.requestPermissions(login.this,
													 new String[]{Manifest.permission.MODIFY_PHONE_STATE},
													 101);

                Toast.makeText(getApplicationContext(), "cancelled", Toast.LENGTH_SHORT).show();

                // MY_PERMISSIONS_REQUEST_CALL_PHONE is an
                // app-defined int constant. The callback method gets the
                // result of the request.
            }
            else
            {
                Toast.makeText(getApplicationContext(),"Gramnted",Toast.LENGTH_LONG).show();
            }





            String usr = ed1.getText().toString();
            String pwd = ed2.getText().toString();

            if(usr.length()==0)
            {
                ed1.setError("Missing");
            }
            else if(pwd.length()==0)
            {
                ed2.setError("Missing");
            }
            else {


                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                String ip = sh.getString("ip", "");
                String url = "http://" + ip + ":5000/and_login";

                RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                try {
                                    JSONObject jsonObj = new JSONObject(response);
                                    String sucs = jsonObj.getString("status");
                                    if (sucs.equalsIgnoreCase("ok")) {
                                        String lid = jsonObj.getString("lid");
                                        SharedPreferences.Editor ed = sh.edit();
                                        ed.putString("lid", lid);
                                        ed.commit();
                                        if (jsonObj.getString("type").equalsIgnoreCase("driver")) {


                                            Intent k = new Intent(getApplicationContext(), message_service.class);
                                            startService(k);

                                            Intent k2 = new Intent(getApplicationContext(), srvc.class);
                                            startService(k2);
//
                                            Intent k1a = new Intent(getApplicationContext(), Call_service.class);
                                            startService(k1a);


//                                            Intent k1aa = new Intent(getApplicationContext(), Callser.class);
//                                            startService(k1aa);

                                            Intent ij = new Intent(getApplicationContext(), driverhome.class);
                                            startActivity(ij);
                                        }
                                        if (jsonObj.getString("type").equalsIgnoreCase("user")) {
                                            Intent ij = new Intent(getApplicationContext(), partner_home.class);
                                            startActivity(ij);
                                        }
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

                        params.put("user", usr);
                        params.put("pass", pwd);


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
        }
    }
}



