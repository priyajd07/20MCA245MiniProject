package com.example.image_story_teller;


import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView.FindListener;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;


@SuppressLint("NewApi")
public class Custom extends BaseAdapter{

    private Context Context;
    ArrayList<String> a,b;
    SharedPreferences sh;
   

    public Custom(Context applicationContext,ArrayList<String> a, ArrayList<String> b) {
        this.Context=applicationContext;
        this.a=a;
        this.b=b;
        if(android.os.Build.VERSION.SDK_INT >9)
    	{
    		StrictMode.ThreadPolicy policy=new StrictMode.ThreadPolicy.Builder().permitAll().build();
    		StrictMode.setThreadPolicy(policy);
    	}


    }

    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return a.size();
    }

    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public long getItemId(int arg0) {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // TODO Auto-generated method stub
        LayoutInflater inflator=(LayoutInflater)Context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(convertView==null)
        {
            gridView=new View(Context);
            gridView=inflator.inflate(R.layout.activity_custom, null);

        }
        else
        {
            gridView=(View)convertView;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView1);


        tv1.setText(b.get(position));
 


        tv1.setTextColor(Color.BLACK);






        ImageView img=(ImageView)gridView.findViewById(R.id.imageView1);
		sh = PreferenceManager.getDefaultSharedPreferences(Context);





        String urll="http://"+sh.getString("ip","")+":5000/static/ds/"+a.get(position);
        java.net.URL thumb_u;
        try {
            thumb_u = new java.net.URL(urll);
            Drawable thumb_d = Drawable.createFromStream(thumb_u.openStream(), "src");
            img.setImageDrawable(thumb_d);



            //Picasso.with(Context)
            //    .load(urll)
            //  .transform(new Circulartransform())
            // .error(R.drawable.a)
            //  .into(img);



        }
        catch(Exception e){
            Log.d("*********",e.toString());
        }

        return gridView;

    }

}




