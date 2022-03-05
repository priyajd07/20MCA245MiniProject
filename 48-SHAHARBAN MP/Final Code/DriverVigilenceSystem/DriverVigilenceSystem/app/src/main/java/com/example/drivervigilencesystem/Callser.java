package com.example.drivervigilencesystem;

import android.annotation.TargetApi;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.os.Build;
import android.os.IBinder;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.telephony.PhoneStateListener;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.widget.Toast;

import com.android.internal.telephony.ITelephony;
import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.lang.reflect.Method;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;


public class Callser extends Service {

    String opn;
    String dt = "", tm = "";
    long diffinmin, diffinhr;
    TelephonyManager telephonyManager;
    TelephonyManager telman;

    public static int flg = 0;
    String phnop = "";

    SharedPreferences sh;


    String url = "";
    String imei;

    @TargetApi(Build.VERSION_CODES.GINGERBREAD)
    @Override
    public void onCreate() {
        //Toast.makeText(getApplicationContext(), "service started", Toast.LENGTH_SHORT).show();

        // TODO Auto-generated method stub
        super.onCreate();


        Toast.makeText(this, "innnnnnnnnnnnn", Toast.LENGTH_SHORT).show();
        try {

            if (Build.VERSION.SDK_INT > 9) {
                StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                StrictMode.setThreadPolicy(policy);
            }

        } catch (Exception e) {
            // TODO: handle exception
        }

        Toast.makeText(getApplicationContext(), "inside service", Toast.LENGTH_SHORT).show();


        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        String hu = sh.getString("ip", "");

        url = "http://" + hu + ":5000/add_calllogs";

        SimpleDateFormat tet = new SimpleDateFormat("hh:mm:ss");
        tm = tet.format(new Date());
        telman = (TelephonyManager) getApplicationContext().getSystemService(TELEPHONY_SERVICE);
//        imei=telman.getDeviceId().toString();

        telman.listen(phlist, PhoneStateListener.LISTEN_CALL_STATE);
        Log.d("....old...", ".....00");
//        Toast.makeText(getApplicationContext(), " \"http://\" + ip + \":8080/Mobihelper/Callin\"", Toast.LENGTH_SHORT).show();

    }

    public PhoneStateListener phlist = new PhoneStateListener() {
        public void onCallStateChanged(int state, String inNum) {

            switch (state) {


                case TelephonyManager.CALL_STATE_IDLE:

                    SimpleDateFormat dd = new SimpleDateFormat("dd/MM/yyyy");
                    SimpleDateFormat tt = new SimpleDateFormat("hh:mm:ss");

                    String d = dd.format(new Date());
                    String t = tt.format(new Date());

                    String duration = "";
                    long tmdiff = 0;

                    //	Log.d("....old...", ".....3");
                    try {
                        Date dt1 = tt.parse(t);
                        Date dt2 = tt.parse(tm);

                        tmdiff = dt1.getTime() - dt2.getTime();

                        tmdiff = TimeUnit.MILLISECONDS.toSeconds(tmdiff);
                        diffinmin = tmdiff / (60);
                        diffinhr = diffinmin / (60);
                        tmdiff -= (diffinmin * 60);

                        duration = diffinhr + ":" + diffinmin + ":" + tmdiff;


                        SharedPreferences shp = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                        Editor edit = shp.edit();
                        edit.putString("duration", duration);
                        edit.commit();


                        Toast.makeText(getApplicationContext(), "call duration" +duration, Toast.LENGTH_LONG).show();

                    } catch (Exception e) {
                        // TODO Auto-generated catch block
                        Toast.makeText(getApplicationContext(), "error1 in call:" + e.getMessage(), Toast.LENGTH_SHORT).show();
                        Log.d("error1", e.getMessage());
                    }


                    SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(getBaseContext());
                    String name = preferences.getString("callstatus", "hi");

                    if (name.equalsIgnoreCase("incoming")) {
                        Log.d("....1....", "..incall..");


                        SharedPreferences shpr = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                        Editor edit1 = shpr.edit();


                        edit1.putString("Number", "incoming call");

                        edit1.commit();


                        try {
                            //call(MainActivity.phoneid,phnop,"incoming",duration,d,t);
                        } catch (Exception e) {
                            // TODO Auto-generated catch block
                            Toast.makeText(getApplicationContext(), "error2 in call:" + e.getMessage(), Toast.LENGTH_SHORT).show();
                            Log.d("error2", e.getMessage());
                        }


                        SharedPreferences sh1 = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

                        String ss = sh1.getString("incoming number", "");

                        String dur = sh1.getString("duration", "");

                        Toast.makeText(getApplicationContext(), ss + "\n" + "incoming call" + "\n" + dur, Toast.LENGTH_LONG).show();

                        insertcall(ss, imei, "incoming", dur);

                        flg = 0;
                    } else if (flg == 1) {
                        Log.d("....1....", "..outcall..");
                        try {
                            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                            opn = sh.getString("num", "");

                            //call1(MainActivity.phoneid,opn,"outgoing",duration,d,t);
                        } catch (Exception e) {
                            // TODO Auto-generated catch block
                            Toast.makeText(getApplicationContext(), "error3 in call:" + e.getMessage(), Toast.LENGTH_SHORT).show();
                            Log.d("error3", e.getMessage());
                        }


                        SharedPreferences sh2 = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


                        String dur = sh2.getString("duration", "");
                        Toast.makeText(getApplicationContext(), opn + "\n" + "Outgoing call" + "\n" + dur, Toast.LENGTH_LONG).show();

                        insertcall(opn, imei, "outgoing", dur);

                        flg = 0;
                    }


                    Editor editor = preferences.edit();
                    editor.putString("callstatus", "idle");
                    editor.commit();

                    break;


                case TelephonyManager.CALL_STATE_OFFHOOK:

                    SimpleDateFormat sm = new SimpleDateFormat("dd/MM/yyyy");
                    SimpleDateFormat sn = new SimpleDateFormat("hh:mm:ss");

                    flg = 1;

                    dt = sm.format(new Date());
                    tm = sn.format(new Date());
                    Toast.makeText(getApplicationContext(), dt + "  " + tm, Toast.LENGTH_LONG).show();

                    SharedPreferences pref = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    String opn = pref.getString("num", "");

                    if (opn.equalsIgnoreCase("")) {
                        opn = phnop;
                    }

                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    String blknum = sh.getString("block", "");

                    int xy = 0;
                    Log.d("...outn..", blknum + "..outn.." + opn);
//                    if (!blknum.equalsIgnoreCase("#")) {
//
//                        String b[] = blknum.split("#");
//                        for (int i = 0; i < b.length; i++) {
//                            if (b[i].length() >= 10 && opn.length() >= 10) {
//                                b[i] = b[i].substring(b[i].length() - 10, b[i].length());
//                                opn = opn.substring(opn.length() - 10, opn.length());
//                                Log.d("....outnum....", b[i] + "..b[i]..outnum.." + opn);
//                            }
//                            if (b[i].equals(opn)) {
//                                xy = 1;
//                            }
//                        }
//                    }

                    if (xy == 1) {
                        ////call reject
                        try {

                            Log.d("...rnggg..", "cutng........");

                            telephonyManager = (TelephonyManager) getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
                            Class c = Class.forName(telephonyManager.getClass().getName());
                            Method m = c.getDeclaredMethod("getITelephony");
                            m.setAccessible(true);
                            ITelephony telephonyService = (ITelephony) m.invoke(telephonyManager);
                            telephonyService.endCall();

                        } catch (Exception e) {
                            // TODO: handle exception
                            Toast.makeText(getApplicationContext(), "error4 in call:" + e.getMessage(), Toast.LENGTH_SHORT).show();
                            Log.d("error4", e.getMessage());
                        }
                    }
                    break;


                case TelephonyManager.CALL_STATE_RINGING:

                    phnop = inNum;
                    Toast.makeText(getApplicationContext(), phnop, Toast.LENGTH_LONG).show();
                    sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    Editor edd = sh.edit();
                    edd.putString("incoming number", phnop);
                    edd.commit();

                    blknum = sh.getString("block", "");

                    // saving the incoming number

                    Editor ed = sh.edit();
                    ed.putString("callstatus", "incoming");
                    ed.putString("num", inNum);
                    ed.commit();
                    ///ends
                    int xyz = 0;
                    Log.d("...rnggg..", blknum + "..innum.." + inNum);
//                    if (!blknum.equalsIgnoreCase("#")) {
//                        String bb[] = blknum.split("#");
//                        for (int i = 0; i < bb.length; i++) {
//                            if (bb[i].length() >= 10) {
//                                bb[i] = bb[i].substring(bb[i].length() - 10, bb[i].length());
//                                inNum = inNum.substring(inNum.length() - 10, inNum.length());
//                                Log.d("...rnggg..substring..", bb[i] + "..innum.." + inNum);
//                            }
//
//                            if (bb[i].equals(inNum)) {
//                                xyz = 1;
//                            }
//                        }
//                    }        ////call reject
                    if (xyz == 1) {
                        try {
                            Log.d("...rnggg..", "cutng........");

                            telephonyManager = (TelephonyManager) getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
                            Class c = Class.forName(telephonyManager.getClass().getName());
                            Method m = c.getDeclaredMethod("getITelephony");
                            m.setAccessible(true);
                            ITelephony telephonyService = (ITelephony) m.invoke(telephonyManager);
                            telephonyService.endCall();


                        } catch (Exception e) {
                            // TODO: handle exception
                            Toast.makeText(getApplicationContext(), "error5 in call:" + e.getMessage(), Toast.LENGTH_SHORT).show();
                            Log.d("error5", e.getMessage());

                        }
                    }

                    break;
            }

        }

        private void insertcall(String ph, String imei, String type, String dur) {

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

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
                    Map<String, String> params = new HashMap<String, String>();

                    params.put("phone", ph);
                    params.put("imei", imei);
                    params.put("dur", dur);
                    params.put("type",type);
                    params.put("ofc_no", sh.getString("ofc_no",""));

                    return params;
                }
            };

            int MY_SOCKET_TIMEOUT_MS = 100000;

            postRequest.setRetryPolicy(new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
            requestQueue.add(postRequest);



        }

    };

        public IBinder onBind(Intent arg0) {

            return null;
        }}


