using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    [Header("UI Panels & Animation Settings")]
    public RectTransform menuPanel; // Masukkan panel hitam yang berisi tombol Play dll ke sini
    public Vector2 hiddenPosition = new Vector2(-500, 0); // Posisi panel saat di luar layar (kiri)
    public Vector2 visiblePosition = new Vector2(0, 0);   // Posisi panel saat tampil di layar
    public float animationSpeed = 0.4f; // Kecepatan animasi (detik)

    [Header("Main Menu Buttons")]
    public Button playButton;
    public Button optionButton;
    public Button creditButton; 
    public Button exitButton;

    [Header("Social Media Buttons")]
    public Button igButton;
    public Button tiktokButton;

    [Header("Target Scene Names")]
    public string playTargetScene = "Category";       
    public string settingsTargetScene = "settings";   
    public string creditTargetScene = "SampleScene"; 
    public string extraTargetScene = "lvlmenuipa";    

    private void Start()
    {
        // Hubungkan fungsi ke tombol utama
        if (playButton != null) playButton.onClick.AddListener(PlayGame);
        if (optionButton != null) optionButton.onClick.AddListener(LoadSettingsScene);
        if (creditButton != null) creditButton.onClick.AddListener(LoadCredits);
        if (exitButton != null) exitButton.onClick.AddListener(QuitGame);

        // Hubungkan fungsi ke tombol sosmed
        if (igButton != null) igButton.onClick.AddListener(OpenInstagram);
        if (tiktokButton != null) tiktokButton.onClick.AddListener(OpenTikTok);

        // --- MENGGANTIKAN ANIMATOR ---
        // Posisikan panel di luar layar dulu saat mulai, lalu luncurkan animasi masuk
        if (menuPanel != null)
        {
            menuPanel.anchoredPosition = hiddenPosition;
            StartCoroutine(SlidePanel(menuPanel, hiddenPosition, visiblePosition, animationSpeed));
        }
    }

    // --- FUNGSI ANIMASI UI (TANPA ANIMATOR) ---
    private IEnumerator SlidePanel(RectTransform panel, Vector2 startPos, Vector2 endPos, float duration)
    {
        float timeElapsed = 0;
        while (timeElapsed < duration)
        {
            // Bergerak mulus dari startPos ke endPos
            panel.anchoredPosition = Vector2.Lerp(startPos, endPos, timeElapsed / duration);
            timeElapsed += Time.deltaTime;
            yield return null;
        }
        // Pastikan posisi akhirnya pas
        panel.anchoredPosition = endPos;
    }

    // --- FUNGSI PINDAH SCENE ---
    public void PlayGame() 
    { 
        SceneManager.LoadScene(playTargetScene); 
    }

    public void LoadSettingsScene()
    {
        SceneManager.LoadScene(settingsTargetScene);
    }

    public void LoadCredits()
    {
        SceneManager.LoadScene(creditTargetScene); 
    }

    public void QuitGame() 
    { 
        Debug.Log("Game Exited"); 
        Application.Quit(); 
    }

    // --- FUNGSI SOSIAL MEDIA ---
    public void OpenInstagram()
    {
        Debug.Log("Buka IG");
        Application.OpenURL("https://instagram.com/usernamekamu"); // Ganti linknya
    }

    public void OpenTikTok()
    {
        Debug.Log("Buka TikTok");
        Application.OpenURL("https://tiktok.com/@usernamekamu"); // Ganti linknya
    }
}