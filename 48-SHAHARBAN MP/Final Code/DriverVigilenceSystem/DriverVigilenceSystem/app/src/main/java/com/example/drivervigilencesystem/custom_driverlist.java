package com.example.drivervigilencesystem;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
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

public class custom_driverlist extends BaseAdapter {
    String[] did,name,email,phone, image, lati, logi;
    private Context context;

    public custom_driverlist(Context appcontext, String[]did, String[]name, String[]email, String[]phone, String[]image, String[]lati, String[]logi)
    {
        this.context=appcontext;
        this.did=did;
        this.name=name;
        this.email=email;
        this.phone=phone;
        this.image=image;
        this.lati=lati;
        this.logi=logi;
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
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.custom_driverlist,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv_name=(TextView)gridView.findViewById(R.id.textView2);
        TextView tv_eml=(TextView)gridView.findViewById(R.id.textView3);
        TextView tv_phn=(TextView)gridView.findViewById(R.id.textView4);
        ImageView img=(ImageView) gridView.findViewById(R.id.imageView4);


        tv_name.setTextColor(Color.RED);
        tv_name.setText(name[i]);
        tv_eml.setTextColor(Color.BLACK);
        tv_eml.setText(email[i]);
        tv_phn.setTextColor(Color.BLACK);
        tv_phn.setText(phone[i]);


        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
        String ip = sh.getString("ip", "");
        String url1="http://"+ip+":5000"+image[i];
        Picasso.with(context).load(url1).transform(new CircleTransform()).into(img);

        ImageView bt_locate=(ImageView) gridView.findViewById(R.id.button3);
        bt_locate.setTag(i);
        bt_locate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                String url="http://maps.google.com/?q="+lati[pos]+","+logi[pos];
                Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                browserIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(browserIntent);
            }
        });

        ImageView bt_msg=(ImageView) gridView.findViewById(R.id.button4);
        bt_msg.setTag(i);
        bt_msg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("sel_did", did[pos]);
                ed.commit();
                Intent ij = new Intent(context, view_msg_frm_driver.class);
                ij.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(ij);
            }
        });

        Button bt_logs=(Button) gridView.findViewById(R.id.button5);
        bt_logs.setTag(i);
        bt_logs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("sel_did", did[pos]);
                ed.commit();
                Intent ij = new Intent(context, partner_view_logs.class);
                ij.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(ij);
            }
        });


        ImageView bt_settings=(ImageView) gridView.findViewById(R.id.button6);
        bt_settings.setTag(i);
        bt_settings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int pos=(int)v.getTag();
                SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor ed=sh.edit();
                ed.putString("sel_did", did[pos]);
                ed.commit();
                Intent ij = new Intent(context, pSettings.class);
                ij.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(ij);
            }
        });



        return gridView;
    }
}
