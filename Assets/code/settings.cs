using UnityEngine;
using UnityEngine.UI;

public class MainMenu : MonoBehaviour
{
    [Header("Panels")]
    public GameObject soundPanel;
    public GameObject graphicPanel;

    [Header("Buttons")]
    public Button soundTabButton;
    public Button graphicTabButton;

    [Header("Button Colors")]
    public Color activeColor = Color.white;    // Warna saat terpilih (terang)
    public Color inactiveColor = Color.gray;   // Warna saat tidak terpilih (agak gelap)

    private void Start()
    {
        // Hubungkan klik tombol ke fungsi
        soundTabButton.onClick.AddListener(ShowSoundSettings);
        graphicTabButton.onClick.AddListener(ShowGraphicSettings);

        // Default: Masuk ke Sound Settings pertama kali
        ShowSoundSettings();
    }

    public void ShowSoundSettings()
    {
        // Switch Panel
        soundPanel.SetActive(true);
        graphicPanel.SetActive(false);

        // Visual Feedback (Warna Tombol)
        SetButtonVisual(soundTabButton, true);
        SetButtonVisual(graphicTabButton, false);

        // Jalankan animasi jika ada
        TriggerTabAnimation(soundTabButton);
    }

    public void ShowGraphicSettings()
    {
        // Switch Panel
        soundPanel.SetActive(false);
        graphicPanel.SetActive(true);

        // Visual Feedback (Warna Tombol)
        SetButtonVisual(soundTabButton, false);
        SetButtonVisual(graphicTabButton, true);

        // Jalankan animasi jika ada
        TriggerTabAnimation(graphicTabButton);
    }

    private void SetButtonVisual(Button btn, bool isActive)
    {
        // Mengubah warna Image tombol
        btn.GetComponent<Image>().color = isActive ? activeColor : inactiveColor;
    }

    private void TriggerTabAnimation(Button btn)
    {
        Animator anim = btn.GetComponent<Animator>();
        if (anim != null)
        {
            anim.SetTrigger("Selected"); // Pastikan ada trigger 'Selected' di Animator tombol
        }
    }
}