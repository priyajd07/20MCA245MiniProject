package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

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

public class Examintro extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    Spinner s1,s2;
    SharedPreferences sh;
    String compid,posttid;
    Button b1;
    public static ArrayList<String> qstn;
    public static ArrayList<String> opt1;
    public static ArrayList<String> opt2;
    public static ArrayList<String> opt3;
    public static ArrayList<String> opt4;
    public static ArrayList<String> ans;
    public static String sqstn="";
    ArrayList<String>company,comid,post,postid;
    String ur,url;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_examintro);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        s1=(Spinner)findViewById(R.id.spinner);
        s2=(Spinner)findViewById(R.id.spinner2);
        b1=(Button)findViewById(R.id.button15);

        url="http://"+sh.getString("ip","")+":5000/addques";


        //	new Insert().execute();
        try
        {
            if(android.os.Build.VERSION.SDK_INT >9)
            {
                StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);
            }
        }
        catch(Exception e)
        {

        }
        String url1 = "http://" + sh.getString("ip", "") + ":5000/select_companyy";

        RequestQueue queue = Volley.newRequestQueue(Examintro.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url1, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);

                    company = new ArrayList<>(ar.length());
                    comid = new ArrayList<>(ar.length());

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        company.add(jo.getString("company_name"));
                        comid.add(jo.getString("login_id"));


                    }

                    ArrayAdapter<String> ad = new ArrayAdapter<String>(Examintro.this, android.R.layout.simple_spinner_item, company);
                    s1.setAdapter(ad);
                    s1.setOnItemSelectedListener(Examintro.this);

                    // l1.setAdapter(new custom2(Monitoring_signal.this,notification,date));

                } catch (JSONException e) {
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {


                Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<String, String>();


                return params;
            }
        };
        queue.add(stringRequest);




        String url2 = "http://" + sh.getString("ip", "") + ":5000/select_postt";

        RequestQueue queue1 = Volley.newRequestQueue(Examintro.this);

        StringRequest stringRequest1 = new StringRequest(Request.Method.POST, url2, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);

                    post = new ArrayList<>(ar.length());
                    postid = new ArrayList<>(ar.length());

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        post.add(jo.getString("job_name"));
                        postid.add(jo.getString("job_id"));


                    }

                    ArrayAdapter<String> ad = new ArrayAdapter<String>(Examintro.this, android.R.layout.simple_spinner_item,post);
                    s2.setAdapter(ad);
                    s2.setOnItemSelectedListener(Examintro.this);

                    // l1.setAdapter(new custom2(Monitoring_signal.this,notification,date));

                } catch (JSONException e) {
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {


                Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<String, String>();
                params.put("cid", sh.getString("cid",""));

                return params;
            }
        };
        queue1.add(stringRequest1);




    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        if (adapterView==s1) {
            compid = comid.get(i);

            SharedPreferences.Editor ed = sh.edit();
            ed.putString("cid", compid);

            ed.commit();
        }
        if(adapterView==s2)
        {
            posttid=postid.get(i);
            SharedPreferences.Editor ed = sh.edit();
            ed.putString("sid", posttid);

            ed.commit();
        }
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                new Insert1().execute();


            }
        });

    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }
    class Insert1 extends AsyncTask<String, String, String> {

        /**
         * Before starting background thread Show Progress Dialog
         * */
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }
        protected String doInBackground(String... args)
        {


//            List<NameValuePair> params = new ArrayList<NameValuePair>();
//            params.add(new BasicNameValuePair("post",post ));
//            params.add(new BasicNameValuePair("cmpid",cmpid ));
//
//
//            Log.d("ins===",ur);
//            JSONArray json=null;
////            JSONObject jsondata=null;
//
//            try {
//                json = (JSONArray)jsonParser.makeHttpRequest(url,"GET", params);
////				jsondata = (JSONObject)jsonParser.makeHttpRequest(ur,"GET", params);
//            } catch (JSONException e1) {
//                // TODO Auto-generated catch block
//                e1.printStackTrace();
//            }
////           Log.d("Reultttttt=====---------",jsondata+"");
//            if(!json.equals(""))
//            {
//                try
//                {
//
//                    qstn=new ArrayList<String>();
//                    opt1=new ArrayList<String>();
//                    opt2=new ArrayList<String>();
//                    opt3=new ArrayList<String>();
//                    opt4=new ArrayList<String>();
//                    ans=new ArrayList<String>();
////
//
//                    for (int i = 0; i < json.length(); i++) {
//                        JSONObject cc=json.getJSONObject(i);
//
//                        qstn.add(cc.getString("question"));
//                        opt1.add(cc.getString("option1"));
//                        opt2.add(cc.getString("option2"));
//                        opt3.add(cc.getString("option3"));
//                        opt4.add(cc.getString("option4"));
//                        ans.add(cc.getString("answer"));
//
//
//                        Log.d("+++++++++++",cc+"");
//
//
//                    }
//
//                }
//                catch(JSONException e)
//                {
//                    Log.d("err====",e.getMessage());
//                }
//            }
//            else {
//
//            }
            RequestQueue queue = Volley.newRequestQueue(Examintro.this);

            StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the response string.
                    Log.d("+++++++++++++++++",response);
                    try {

                        JSONArray ar=new JSONArray(response);
                        qstn=new ArrayList<String>();
                        opt1=new ArrayList<String>();
                        opt2=new ArrayList<String>();
                        opt3=new ArrayList<String>();
                        opt4=new ArrayList<String>();
                        ans=new ArrayList<String>();

                        for(int i=0;i<ar.length();i++)
                        {
                            JSONObject cc=ar.getJSONObject(i);
                            qstn.add(cc.getString("question"));
                            opt1.add(cc.getString("option1"));
                            opt2.add(cc.getString("option2"));
                            opt3.add(cc.getString("option3"));
                            opt4.add(cc.getString("option4"));
                            ans.add(cc.getString("correct_answer"));
                        }


                    } catch (Exception e) {
                        Log.d("rrrrr=========", e.toString());
                    }

                    if (qstn.size()!=0) {
                        Intent i=new Intent(getApplicationContext(), Exam.class);
                        i.putStringArrayListExtra("qstn", qstn);
                        i.putStringArrayListExtra("opt1", opt1);
                        i.putStringArrayListExtra("opt2", opt2);
                        i.putStringArrayListExtra("opt3", opt3);
                        i.putStringArrayListExtra("opt4", opt4);
                        i.putStringArrayListExtra("ans", ans);
                        startActivity(i);



                    }



                }

            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                    Log.d("errrr=========", error.toString());
                }
            }) {
                @Override
                protected Map<String, String> getParams() {
                    Map<String, String> params = new HashMap<String,String>();
                    params.put("cid", sh.getString("cid",""));
                    params.put("sid", sh.getString("sid",""));

                    return params;
                }
            };
            queue.add(stringRequest);

            return null;
        }

        @Override
        protected void onProgressUpdate(String... values) {
//        	e.setText(values[0]);
            // TODO Auto-generated method stub, text, duration)
        }
        protected void onPostExecute(String file_url) {
            // dismiss the dialog once done
            // pDialog.dismiss();



        }
    }
}
