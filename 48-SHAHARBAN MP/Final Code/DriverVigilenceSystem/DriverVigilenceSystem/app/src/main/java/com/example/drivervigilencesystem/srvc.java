
package com.example.drivervigilencesystem;

import android.Manifest;
import android.app.ActionBar;
import android.app.AlertDialog;
import android.app.Service;
import android.content.ContentResolver;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.media.AudioManager;
import android.os.Bundle;
import android.os.Handler;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.provider.Settings;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.WindowManager;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.core.app.ActivityCompat;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class srvc extends Service {

    TextView timerTextView;
    long startTime = 0;

    private static final String TAG = "AusteerLogging";

    private String timeStamp = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss").format(System.currentTimeMillis());
    private String filename = "Austeer-" + timeStamp + ".csv";
    private String filepath = "Austeer";
    File envpath;
    File outputFile;
    String outputString = "";
    FileWriter fw;

    TextView speedTextView;
    TextView locationTextView;
    TextView steeringTextView;
    TextView storageTextView;

    String locString = "";
    String altitudeString = "";
    String speedString = "";
    String steerStringX="";
    String steerStringY="";
    String steerStringZ="";

    List<Double> speedlist = new ArrayList();
    Double lastLat=0.0;
    Double lastLng=0.0;
    Double lastAlt=0.0;
    Long lastTime= Long.valueOf(0);

    LocationManager locationManager;
    LocationListener li;

    SensorManager sMgr;
    Sensor gyro;
    SensorEventListener sev;
    private ContentResolver cresovler;


    String dis="";
    public void distruptionchecker(String lati,String longi)
    {
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String IP = sh.getString("ip", "");
        String url = "http://" + IP + ":5000/and_check_disrupt";

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            String status = jsonObj.getString("status");
                            if (status.equalsIgnoreCase("ok")) {
                                String plc=jsonObj.getString("dist");
                                dis="distruption near "+plc;
                                if (!plc.equalsIgnoreCase("no"))
                                {
                                    Handler hnd=new Handler();
                                    hnd.post(new Runnable() {
                                        @Override
                                        public void run() {
                                            Toast.makeText(getApplicationContext(), dis, Toast.LENGTH_SHORT).show();
                                            t1.speak(dis, TextToSpeech.QUEUE_FLUSH, null);
                                        }
                                    });


                                }

                            } else {
                                Toast.makeText(getApplicationContext(),  "No values", Toast.LENGTH_LONG);
                            }





                        } catch (JSONException e) {
                            Toast.makeText(getApplicationContext(), "Error"+e.getMessage(), Toast.LENGTH_LONG).show();
                            e.printStackTrace();
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
                params.put("longi",latlik);
                params.put("lati",lonlik);

                return params;
            }
        };

        int MY_SOCKET_TIMEOUT_MS=50000;

        postRequest.setRetryPolicy(new DefaultRetryPolicy(
                MY_SOCKET_TIMEOUT_MS,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        requestQueue.add(postRequest);






}







    boolean ScreenBrightness(String level, Context context) {

        try {
            android.provider.Settings.System.putInt(
                    context.getContentResolver(),
                    android.provider.Settings.System.SCREEN_BRIGHTNESS, Integer.parseInt(level));
            return true;
        }

        catch (Exception e) {


            Toast.makeText(getApplicationContext(),"eeeeeeeeerrrrrrrrrreeee"+e.getMessage().toLowerCase(),Toast.LENGTH_LONG).show();


            Log.d("Screen Brightness", "error changing screen brightness"+e.getMessage().toString());
            return false;
        }


       // return false;
    }

    public  void changetouch(String tch)
    {
        if(tch.equalsIgnoreCase("NO")) ///// change here to work in college >=0
            {

                Toast.makeText(getApplicationContext(),"Touch not blocked",Toast.LENGTH_LONG).show();

                Intent ints=new Intent(getApplicationContext(),GlobalTouchService.class);
                stopService(ints);
            }
            else
            {
                Toast.makeText(getApplicationContext(),"Touch  blocked",Toast.LENGTH_LONG).show();


                Intent ints=new Intent(getApplicationContext(),GlobalTouchService.class);
                startService(ints);
            }
    }



    public void changemode(String mode)
    {

                String ms= mode;
                Log.d("IN--- MODE", ms);


                if(ms.equalsIgnoreCase("SILENT"))
                {
                    AudioManager am=(AudioManager) getSystemService(getApplicationContext().AUDIO_SERVICE);
                    am.setRingerMode(AudioManager.RINGER_MODE_SILENT);

                    Log.d("IN--- MODE", "SILENT1");
                    Toast.makeText(getApplicationContext(),"Mode changed to SILENT",Toast.LENGTH_SHORT).show();
                }
                else if(ms.equalsIgnoreCase("GENERAL"))
                {
                    AudioManager am=(AudioManager) getSystemService(getApplicationContext().AUDIO_SERVICE);
                    am.setRingerMode(AudioManager.RINGER_MODE_NORMAL);

                    Toast.makeText(getApplicationContext(),"Mode changed to General",Toast.LENGTH_SHORT).show();
                    Log.d("IN--- MODE", "GEN");
                }
                else if(ms.equalsIgnoreCase("VIBRATE")) {
                    AudioManager am = (AudioManager) getSystemService(getApplicationContext().AUDIO_SERVICE);
                    am.setRingerMode(AudioManager.RINGER_MODE_VIBRATE);
                    Toast.makeText(getApplicationContext(), "Mode changed to Vibrate", Toast.LENGTH_SHORT).show();
                    Log.d("IN--- MODE", "VIB");
                }
    }







    //runs without a timer by reposting this handler at the end of the runnable
    Handler timerHandler = new Handler();


    int flag=0;
    TextToSpeech t1;

    Runnable timerRunnable = new Runnable() {

        @Override
        public void run() {
            long millis = System.currentTimeMillis() - startTime;
            int seconds = (int) (millis / 1000);
            int minutes = seconds / 60;
            seconds = seconds % 60;

            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String IP = sh.getString("ip", "");
            String url = "http://" + IP + ":5000/insertintodriverlogs";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String status = jsonObj.getString("status");

                                if(status.equalsIgnoreCase("ok"))
                                {
                                    String mode= jsonObj.getString("mode");
                                    String bri= jsonObj.getString("bri");
                                    String tch= jsonObj.getString("tch");
                                    String blk= jsonObj.getString("blk");
                                    String typ= jsonObj.getString("typ");
                                    String msg= jsonObj.getString("msg");
                                    String distrupt= jsonObj.getString("distrupt");

                                    changemode(mode);
                                    changetouch(tch);


//                                    distruptionchecker(latlik,lonlik);

//                                    changebrighness(bri);

                                    ScreenBrightness(bri,srvc.this);
                                    SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                    SharedPreferences.Editor ed=sh.edit();
                                    ed.putString("block", blk);
                                    ed.putString("MSGS",msg);
                                    ed.commit();





                                } else {
                                    Toast.makeText(getApplicationContext(),  "No values", Toast.LENGTH_LONG);
                                }





                            } catch (JSONException e) {
                                Toast.makeText(getApplicationContext(), "Error"+e.getMessage(), Toast.LENGTH_LONG).show();
                                e.printStackTrace();
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
                    params.put("lid",sh.getString("lid",""));
                    params.put("speed", speedString);
                    params.put("longi", lonlik);
                    params.put("lati", latlik);
                    params.put("angle", steerStringY);
                    params.put("place",place);
//                params.put("username", E15.getText().toString());
//                params.put("password", E16.getText().toString());

//                params.put("asid",sh.getString("assid",""));
                    return params;
                }
            };

            int MY_SOCKET_TIMEOUT_MS=100000;

            postRequest.setRetryPolicy(new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
            requestQueue.add(postRequest);
            timerHandler.postDelayed(this, 15000);
        }
    };




    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
    public static  String latlik="",lonlik="",place="";




    @Override
    public void onCreate() {
        super.onCreate();
        //////
        final DecimalFormat df = new DecimalFormat("#.####");
        df.setRoundingMode(RoundingMode.CEILING);

        final DecimalFormat df2 = new DecimalFormat("#.#");
        df2.setRoundingMode(RoundingMode.CEILING);

//              getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

//        timerTextView = (TextView) findViewById(R.id.timerTextView);
//        locationTextView = (TextView) findViewById(R.id.locationTextView);
//        speedTextView = (TextView) findViewById(R.id.speedTextView);
//        steeringTextView = (TextView) findViewById(R.id.steeringTextView);

        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);

        li = new LocationListener() {
            public void onLocationChanged(Location location) {
                // Called when a new location is found by the network location provider.

                Double newLat = location.getLatitude();
                Double newLng = location.getLongitude();
                Double newAlt = location.getAltitude();
                Long newTime = location.getTime();


                Geocoder geoCoder = new Geocoder(getBaseContext(), Locale.getDefault());
                try {

                    List<Address> addresses = geoCoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
                    // Toast.makeText(getApplicationContext(), addresses+"...........llooc", Toast.LENGTH_SHORT).show();
                    if (addresses.size() > 0) {
                        for (int index = 0; index < addresses.get(0).getMaxAddressLineIndex(); index++)
                            place += addresses.get(0).getAddressLine(index) + " ";
                        place = addresses.get(0).getFeatureName().toString();
                        //  Toast.makeText(getApplicationContext(), place, Toast.LENGTH_SHORT).show();
                        // subloc = addresses.get(0).getSubLocality().toString();
                    }

                } catch (IOException e) {
                    //  e.printStackTrace();
                    // Toast.makeText(getApplicationContext(), e.getMessage().toString()+"", Toast.LENGTH_SHORT).show();
                }




                altitudeString = Double.toString(newAlt);

                Float accuracy = location.getAccuracy();

                // Altitude too inaccurate so just use the same altitude for calculating speed,
                // you're not moving that fast unless you fall off a cliff

                locString = df.format(newLat) + ", " + df.format(newLng);


                latlik= newLat+"";
                lonlik= newLng+"";


                Log.v(TAG, "LOCATION , lat=" + df.format(newLat) + ", lon=" + df.format(newLng) + "(Accuracy: " + accuracy + ")");

                // on first run set location and start timer
                if (lastLat == 0.0) {
                    startTime = System.currentTimeMillis();
                    if(flag==0) {
                        timerHandler.postDelayed(timerRunnable, 0);
                    flag++;

                    }
                    speedString = "0";
                    lastLat = newLat;
                    lastLng = newLng;
                    lastAlt = newAlt;
                    lastTime = newTime;
                } else {
                    Double dist = distance(lastLat, newLat, lastLng, newLng, newAlt, newAlt);

                    Log.v(TAG, "DISTANCE = " + dist);

                    float timediff = (newTime - lastTime) / 1000;

                    if (timediff == 0) {
                        // do nothing because distance is less than accuracy
                        // or measurement too quick
                        Log.v(TAG, "SPEED UNCHANGED");
                    } else {
                        Double speed = Math.abs(dist) / timediff;
                        // Average speed from last five position results
                        speedlist.add(speed);
                        if (speedlist.size() > 5) {
                            speedlist.remove(0);
                            Double averagespeed = averageSpeed(speedlist);
                            if (averagespeed < 0.5) { averagespeed = 0.0; }
                            speedString = df2.format(Math.abs(averagespeed));
                            Log.v(TAG, "SPEEDS = "+speedlist.toString());
                            Log.v(TAG, "ALTITUDE = "+altitudeString);
                        }
                        // only update speeds if dist/time is changed
                        lastLat = newLat;
                        lastLng = newLng;
                        lastAlt = newAlt;
                        lastTime = newTime;
                    }
                }


            }

            public void onStatusChanged(String provider, int status, Bundle extras) {
            }

            public void onProviderEnabled(String provider) {
            }

            public void onProviderDisabled(String provider) {
            }
        };

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            new AlertDialog.Builder(this)
                    .setTitle("Permissions Needed")
                    .setMessage("You need to give Austeer permission to use your location.")
                    .setNeutralButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int which) {
                            // do nothing
                        }
                    })
                    .setIcon(android.R.drawable.ic_dialog_alert)
                    .show();
        }
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, li);
        locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, li);

        sMgr = (SensorManager) getSystemService(SENSOR_SERVICE);
        gyro = sMgr.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);

        // With Accelerometer, flat on a table is X-0, Y-0, Z-10
        // Held flat upward in portrait mode, X-0, y-10, Z-0
        // Held flat upward in landscape: X-10, Y-0, Z-0
        // Steering mode fixed to steering wheel landscape: Just use Y-value

        sev = new SensorEventListener() {
            public void onAccuracyChanged(Sensor sensor, int accuracy) {
            }

            public void onSensorChanged(SensorEvent event) {
                float axisX = event.values[0];
                float axisY = event.values[1];
                float axisZ = event.values[2];
                // Trying to remove negative zero but doing it wrong.
//                if (1 / axisY > 0) { } else { axisY = Math.abs(axisY); }
                steerStringX = Float.toString(Math.round(axisX * 10) / 10);
                steerStringY = String.format("%.2f", axisY / 10);
                steerStringZ = Float.toString(Math.round(axisZ * 10) / 10);
            }
        };

        sMgr.registerListener(sev, gyro, SensorManager.SENSOR_DELAY_FASTEST);





        //////






    }

    public Double distance(double lat1, double lat2, double lon1,
                           double lon2, double el1, double el2) {

        final int R = 6371; // Radius of the earth

        Double latDistance = Math.toRadians(lat2 - lat1);
        Double lonDistance = Math.toRadians(lon2 - lon1);
        Double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        Double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        double distance = R * c * 1000; // convert to meters

        double height = el1 - el2;

        distance = Math.pow(distance, 2) + Math.pow(height, 2);

        return Math.sqrt(distance);
    }

    public Double averageSpeed(List speeds) {
        Double total = 0.0;
        for (int i = 0; i < speeds.size(); i++) {
            total = total + (double)speeds.get(i);
        }
        return (total / speeds.size());
    }



}
