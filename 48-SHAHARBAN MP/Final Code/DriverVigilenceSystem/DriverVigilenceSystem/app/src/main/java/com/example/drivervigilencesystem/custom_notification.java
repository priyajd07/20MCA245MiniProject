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
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class custom_notification extends BaseAdapter {



    String[] subject, content, date;
    private Context context;

    public custom_notification(Context appcontext, String[]sub, String[]cont, String[]date)
    {
        this.context=appcontext;
        this.subject=sub;
        this.content=cont;
        this.date=date;
    }

    @Override
    public int getCount() {
        return subject.length;
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
            gridView=inflator.inflate(R.layout.custom_notification,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv=(TextView)gridView.findViewById(R.id.txt_sn);
        TextView tv2=(TextView)gridView.findViewById(R.id.txt_msg);
        TextView tv3=(TextView)gridView.findViewById(R.id.txt_date);



        tv.setTextColor(Color.RED);
        tv.setText(subject[i]);
        tv2.setTextColor(Color.BLACK);
        tv2.setText(content[i]);
        tv3.setTextColor(Color.BLACK);
        tv3.setText(date[i]);

        return gridView;
    }
}
