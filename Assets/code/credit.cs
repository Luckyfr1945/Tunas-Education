using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class credit : MonoBehaviour
{

    [Header("Tombol")]
    public Button exitButton; 

    private void Start()
    {
        if (exitButton != null) exitButton.onClick.AddListener(BackToMainMenu);
 
    }

    public void BackToMainMenu()
    {
        SceneManager.LoadScene("mainmenu"); 
    }

}
