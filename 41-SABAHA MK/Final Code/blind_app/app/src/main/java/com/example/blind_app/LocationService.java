package com.example.blind_app;


import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;


import android.annotation.TargetApi;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;

import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.IBinder;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.provider.Settings;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

@TargetApi(Build.VERSION_CODES.GINGERBREAD)
public class LocationService extends Service{
	private LocationManager locationManager;
    private Boolean locationChanged;
    
    private Handler handler = new Handler();
    public static Location curLocation;
    public static boolean isService = true;
    String phoneid="";    
    public static String lati,longi,place;
    String  lat1, lat2, longi1, longi2;
	
    LocationListener locationListener = new LocationListener() {
    public void onLocationChanged(Location location) {
   // Toast.makeText(getApplicationContext(), "change",Toast.LENGTH_LONG).show();
    if (curLocation == null) {
        curLocation = location;
    locationChanged = true;
    }
    else if (curLocation.getLatitude() == location.getLatitude() && curLocation.getLongitude() == location.getLongitude()){
    locationChanged = false;
    return;
    }
    else
       locationChanged = true;
       curLocation = location;
       if (locationChanged)
                locationManager.removeUpdates(locationListener);
       }
       public void onProviderDisabled(String provider) {
        }

        public void onProviderEnabled(String provider) 
        {
        	
        }
                
        public void onStatusChanged(String provider, int status,Bundle extras) {
            if (status == 0)// UnAvailable
            {
            } else if (status == 1)// Trying to Connect
            {
            } else if (status == 2) {// Available
            }
        }		
    };
    
    
    String tempplace="";
    long time= 0;
    
    
    @Override
    public void onCreate() {
   	

        super.onCreate();
        
        
        time= System.currentTimeMillis();
        
        
        if (Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        
        curLocation = getBestLocation();
      
        if (curLocation == null){
        	System.out.println("starting problem.........3...");
        	Toast.makeText(this, "GPS problem..........", Toast.LENGTH_SHORT).show();
       }
        else{
         	// Log.d("ssssssssssss", String.valueOf("latitude2.........."+curLocation.getLatitude()));        	 
        }
        isService =  true;
    }    
    final String TAG="LocationService";    
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
    	return super.onStartCommand(intent, flags, startId);
   }
   @Override
   
   public void onLowMemory() {
       super.onLowMemory();
   }

   @Override
   public void onStart(Intent i, int startId){
	  Toast.makeText(this, "Start services", Toast.LENGTH_SHORT).show();
	 
	  String provider = Settings.Secure.getString(getContentResolver(), Settings.Secure.LOCATION_PROVIDERS_ALLOWED);

	  if(!provider.contains("gps"))
        { //if gps is disabled
        	final Intent poke = new Intent();
        	poke.setClassName("com.android.settings","com.android.settings.widget.SettingsAppWidgetProvider"); 
        	poke.addCategory(Intent.CATEGORY_ALTERNATIVE);
        	poke.setData(Uri.parse("3")); 
        	sendBroadcast(poke);
        }	  
	  
//	  TelephonyManager telephonyManager  = (TelephonyManager)getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
//	  phoneid=telephonyManager.getDeviceId().toString();
	  
//	  SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
      handler.postDelayed(GpsFinder,10000);
       	 
   }
   @Override
   public void onDestroy() {
	   String provider = Settings.Secure.getString(getContentResolver(),Settings.Secure.LOCATION_PROVIDERS_ALLOWED);
	   if(provider.contains("gps"))
	   {
	   final Intent poke = new Intent();
	   poke.setClassName("com.android.settings","com.android.settings.widget.SettingsAppWidgetProvider");
	   poke.addCategory(Intent.CATEGORY_ALTERNATIVE);
	   poke.setData(Uri.parse("3")); 
	   sendBroadcast(poke);
	   }
	   handler.removeCallbacks(GpsFinder);
       handler = null;
       Toast.makeText(this, "Service Stopped..!!", Toast.LENGTH_SHORT).show();
       isService = false;
   }
   public IBinder onBind(Intent arg0) 
   {
         return null;
   }
   public Runnable GpsFinder = new Runnable(){
   public void run(){
		Log.d("loc....parr", "1");
    	Location tempLoc = getBestLocation();
        if(tempLoc!=null)
        {        	
    	   curLocation = tempLoc;            
           lati=String.valueOf(curLocation.getLatitude());
           longi=String.valueOf(curLocation.getLongitude());  
           Toast.makeText(getBaseContext(), lati+""+longi,Toast.LENGTH_SHORT).show();			

           String loc="";
	       String address="";
	     //  String place="";
	       String subloc="";
	       Geocoder geoCoder = new Geocoder( getBaseContext(), Locale.getDefault());      
	       try
	       {    	
	            List<Address> addresses = geoCoder.getFromLocation(curLocation.getLatitude(), curLocation.getLongitude(), 1);
	            if (addresses.size() > 0)
	            {        	  
	                 for(int index = 0;index < addresses.get(0).getMaxAddressLineIndex(); index++)
	            		address += addresses.get(0).getAddressLine(index) + " ";
	            	 place=addresses.get(0).getFeatureName().toString();
	            	 Toast.makeText(getApplicationContext(), place, Toast.LENGTH_SHORT).show();
	            	 subloc=addresses.get(0).getSubLocality().toString();
	            }

           else
	            {
          	 
            }      	
	          }
	          catch (IOException e) 
	          {        
	            e.printStackTrace();
	          }


            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String hu = sh.getString("ip", "");
            String url = "http://" + hu + ":5000/location_post";


            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                if (jsonObj.getString("status").equalsIgnoreCase("ok")) {



                                }

                                // }
                                else {
                                    Toast.makeText(getApplicationContext(), "invalid username or password", Toast.LENGTH_LONG).show();
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

                    String username;
                    params.put("blindid", sh.getString("blindid",""));
                    params.put("lattitude", LocationService.lati);
                    params.put("longitude", LocationService.longi);
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
        else 
        {
			     }
        handler.postDelayed(GpsFinder,10000);// register again to start after 20 seconds...        
    }
  
  };
 
  

    
  
  
  
  	private Location getBestLocation() {
        Location gpslocation = null;
        Location networkLocation = null;
        if(locationManager==null){
          locationManager = (LocationManager) getApplicationContext() .getSystemService(Context.LOCATION_SERVICE);
        }
        try 
        {
            if(locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER))
            {            	 
            	 locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,5000, 0, locationListener);// here you can set the 2ndargument time interval also that after how much time it will get the gps location
                gpslocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
             //  System.out.println("starting problem.......7.11....");
              
            }
            if(locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)){
                locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER,5000, 0, locationListener);
                networkLocation = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER); 
            }
        } catch (IllegalArgumentException e) {
            Log.e("error", e.toString());
        }
        if(gpslocation==null && networkLocation==null)
            return null;

        if(gpslocation!=null && networkLocation!=null){
            if(gpslocation.getTime() < networkLocation.getTime()){
                gpslocation = null;
                return networkLocation;
            }else{
                networkLocation = null;
                return gpslocation;
            }
        }
        if (gpslocation == null) {
            return networkLocation;
        }
        if (networkLocation == null) {
            return gpslocation;
        }
        return null;
    }
	
}