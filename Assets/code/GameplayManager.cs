using UnityEngine;
using TMPro; 
using UnityEngine.SceneManagement;
using System.Collections.Generic; 

public class GameplayManager : MonoBehaviour
{
    [Header("Identitas Kategori (WAJIB BEDA TIAP SCENE)")]
    [Tooltip("Ketik: IPA, MATH, atau SARKASME")]
    public string kodeKategori = "IPA"; 

    [Header("Bank Soal")]
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
    public float waktuDasar = 30f; 
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
        if (kumpulanSoal.Length == 0) return;

        // Cari pakai label kategori
        int soalTersimpan = PlayerPrefs.GetInt(kodeKategori + "_Level_" + levelAktif + "_Soal", -1);

        if (soalTersimpan != -1)
        {
            indexSoalTerpilih = soalTersimpan;
            soalSaatIni = kumpulanSoal[indexSoalTerpilih];
        }
        else
        {
            List<int> soalBelumTerpakai = new List<int>();

            for (int i = 0; i < kumpulanSoal.Length; i++)
            {
                bool sudahDipakai = false;
                for (int lvl = 1; lvl <= 20; lvl++) 
                {
                    // Cek kuncian soal pakai label kategori juga
                    if (PlayerPrefs.GetInt(kodeKategori + "_Level_" + lvl + "_Soal", -1) == i)
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
            int kelipatanKesulitan = (levelAktif - 1) / 5;
            float waktuLevelIni = waktuDasar - (kelipatanKesulitan * potonganWaktu);
            if (waktuLevelIni < 5f) waktuLevelIni = 5f;

            scriptTimer.maxTime = waktuLevelIni; 
            scriptTimer.ResetTimer();
        }
    }

    public void CekJawaban(int indeksPilihan)
    {
        if (isGameSelesai) return; 
        scriptTimer.enabled = false; 

        if (indeksPilihan == soalSaatIni.indeksJawabanBenar) Menang();
        else Kalah("Yah, Jawaban Salah!");
    }

    private void Menang()
    {
        isGameSelesai = true;
        panelMenang.SetActive(true);
        // Simpan kemenangan dengan label kategori
        PlayerPrefs.SetInt(kodeKategori + "_Level_" + levelAktif + "_Soal", indexSoalTerpilih);
        PlayerPrefs.Save();
    }

    private void Kalah(string pesan)
    {
        isGameSelesai = true;
        if(scriptTimer != null) scriptTimer.enabled = false; 
        if (panelPause != null) panelPause.SetActive(false);
        panelKalah.SetActive(true);
    }

    public void PauseGame() { if (!isGameSelesai) { panelPause.SetActive(true); } }
    public void LanjutGame() { panelPause.SetActive(false); Time.timeScale = 1f; }
    public void UlangiLevel() { Time.timeScale = 1f; SceneManager.LoadScene(SceneManager.GetActiveScene().name); }
    public void KeMenuUtama() { Time.timeScale = 1f; SceneManager.LoadScene("Category"); }
    
    public void LanjutLevelBerikutnya()
    {
        PlayerPrefs.SetInt("LevelAktif", levelAktif + 1);
        PlayerPrefs.Save();
        Time.timeScale = 1f; 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}