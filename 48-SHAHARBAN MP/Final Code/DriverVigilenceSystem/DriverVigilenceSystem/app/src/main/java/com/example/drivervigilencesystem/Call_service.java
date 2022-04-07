package com.example.drivervigilencesystem;

import android.Manifest;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.IBinder;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.telecom.TelecomManager;
import android.telephony.PhoneStateListener;
import android.telephony.SmsManager;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.widget.Toast;

//import com.android.internal.telephony.ITelephony;

import androidx.annotation.RequiresApi;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.android.internal.telephony.ITelephony;

import org.json.JSONArray;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;


public class Call_service extends Service {
	

	String imei;
	String opn;
	String dt="",tm="";
	long diffinmin,diffinhr;
	TelephonyManager telephonyManager;
	TelephonyManager telman;

	 public static int flg=0;	
	 String phnop="";
	// @TargetApi(Build.VERSION_CODES.GINGERBREAD)
	@Override
	public void onCreate() 
	 {		
		 //Toast.makeText(getApplicationContext(), "service started", Toast.LENGTH_SHORT).show();
		 
		// TODO Auto-generated method stub
		super.onCreate();
		
		if (android.os.Build.VERSION.SDK_INT > 9)
		{
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }


		 SimpleDateFormat tet=new SimpleDateFormat("hh:mm:ss");
		 tm=tet.format(new Date());
		 telman=(TelephonyManager)getApplicationContext().getSystemService(TELEPHONY_SERVICE);
		//imei=telman.getDeviceId().toString();
		
		 telman.listen(phlist,PhoneStateListener.LISTEN_CALL_STATE);
		 Log.d("....old...", ".....00");
	}
  
	 public PhoneStateListener phlist=new PhoneStateListener()
   {
	   @RequiresApi(api = Build.VERSION_CODES.P)
	   public void onCallStateChanged(int state, String inNum)
	   {

		  switch (state)
		  {




		     case TelephonyManager.CALL_STATE_IDLE:

		    	 		SimpleDateFormat dd=new SimpleDateFormat("dd/MM/yyyy");
						SimpleDateFormat tt=new SimpleDateFormat("hh:mm:ss");

						String d=dd.format(new Date());
						String t=tt.format(new Date());

						String duration="";
						long tmdiff=0;

					//	Log.d("....old...", ".....3");
						try
						{
								Date dt1=tt.parse(t);
								Date dt2=tt.parse(tm);

								tmdiff=dt1.getTime()-dt2.getTime();

								tmdiff=TimeUnit.MILLISECONDS.toSeconds(tmdiff);
								diffinmin=tmdiff/(60);
								diffinhr=diffinmin/(60);
								tmdiff-=(diffinmin*60);

								duration=diffinhr+":"+ diffinmin + ":"+ tmdiff;


								SharedPreferences shp=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
								Editor edit=shp.edit();
								edit.putString("duration", duration);
								edit.commit();




								//Toast.makeText(getApplicationContext(), "call duration" +duration, Toast.LENGTH_LONG).show();

						}
						catch (Exception e)
						{
							// TODO Auto-generated catch block
							//Toast.makeText(getApplicationContext(), "error1 in call:"+e.toString(), Toast.LENGTH_SHORT).show();
							 //Toast.makeText(getApplicationContext(), "5",Toast.LENGTH_SHORT).show();
							Log.d("error1",e.toString());
						}


						SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(getBaseContext());
						String name = preferences.getString("callstatus", "hi");

						if(name.equalsIgnoreCase("incoming"))
						{
							 //Toast.makeText(getApplicationContext(), "4",Toast.LENGTH_SHORT).show();
							Log.d("....1....", "..incall..");


							SharedPreferences shpr=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
							Editor edit1=shpr.edit();


							//edit1.putString("Number", "incoming call");

							edit1.commit();



							try
							{
								//call(MainActivity.phoneid,phnop,"incoming",duration,d,t);
							}
							catch (Exception e)
							{
								// TODO Auto-generated catch block
								//Toast.makeText(getApplicationContext(), "error2 in call:"+e.toString(), Toast.LENGTH_SHORT).show();
								Log.d("error2",e.toString());
							}


							SharedPreferences sh1=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

						String ss=sh1.getString("incoming number", "");

							String dur=sh1.getString("duration", "");

							//Toast.makeText(getApplicationContext(),ss  +"\n"+  "incoming call" +"\n" +dur , Toast.LENGTH_LONG).show();


//							imei=telman.getDeviceId().toString();
//							//Toast.makeText(getApplicationContext(), "inserting   INCOMING", Toast.LENGTH_LONG).show();
//
//							db.sendcall(ss,imei, "INCOMING",dur);
//


							 flg=0;
						 }


						 else if(flg==1)
						 {

							 //Toast.makeText(getApplicationContext(), "1",Toast.LENGTH_SHORT).show();


							 Log.d("....1....", "..outcall..");
							 try
							 {
								SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
								opn=sh.getString("num", "");


								//Toast.makeText(getApplicationContext(), "kooooooooooooooy"+opn,Toast.LENGTH_LONG).show();



								//call1(MainActivity.phoneid,opn,"outgoing",duration,d,t);
							 }
							 catch (Exception e)
							 {
								// TODO Auto-generated catch block
								 //Toast.makeText(getApplicationContext(), "error3 in call:"+e.toString(), Toast.LENGTH_SHORT).show();
								 Log.d("error3",e.toString());
							 }


							 SharedPreferences sh2=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


								String dur=sh2.getString("duration", "");
								Toast.makeText(getApplicationContext(),opn+"\n"+"Outgoing call"+"\n"+dur , Toast.LENGTH_LONG).show();

//								imei=telman.getDeviceId().toString();
//								//Toast.makeText(getApplicationContext(), "inserting   OUTGOING", Toast.LENGTH_LONG).show();
//
//								db.sendcall(opn,imei, "OUTGOING",dur);
//
							 flg=0;
						 }


				         Editor editor = preferences.edit();
				         editor.putString("callstatus","idle");
				         editor.commit();

				         break;



		     case TelephonyManager.CALL_STATE_OFFHOOK:

		    	 		SimpleDateFormat sm=new SimpleDateFormat("dd/MM/yyyy");
		    	 		SimpleDateFormat sn=new SimpleDateFormat("hh:mm:ss");

		    	 		flg=1;

		    	 		dt=sm.format(new Date());
		    	 		tm=sn.format(new Date());
		    	 		//Toast.makeText(getApplicationContext(), dt + "  " + tm, Toast.LENGTH_LONG).show();











		    	 		Toast.makeText(getApplicationContext(),opn+" is number", Toast.LENGTH_SHORT).show();

		    	 		SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
		    	 		String block=sh.getString("block","" );
		    	 		if(block.equalsIgnoreCase("NO"))
						{

						}
						else {


                            try {
//                                Class c = null;
//
//                                    c = Class.forName(telephonyManager.getClass().getName());
//
//                                    Method m = c.getDeclaredMethod("getITelephony");
//                                    m.setAccessible(true);
//                                    ITelephony telephonyService = (ITelephony) m.invoke(telephonyManager);
//                                      telephonyService.silenceRinger();
//                                    telephonyService.endCall();



								TelephonyManager manager = (TelephonyManager) getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
								Class c = Class.forName(manager.getClass().getName());
								Method m = c.getDeclaredMethod("getITelephony");
								m.setAccessible(true);
								ITelephony telephony = (ITelephony)m.invoke(manager);
								telephony.answerRingingCall();



                                    ;
                                } catch (ClassNotFoundException e) {
                                    e.printStackTrace();
                                } catch (NoSuchMethodException e) {
                                    e.printStackTrace();
                                } catch (IllegalAccessException e) {
                                    e.printStackTrace();
                                } catch (InvocationTargetException e) {
                                    e.printStackTrace();
                                }

                            }





                 break;


		     case TelephonyManager.CALL_STATE_RINGING:

		     			phnop=inNum;
		     			Toast.makeText(getApplicationContext(), phnop+"---------------", Toast.LENGTH_LONG).show();



				 sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

				 String numbersandmessage1 = sh.getString("numbersandmessage", "");
				 Toast.makeText(getApplicationContext(), phnop + "Call blocked" + numbersandmessage1, Toast.LENGTH_SHORT).show();






				 try
							{




								 sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
								 String blocks=sh.getString("block", "");


								 Toast.makeText(getApplicationContext(),"Block number status"+blocks,Toast.LENGTH_LONG).show();



								 if(blocks.equalsIgnoreCase("Yes")) {




									 Toast.makeText(getApplicationContext(), phnop + "-----------" + ""+sh.getString("MSGS",""), Toast.LENGTH_SHORT).show();
									 SmsManager smmngr = SmsManager.getDefault();
									 sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
									 smmngr.sendTextMessage(phnop, null, sh.getString("MSGS","NA"), null, null);


									 Toast.makeText(getApplicationContext(), "automessagesent", Toast.LENGTH_SHORT).show();



									 Toast.makeText(getApplicationContext(),"Call blokedddddd hihihihi",Toast.LENGTH_SHORT).show();
////


									 try {
//										 if (Build.VERSION.SDK_INT > Build.VERSION_CODES.M
//												 || checkSelfPermission(Manifest.permission.CALL_PHONE)
//												 == PackageManager.PERMISSION_DENIED) {
//										 	Toast.makeText(getApplicationContext(),"Denied",Toast.LENGTH_LONG).show();
//											 return;
//										 }
//
//										 try {
//											 TelephonyManager telephonyManager = (TelephonyManager) getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
//											 Class c = Class.forName(telephonyManager.getClass().getName());
//											 Method m = c.getDeclaredMethod("getITelephony");
//											 m.setAccessible(true);
//											 ITelephony telephonyService = (ITelephony) m.invoke(telephonyManager);
//											 telephonyService.endCall();
//
//										 } catch (Exception ex) {
//											 Log.d("aaaaaaaaaabbbbbbb",ex.getMessage().toString());
//											 Toast.makeText(getApplicationContext(),"bbbb block errror"+ ex.getMessage().toLowerCase(),Toast.LENGTH_LONG).show();
//										 }

										 TelephonyManager manager = (TelephonyManager) getApplicationContext().getSystemService(Context.TELEPHONY_SERVICE);
										 Class c = Class.forName(manager.getClass().getName());
										 Method m = c.getDeclaredMethod("getITelephony");
										 m.setAccessible(true);
										 ITelephony telephony = (ITelephony)m.invoke(manager);
										 telephony.endCall();






									 }
									 catch (Exception ex)
									 {

									 	Log.d("aaaaaaaaaa",ex.getMessage().toString());


									 	Toast.makeText(getApplicationContext(),"block errror"+ ex.getMessage().toLowerCase(),Toast.LENGTH_LONG).show();
									 }
//



								 }
							}
							catch (Exception e) 
							{
								// TODO: handle exception
								//Toast.makeText(getApplicationContext(), "error5 in call:"+e.toString(), Toast.LENGTH_SHORT).show();
								Log.d("error5",e.toString());
								
							}

					break;
		  }	
		 
	   }

   };
  

	
	public IBinder onBind(Intent arg0) {
		
		return null;
	}

}
