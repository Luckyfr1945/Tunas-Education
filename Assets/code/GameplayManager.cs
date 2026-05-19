using UnityEngine;
using TMPro; 
using UnityEngine.SceneManagement;
using System.Collections.Generic; 

public class GameplayManager : MonoBehaviour
{
    [Header("Bank Soal (Masukkan Banyak File Soal Kesini)")]
    public DataSoal[] kumpulanSoal; 
    
    private DataSoal soalSaatIni; 
    private int levelAktif;
    private int indexSoalTerpilih; 

    [Header("UI Teks")]
    public TMP_Text teksPertanyaan;
    public TMP_Text[] teksPilihanJawaban; 

    [Header("Komponen Timer")]
    public TimerBar scriptTimer; 

    [Header("Pengaturan Kesulitan Waktu")]
    [Tooltip("Waktu standar untuk level 1-5 (dalam detik)")]
    public float waktuDasar = 30f; 
    [Tooltip("Berapa detik waktu akan dikurangi setiap naik 5 level?")]
    public float potonganWaktu = 5f; 

    [Header("UI Panel")]
    public GameObject panelMenang;
    public GameObject panelKalah;
    public GameObject panelPause; 

    private bool isGameSelesai = false; 

    private void Start()
    {
        Time.timeScale = 1f; 
        levelAktif = PlayerPrefs.GetInt("LevelAktif", 1);

        panelMenang.SetActive(false);
        panelKalah.SetActive(false);
        if(panelPause != null) panelPause.SetActive(false);
        
        isGameSelesai = false;
        PilihSoalRandom();
    }

    private void Update()
    {
        if (!isGameSelesai && scriptTimer != null && scriptTimer.timerSlider.value <= 0f)
        {
            Kalah("Waktu Habis coy!");
        }
    }

    private void PilihSoalRandom()
    {
        if (kumpulanSoal.Length == 0)
        {
            Debug.LogError("Bank Soal kosong! Masukkan file DataSoal ke Inspector.");
            return;
        }

        int soalTersimpan = PlayerPrefs.GetInt("Level_" + levelAktif + "_Soal", -1);

        if (soalTersimpan != -1)
        {
            Debug.Log("Level ini sudah tamat. Memuat soal lama...");
            indexSoalTerpilih = soalTersimpan;
            soalSaatIni = kumpulanSoal[indexSoalTerpilih];
        }
        else
        {
            Debug.Log("Level baru atau belum tamat. Mencari soal acak yang belum terpakai...");
            List<int> soalBelumTerpakai = new List<int>();

            for (int i = 0; i < kumpulanSoal.Length; i++)
            {
                bool sudahDipakai = false;
                for (int lvl = 1; lvl <= 20; lvl++) 
                {
                    if (PlayerPrefs.GetInt("Level_" + lvl + "_Soal", -1) == i)
                    {
                        sudahDipakai = true;
                        break;
                    }
                }
                if (!sudahDipakai) soalBelumTerpakai.Add(i);
            }

            if (soalBelumTerpakai.Count > 0)
            {
                int acak = Random.Range(0, soalBelumTerpakai.Count);
                indexSoalTerpilih = soalBelumTerpakai[acak];
                soalSaatIni = kumpulanSoal[indexSoalTerpilih];
            }
            else
            {
                Debug.LogWarning("Bank soal habis! Mengambil soal acak biasa.");
                indexSoalTerpilih = Random.Range(0, kumpulanSoal.Length);
                soalSaatIni = kumpulanSoal[indexSoalTerpilih];
            }
        }

        TampilkanSoal();
    }

    private void TampilkanSoal()
    {
        teksPertanyaan.text = soalSaatIni.teksPertanyaan;
        for (int i = 0; i < teksPilihanJawaban.Length; i++)
        {
            teksPilihanJawaban[i].text = soalSaatIni.pilihanJawaban[i];
        }

        if (scriptTimer != null) 
        {
            // --- LOGIKA WAKTU SEMAKIN CEPAT ---
            // Hitung tingkat kesulitan (0 untuk lvl 1-5, 1 untuk 6-10, 2 untuk 11-15, dst)
            int kelipatanKesulitan = (levelAktif - 1) / 5;
            
            // Kurangi waktu dasar dengan potongan waktu
            float waktuLevelIni = waktuDasar - (kelipatanKesulitan * potonganWaktu);

            // Jaga-jaga biar waktunya gak sampai minus atau 0 (minimal 5 detik)
            if (waktuLevelIni < 5f) waktuLevelIni = 5f;

            // MENGIRIM WAKTU BARU KE SCRIPT TIMER
            // ⚠️ PENTING: Ganti kata "waktuMaksimal" di bawah ini dengan nama variabel asli yang ada di script TimerBar.cs milikmu!
            scriptTimer.maxTime = waktuLevelIni;

            scriptTimer.ResetTimer();
        }
    }

    public void CekJawaban(int indeksPilihan)
    {
        if (isGameSelesai) return; 
        scriptTimer.enabled = false; 

        if (indeksPilihan == soalSaatIni.indeksJawabanBenar)
        {
            Menang();
        }
        else
        {
            Kalah("Yah, Jawaban Salah!");
        }
    }

    private void Menang()
    {
        isGameSelesai = true;
        panelMenang.SetActive(true);
        PlayerPrefs.SetInt("Level_" + levelAktif + "_Soal", indexSoalTerpilih);
        PlayerPrefs.Save();
    }

    private void Kalah(string pesan)
    {
        isGameSelesai = true;
        if(scriptTimer != null) scriptTimer.enabled = false; 
        if (panelPause != null) panelPause.SetActive(false);
        panelKalah.SetActive(true);
    }

    public void PauseGame()
    {
        if (isGameSelesai) return; 
        panelPause.SetActive(true);
    }

    public void LanjutGame()
    {
        panelPause.SetActive(false);
        Time.timeScale = 1f; 
    }

    public void UlangiLevel()
    {
        Time.timeScale = 1f; 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void KeMenuUtama()
    {
        Time.timeScale = 1f; 
        SceneManager.LoadScene("Category"); 
    }

    public void LanjutLevelBerikutnya()
    {
        int levelBaru = levelAktif + 1;
        PlayerPrefs.SetInt("LevelAktif", levelBaru);
        PlayerPrefs.Save();
        
        Time.timeScale = 1f; 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}