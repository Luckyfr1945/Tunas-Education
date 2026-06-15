using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

public class MenuButtonAnimator : MonoBehaviour
{
    [Header("Masukkan Tombol Disini")]
    public Button playButton;
    public Button optionButton;
    public Button creditButton;
    public Button exitButton;

    [Space(10)] // Jarak di Inspector
    public Button igButton;
    public Button tiktokButton;

    [Header("Pengaturan Animasi Ukuran")]
    public Vector3 hoverScale = new Vector3(1.1f, 1.1f, 1f); // Ukuran membesar 10%
    public float animSpeed = 10f; // Kecepatan efek

    [Header("Pengaturan Warna (Hanya Tombol Utama)")]
    // Contoh warna, bisa kamu ubah di Inspector
    public Color normalColor = Color.white;    // Warna saat diam (misal putih biasa)
    public Color highlightColor = Color.yellow; // Warna saat kursor diatas/dipilih (misal kuning)

    private void Start()
    {
        // --- 1. SETUP TOMBOL UTAMA (Pakai Animasi Ukuran DAN Warna) ---
        SetupButtonAnimation(playButton, true);
        SetupButtonAnimation(optionButton, true);
        SetupButtonAnimation(creditButton, true);
        SetupButtonAnimation(exitButton, true);

        // --- 2. SETUP TOMBOL SOSMED (Hanya Animasi Ukuran, Tanpa Warna) ---
        SetupButtonAnimation(igButton, false);
        SetupButtonAnimation(tiktokButton, false);
    }

    // Fungsi setup yang diperbarui, sekarang menerima bool 'useColor'
    private void SetupButtonAnimation(Button btn, bool useColor)
    {
        if (btn != null)
        {
            // Ambil component Image di tombol untuk mengubah warnanya nanti
            Image btnImage = btn.GetComponent<Image>();
            if (btnImage == null)
            {
                Debug.LogWarning("Tombol " + btn.name + " tidak punya komponen Image. Efek warna tidak akan bekerja.");
                // Jika tidak ada Image, paksa useColor jadi false
                useColor = false; 
            }

            // Otomatis menambahkan script "ButtonHoverHelper"
            ButtonHoverHelper helper = btn.gameObject.AddComponent<ButtonHoverHelper>();
            
            // Masukkan pengaturan ke script Helper
            helper.hoverScale = this.hoverScale;
            helper.animSpeed = this.animSpeed;
            
            // Beritahu helper apakah harus mengubah warna atau tidak
            helper.useColorChange = useColor;
            
            if (useColor)
            {
                helper.btnImage = btnImage; // Masukkan reference Image-nya
                helper.normalColor = this.normalColor;
                helper.highlightColor = this.highlightColor;
            }
        }
    }
}

// =========================================================================
// SCRIPT HELPER (DIPERBARUI UNTUK MENANGANI WARNA)
// Biarkan saja di bawah sini.
// =========================================================================
public class ButtonHoverHelper : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, ISelectHandler, IDeselectHandler
{
    [HideInInspector] public Vector3 hoverScale;
    [HideInInspector] public float animSpeed;

    // Tambahan untuk warna
    [HideInInspector] public bool useColorChange;
    [HideInInspector] public Image btnImage;
    [HideInInspector] public Color normalColor;
    [HideInInspector] public Color highlightColor;

    private Vector3 originalScale;
    private Vector3 targetScale;

    private void Start()
    {
        originalScale = transform.localScale;
        targetScale = originalScale;

        // Set warna awal jika menggunakan fitur warna
        if (useColorChange && btnImage != null)
        {
            btnImage.color = normalColor;
        }
    }

    private void Update()
    {
        // Efek membesar/mengecil yang smooth (menggunakan unscaledDeltaTime agar tetap berjalan saat game pause)
        transform.localScale = Vector3.Lerp(transform.localScale, targetScale, Time.unscaledDeltaTime * animSpeed);
    }

    // --- KETIKA CURSOR MASUK / DIPILIH PANAH ---
    public void OnPointerEnter(PointerEventData eventData) { ActivateHighlight(); }
    public void OnSelect(BaseEventData eventData) { ActivateHighlight(); }

    // --- KETIKA CURSOR KELUAR / PINDAH PILIHAN ---
    public void OnPointerExit(PointerEventData eventData) { DeactivateHighlight(); }
    public void OnDeselect(BaseEventData eventData) { DeactivateHighlight(); }


    private void ActivateHighlight()
    {
        targetScale = hoverScale;
        // Hanya ganti warna jika useColorChange true
        if (useColorChange && btnImage != null)
        {
            btnImage.color = highlightColor;
        }
    }

    private void DeactivateHighlight()
    {
        targetScale = originalScale;
        // Hanya ganti warna jika useColorChange true
        if (useColorChange && btnImage != null)
        {
            btnImage.color = normalColor;
        }
    }
}