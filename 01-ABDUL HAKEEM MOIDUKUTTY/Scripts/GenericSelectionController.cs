using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;


public class GenericSelectionController : MonoBehaviour
{
    
[SerializeField]
List<GameObject> objects;

[SerializeField]
Button forwardButton;

[SerializeField]
Button backButton;
[SerializeField]
Button backToMenuButton;
GameObject currentObject;
int index = 0;

void Awake() {
    SetCurrentObject();
    forwardButton.onClick.AddListener(HandleForwardButtonClicked);
    backButton.onClick.AddListener(HandleBackButtonClicked);
    backToMenuButton.onClick.AddListener(HandleBackToMenuButtonClicked);
}
void OnDestroy() {
    forwardButton.onClick.RemoveListener(HandleForwardButtonClicked);
    backButton.onClick.RemoveListener(HandleBackButtonClicked);
    backToMenuButton.onClick.RemoveListener(HandleBackToMenuButtonClicked);
}

void HandleForwardButtonClicked()
{
    index = (index + 1 < objects.Count) ? index + 1 : 0;
    currentObject = objects[index];
    SetCurrentObject(); 
}

void HandleBackButtonClicked()
{
    index = (index -1 > -1) ? index - 1  : objects.Count -1;
    currentObject = objects[index];
    SetCurrentObject();
}

void SetCurrentObject()
{
    foreach(GameObject obj in objects)
    {
        obj.SetActive(false);
    }
    currentObject = objects[index];
    currentObject.SetActive(true);

    GameState.levelIndex = index;
}
void HandleBackToMenuButtonClicked()
{
    SceneManager.LoadSceneAsync("MainMenu");
}
}
