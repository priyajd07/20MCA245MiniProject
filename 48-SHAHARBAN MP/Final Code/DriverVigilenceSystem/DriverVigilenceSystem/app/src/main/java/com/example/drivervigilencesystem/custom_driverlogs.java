package com.example.drivervigilencesystem;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class custom_driverlogs extends BaseAdapter {



    String[] date,  time, speed, angle;
    private Context context;

    public custom_driverlogs(Context appcontext, String[]date, String[]time, String[]speed, String[]angle)
    {
        this.context=appcontext;
        this.time=time;
        this.date=date;
        this.speed=speed;
        this.angle=angle;
    }

    @Override
    public int getCount() {
        return time.length;
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
            gridView=inflator.inflate(R.layout.custom_driverlogs,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv_date=(TextView)gridView.findViewById(R.id.textView60);
        TextView tv_time=(TextView)gridView.findViewById(R.id.textView62);
        TextView tv_speed=(TextView)gridView.findViewById(R.id.textView61);
        TextView tv_angle=(TextView)gridView.findViewById(R.id.textView64);



        tv_date.setTextColor(Color.RED);
        tv_date.setText(date[i]);
        tv_time.setTextColor(Color.BLACK);
        tv_time.setText(time[i]);
        tv_speed.setTextColor(Color.BLACK);
        tv_speed.setText("Speed : " + speed[i]);
        tv_angle.setTextColor(Color.BLACK);
        tv_angle.setText("Angle : " + angle[i]);

        return gridView;
    }
}
