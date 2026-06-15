using UnityEngine;
using UnityEngine.SceneManagement;

public class MusicManager : MonoBehaviour
{
    private static MusicManager instance;
    private AudioSource audioSource;

    [Header("Songs List")]
    [Tooltip("Masukkan 2 lagu untuk Main Menu / Level Menu")]
    public AudioClip[] menuSongs;
    [Tooltip("Masukkan 2 lagu untuk Gameplay")]
    public AudioClip[] gameplaySongs;

    private bool isGameplayScene = false;

    void Awake()
    {
        // Mencegah lagu menumpuk dobel saat kamu bolak-balik antar scene
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject); // Objek abadi menembus scene!
        }
        else
        {
            Destroy(gameObject); // Hancurkan kembarannya jika sudah ada yang menyala
            return;
        }
    }

    void Start()
    {
        // Hindari inisialisasi pada instance duplikat yang akan dihancurkan
        if (instance != this) return;

        audioSource = GetComponent<AudioSource>();
        if (audioSource != null)
        {
            float savedVolume = PlayerPrefs.GetFloat("SFX_Volume", 100f);
            audioSource.volume = savedVolume / 100f;
        }

        // Daftarkan listener untuk mendeteksi transisi scene
        SceneManager.sceneLoaded += OnSceneLoaded;

        // Jalankan pengecekan lagu untuk scene awal
        CheckAndPlayMusic(SceneManager.GetActiveScene().name);
    }

    private void OnDestroy()
    {
        if (instance == this)
        {
            SceneManager.sceneLoaded -= OnSceneLoaded;
        }
    }

    private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
    {
        if (instance == this)
        {
            CheckAndPlayMusic(scene.name);
        }
    }

    private void CheckAndPlayMusic(string sceneName)
    {
        if (audioSource == null) return;

        // Deteksi apakah scene saat ini adalah gameplay
        bool newIsGameplay = sceneName.ToLower().Contains("gameplay");

        // Jika berganti tipe scene (Menu <-> Gameplay) ATAU tidak ada musik menyala, mainkan musik baru
        if (newIsGameplay != isGameplayScene || !audioSource.isPlaying)
        {
            isGameplayScene = newIsGameplay;
            PlayCategoryMusic();
        }
    }

    private void PlayCategoryMusic()
    {
        AudioClip[] targetPool = isGameplayScene ? gameplaySongs : menuSongs;

        if (targetPool == null || targetPool.Length == 0)
        {
            // Fallback: Jika pool lagu kosong di Inspector, mainkan lagu default AudioSource jika ada
            if (audioSource.clip != null && !audioSource.isPlaying)
            {
                audioSource.Play();
            }
            return;
        }

        // Pilih lagu secara acak dari pool yang sesuai
        int randomIndex = Random.Range(0, targetPool.Length);
        AudioClip selectedClip = targetPool[randomIndex];

        // Hanya ganti lagu jika klip yang terpilih berbeda dengan lagu yang sedang berjalan
        if (selectedClip != null && selectedClip != audioSource.clip)
        {
            audioSource.clip = selectedClip;
            audioSource.loop = true;
            audioSource.Play();
        }
        else if (selectedClip != null && !audioSource.isPlaying)
        {
            audioSource.Play();
        }
    }

    // Fungsi tambahan agar slider bisa mengontrol volumenya dari scene manapun
    public void UbahVolume(float value)
    {
        if (audioSource == null) audioSource = GetComponent<AudioSource>();
        if (audioSource != null)
        {
            audioSource.volume = value / 100f;
        }
    }
}
