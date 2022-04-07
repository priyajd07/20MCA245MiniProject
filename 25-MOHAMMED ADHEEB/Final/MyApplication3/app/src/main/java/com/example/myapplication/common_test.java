package com.example.myapplication;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class common_test extends AppCompatActivity {
    TextView t0;
    RadioButton r1,r2,r3,r4;
    Button b1;
    String rid="",ss="",ur="";
    SharedPreferences sp;
    int index=0,mark=0;
    public static ArrayList<String> qstn;
    public static ArrayList<String> opt1;
    public static ArrayList<String> opt2;
    public static ArrayList<String> opt3;
    public static ArrayList<String> opt4;
    public static ArrayList<String> ans;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_common_test);
        t0=(TextView)findViewById(R.id.textView1);
        r1=(RadioButton)findViewById(R.id.radio0);
        r2=(RadioButton)findViewById(R.id.radio1);
        r3=(RadioButton)findViewById(R.id.radio2);
        r4=(RadioButton)findViewById(R.id.radio3);
        b1=(Button)findViewById(R.id.button1);
        sp=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        qstn=getIntent().getStringArrayListExtra("qstn");
        opt1=getIntent().getStringArrayListExtra("opt1");
        opt2=getIntent().getStringArrayListExtra("opt2");
        opt3=getIntent().getStringArrayListExtra("opt3");
        opt4=getIntent().getStringArrayListExtra("opt4");
        ans=getIntent().getStringArrayListExtra("ans");

        t0.setText(qstn.get(index));
        r1.setText(opt1.get(index));
        r2.setText(opt2.get(index));
        r3.setText(opt3.get(index));
        r4.setText(opt4.get(index));
        b1.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {

                String answer=ans.get(index);
                String cans="";
                if(r1.isChecked())
                {
                    cans=r1.getText().toString();
                }
                else if (r2.isChecked()) {
                    cans=r2.getText().toString();

                }
                else if (r3.isChecked()) {
                    cans=r3.getText().toString();


                }
                else {
                    cans=r4.getText().toString();
                }
                if (cans.equals(answer)) {
                    mark=mark+1;

                }

                index=index+1;
                if ((qstn.size()+"").equalsIgnoreCase(index+"")) {
                    new Insert1().execute();

                }
                else {

                    qstn=getIntent().getStringArrayListExtra("qstn");
                    opt1=getIntent().getStringArrayListExtra("opt1");
                    opt2=getIntent().getStringArrayListExtra("opt2");
                    opt3=getIntent().getStringArrayListExtra("opt3");
                    opt4=getIntent().getStringArrayListExtra("opt4");
                    t0.setText(qstn.get(index));
                    r1.setText(opt1.get(index));
                    r2.setText(opt2.get(index));
                    r3.setText(opt3.get(index));
                    r4.setText(opt4.get(index));
                }

                // TODO Auto-generated method stub

            }
        });
    }


    class Insert1 extends AsyncTask<String, String, String> {

        /**
         * Before starting background thread Show Progress Dialog
         * */
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }
        protected String doInBackground(String... args)
        {


//            List<NameValuePair> params = new ArrayList<NameValuePair>();
//            params.add(new BasicNameValuePair("rid",rid ));
//            params.add(new BasicNameValuePair("mark",mark+"" ));
//
//
//            Log.d("ins===",ur);
//
//            JSONObject jsondata=null;
//            try {
//
//
//                jsondata = (JSONObject)jsonParser.makeHttpRequest(ur,"GET", params);
//            } catch (JSONException e1) {
//                // TODO Auto-generated catch block
//                e1.printStackTrace();
//            }
//            Log.d("Reultttttt=-",jsondata+"");
//            String ss=null;
//
//            try {
//                Log.d("==============", "Emmmntered");
//                ss=jsondata.getString("task");
//                Log.d("Msg+++++++", ss);
//                if(!ss.equals("failed"))
//                {
//                    Log.d("**********", "success");
//
//
//                    //Toast.makeText(getApplicationContext(), "Doneeeee", Toast.LENGTH_LONG).show();
//                }
//                else
//                {
//                    publishProgress(ss);
//                }
//            }
//            catch(Exception e)
//            {
//
//                Log.d("==============", "Catched");
//
//                Log.d( "Error"+e,"================");
//            }


            RequestQueue queue = Volley.newRequestQueue(common_test.this);
            ur="http://"+sp.getString("ip","")+":5000/markup";
            // Request a string response from the provided URL.
            StringRequest stringRequest = new StringRequest(Request.Method.POST, ur,new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    // Display the response string.
                    Log.d("+++++++++++++++++",response);

                    try {
                        JSONObject json=new JSONObject(response);
                        ss=json.getString("task");

                        if(ss.equalsIgnoreCase("invalid"))
                        {
                            Toast.makeText(getApplicationContext(),"invalid",Toast.LENGTH_LONG).show();
                        }
                        else
                        {
//
                            publishProgress(ss);
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();

                    }

                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {


                    Toast.makeText(getApplicationContext(),"invalid",Toast.LENGTH_LONG).show();
                }
            }){
                @Override
                protected Map<String, String> getParams()
                {
                    Map<String, String>  params = new HashMap<String, String>();

                    params.put("mark",mark+"");
                    params.put("lid",sp.getString("lid",""));
                    params.put("cid", sp.getString("cid",""));
                    params.put("sid", sp.getString("sid",""));
                    params.put("index",index+"");

                    return params;
                }
            };
            // Add the request to the RequestQueue.
            queue.add(stringRequest);

            return ss;

        }

        @Override
        protected void onProgressUpdate(String... values) {
//        	e.setText(values[0]);
            // TODO Auto-generated method stub, text, duration)
        }
        protected void onPostExecute(String file_url) {
            // dismiss the dialog once done
            // pDialog.dismiss();

            Toast.makeText(getApplicationContext(), "Completed", Toast.LENGTH_LONG).show();
            Intent i=new Intent(getApplicationContext(),Candidate_home.class);
            startActivity(i);

        }

    }
}
