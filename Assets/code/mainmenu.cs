using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    [Header("Menu Buttons")]
    public Button playButton;
    public Button exitButton;

    [Header("Settings")]
    public string sceneToLoad = "GameScene";

    private void Start()
    {
        // Memastikan tombol sudah di-assign sebelum menambah listener
        if (playButton != null)
        {
            playButton.onClick.AddListener(PlayGame);
        }
            
        if (exitButton != null)
        {
            exitButton.onClick.AddListener(QuitGame);
        }
    }

    public void PlayGame()
    {
        // Pindah ke scene yang ditentukan (pastikan nama scene sama dengan di Build Settings)
        Debug.Log("Pindah ke scene: " + sceneToLoad);
        SceneManager.LoadScene(sceneToLoad);
    }

    public void QuitGame()
    {
        // Keluar dari aplikasi
        Debug.Log("Keluar dari aplikasi...");
        Application.Quit();

        // Tambahan khusus agar tombol Quit berfungsi saat di test di dalam Editor Unity
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #endif
    }
}
