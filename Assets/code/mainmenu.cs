using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Collections; // Dibutuhkan untuk Coroutine

public class MainMenu : MonoBehaviour
{
    [Header("Menu Buttons")]
    public Button playButton;
    public Button optionButton; // Tambah tombol Option/Settings
    public Button exitButton;

    [Header("Settings Popup")]
    public GameObject settingsPanel; 
    public Button closeSettingsButton; // Tombol exit di dalam panel

    [Header("Settings")]
    public string sceneToLoad = "GameScene";

    private void Start()
    {
        if (playButton != null) playButton.onClick.AddListener(PlayGame);
        if (exitButton != null) exitButton.onClick.AddListener(QuitGame);
        
        // Listener baru untuk Settings
        if (optionButton != null) optionButton.onClick.AddListener(OpenSettings);
        if (closeSettingsButton != null) closeSettingsButton.onClick.AddListener(CloseSettings);

        // Sembunyikan panel di awal
        if (settingsPanel != null) settingsPanel.SetActive(false);
    }

    public void OpenSettings()
    {
        if (settingsPanel != null)
        {
            settingsPanel.SetActive(true); // Aktifkan dulu biar animasinya jalan
            Animator anim = settingsPanel.GetComponent<Animator>();
            if (anim != null) anim.SetTrigger("Open");
        }
    }

    public void CloseSettings()
    {
        if (settingsPanel != null)
        {
            Animator anim = settingsPanel.GetComponent<Animator>();
            if (anim != null)
            {
                anim.SetTrigger("Close");
                // Tunggu 0.5 detik (sesuai durasi animasi kamu) baru hilangkan object
                StartCoroutine(WaitAndDisable(0.5f)); 
            }
            else
            {
                settingsPanel.SetActive(false);
            }
        }
    }

    private IEnumerator WaitAndDisable(float delay)
    {
        yield return new WaitForSeconds(delay);
        settingsPanel.SetActive(false); // Akhirnya object hilang setelah animasi
    }

    // Fungsi PlayGame dan QuitGame tetap sama...
    public void PlayGame() { SceneManager.LoadScene(sceneToLoad); }
    public void QuitGame() { Application.Quit(); }
}
