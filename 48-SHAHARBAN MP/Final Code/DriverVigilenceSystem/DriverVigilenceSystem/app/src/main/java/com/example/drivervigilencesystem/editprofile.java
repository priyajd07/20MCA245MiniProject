package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

public class editprofile extends AppCompatActivity implements View.OnClickListener {

    EditText ed_name,ed_houseno,ed_place,ed_post,ed_pin,ed_phone;
    ImageView iv1;
    Button bt1;


    //////////////          file upload
    String path, atype, fname, attach="";
    byte[] byteArray = null;
    void showfilechooser(int string) {
        // TODO Auto-generated method stub
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        //getting all types of files

        intent.setType("*/*");
        intent.addCategory(Intent.CATEGORY_OPENABLE);

        try {
            startActivityForResult(Intent.createChooser(intent, "Select a File to Upload"), string);
        } catch (android.content.ActivityNotFoundException ex) {
            // Potentially direct the user to the Market with a Dialog
            Toast.makeText(getApplicationContext(), "Please install a File Manager.", Toast.LENGTH_SHORT).show();

        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK) {
            if (requestCode == 1) {
                ////
                Uri uri = data.getData();

                try {
                    path = FileUtils.getPath(this, uri);

                    File fil = new File(path);
                    float fln = (float) (fil.length() / 1024);
                    atype = path.substring(path.lastIndexOf(".") + 1);


                    fname = path.substring(path.lastIndexOf("/") + 1);
                } catch (URISyntaxException e) {
                    e.printStackTrace();
                }

                try {

                    File imgFile = new File(path);

                    if (imgFile.exists()) {

                        Bitmap myBitmap = BitmapFactory.decodeFile(imgFile.getAbsolutePath());
                        iv1.setImageBitmap(myBitmap);

                    }


                    File file = new File(path);
                    byte[] b = new byte[8192];
                    Log.d("bytes read", "bytes read");

                    InputStream inputStream = new FileInputStream(file);
                    ByteArrayOutputStream bos = new ByteArrayOutputStream();

                    int bytesRead = 0;

                    while ((bytesRead = inputStream.read(b)) != -1) {
                        bos.write(b, 0, bytesRead);
                    }
                    byteArray = bos.toByteArray();

                    String str = Base64.encodeToString(byteArray, Base64.NO_WRAP);
                    attach = str;


                } catch (Exception e) {
                    Toast.makeText(this, "String :" + e.getMessage().toString(), Toast.LENGTH_LONG).show();
                }
            }
        }
    }
    /////////////////


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_editprofile);
        ed_name=(EditText)findViewById(R.id.e2);
        ed_houseno=(EditText)findViewById(R.id.e3);
        ed_place=(EditText)findViewById(R.id.e4);
        ed_post=(EditText)findViewById(R.id.e5);
        ed_pin=(EditText)findViewById(R.id.e6);
        ed_phone=(EditText)findViewById(R.id.e7);
        bt1=(Button) findViewById(R.id.b1);
        iv1=(ImageView) findViewById(R.id.i1);
        bt1.setOnClickListener(this);
        iv1.setOnClickListener(this);

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
                                String phone = jsonObj.getString("phone");
                                String photo = jsonObj.getString("photo");
                                String house = jsonObj.getString("house");
                                String place = jsonObj.getString("place");
                                String post = jsonObj.getString("post");
                                String pin = jsonObj.getString("pin");


                                ed_name.setText(name);
                                ed_phone.setText(phone);
                                ed_houseno.setText(house);
                                ed_place.setText(place);
                                ed_post.setText(post);
                                ed_pin.setText(pin);

                                String url1="http://"+ip+":5000"+photo;
                                Picasso.with(getApplicationContext()).load(url1).transform(new CircleTransform()).into(iv1);

                            } else {

                                Toast.makeText(getApplicationContext(), "No data", Toast.LENGTH_SHORT).show();



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
        if(v==iv1){
            showfilechooser(1);
        }
        if(v==bt1) {
            String name = ed_name.getText().toString();
            String hsno = ed_houseno.getText().toString();
            String plc = ed_place.getText().toString();
            String post = ed_post.getText().toString();
            String pin = ed_pin.getText().toString();
            String cntctno = ed_phone.getText().toString();

            if(name.length()==0){ ed_name.setError("Missing");}
            else if(hsno.length()==0){ ed_houseno.setError("Missing");}
            else if(plc.length()==0){ ed_place.setError("Missing");}
            else if(post.length()==0){ ed_post.setError("Missing");}
            else if(pin.length()==0){ ed_pin.setError("Missing");}
            else if(pin.length()!=6){ ed_pin.setError("invalid");}
            else if(cntctno.length()==0){ ed_phone.setError("Missing");}
            else if(cntctno.length()!=10){ ed_phone.setError("invalid");}
            else {





            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String ip = sh.getString("ip", "");
            String url = "http://" + ip + ":5000/and_edit_profile_driver";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {
                                    Toast.makeText(getApplicationContext(), "Profile updated", Toast.LENGTH_SHORT).show();

                                    Intent ij = new Intent(getApplicationContext(),viewprofile.class);
                                    startActivity(ij);

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

                    params.put("name", name);
                    params.put("hsno", hsno);
                    params.put("place", plc);
                    params.put("post", post);
                    params.put("pin", pin);
                    params.put("cntctno",cntctno);
                    params.put("image", attach);
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
        }}
    }
}