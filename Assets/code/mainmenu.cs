using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    [Header("Main Menu Buttons")]
    public Button playButton;
    public Button optionButton;
    public Button creditButton; 
    public Button exitButton;

    [Header("Target Scene Names")]
    // Nama scene harus sesuai dengan yang ada di Build Settings
    public string playTargetScene = "Category";       
    public string settingsTargetScene = "settings";   
    public string creditTargetScene = "SampleScene"; // Ganti jika sudah ada scene credit
    public string extraTargetScene = "lvlmenuipa";    

    private void Start()
    {
        // Hubungkan fungsi ke tombol
        if (playButton != null) playButton.onClick.AddListener(PlayGame);
        if (optionButton != null) optionButton.onClick.AddListener(LoadSettingsScene);
        if (creditButton != null) creditButton.onClick.AddListener(LoadCredits);
        if (exitButton != null) exitButton.onClick.AddListener(QuitGame);
    }

    // 1. Pindah ke scene Category
    public void PlayGame() 
    { 
        SceneManager.LoadScene(playTargetScene); 
    }

    // 2. Sekarang Option langsung pindah Scene (bukan buka popup)
    public void LoadSettingsScene()
    {
        SceneManager.LoadScene(settingsTargetScene);
    }

    // 3. Pindah ke Credits
    public void LoadCredits()
    {
        SceneManager.LoadScene(creditTargetScene); 
    }

    // 4. Keluar Game
    public void QuitGame() 
    { 
        Debug.Log("Game Exited"); // Muncul di console saat testing
        Application.Quit(); 
    }
}