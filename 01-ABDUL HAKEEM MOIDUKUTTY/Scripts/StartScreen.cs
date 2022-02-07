using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
public class StartScreen : MonoBehaviour
{
    [SerializeField]
    Button startButton;

    void Awake() {
        startButton.onClick.AddListener(LoadMainMenu);
    }
    //removing the listeners after use or when not need helps in freeing up space
    void OnDestroy() {
        startButton.onClick.RemoveListener(LoadMainMenu);
    }

    void LoadMainMenu(){
        SceneManager.LoadSceneAsync("MainMenu");
    }
}
