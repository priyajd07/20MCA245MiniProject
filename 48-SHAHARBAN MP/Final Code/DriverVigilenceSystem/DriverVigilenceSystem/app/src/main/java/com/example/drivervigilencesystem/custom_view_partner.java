package com.example.drivervigilencesystem;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
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

public class custom_view_partner extends BaseAdapter {
    String[] pid,name,relation,phone, image;
    private Context context;

    public custom_view_partner(Context appcontext, String[]pid, String[]name, String[]relation, String[]phone, String[]image)
    {
        this.context=appcontext;
        this.pid=pid;
        this.name=name;
        this.relation=relation;
        this.phone=phone;
        this.image=image;
    }

    @Override
    public int getCount() {
        return name.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);

            gridView=inflator.inflate(R.layout.custom_view_partner,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv_name=(TextView)gridView.findViewById(R.id.t4);
        TextView tv_rel=(TextView)gridView.findViewById(R.id.t5);
        TextView tv_phn=(TextView)gridView.findViewById(R.id.t7);
        Button tv_view_more=(Button) gridView.findViewById(R.id.t6);
        ImageView img=(ImageView) gridView.findViewById(R.id.imageView6);


        tv_name.setTextColor(Color.RED);
        tv_name.setText(name[i]);
        tv_rel.setTextColor(Color.BLACK);
        tv_rel.setText(relation[i]);
        tv_phn.setTextColor(Color.BLACK);
        tv_phn.setText(phone[i]);


        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
        String ip = sh.getString("ip", "");
        String url1="http://"+ip+":5000"+image[i];
        Picasso.with(context).load(url1).transform(new CircleTransform()).into(img);

        tv_view_more.setTag(i);
        tv_view_more.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("sel_pid", pid[pos]);
                ed.commit();
                Intent ij=new Intent(context, view_msg_frm_partner.class);
                ij.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(ij);
            }
        });


        ImageView im_del=(ImageView) gridView.findViewById(R.id.imageView5);
        im_del.setTag(i);
        im_del.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
                String hu = sh.getString("ip", "");
                String url = "http://" + hu + ":5000/and_driver_delete_partner";
                RequestQueue requestQueue = Volley.newRequestQueue(context);
                StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                // response
                                try {
                                    JSONObject jsonObj = new JSONObject(response);
                                    if (jsonObj.getString("status").equalsIgnoreCase("ok")) {

                                        Toast.makeText(context, "Deleted", Toast.LENGTH_LONG).show();
                                        Intent ij=new Intent(context, view_partner.class);
                                        ij.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                                        context.startActivity(ij);
                                    }


                                    // }
                                    else {
                                        Toast.makeText(context, "No partners", Toast.LENGTH_LONG).show();
                                    }

                                }    catch (Exception e) {
                                    Toast.makeText(context, "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                                }
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // error
                                Toast.makeText(context, "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                ) {
                    @Override
                    protected Map<String, String> getParams() {
                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
                        Map<String, String> params = new HashMap<String, String>();

                        params.put("pid", pid[pos]);


                        return params;
                    }
                };

                int MY_SOCKET_TIMEOUT_MS=100000;

                postRequest.setRetryPolicy(new DefaultRetryPolicy(
                        MY_SOCKET_TIMEOUT_MS,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
                requestQueue.add(postRequest);

            }
        });

        return gridView;
    }
}
