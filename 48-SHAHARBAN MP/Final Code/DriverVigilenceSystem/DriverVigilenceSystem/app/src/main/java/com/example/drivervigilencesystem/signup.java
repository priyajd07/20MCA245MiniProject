package com.example.drivervigilencesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
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

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

public class signup extends AppCompatActivity implements View.OnClickListener {
    EditText ed_name,ed_houseno,ed_place,ed_post,ed_pin,ed_phone,ed_email,ed_password,ed_cnfrmpaswrd;
    ImageView iv1;
    Button bt1;


    //////////////          file upload
    String path, atype, fname, attach;
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
        setContentView(R.layout.activity_signup);


        ed_name=(EditText)findViewById(R.id.e2);
        ed_houseno=(EditText)findViewById(R.id.e3);
        ed_place=(EditText)findViewById(R.id.e4);
        ed_post=(EditText)findViewById(R.id.e5);
        ed_pin=(EditText)findViewById(R.id.e6);
        ed_phone=(EditText)findViewById(R.id.e7);
        ed_email=(EditText)findViewById(R.id.e8);
        ed_password=(EditText)findViewById(R.id.e9);
        ed_cnfrmpaswrd=(EditText)findViewById(R.id.e10);
        bt1=(Button) findViewById(R.id.b1);
        iv1=(ImageView) findViewById(R.id.i1);
        bt1.setOnClickListener(this);
        iv1.setOnClickListener(this);


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
            String email = ed_email.getText().toString();
            String password = ed_password.getText().toString();
            String cnfrmpwd = ed_cnfrmpaswrd.getText().toString();
            String emailPattern = "[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+";




            if(name.length()==0)
            {
                ed_name.setError("Missing");
            }
            else if(hsno.length()==0)
            {
                ed_houseno.setError("Missing");
            }
            else if(plc.length()==0)
            {
                ed_place.setError("Missing");
            }
            else if(post.length()==0)
            {
                ed_post.setError("Missing");
            }
            else if(pin.length()==0)
            {
                ed_pin.setError("Missing");
            }
            else if(cntctno.length()==0)
            {
                ed_phone.setError("Missing");
            }
            else if(email.length()==0)
            {
                ed_email.setError("Missing");
            }
            else if(password.length()==0)
            {
                ed_password.setError("Missing");
            }
            else if(cnfrmpwd.length()==0)
            {
                ed_cnfrmpaswrd.setError("Missing");
            }
            else if(!password.equalsIgnoreCase(cnfrmpwd)){
                ed_cnfrmpaswrd.setError("Password mismatch");
            }



            else {

                if (email.matches(emailPattern)) {

                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    String ip = sh.getString("ip", "");
                    String url = "http://" + ip + ":5000/and_signup";

                    RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                    StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                            new Response.Listener<String>() {
                                @Override
                                public void onResponse(String response) {
                                    try {
                                        JSONObject jsonObj = new JSONObject(response);
                                        String sucs = jsonObj.getString("status");
                                        if (sucs.equalsIgnoreCase("ok")) {
                                            Toast.makeText(getApplicationContext(), "Registered", Toast.LENGTH_SHORT).show();

                                            Intent ij = new Intent(getApplicationContext(), login.class);
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
                            params.put("cntctno", cntctno);
                            params.put("email", email);
                            params.put("pass", password);
                            params.put("image", attach);
                            params.put("reg_type", sh.getString("reg_type", ""));


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
                else
                {
                    Toast.makeText(getApplicationContext(),"Invalid email address", Toast.LENGTH_SHORT).show();
                }

            }






        }
    }
}