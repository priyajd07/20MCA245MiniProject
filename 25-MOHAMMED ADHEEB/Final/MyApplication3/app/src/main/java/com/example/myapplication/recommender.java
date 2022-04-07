package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import androidx.appcompat.app.AppCompatActivity;

public class recommender extends AppCompatActivity implements AdapterView.OnItemClickListener{
    SharedPreferences sh;
    ListView l11;
    String url;
    ArrayList<String>post,skill,qua,description,exp,postid;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommender);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l11=findViewById(R.id.l11);
        try
        {
            if(android.os.Build.VERSION.SDK_INT>9)
            {
                StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);
            }
        }
        catch(Exception e)
        {
        }
        RequestQueue queue = Volley.newRequestQueue(recommender.this);
        url = "http://" + sh.getString("ip", "") + ":5000/recommendation";

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    post= new ArrayList<>();
                    skill=new ArrayList<>();
                    qua=new ArrayList<>();
                    description=new ArrayList<>();
                    exp=new ArrayList<>();
                    postid=new ArrayList<>();

                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        post.add(jo.getString("job_name"));
                        skill.add(jo.getString("description"));
                        qua.add(jo.getString("qualification"));
                        description.add(jo.getString("description"));
                        exp.add(jo.getString("experience"));
                        postid.add(jo.getString("job_id"));


                    }

                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);
                    l11.setAdapter(new Custom2(recommender.this,post,description));
                            l11.setOnItemClickListener(recommender.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(recommender.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("lid", sh.getString("lid", ""));

                return params;
            }
        };
        stringRequest.setRetryPolicy(new DefaultRetryPolicy(
                10000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT)
        );
        queue.add(stringRequest);


    }

    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Intent ik=new Intent(getApplicationContext(),Apply.class);
        ik.putExtra("post",post.get(position));
        ik.putExtra("descrption",description.get(position));
        ik.putExtra("qualification",qua.get(position));
        ik.putExtra("skill",skill.get(position));
        ik.putExtra("experence",exp.get(position));
        ik.putExtra("jobid",postid.get(position));
        startActivity(ik);

    }
}