package com.example.myapplication;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;


public class add_more_personal_details extends AppCompatActivity {
    EditText e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12;
    Button b1, b2;
    SharedPreferences sh;
    RadioButton r1, r2;


    String res;
    String fileName = "", path = "";
    private static final int FILE_SELECT_CODE = 0;
    String dob, obective, house, place, post, pin, father, mother, quardn, relatn;
    String gender = "";
    String url, ip, lid,title,url1;
    String PathHolder="";
    byte[] filedt=null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_more_personal_details);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
         url = "http://" + sh.getString("ip", "") + ":5000/addmore_personal_details";
        r1 = (RadioButton) findViewById(R.id.radioButton);
        r2 = (RadioButton) findViewById(R.id.radioButton2);

        e2 = (EditText) findViewById(R.id.editText19);
        e3 = (EditText) findViewById(R.id.editText20);
        e4 = (EditText) findViewById(R.id.editText21);
        e5 = (EditText) findViewById(R.id.editText22);
        e6 = (EditText) findViewById(R.id.editText23);
        e7 = (EditText) findViewById(R.id.editText24);
        e8 = (EditText) findViewById(R.id.editText25);
        e9 = (EditText) findViewById(R.id.editText26);
        e10 = (EditText) findViewById(R.id.editText27);
        e11 = (EditText) findViewById(R.id.editText28);
        e12 = findViewById(R.id.editTextTextPersonName3);
        b1 = (Button) findViewById(R.id.button12);
        b2 = (Button) findViewById(R.id.button13);

          if (android.os.Build.VERSION.SDK_INT > 9) {
              StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
              StrictMode.setThreadPolicy(policy);
          }






        url1 = "http://" + sh.getString("ip", "") + ":5000/viewpro";
        RequestQueue queue = Volley.newRequestQueue(add_more_personal_details.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url1,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);

                    {
                        JSONObject jo=ar.getJSONObject(0);
                        e2.setText(jo.getString("dob"));
                        e3.setText(jo.getString("objective"));

                        e4.setText(jo.getString("house"));
                        e5.setText(jo.getString("place"));
                        e6.setText(jo.getString("post"));
                        e7.setText(jo.getString("pin"));
                        e8.setText(jo.getString("father"));
                        e9.setText(jo.getString("mother"));
                        e10.setText(jo.getString("guardian"));
                        e11.setText(jo.getString("relation_to_guardian"));
                        if(r1.isChecked())
                        {
                                r1.setChecked(true);
                        }
                        else{
                            r2.setChecked(true);

                        }





                    }


                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(),"Error",Toast.LENGTH_LONG).show();
            }
        }){
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String>  params = new HashMap<String, String>();

                params.put("lid", sh.getString("lid", ""));


                return params;
            }
        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);















        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
                intent.setType("*/*");
//            intent.setType("application/pdf");
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                startActivityForResult(intent, 7);
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                dob = e2.getText().toString();
                obective = e3.getText().toString();

                if (r1.isChecked()) {
                    gender = r1.getText().toString();
                } else {
                    gender = r2.getText().toString();
                }
                house = e4.getText().toString();
                place = e5.getText().toString();
                post = e6.getText().toString();
                pin = e7.getText().toString();
                father = e8.getText().toString();
                mother = e9.getText().toString();
                quardn = e10.getText().toString();
                relatn = e11.getText().toString();

                if (dob.equalsIgnoreCase("")) {
                    e2.setError("Enter dob");
                }
                if (obective.equalsIgnoreCase("")) {
                    e3.setError("Enter objective");
                } else if (!obective.matches("^[a-z A-Z ]*$")) {
                    e3.setError("characters allowed");
                } else if (house.equalsIgnoreCase("")) {
                    e4.setError("Enter house");
                } else if (!house.matches("^[a-zA-Z]*$")) {
                    e4.setError("characters allowed");
                } else if (place.equalsIgnoreCase("")) {
                    e5.setError("Enter place");
                } else if (!place.matches("^[a-zA-Z]*$")) {
                    e5.setError("characters allowed");
                } else if (post.equalsIgnoreCase("")) {
                    e6.setError("Enter post");
                } else if (!post.matches("^[a-zA-Z]*$")) {
                    e6.setError("characters allowed");
                } else if (pin.equalsIgnoreCase("")) {
                    e7.setError("Enter pin");
                } else if (pin.length() != 6) {
                    e7.setError("Invalid pincode");
                } else if (father.equalsIgnoreCase("")) {
                    e8.setError("Enter father name ");
                } else if (!father.matches("^[a-zA-Z]*$")) {
                    e8.setError("characters allowed");
                } else if (mother.equalsIgnoreCase("")) {
                    e9.setError("Enter mother name");
                } else if (!mother.matches("^[a-zA-Z]*$")) {
                    e9.setError("characters allowed");
                } else if (quardn.equalsIgnoreCase("")) {
                    e10.setError("Enter Guardian");
                } else if (!quardn.matches("^[a-zA-Z]*$")) {
                    e10.setError("characters allowed");
                } else if (relatn.equalsIgnoreCase("")) {
                    e11.setError("Enter relation");
                } else if (!relatn.matches("^[a-zA-Z]*$")) {
                    e11.setError("characters allowed");
                } else {

                    uploadBitmap(title);
                }

            }
        });

    }



    ProgressDialog pd;
    private void uploadBitmap(final String title) {
        pd=new ProgressDialog(add_more_personal_details.this);
        pd.setMessage("Uploading....");
        pd.show();
        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                new Response.Listener<NetworkResponse>() {
                    @Override
                    public void onResponse(NetworkResponse response1) {
                        pd.dismiss();
                        String x=new String(response1.data);
                        try {
                            JSONObject obj = new JSONObject(new String(response1.data));
//                        Toast.makeText(Upload_agreement.this, "Report Sent Successfully", Toast.LENGTH_LONG).show();
                            if (obj.getString("task").equalsIgnoreCase("success")) {

                                Toast.makeText(add_more_personal_details.this, "Successfully uploaded", Toast.LENGTH_LONG).show();
                                Intent i=new Intent(getApplicationContext(),add_more_personal_details.class);
                                startActivity(i);
                            } else {
                                Toast.makeText(getApplicationContext(), "failed", Toast.LENGTH_LONG).show();
                            }

                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }


                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }) {

            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<>();


                params.put("dob",dob);
                params.put("obective",obective);
                params.put("file",gender);
                params.put("house",house);
                params.put("place",place);
                params.put("post",post);
                params.put("pin",pin);
                params.put("father",father);
                params.put("mother",mother);
                params.put("quardn",quardn);
                params.put("relatn",relatn);
                params.put("lid",sh.getString("lid",""));

              return params;
            }

            @Override
            protected Map<String, DataPart> getByteData() {
                Map<String, DataPart> params = new HashMap<>();
                long imagename = System.currentTimeMillis();
                params.put("file", new DataPart(PathHolder , filedt ));









                return params;
            }
        };

        Volley.newRequestQueue(this).add(volleyMultipartRequest);
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode) {
            case 7:
                if (resultCode == RESULT_OK) {
                    Uri uri = data.getData();
                    Log.d("File Uri", "File Uri: " + uri.toString());
                    // Get the path
                    try {
                        PathHolder = FileUtils.getPathFromURI(this, uri);
//                        PathHolder = data.getData().getPath();
//                        Toast.makeText(this, PathHolder, Toast.LENGTH_SHORT).show();

                        filedt = getbyteData(PathHolder);
                        Log.d("filedataaa", filedt + "");
//                        Toast.makeText(this, filedt+"", Toast.LENGTH_SHORT).show();
                        e12.setText(PathHolder);
                    }
                    catch (Exception e){
                        Toast.makeText(this, ""+e.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
                break;
        }
    }

    private byte[] getbyteData(String pathHolder) {
        Log.d("path", pathHolder);
        File fil = new File(pathHolder);
        int fln = (int) fil.length();
        byte[] byteArray = null;
        try {
            InputStream inputStream = new FileInputStream(fil);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            byte[] b = new byte[fln];
            int bytesRead = 0;

            while ((bytesRead = inputStream.read(b)) != -1) {
                bos.write(b, 0, bytesRead);
            }
            byteArray = bos.toByteArray();
            inputStream.close();
        } catch (Exception e) {
        }
        return byteArray;


    }





}

