using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelMenu : MonoBehaviour
{
    public string categoryScene = "Category";

    public void BackToCategory()
    {
        SceneManager.LoadScene(categoryScene);
    }
}