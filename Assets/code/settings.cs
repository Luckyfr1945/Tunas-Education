using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class settings : MonoBehaviour
{
    [Header("Isi Konten Panel")]
    public GameObject soundPanel;
    public GameObject graphicPanel;

    [Header("Tombol")]
    public Button soundTabButton;
    public Button graphicTabButton;
    public Button exitButton;

    [Header("Warna Tombol")]
    public Color activeColor = Color.white;    
    public Color inactiveColor = Color.gray;   

    [Header("Pengaturan Suara")]
    public Slider sfxSlider;
    // Variabel Sfx Audio Source dihapus karena sekarang otomatis dicari lewat radar

    private void Start()
    {
        if (soundTabButton != null) soundTabButton.onClick.AddListener(ShowSoundSettings);
        if (graphicTabButton != null) graphicTabButton.onClick.AddListener(ShowGraphicSettings);
        if (exitButton != null) exitButton.onClick.AddListener(BackToMainMenu);

        ShowSoundSettings(); 

        if (sfxSlider != null)
        {
            float savedVolume = PlayerPrefs.GetFloat("SFX_Volume", 100f);
            sfxSlider.value = savedVolume; 
            sfxSlider.onValueChanged.AddListener(SetSFXVolume);
        }
    }

    public void BackToMainMenu()
    {
        SceneManager.LoadScene("mainmenu"); 
    }

    public void SetSFXVolume(float value)
    {
        PlayerPrefs.SetFloat("SFX_Volume", value);
        PlayerPrefs.Save(); 

        // Radar pencari: Cari objek MusicManager di scene manapun, lalu ubah volumenya
        MusicManager music = FindObjectOfType<MusicManager>();
        if (music != null)
        {
            music.UbahVolume(value);
        }
    }

    public void ShowSoundSettings()
    {
        if (soundPanel != null) soundPanel.SetActive(true);
        if (graphicPanel != null) graphicPanel.SetActive(false);
        SetButtonVisual(soundTabButton, true);
        SetButtonVisual(graphicTabButton, false);
    }

    public void ShowGraphicSettings()
    {
        if (soundPanel != null) soundPanel.SetActive(false);
        if (graphicPanel != null) graphicPanel.SetActive(true);
        SetButtonVisual(soundTabButton, false);
        SetButtonVisual(graphicTabButton, true);
    }

    private void SetButtonVisual(Button btn, bool isActive)
    {
        if (btn != null && btn.GetComponent<Image>() != null)
        {
            btn.GetComponent<Image>().color = isActive ? activeColor : inactiveColor;
        }
    }
}
