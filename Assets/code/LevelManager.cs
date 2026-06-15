using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class LevelSelection : MonoBehaviour
{
    [Header("Identitas Kategori (WAJIB BEDA TIAP SCENE)")]
    [Tooltip("Ketik: IPA, MATH, atau SARKASME")]
    public string kodeKategori = "IPA"; 

    [Header("Pengaturan Scene")]
    public string namaSceneGameplay = "gameplay_ipa"; 
    public string namaSceneKembali = "Category"; 

    [Header("Validasi Visual Level")]
    public Button[] arrayTombolLevel; 
    
    [Tooltip("Masukkan objek gembok ke sini. Atur Size jadi 20. Untuk Element 0 (Level 1) biarkan kosong.")]
    public GameObject[] arrayGembok; 
    
    [Tooltip("Warna untuk level yang sudah diselesaikan (Abu-abu / Hitam)")]
    public Color warnaSelesai = new Color32(80, 80, 80, 255); 
    [Tooltip("Warna untuk level aktif dan terkunci (Warna asli tombol)")]
    public Color warnaBelum = Color.white; 

    private void Start()
    {
        // Deteksi kategori otomatis dari nama scene
        string sceneName = SceneManager.GetActiveScene().name.ToLower();
        if (sceneName.Contains("ipa")) kodeKategori = "IPA";
        else if (sceneName.Contains("math")) kodeKategori = "MATH";
        else if (sceneName.Contains("sarkas")) kodeKategori = "SARKAS";

        CekStatusLevel();
    }

    private void CekStatusLevel()
    {
        if (arrayTombolLevel == null || arrayTombolLevel.Length == 0) return;

        // 1. Cari tahu level aktif tertinggi (level pertama yang belum diselesaikan)
        int levelAktifTertinggi = 1;
        for (int i = 1; i <= arrayTombolLevel.Length; i++)
        {
            // Cek apakah level ini sudah ada di riwayat memori (selesai)
            if (PlayerPrefs.GetInt(kodeKategori + "_Level_" + i + "_Soal", -1) != -1)
            {
                levelAktifTertinggi = i + 1; // Jika level selesai, buka akses ke level berikutnya
            }
            else
            {
                break; // Hentikan pengecekan di level pertama yang belum diselesaikan
            }
        }

        // 2. Terapkan visual ke tombol dan gembok sesuai 3 logika utama secara berurutan
        for (int i = 0; i < arrayTombolLevel.Length; i++)
        {
            int nomorLevel = i + 1; 

            // Ambil referensi objek gembok untuk level ini (jika ada)
            GameObject gembokLevelIni = (arrayGembok != null && i < arrayGembok.Length) ? arrayGembok[i] : null;

            if (nomorLevel < levelAktifTertinggi)
            {
                // LOGIKA 1: SUDAH SELESAI (Hitam/Abu-abu, Gembok Hilang, Ga bisa diklik)
                arrayTombolLevel[i].image.color = warnaSelesai;
                arrayTombolLevel[i].interactable = false;
                if (gembokLevelIni != null) gembokLevelIni.SetActive(false);
            }
            else if (nomorLevel == levelAktifTertinggi)
            {
                // LOGIKA 2: LEVEL SAAT INI / TERBARU (Warna normal, Gembok Hilang, BISA DIKLIK)
                arrayTombolLevel[i].image.color = warnaBelum;
                arrayTombolLevel[i].interactable = true;
                if (gembokLevelIni != null) gembokLevelIni.SetActive(false);
            }
            else
            {
                // LOGIKA 3: LEVEL SELANJUTNYA / TERKUNCI (Warna normal, Gembok Muncul, Ga bisa diklik)
                arrayTombolLevel[i].image.color = warnaBelum;
                arrayTombolLevel[i].interactable = false;
                if (gembokLevelIni != null) gembokLevelIni.SetActive(true);
            }
        }
    }

    public void PilihLevel(int nomorLevel)
    {
        PlayerPrefs.SetInt("LevelAktif", nomorLevel);
        PlayerPrefs.Save();
        SceneManager.LoadScene(namaSceneGameplay);
    }

    public void KembaliKeKategori()
    {
        SceneManager.LoadScene(namaSceneKembali);
    }
}