using UnityEngine;

public class MusicManager : MonoBehaviour
{
    private static MusicManager instance;
    private AudioSource audioSource;

    void Awake()
    {
        // Mencegah lagu menumpuk dobel saat kamu bolak-balik antar scene
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject); // Ini mantra agar objeknya abadi menembus scene!
        }
        else
        {
            Destroy(gameObject); // Hancurkan kembarannya jika sudah ada yang menyala
            return;
        }
    }

    void Start()
    {
        // Otomatis atur volume saat game baru dibuka
        audioSource = GetComponent<AudioSource>();
        if (audioSource != null)
        {
            float savedVolume = PlayerPrefs.GetFloat("SFX_Volume", 100f);
            audioSource.volume = savedVolume / 100f;
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
