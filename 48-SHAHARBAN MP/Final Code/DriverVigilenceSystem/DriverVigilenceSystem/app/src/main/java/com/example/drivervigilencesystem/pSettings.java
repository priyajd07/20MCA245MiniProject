package com.example.drivervigilencesystem;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.SeekBar;
import android.widget.Switch;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class pSettings extends AppCompatActivity implements View.OnClickListener, SeekBar.OnSeekBarChangeListener, CompoundButton.OnCheckedChangeListener {
    String speed="";
    String mode="";
    Integer brightness;
    String callblock="NO",touch="NO";
    String automessage="NO";

    String message="";
    String messagetype="ALL";


    Button B17,B18,B19,B20,B21;
    RadioButton R4,R5,R6;
    EditText E35;
    Switch Sw1,Sw2,Sw3;
    SeekBar SB1;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_psettings);

        B17=(Button)findViewById(R.id.btn_psplimit1);
        B18=(Button)findViewById(R.id.btn_psplimit2);
        B19=(Button)findViewById(R.id.btn_splimit3);
        B20=(Button)findViewById(R.id.btn_savesettings);
        B21=(Button)findViewById(R.id.btn_cancelsettings);
        R4=(RadioButton)findViewById(R.id.rd_silent);
        R5=(RadioButton)findViewById(R.id.rd_vibrate);
        R6=(RadioButton)findViewById(R.id.rd_general);

        E35=(EditText)findViewById(R.id.ed_urmsg);
        Sw1=(Switch)findViewById(R.id.swt_touch);
        Sw2=(Switch)findViewById(R.id.swt_callblock);
        Sw3=(Switch)findViewById(R.id.swt_automsg);
        SB1=(SeekBar)findViewById(R.id.sb_brightness);

        B17.setOnClickListener(this);
        B18.setOnClickListener(this);
        B19.setOnClickListener(this);
        B20.setOnClickListener(this);
        B21.setOnClickListener(this);


        Sw1.setOnCheckedChangeListener(this);
        Sw2.setOnCheckedChangeListener(this);
        Sw3.setOnCheckedChangeListener(this);

        SB1.setOnSeekBarChangeListener(this);

    }

    @Override
    public void onClick(View view) {

        if (view == B17) {

//            Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();

            speed = "0-40";
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String ip = sh.getString("ip", "");

            String url = "http://" + ip + ":5000/driverspeedsetting_view";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {
                                   String mode = jsonObj.getString("mode");
                                    if(mode.equals("SILENT"))
                                    {
                                        R4.setChecked(true);

                                    }if(mode.equals("VIBRATE"))
                                    {
                                        R5.setChecked(true);
                                    }if(mode.equals("GENERAL")) {
                                        R6.setChecked(true);
                                    }

                                    String brightness = jsonObj.getString("bright");
                                    SB1.setProgress(Integer.parseInt(brightness));

                                    String touch1 = jsonObj.getString("touch");
                                    if(touch1.equals("YES"))
                                        Sw1.setChecked(true);
                                    else
                                        Sw1.setChecked(false);


                                    String callblock = jsonObj.getString("callblock");
                                    if(callblock.equals("YES"))
                                        Sw2.setChecked(true);
                                    else
                                        Sw2.setChecked(false);

                                    String automessage = jsonObj.getString("automessage");
                                    if(automessage.equals("YES"))
                                        Sw3.setChecked(true);

                                    else
                                        Sw3.setChecked(false);
                                    String message = jsonObj.getString("message");
                                    E35.setText(message);
                                    String type = jsonObj.getString("messagetype");


//                                         Toast.makeText(getApplicationContext(), "success", Toast.LENGTH_LONG).show();

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

                    params.put("driverid", sh.getString("sel_did", ""));
                    params.put("speed", speed);

                    return params;
                }
            };


            requestQueue.add(postRequest);
        }
        if(view==B18) {
            speed="40-60";
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String ip = sh.getString("ip", "");

            String url = "http://" + ip + ":5000/driverspeedsetting_view";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {
                                    String mode = jsonObj.getString("mode");
                                    if(mode.equals("SILENT"))
                                    {
                                        R4.setChecked(true);



                                    }if(mode.equals("VIBRATE"))
                                    {
                                        R5.setChecked(true);
                                    }if(mode.equals("GENERAL"))
                                    {
                                        R6.setChecked(true);
                                    }

                                    String brightness = jsonObj.getString("bright");
                                    SB1.setProgress(Integer.parseInt(brightness));

                                    String touch1 = jsonObj.getString("touch");
                                    if(touch1.equals("YES"))
                                        Sw1.setChecked(true);
                                    else
                                        Sw1.setChecked(false);


                                    String callblock = jsonObj.getString("callblock");
                                    if(callblock.equals("YES"))
                                        Sw2.setChecked(true);
                                    else
                                        Sw2.setChecked(false);

                                    String automessage= jsonObj.getString("automessage");
                                    if(automessage.equals("YES"))
                                        Sw3.setChecked(true);
                                    else
                                        Sw3.setChecked(false);

                                    String message = jsonObj.getString("message");
                                    E35.setText(message);
                                    String type = jsonObj.getString("messagetype");


//                                    Toast.makeText(getApplicationContext(), "success", Toast.LENGTH_LONG).show();

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

                    params.put("driverid", sh.getString("sel_did", ""));
                    params.put("speed", speed);

                    return params;
                }
            };


            requestQueue.add(postRequest);




        }
        if(view==B19) {
            speed=">60";
            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String ip = sh.getString("ip", "");

            String url = "http://" + ip + ":5000/driverspeedsetting_view";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();

                            // response
                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {
                                    String mode = jsonObj.getString("mode");
                                    if(mode.equals("SILENT"))
                                    {
                                        R4.setChecked(true);



                                    }if(mode.equals("VIBRATE"))
                                    {
                                        R5.setChecked(true);
                                    }if(mode.equals("GENERAL")){
                                        R6.setChecked(true);
                                    }

                                    String brightness = jsonObj.getString("bright");
                                    SB1.setProgress(Integer.parseInt(brightness));

                                    String touch1 = jsonObj.getString("touch");
                                    if(touch1.equals("YES"))
                                        Sw1.setChecked(true);
                                    else
                                        Sw1.setChecked(false);


                                    String callblock = jsonObj.getString("callblock");
                                    if(callblock.equals("YES"))
                                        Sw2.setChecked(true);
                                    else
                                        Sw2.setChecked(false);


                                    String automessage = jsonObj.getString("automessage");
                                    if(automessage.equals("YES"))
                                        Sw3.setChecked(true);
                                    else
                                        Sw3.setChecked(false);

                                    String message = jsonObj.getString("message");
                                    E35.setText(message);
                                    String type = jsonObj.getString("messagetype");


//                                    Toast.makeText(getApplicationContext(), "success", Toast.LENGTH_LONG).show();

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

                    params.put("driverid", sh.getString("sel_did", ""));
                    params.put("speed", speed);

                    return params;
                }
            };


            requestQueue.add(postRequest);




        }
        if(view==B20){
//            Intent i = new Intent(getApplicationContext(), User_profile.class);
//            startActivity(i);


            if(R4.isChecked()==true)
            {
                mode ="SILENT";

            }
            else if(R5.isChecked()==true)
            {
                mode="VIBRATE";


            }
            else
            {
                mode="GENERAL";


            }

            if(Sw3.isChecked()==true)
            {
                automessage="YES";

            }else
            {
                automessage="NO";
            }




            final String message=E35.getText().toString();
            SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String IP = sp.getString("ip", "");
            String url = "http://" + IP + ":5000/driverspeed_settings";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            //    Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {


//                            Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                String sucs = jsonObj.getString("status");
                                if (sucs.equalsIgnoreCase("ok")) {


                                    Intent i = new Intent(getApplicationContext(), partner_view_driver.class);
                                    startActivity(i);
//

//                                    Toast.makeText(getApplicationContext(), "success", Toast.LENGTH_LONG).show();

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
                    params.put("driverid",sh.getString("sel_did",""));
                    params.put("speed", speed);
                    params.put("mode", mode);
                    params.put("brightness",brightness+"");
                    params.put("touch", touch);
                    params.put("callblock", callblock);
                    params.put("automessage", automessage);
                    params.put("message", message);
                    params.put("messagetype", messagetype);

//                params.put("asid",sh.getString("assid",""));
                    return params;
                }
            };


            requestQueue.add(postRequest);




        }if(view==B21)
        {
            Intent i = new Intent(getApplicationContext(), partner_view_driver.class);
            startActivity(i);

        }





    }

    @Override
    public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
        brightness=i;


    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {

    }

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {

    }

    @Override
    public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
        if(compoundButton==Sw1)
        {
            if(b==true)
            {
                touch="YES";
//                Toast.makeText( getApplicationContext(),touch , Toast.LENGTH_SHORT).show();

            }else
                touch = "NO";
//            Toast.makeText(getApplicationContext(), touch, Toast.LENGTH_SHORT).show();


        }
        if(compoundButton==Sw2)
        {
            if(b==true)
            {
                callblock="YES";
//                Toast.makeText( getApplicationContext(),callblock , Toast.LENGTH_SHORT).show();


            }else
                callblock = "NO";
//            Toast.makeText(getApplicationContext(), callblock, Toast.LENGTH_SHORT).show();



        }
    }
}
