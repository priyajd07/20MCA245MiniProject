using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIController : MonoBehaviour
{

[SerializeField]
List<RenderTexture> renderTextures;

[SerializeField]
RawImage miniMapImage;

[SerializeField]
TMPro.TextMeshProUGUI mphText;

[SerializeField]
TMPro.TextMeshProUGUI timerText;

public float totalTime;

public void HandleShowMiniMap(Camera miniMapCamera)
{
    miniMapCamera.targetTexture = renderTextures [ GameState.levelIndex];
    miniMapImage.texture = renderTextures [ GameState.levelIndex ];
}

public void HandleShowMPHText(double mph)
{
    mphText.text = mph + " MPH";
}
void Update()
{
    if(!GameState.isRaceMode)
    {
        return;
    }    
    totalTime += Time.deltaTime;
    int minutes = (int) totalTime/60;
    int seconds = (int) totalTime % 60;

    timerText.text = string.Format("Total Time : {0} : {1}", minutes.ToString("00"), seconds.ToString("00"));
}

}
