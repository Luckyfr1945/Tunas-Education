using UnityEngine;
using TMPro; 
using UnityEngine.SceneManagement;
using System.Collections.Generic; // Wajib ada untuk sistem List Bank Soal

public class GameplayManager : MonoBehaviour
{
    [Header("Bank Soal (Masukkan Banyak File Soal Kesini)")]
    public DataSoal[] kumpulanSoal; 
    
    // Variabel penyimpanan ditaruh di DALAM class
    private DataSoal soalSaatIni; 
    private int levelAktif;
    private int indexSoalTerpilih; 

    [Header("UI Teks")]
    public TMP_Text teksPertanyaan;
    public TMP_Text[] teksPilihanJawaban; 

    [Header("Komponen Timer")]
    public TimerBar scriptTimer; 

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

    // --- FUNGSI MENCARI SOAL ---
    private void PilihSoalRandom()
    {
        if (kumpulanSoal.Length == 0)
        {
            Debug.LogError("Bank Soal kosong!");
            return;
        }

        // Cek apakah level ini sudah pernah dimenangkan sebelumnya
        int soalTersimpan = PlayerPrefs.GetInt("Level_" + levelAktif + "_Soal", -1);

        if (soalTersimpan != -1)
        {
            // Kalau SUDAH PERNAH MENANG: Munculkan pertanyaan yang SAMA PERSIS
            Debug.Log("Level ini sudah tamat. Memuat soal lama...");
            indexSoalTerpilih = soalTersimpan;
            soalSaatIni = kumpulanSoal[indexSoalTerpilih];
        }
        else
        {
            // Kalau BELUM PERNAH MENANG: Cari soal acak yang belum terpakai
            Debug.Log("Level baru. Mencari soal acak yang belum terpakai...");
            
            List<int> soalBelumTerpakai = new List<int>();

            for (int i = 0; i < kumpulanSoal.Length; i++)
            {
                bool sudahDipakai = false;
                
                // Cek 20 level
                for (int lvl = 1; lvl <= 20; lvl++) 
                {
                    if (PlayerPrefs.GetInt("Level_" + lvl + "_Soal", -1) == i)
                    {
                        sudahDipakai = true;
                        break;
                    }
                }

                if (!sudahDipakai)
                {
                    soalBelumTerpakai.Add(i);
                }
            }

            // Pilih acak dari daftar yang belum terpakai
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

        if (scriptTimer != null) scriptTimer.ResetTimer();
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

    // --- FUNGSI MENANG ---
    private void Menang()
    {
        Debug.Log("Jawaban Benar!");
        isGameSelesai = true;
        panelMenang.SetActive(true);

        // Saat menang, kunci soal ini permanen ke level yang sedang dimainkan
        PlayerPrefs.SetInt("Level_" + levelAktif + "_Soal", indexSoalTerpilih);
        PlayerPrefs.Save();
    }

    private void Kalah(string pesan)
    {
        isGameSelesai = true;
        if(scriptTimer != null) scriptTimer.enabled = false; 
        panelKalah.SetActive(true);
    }

    // --- FUNGSI TOMBOL ---
    public void PauseGame()
    {
        if (isGameSelesai) return; 
        panelPause.SetActive(true);
        Time.timeScale = 0f; 
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