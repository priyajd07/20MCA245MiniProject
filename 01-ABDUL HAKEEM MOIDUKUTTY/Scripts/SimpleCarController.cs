using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SimpleCarController : MonoBehaviour
{
    private const string HORIZONTAL = "Horizontal";
    private const string VERTICAL =  "Vertical";
    private float HorizontalInput;
    private float VerticalInput;
    private float steerAngle;
    private float currentbreakForce;
    private bool isBreaking;
    
    private float currentNitroForce;
    private bool isNitroOn;


    [SerializeField] private float motorForce;
    [SerializeField] private float breakForce;
    [SerializeField] private float nitroForce;
    [SerializeField] private float maxSteerAngle;
    [SerializeField] private WheelCollider frontLeftWheelCollider;
    [SerializeField] private WheelCollider frontRightWheelCollider;
    [SerializeField] private WheelCollider rearLeftWheelCollider;
    [SerializeField] private WheelCollider rearRightWheelCollider;

    [SerializeField] private Transform frontLeftWheelTransform;
    [SerializeField] private Transform frontRightWheelTransform;
    [SerializeField] private Transform rearLeftWheelTransform;
    [SerializeField] private Transform rearRightWheelTransform;


    
    public Vector3 com;
    public Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.centerOfMass = com;
    }
    private void FixedUpdate() {
        GetInput();
        HandleMotor();
        HandleSteering();
        UpdateWheels();
    }

    private void GetInput()
    {
        HorizontalInput = Input.GetAxis(HORIZONTAL);
        VerticalInput = Input.GetAxis(VERTICAL);
        isBreaking = Input.GetKey(KeyCode.Space);
        isNitroOn = Input.GetKey(KeyCode.LeftShift);
    }

    private void HandleMotor()
    {
        frontLeftWheelCollider.motorTorque = VerticalInput * motorForce * 10;
        frontRightWheelCollider.motorTorque = VerticalInput * motorForce * 10;
        currentbreakForce = isBreaking ? breakForce : 0f;
        currentNitroForce = isNitroOn ? nitroForce : 0f;
        ApplyBreaking(); 
        //ApplyNitrous(); 
    }

    private void ApplyNitrous()
    {
        frontRightWheelCollider.motorTorque =  currentNitroForce;
        frontLeftWheelCollider.motorTorque = currentNitroForce;
        rearLeftWheelCollider.motorTorque =  currentNitroForce;
        rearRightWheelCollider.motorTorque =   currentNitroForce;
    }
    private void ApplyBreaking()
    {
        frontRightWheelCollider.brakeTorque = currentbreakForce;
        frontLeftWheelCollider.brakeTorque = currentbreakForce;
        rearLeftWheelCollider.brakeTorque = currentbreakForce;
        rearRightWheelCollider.brakeTorque = currentbreakForce;
    }

    private void HandleSteering()
    {
        steerAngle = maxSteerAngle * HorizontalInput;
        frontRightWheelCollider.steerAngle = steerAngle;
        frontLeftWheelCollider.steerAngle = steerAngle;        
    }
    
    private void UpdateWheels()
    {
        UpdateSingleWheel(frontLeftWheelCollider, frontLeftWheelTransform);
        UpdateSingleWheel(frontRightWheelCollider, frontRightWheelTransform);
        UpdateSingleWheel(rearLeftWheelCollider, rearLeftWheelTransform);
        UpdateSingleWheel(rearRightWheelCollider, rearRightWheelTransform);
    
    }

    private void UpdateSingleWheel(WheelCollider wheelCollider, Transform wheelTransform)
    {
        Vector3 pos;
        Quaternion rot;
        wheelCollider.GetWorldPose(out pos, out rot);
        wheelTransform.rotation = rot;
        wheelTransform.position = pos;
   
    }
}