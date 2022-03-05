package com.example.drivervigilencesystem;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class custom_message extends BaseAdapter {



    String[] message,  date;
    private Context context;

    public custom_message(Context appcontext, String[]message, String[]date)
    {
        this.context=appcontext;
        this.message=message;
        this.date=date;
    }

    @Override
    public int getCount() {
        return message.length;
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
            gridView=inflator.inflate(R.layout.custom_message,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv=(TextView)gridView.findViewById(R.id.txt_sn);
        TextView tv2=(TextView)gridView.findViewById(R.id.txt_msg);



        tv.setTextColor(Color.RED);
        tv.setText(date[i]);
        tv2.setTextColor(Color.BLACK);
        tv2.setText(message[i]);

        return gridView;
    }
}
