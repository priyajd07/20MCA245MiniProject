package com.example.drivervigilencesystem;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Handler;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.speech.tts.TextToSpeech;
import android.widget.Toast;

import androidx.annotation.Nullable;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Locale;
import java.util.Map;


public class message_service extends Service implements TextToSpeech.OnInitListener {

    TextToSpeech t1;

    Handler hnd;


    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }


    Runnable rn=new Runnable() {
        @Override
        public void run() {

            callmsg();
        }
    };


    String message="";
    public  void callmsg()
    {
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip= sh.getString("ip", "");

        String url="http://"+ip+":5000/getmsg";


        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

//                        Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();

                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            String sucs = jsonObj.getString("status");
                            if (sucs.equalsIgnoreCase("ok")) {

                                String msgid=jsonObj.getString("msgid");
                                 message=jsonObj.getString("message");
                                t1.speak(message, TextToSpeech.QUEUE_FLUSH, null);


                                 hnd.post(new Runnable() {
                                     @Override
                                     public void run() {

                                         t1.speak(message, TextToSpeech.QUEUE_FLUSH, null);

                                     }
                                 });




                                Toast.makeText(message_service.this, message, Toast.LENGTH_SHORT).show();


                                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                SharedPreferences.Editor Ed=sh.edit();
                                Ed.putString("mid",msgid);
                                Ed.commit();




//                                Toast.makeText(getApplicationContext(),"success",Toast.LENGTH_LONG).show();

                            }


                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() {
                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();

                params.put("msgid", sh.getString("mid","0"));
                params.put("driverid",sh.getString("lid",""));



                return params;
            }
        };


        requestQueue.add(postRequest);



        hnd.postDelayed(rn,25000);

    }



    @Override
    public void onCreate() {
        super.onCreate();
        t1=new TextToSpeech(this,this);


        hnd=new Handler();
        hnd.post(rn);
    }

    @Override
    public void onInit(int i) {
        if(i != TextToSpeech.ERROR) {
            t1.setLanguage(Locale.UK);

            t1.speak(message, TextToSpeech.QUEUE_FLUSH, null);
            Toast.makeText(getApplicationContext(), "speech config successfully" , Toast.LENGTH_SHORT).show();

        }
//        else
//        {
//           Toast.makeText(getApplicationContext(), "Failed to start" , Toast.LENGTH_SHORT).show();
//        }


    }
}
