using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class CategoryMenu : MonoBehaviour
{
    [Header("Category Buttons")]
    public Button ipaButton;
    public Button mathButton;
    public Button sarkasmeButton;

    [Header("Scene Names")]
    public string ipaScene = "lvlmenuipa";
    public string mathScene = "lvlmenumath";
    public string sarkasmeScene = "lvlmenusarkas";

    private void Start()
    {
        if (ipaButton != null)
            ipaButton.onClick.AddListener(() => LoadCategory(ipaScene));

        if (mathButton != null)
            mathButton.onClick.AddListener(() => LoadCategory(mathScene));

        if (sarkasmeButton != null)
            sarkasmeButton.onClick.AddListener(() => LoadCategory(sarkasmeScene));
    }

    void LoadCategory(string sceneName)
    {
        SceneManager.LoadScene(sceneName);
    }

    public string mainMenuScene = "MainMenu";

    public void ExitToMainMenu()
    {
        SceneManager.LoadScene(mainMenuScene);
    }
}