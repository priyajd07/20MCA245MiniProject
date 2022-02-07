using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
public class RaceManager : MonoBehaviour
{

[SerializeField]
UIController uiController;

Car_controller carController;

public List<GameObject> carsOnTrack;
void Awake() 
{
    GameObject playerCar = carsOnTrack[GameState.playerCar];
    if(carController != null)
    {
        uiController.HandleShowMiniMap(carController.miniMapCamera);
        carController.MPH += uiController.HandleShowMPHText;
    }    
}

void OnDestroy() 
{
    if(carController != null)
    {
        carController.MPH -= uiController.HandleShowMPHText;
    }    
}

}
