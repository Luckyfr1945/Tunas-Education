using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    [Header("UI Panels & Animation Settings")]
    public RectTransform menuPanel; // Masukkan panel yang berisi tombol Play dll ke sini
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

    [Header("Popup Are You Ready (Mode Pameran)")]
    [Tooltip("Panel popup 'Are You Ready?'")]
    public GameObject readyPopupPanel;
    [Tooltip("Tombol 'Mulai / Siap / Yes' di dalam popup")]
    public Button btnConfirmPlay;
    [Tooltip("Tombol 'Batal / Tidak / Cancel' di dalam popup")]
    public Button btnCancelPlay;

    [Header("Target Scene Names")]
    public string playTargetScene = "gameplay_ipa"; // Langsung ke scene gameplay untuk 1 kategori pameran     
    public string settingsTargetScene = "settings";   
    public string creditTargetScene = "credit"; 

    private void Start()
    {
        // Hubungkan fungsi ke tombol utama
        if (playButton != null) playButton.onClick.AddListener(OnPlayButtonClicked);
        if (optionButton != null) optionButton.onClick.AddListener(LoadSettingsScene);
        if (creditButton != null) creditButton.onClick.AddListener(LoadCredits);
        if (exitButton != null) exitButton.onClick.AddListener(QuitGame);

        // Setup Popup Are You Ready
        if (readyPopupPanel != null)
        {
            readyPopupPanel.SetActive(false);
        }

        if (btnConfirmPlay != null) btnConfirmPlay.onClick.AddListener(ConfirmPlayGame);
        if (btnCancelPlay != null) btnCancelPlay.onClick.AddListener(CancelPlayGame);

        // Animasi panel masuk
        if (menuPanel != null)
        {
            menuPanel.anchoredPosition = hiddenPosition;
            StartCoroutine(SlidePanel(menuPanel, hiddenPosition, visiblePosition, animationSpeed));
        }
    }

    private IEnumerator SlidePanel(RectTransform panel, Vector2 startPos, Vector2 endPos, float duration)
    {
        float timeElapsed = 0;
        while (timeElapsed < duration)
        {
            panel.anchoredPosition = Vector2.Lerp(startPos, endPos, timeElapsed / duration);
            timeElapsed += Time.deltaTime;
            yield return null;
        }
        panel.anchoredPosition = endPos;
    }

    // --- LOGIKA POPUP ARE YOU READY ---
    public void OnPlayButtonClicked()
    {
        if (readyPopupPanel != null)
        {
            readyPopupPanel.SetActive(true);
        }
        else
        {
            // Jika popup belum dipasang di Inspector, langsung konfirmasi mulai game
            ConfirmPlayGame();
        }
    }

    public void ConfirmPlayGame()
    {
        // Reset data pameran sebelum masuk gameplay (Level 1, Darah Penuh)
        PlayerPrefs.SetInt("LevelAktif", 1);
        PlayerPrefs.SetInt("SisaNyawa", 3);
        
        // Hapus riwayat soal lama agar pengunjung baru dapat soal acak fresh
        for (int i = 1; i <= 50; i++)
        {
            PlayerPrefs.DeleteKey("IPA_Level_" + i + "_Soal");
            PlayerPrefs.DeleteKey("MATH_Level_" + i + "_Soal");
            PlayerPrefs.DeleteKey("SARKAS_Level_" + i + "_Soal");
        }
        PlayerPrefs.Save();

        SceneManager.LoadScene(playTargetScene);
    }

    public void CancelPlayGame()
    {
        if (readyPopupPanel != null)
        {
            readyPopupPanel.SetActive(false);
        }
    }

    // --- FUNGSI PINDAH SCENE LAINNYA ---
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
}