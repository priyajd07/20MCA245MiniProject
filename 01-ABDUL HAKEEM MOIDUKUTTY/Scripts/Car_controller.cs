using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System; 

[System.Serializable]
public class AxleInfo
{
    public WheelCollider leftWheel;
    public WheelCollider rightWheel;
    public bool motor;
    public bool steering;
}

public class Car_controller : MonoBehaviour
{
    public List<AxleInfo> axleinfos;
    public float maxMotorTorque;
    public float maxSteeringAngle;
    public float acceleration;
    public Camera miniMapCamera;
    public Rigidbody rigidbody;
    public Action<double> MPH;

     void FixedUpdate() {
         // moves the car forward and backwards
        float motor = maxMotorTorque * Input.GetAxis("Vertical") * acceleration;
        // turning
        float steering = maxSteeringAngle * Input.GetAxis("Horizontal");

        foreach(AxleInfo axleInfo in axleinfos)
            {
                if(axleInfo.steering)
                {
                axleInfo.leftWheel.steerAngle = steering;
                axleInfo.rightWheel.steerAngle = steering;
                }
                if(axleInfo.motor)
                {
                    axleInfo.leftWheel.motorTorque = motor;
                    axleInfo.rightWheel.motorTorque = motor;
                }
            }
            
        double mph = rigidbody.velocity.magnitude * 2.237;
        mph = Math.Round(mph, 0);
        MPH?.Invoke(mph);
        

    }
}
