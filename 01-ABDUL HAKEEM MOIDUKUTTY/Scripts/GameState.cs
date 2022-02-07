using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameState : MonoBehaviour
{
   public static int playerCar = 0;
   public static int levelIndex = 0;
   public static bool canMove = false;

   public static bool isRaceMode = false;

   public const string car1 = "Car1";
   public const string car2 = "Car2";
   public const string car3 = "Car3";
   public const string car4 = "Car4";
   public const string car5 = "Car5";

    void Awake() {
       DontDestroyOnLoad(gameObject);
   }
}
