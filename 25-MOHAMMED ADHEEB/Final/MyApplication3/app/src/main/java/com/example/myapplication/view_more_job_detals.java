package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

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

public class view_more_job_detals extends AppCompatActivity  implements AdapterView.OnItemClickListener {
    ListView l1;
    SharedPreferences sh;
    String cid;
    ArrayList<String>post,skill,qualification,descrption,experence,jobid;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_more_job_detals);
        cid=getIntent().getStringExtra("cid");
        l1=(ListView)findViewById(R.id.listview);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String url ="http://"+sh.getString("ip", "") + ":5000/viewcomp_vacancy";
        RequestQueue queue = Volley.newRequestQueue(view_more_job_detals.this);

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONArray ar=new JSONArray(response);
                    post= new ArrayList<>();
                    skill= new ArrayList<>();
                    qualification=new ArrayList<>();
                    descrption= new ArrayList<>();
                    experence= new ArrayList<>();
                    jobid= new ArrayList<>();


                    for(int i=0;i<ar.length();i++)
                    {
                        JSONObject jo=ar.getJSONObject(i);
                        post.add(jo.getString("job_name"));
                        skill.add(jo.getString("skills_required"));
                        qualification.add(jo.getString("qualification"));
                        descrption.add(jo.getString("description"));
                        experence.add(jo.getString("experience"));
                        jobid.add(jo.getString("job_id"));





                    }
                    // ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
                    //lv.setAdapter(ad);

                    l1.setAdapter(new Custom2(view_more_job_detals.this,post,descrption));
                    l1.setOnItemClickListener(view_more_job_detals.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(view_more_job_detals.this, "err"+error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("cid",cid);
                params.put("id1",sh.getString("lid",""));



                return params;
            }
        };
        queue.add(stringRequest);





    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        Intent in = new Intent(getApplicationContext(), Apply.class);
        in.putExtra("post", post.get(i));
        in.putExtra("skill", skill.get(i));
        in.putExtra("qualification", qualification.get(i));
        in.putExtra("descrption", descrption.get(i));
        in.putExtra("experence", experence.get(i));
        in.putExtra("jobid", jobid.get(i));
        startActivity(in);




    }
}
