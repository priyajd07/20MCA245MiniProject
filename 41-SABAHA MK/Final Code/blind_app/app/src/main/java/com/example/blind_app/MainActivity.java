package com.example.blind_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.camerakit.CameraKit;
import com.camerakit.CameraKitView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity implements RecognitionListener, View.OnClickListener {
    com.google.android.material.textfield.TextInputLayout et,edblindid;
    Button bt;

    CameraKitView cameraKitView;

    private SpeechRecognizer speech = null;
    private Intent recognizerIntent;

    public void start(){


//        Toast.makeText(getApplicationContext(),"111",Toast.LENGTH_LONG).show();


        speech = SpeechRecognizer.createSpeechRecognizer(this);
        speech.setRecognitionListener(this);
        recognizerIntent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE,
                "en");
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 10);
        speech.startListening(recognizerIntent);
//        Toast.makeText(getApplicationContext(),"222",Toast.LENGTH_LONG).show();



    }

//    EditText edblindid;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        et=findViewById(R.id.editTextTextPersonName);
        edblindid=findViewById(R.id.editTextTextPersonName2);
        bt=findViewById(R.id.button);
        bt.setOnClickListener(this);

        cameraKitView = findViewById(R.id.camera);

        cameraKitView.setFacing(CameraKit.FACING_BACK);
        try {
            cameraKitView.onStart();
        }catch (Exception e)
        {
            Toast.makeText(this, e.toString(), Toast.LENGTH_SHORT).show();
        }








    }

    @Override
    public void onReadyForSpeech(Bundle bundle) {

    }

    @Override
    public void onBeginningOfSpeech() {

    }

    @Override
    public void onRmsChanged(float v) {

    }

    @Override
    public void onBufferReceived(byte[] bytes) {

    }

    @Override
    public void onEndOfSpeech() {
        speech.startListening(recognizerIntent);

    }

    @Override
    public void onError(int i) {
        speech.startListening(recognizerIntent);

    }

    @Override
    public void onResults(Bundle bundle) {

        ArrayList<String> matches = bundle
                .getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
        String text = "";
        for (String result : matches) {
            text += result + "\n";
            Toast.makeText(getApplicationContext(), result, Toast.LENGTH_LONG).show();

            if(result.equalsIgnoreCase("location"))
            {
                Speakerbox a= new Speakerbox(getApplication());
                a.play("You are now at "+ LocationService.place);
            }

            else if(result.toString().contains("camera")) {

                familiarpersondetection();

            }
            else if(result.equalsIgnoreCase("emergency"))
            {



                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                String hu = sh.getString("ip", "");
                String url = "http://" + hu + ":5000/emergency_addhelp_post";


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


                                        Speakerbox a= new Speakerbox(getApplication());
                                        a.play("EMERGENCY MESSAGE SENT SUCCESSFULLY");


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






        }

        speech.startListening(recognizerIntent);


    }



    @Override
    public void onPartialResults(Bundle bundle) {

    }

    @Override
    public void onEvent(int i, Bundle bundle) {

    }

    @Override
    public void onClick(View view) {

        String name=et.getEditText().getText().toString();
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed = sh.edit();
        ed.putString("ip", name);
        ed.putString("blindid", edblindid.getEditText().getText().toString());
        ed.commit();

        startService(new Intent(getApplicationContext(),LocationService.class));
        start();
    }
    public void familiarpersondetection()
    {
        cameraKitView.captureImage(new CameraKitView.ImageCallback() {
            @Override
            public void onImage(CameraKitView view, final byte[] photo) {

                cameraKitView.captureImage(new CameraKitView.ImageCallback() {
                    @Override
                    public void onImage(CameraKitView view, final byte[] photo) {

                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                        String hu = sh.getString("ip", "");
                        String url = "http://" + hu + ":5000/face_recognition_post";


                        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                                new Response.Listener<NetworkResponse>() {
                                    @Override
                                    public void onResponse(NetworkResponse response) {
                                        try {

                                            JSONObject obj = new JSONObject(new String(response.data));
                                            String dis = obj.getString("status");
                                            if (dis.equalsIgnoreCase("ok")) {

                                                String result = obj.getString("result");

                                                Toast.makeText(getApplicationContext(), "person found..", Toast.LENGTH_LONG).show();



                                                Speakerbox a= new Speakerbox(getApplication());
                                                a.play(result);



                                            } else {

                                                Speakerbox a= new Speakerbox(getApplication());
                                                a.play("invalid person");



                                                Toast.makeText(getApplicationContext(), "Invalid person..", Toast.LENGTH_LONG).show();

                                            }
                                        } catch (JSONException e) {
                                            Toast.makeText(getApplicationContext(), "error", Toast.LENGTH_SHORT).show();
                                            e.printStackTrace();
                                        }
                                    }
                                },
                                new Response.ErrorListener() {
                                    @Override
                                    public void onErrorResponse(VolleyError error) {
                                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                                    }
                                }) {


                            @Override
                            protected Map<String, String> getParams() {
                                Map<String, String> params = new HashMap<>();
                                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                params.put("bid", sh.getString("blindid",""));
                                return params;
                            }

                            @Override
                            protected Map<String, DataPart> getByteData() {
                                Map<String, DataPart> params = new HashMap<>();
                                long imagename = System.currentTimeMillis();
                                params.put("pic", new DataPart("a.jpg", photo));

                                return params;
                            }
                        };
                        int MY_SOCKET_TIMEOUT_MS = 60000;

                        volleyMultipartRequest.setRetryPolicy(new DefaultRetryPolicy(
                                MY_SOCKET_TIMEOUT_MS,
                                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));

                        Volley.newRequestQueue(getApplicationContext()).add(volleyMultipartRequest);


                    }

                });

            }


        });
    }
}