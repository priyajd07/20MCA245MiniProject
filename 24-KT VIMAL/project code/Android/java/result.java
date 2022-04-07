package com.example.ocrappnew;

import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.os.PowerManager;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.HashMap;
import java.util.Map;

public class result extends Activity {
TextView e2,e3,e4,t1;
EditText e1;
Spinner s1,s2,s3;
    private static final int FILE_SELECT_CODE = 0;
    int res;
    String fileName="",path="";
Button b1;
String ff,ft,fs,text,url,ip;
    String []fface={"Select","Berlin Sans FB","Algerian","Arial Black","Agency FB","Arial Rounded MT Bold","Bahnschrift Light","Bahnschrift Light","Bahnschrift Light Condensed","Bahnschrift Light Condensed","Blackadder ITC","Bahnschrift SemiLight SemiConde","Brush Script MT","High Tower Text","High Tower Text","Segoe UI Emoji","Castellar","Bookman Old Style","Nirmala UI Semilight","Broadway","Georgia","Gigi"};
    String []ftype={"Select","normal","bold","italic","all"};
    String []fsize={"Select","12","16","20","24","28","32","36","40","44","48","52","56","60","64","68","72","76","80","84","88","92","96","100"};

    ProgressDialog mProgressDialog;
    private PowerManager.WakeLock mWakeLock;
    static final int DIALOG_DOWNLOAD_PROGRESS = 2;
    SharedPreferences sh;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);
        e1=findViewById(R.id.editTextTextMultiLine);
        e2=findViewById(R.id.textView17);
        e3=findViewById(R.id.textView18);
        e4=findViewById(R.id.textView19);
        s1=findViewById(R.id.spinner2);
        s2=findViewById(R.id.spinner4);
        s3=findViewById(R.id.spinner5);
        b1=findViewById(R.id.button20);
        t1=findViewById(R.id.textView2);



        e1.setText(getIntent().getStringExtra("text"));
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        ip=sh.getString("ip","");

        url="http://"+sh.getString("ip","")+":5000/imgtotext1";


        ArrayAdapter<String> ad=new ArrayAdapter<>(result.this,android.R.layout.simple_list_item_1,fface);
        s1.setAdapter(ad);

        ArrayAdapter<String> ad1=new ArrayAdapter<>(result.this,android.R.layout.simple_list_item_1,ftype);
        s2.setAdapter(ad1);

        ArrayAdapter<String> ad2=new ArrayAdapter<>(result.this,android.R.layout.simple_list_item_1,fsize);
        s3.setAdapter(ad2);
        if(android.os.Build.VERSION.SDK_INT>9)
        {
            StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                ff=s1.getSelectedItem().toString();
                ft=s2.getSelectedItem().toString();
                fs=s3.getSelectedItem().toString();
                text=e1.getText().toString();






                url="http://"+sh.getString("ip","")+":5000/imgtotext2";

                RequestQueue queue = Volley.newRequestQueue(result.this);

                // Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.

                        try {
                            JSONObject jo=new JSONObject(response);
                            String re=jo.getString("task");


                            Intent ik = new Intent(getApplicationContext(), result.class);
                            ik.putExtra("text",text);
                            startActivity(ik);


                            SharedPreferences.Editor ed=sh.edit();
                            ed.putString("image",re);
                            ed.commit();

                            startDownload(re);

                            Toast.makeText(getApplicationContext(), " out put "+re, Toast.LENGTH_LONG).show();


                        } catch (Exception e) {

                            Toast.makeText(result.this, ""+e, Toast.LENGTH_SHORT).show();

                        }

                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(result.this, "error"+error, Toast.LENGTH_SHORT).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        params.put("text",text);
                        params.put("fface", ff);
                        params.put("ftype", ft);
                        params.put("fsize", fs);
                        params.put("id", sh.getString("lid",""));


                        return params;
                    }
                };
                // Add the request to the RequestQueue.
                queue.add(stringRequest);
//



//
//
//


            }
        });
    }

    private void startDownload(String ress) {

        String url = "http://"+sh.getString("ip","")+":5000/static/texttodoc/"+ress;

        new DownloadFileAsync().execute(url);
    }




    class DownloadFileAsync extends AsyncTask<String, String, String> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
            mWakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK,
                    getClass().getName());
            mWakeLock.acquire();
            showDialog(DIALOG_DOWNLOAD_PROGRESS);
        }
        @Override
        protected String doInBackground(String... aurl) {
            int count;

            try {
                Log.d("aurllll",aurl[0]);

                URL url = new URL(aurl[0]);
                URLConnection conexion = url.openConnection();
                conexion.connect();

                int lenghtOfFile = conexion.getContentLength();
                Log.d("ANDRO_ASYNC", "Length of file: " + lenghtOfFile);

//	String filename = new SimpleDateFormat("dd-MM-yyyy-hh-mm-ss").format(new Date())+"ticket.html";
                InputStream input = new BufferedInputStream(url.openStream());
                File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
                File myFile = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)+"/"+sh.getString("image",""));
//                File myFile = new File(storageDir, "icon.jpg");
//                OutputStream output = new FileOutputStream(Environment.getExternalStorageDirectory() + "/" + sh.getString("orginal", ""));
                OutputStream output =new FileOutputStream(myFile);
                byte data[] = new byte[1024];

                long total = 0;

                while ((count = input.read(data)) != -1) {
                    total += count;
                    publishProgress(""+(int)((total*100)/lenghtOfFile));
                    output.write(data, 0, count);
                }

                output.flush();
                output.close();
                input.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }

        protected void onProgressUpdate(String... progress) {
            Log.d("ANDRO_ASYNC",progress[0]);
            mProgressDialog.setProgress(Integer.parseInt(progress[0]));
        }

        @Override
        protected void onPostExecute(String unused) {
            dismissDialog(DIALOG_DOWNLOAD_PROGRESS);
        }
    }


    @Override
    protected Dialog onCreateDialog(int id) {
        switch (id) {
            case DIALOG_DOWNLOAD_PROGRESS:
                mProgressDialog = new ProgressDialog(this);
                mProgressDialog.setMessage("Downloading File...");
                mProgressDialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
                mProgressDialog.setCancelable(false);
                mProgressDialog.show();
                return mProgressDialog;
        }
        return null;
    }

}

