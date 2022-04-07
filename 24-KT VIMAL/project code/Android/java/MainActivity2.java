package com.example.ocrappnew;

import static android.Manifest.permission.RECORD_AUDIO;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.os.PowerManager;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.speech.RecognizerIntent;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class MainActivity2 extends Activity {

    private static final int REQUEST_CODE_SPEECH_INPUT = 1;
    SharedPreferences sh;
    String url;

    ProgressDialog mProgressDialog;
    private PowerManager.WakeLock mWakeLock;
    static final int DIALOG_DOWNLOAD_PROGRESS = 2;
    // Initializing all variables..
    private TextView startTV, stopTV, statusTV,t1;

    // creating a variable for medi recorder object class.
    private MediaRecorder mRecorder;

    // creating a variable for mediaplayer class
    private MediaPlayer mPlayer;

    // string variable is created for storing a file name
    private static String mFileName = null;

    // constant for storing audio permission
    public static final int REQUEST_AUDIO_PERMISSION_CODE = 1;
    String res;
    String fileName = "", path = "";
    private static final int FILE_SELECT_CODE = 0;
    String PathHolder="";
    byte[] filedt=null;
    private String simpleDateFormat;
    String result=" ";
    TextView b1;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy polphotouploadicy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(polphotouploadicy);
        }

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = "http://"+sh.getString("ip","")+":5000/photoupload";
        b1=findViewById(R.id.btn);
        statusTV = findViewById(R.id.idTVstatus);
        startTV = findViewById(R.id.btnRecord);
        stopTV = findViewById(R.id.btnStop);

        t1 = findViewById(R.id.idTVstatus7);
//        stopplayTV = findViewById(R.id.btnStopPlay);
//        stopTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        playTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        stopplayTV.setBackgroundColor(getResources().getColor(R.color.purple_200));

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                url="http://192.168.225.169:5000/texttodoc";

                RequestQueue queue = Volley.newRequestQueue(MainActivity2.this);

                // Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.

                        try {
                            JSONObject jo = new JSONObject(response);
                            String status = jo.getString("task");

                            Toast.makeText(MainActivity2.this, status + " text to doc", Toast.LENGTH_SHORT).show();

                            SharedPreferences.Editor ed = sh.edit();
                            ed.putString("image", status);
                            ed.commit();
                            startDownload1(status);


                        } catch (Exception e) {
                            Log.d("=========", e.toString());
                            Toast.makeText(MainActivity2.this, "" + e, Toast.LENGTH_SHORT).show();

                        }

                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(MainActivity2.this, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        params.put("text", result);


                        return params;
                    }
                };
                // Add the request to the RequestQueue.
                queue.add(stringRequest);

            }
        });
        startTV.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // start recording method will
                // start the recording of audio.

                startRecording();



            }
        });
        stopTV.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // pause Recording method will
                // pause the recording of audio.
//                Toast.makeText(getApplicationContext(),mFileName,Toast.LENGTH_LONG).show();

                pauseRecording();

                filedt = getbyteData(mFileName);
                Log.d("filedataaa", filedt + "");

//                startTV.setText(mFileName);
                uploadFile(mFileName);
            }
        });
//        playTV.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                // play audio method will play
//                // the audio which we have recorded
//                playAudio();
//            }
//        });
//        stopplayTV.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                // pause play method will
//                // pause the play of audio
//                pausePlaying();
//            }
//        });
    }

    private void startDownload1(String status) {


        String url = "http://192.168.225.169:5000/static/texttodoc/"+status;

        new DownloadFileAsync().execute(url);
    }
    class DownloadFileAsync extends AsyncTask<String, String, String> {

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
            mWakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK,
                    getClass().getName());
            mWakeLock.acquire();
            showDialog(DIALOG_DOWNLOAD_PROGRESS);
        }
        @Override
        protected String doInBackground(String... aurl) {
            int count;

            try {
                Log.d("aurllll",aurl[0]);

                URL url = new URL(aurl[0]);
                URLConnection conexion = url.openConnection();
                conexion.connect();

                int lenghtOfFile = conexion.getContentLength();
                Log.d("ANDRO_ASYNC", "Length of file: " + lenghtOfFile);

//	String filename = new SimpleDateFormat("dd-MM-yyyy-hh-mm-ss").format(new Date())+"ticket.html";
                InputStream input = new BufferedInputStream(url.openStream());
                File storageDir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
                File myFile = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)+"/"+sh.getString("image",""));
//                File myFile = new File(storageDir, "icon.jpg");
//                OutputStream output = new FileOutputStream(Environment.getExternalStorageDirectory() + "/" + sh.getString("orginal", ""));
                OutputStream output =new FileOutputStream(myFile);
                byte data[] = new byte[1024];

                long total = 0;

                while ((count = input.read(data)) != -1) {
                    total += count;
                    publishProgress(""+(int)((total*100)/lenghtOfFile));
                    output.write(data, 0, count);
                }

                output.flush();
                output.close();
                input.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }

        protected void onProgressUpdate(String... progress) {
            Log.d("ANDRO_ASYNC",progress[0]);
            mProgressDialog.setProgress(Integer.parseInt(progress[0]));
        }

        @Override
        protected void onPostExecute(String unused) {
            dismissDialog(DIALOG_DOWNLOAD_PROGRESS);
        }
    }
    @Override
    protected Dialog onCreateDialog(int id) {
        switch (id) {
            case DIALOG_DOWNLOAD_PROGRESS:
                mProgressDialog = new ProgressDialog(this);
                mProgressDialog.setMessage("Downloading File...");
                mProgressDialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
                mProgressDialog.setCancelable(false);
                mProgressDialog.show();
                return mProgressDialog;
        }
        return null;
    }

    private void startRecording() {
        // check permission method is used to check
        // that the user has granted permission
        // to record nd store the audio.
        if (CheckPermissions()) {

            // setbackgroundcolor method will change
            // the background color of text view.
//            stopTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
            startTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//            playTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//            stopplayTV.setBackgroundColor(getResources().getColor(R.color.purple_200));

            // we are here initializing our filename variable
            // with the path of the recorded audio file.


            mFileName = Environment.getExternalStorageDirectory().getAbsolutePath();
            mFileName += "/AudioRecording.3gp";

            // below method is used to initialize
            // the media recorder clss
            mRecorder = new MediaRecorder();

            // below method is used to set the audio
            // source which we are using a mic.
            mRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
//            Intent intent
//                    = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
//            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
//                    RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
//            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE,
//                    Locale.getDefault());
//            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak to text");
//
//            try {
//                startActivityForResult(intent, REQUEST_CODE_SPEECH_INPUT);
//            }
//            catch (Exception e) {
//                Toast
//                        .makeText(MainActivity.this, " " + e.getMessage(),
//                                Toast.LENGTH_SHORT)
//                        .show();
//            }
            // below method is used to set
            // the output format of the audio.
            mRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);

            // below method is used to set the
            // audio encoder for our recorded audio.
            mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);

            // below method is used to set the
            // output file location for our recorded audio
            mRecorder.setOutputFile(mFileName);

            try {
                // below mwthod will prepare
                // our audio recorder class
                mRecorder.prepare();
            } catch (IOException e) {
                Log.e("TAG", "prepare() failed");
            }
            // start method will start
            // the audio recording.
            mRecorder.start();
            statusTV.setText("Recording Started");
        } else {
            // if audio recording permissions are
            // not granted by user below method will
            // ask for runtime permission for mic and storage.
            RequestPermissions();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        // this method is called when user will
        // grant the permission for audio recording.
        switch (requestCode) {
            case REQUEST_AUDIO_PERMISSION_CODE:
                if (grantResults.length > 0) {
                    boolean permissionToRecord = grantResults[0] == PackageManager.PERMISSION_GRANTED;
                    boolean permissionToStore = grantResults[1] == PackageManager.PERMISSION_GRANTED;
                    if (permissionToRecord && permissionToStore) {
                        Toast.makeText(getApplicationContext(), "Permission Granted", Toast.LENGTH_LONG).show();
                    } else {
                        Toast.makeText(getApplicationContext(), "Permission Denied", Toast.LENGTH_LONG).show();
                    }
                }
                break;
        }
    }

    public boolean CheckPermissions() {
        // this method is used to check permission
        int result = ContextCompat.checkSelfPermission(getApplicationContext(), WRITE_EXTERNAL_STORAGE);
        int result1 = ContextCompat.checkSelfPermission(getApplicationContext(), RECORD_AUDIO);
        return result == PackageManager.PERMISSION_GRANTED && result1 == PackageManager.PERMISSION_GRANTED;
    }

    private void RequestPermissions() {
        // this method is used to request the
        // permission for audio recording and storage.
        ActivityCompat.requestPermissions(MainActivity2.this, new String[]{RECORD_AUDIO, WRITE_EXTERNAL_STORAGE}, REQUEST_AUDIO_PERMISSION_CODE);
    }


    public void playAudio() {
        stopTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
        startTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        playTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        stopplayTV.setBackgroundColor(getResources().getColor(R.color.purple_200));

        // for playing our recorded audio
        // we are using media player class.
        mPlayer = new MediaPlayer();
        try {
            // below method is used to set the
            // data source which will be our file name
            mPlayer.setDataSource(mFileName);

            // below method will prepare our media player
            mPlayer.prepare();

            // below method will start our media player.
            mPlayer.start();
            statusTV.setText("Recording Started Playing");
        } catch (IOException e) {
            Log.e("TAG", "prepare() failed");
        }
    }

    public void pauseRecording() {
        stopTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        startTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        playTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        stopplayTV.setBackgroundColor(getResources().getColor(R.color.purple_200));

        // below method will stop
        // the audio recording.
        statusTV.setText("Recording Stoped");

        mRecorder.stop();

        // below me
        // thod will release
        // the media recorder class.
        mRecorder.release();
        mRecorder = null;





    }

    private void uploadFile(String filepath) {

        VolleyMultipartRequest volleyMultipartRequest = new VolleyMultipartRequest(Request.Method.POST, url,
                new Response.Listener<NetworkResponse>() {
                    @Override
                    public void onResponse(NetworkResponse response1) {

                        String x=new String(response1.data);
                        try {
                            JSONObject obj = new JSONObject(new String(response1.data));
                            result+=obj.getString("task")+" ";
                        Toast.makeText(MainActivity2.this, obj.getString("task"), Toast.LENGTH_LONG).show();
                           t1.setText(result);

//                            if (obj.getString("task").equalsIgnoreCase("success")) {
//
//                                Toast.makeText(MainActivity2.this, "Successfully uploaded", Toast.LENGTH_LONG).show();
//                                Intent i=new Intent(getApplicationContext(), MainActivity2.class);
//                                startActivity(i);
//                            } else {
//                                Toast.makeText(getApplicationContext(), "failed", Toast.LENGTH_LONG).show();
//                            }

                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                        }


                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(getApplicationContext(), error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }) {

            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<>();





                return params;
            }


            protected Map<String, VolleyMultipartRequest.DataPart> getByteData() {
                Map<String, VolleyMultipartRequest.DataPart> params = new HashMap<>();
                long imagename = System.currentTimeMillis();

                params.put("file", new VolleyMultipartRequest.DataPart(mFileName , filedt ));
                return params;
            }
        };

        Volley.newRequestQueue(this).add(volleyMultipartRequest);

    }

    private byte[] getbyteData(String pathHolder) {
        Log.d("path", pathHolder);
        File fil = new File(pathHolder);
        int fln = (int) fil.length();
        byte[] byteArray = null;
        try {
            InputStream inputStream = new FileInputStream(fil);
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            byte[] b = new byte[fln];
            int bytesRead = 0;

            while ((bytesRead = inputStream.read(b)) != -1) {
                bos.write(b, 0, bytesRead);
            }
            byteArray = bos.toByteArray();
            inputStream.close();
        } catch (Exception e) {
            Toast.makeText(getApplicationContext(),e+"",Toast.LENGTH_LONG).show();
        }
        return byteArray;




    }

    public void pausePlaying() {
        // this method will release the media player
        // class and pause the playing of our recorded audio.
        mPlayer.release();
        mPlayer = null;
        stopTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
        startTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        playTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
//        stopplayTV.setBackgroundColor(getResources().getColor(R.color.purple_200));
        statusTV.setText("Recording Play Stopped");
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CODE_SPEECH_INPUT) {
            if (resultCode == RESULT_OK && data != null) {
                ArrayList<String> result = data.getStringArrayListExtra(
                        RecognizerIntent.EXTRA_RESULTS);
                statusTV.setText(
                        Objects.requireNonNull(result).get(0));
            }
        }
    }
}