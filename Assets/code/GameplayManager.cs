using UnityEngine;
using TMPro; 
using UnityEngine.SceneManagement;
using System.Collections.Generic; 

public class GameplayManager : MonoBehaviour
{
    [Header("Identitas Kategori (WAJIB BEDA TIAP SCENE)")]
    [Tooltip("Ketik: IPA, MATH, atau SARKASME")]
    public string kodeKategori = "IPA"; 

    [Header("Sistem Darah / Nyawa")]
    public int nyawaMaksimal = 3;
    private int nyawaSaatIni;
    [Tooltip("Masukkan object hati sesuai urutan: Index 0 (Habis), Index 1 (Tinggal 1), Index 2 (Tinggal 2), Index 3 (Penuh)")]
    public GameObject[] statusHatiUI; 

    [Header("Bank Soal")]
    public DataSoal[] kumpulanSoal; 
    
    private DataSoal soalSaatIni; 
    private int levelAktif;
    private int indexSoalTerpilih; 
    
    // Batas maksimal level untuk pengecekan riwayat soal (bisa dinaikkan jika soalmu sangat banyak)
    private int batasMaksimalLevel = 50; 

    [Header("UI Teks")]
    public TMP_Text teksPertanyaan;
    public TMP_Text[] teksPilihanJawaban; 
    [Tooltip("Masukkan TextMeshPro untuk tampilan tulisan Level di sini")]
    public TMP_Text teksLevelUI; 

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

        // Auto-detect category
        string sceneName = SceneManager.GetActiveScene().name.ToLower();
        if (sceneName.Contains("ipa")) kodeKategori = "IPA";
        else if (sceneName.Contains("math")) kodeKategori = "MATH";
        else if (sceneName.Contains("sarkas")) kodeKategori = "SARKAS";

        // LOAD DATA
        levelAktif = PlayerPrefs.GetInt("LevelAktif", 1);
        nyawaSaatIni = PlayerPrefs.GetInt("SisaNyawa", nyawaMaksimal);

        // Update UI
        if (teksLevelUI != null) teksLevelUI.text = "LEVEL " + levelAktif;
        UpdateUIHati();

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
            JawabanSalah(true); 
        }
    }

    private void UpdateUIHati()
    {
        if (statusHatiUI == null || statusHatiUI.Length == 0) return;

        for (int i = 0; i < statusHatiUI.Length; i++)
        {
            if (statusHatiUI[i] != null)
            {
                statusHatiUI[i].SetActive(i == nyawaSaatIni);
            }
        }
    }

    private void PilihSoalRandom()
    {
        if (kumpulanSoal == null || kumpulanSoal.Length == 0) return;

        int soalTersimpan = PlayerPrefs.GetInt(kodeKategori + "_Level_" + levelAktif + "_Soal", -1);

        if (soalTersimpan != -1 && soalTersimpan < kumpulanSoal.Length && kumpulanSoal[soalTersimpan] != null)
        {
            indexSoalTerpilih = soalTersimpan;
            soalSaatIni = kumpulanSoal[indexSoalTerpilih];
        }
        else
        {
            List<int> soalBelumTerpakai = new List<int>();

            for (int i = 0; i < kumpulanSoal.Length; i++)
            {
                if (kumpulanSoal[i] == null) continue; 

                bool sudahDipakai = false;
                for (int lvl = 1; lvl <= batasMaksimalLevel; lvl++) 
                {
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
                List<int> validIndices = new List<int>();
                for (int i = 0; i < kumpulanSoal.Length; i++)
                {
                    if (kumpulanSoal[i] != null) validIndices.Add(i);
                }

                if (validIndices.Count > 0)
                {
                    indexSoalTerpilih = validIndices[Random.Range(0, validIndices.Count)];
                    soalSaatIni = kumpulanSoal[indexSoalTerpilih];
                }
            }
        }

        TampilkanSoal();
    }

    private void TampilkanSoal()
    {
        if (soalSaatIni == null) return;

        if (teksPertanyaan != null) teksPertanyaan.text = soalSaatIni.teksPertanyaan;
        
        for (int i = 0; i < teksPilihanJawaban.Length; i++)
        {
            if (teksPilihanJawaban[i] != null)
            {
                if (soalSaatIni.pilihanJawaban != null && i < soalSaatIni.pilihanJawaban.Length)
                    teksPilihanJawaban[i].text = soalSaatIni.pilihanJawaban[i];
                else
                    teksPilihanJawaban[i].text = "-";
            }
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
        if (isGameSelesai || soalSaatIni == null) return; 

        if (indeksPilihan == soalSaatIni.indeksJawabanBenar) 
        {
            if (scriptTimer != null) scriptTimer.enabled = false; 
            Menang();
        }
        else 
        {
            JawabanSalah(false); 
        }
    }

    private void JawabanSalah(bool karenaWaktu)
    {
        nyawaSaatIni--; 
        UpdateUIHati(); 

        PlayerPrefs.SetInt("SisaNyawa", nyawaSaatIni);
        PlayerPrefs.Save();

        if (nyawaSaatIni <= 0)
        {
            if (karenaWaktu) Kalah("Waktu habis dan darah habis!");
            else Kalah("Yah, Darah Habis karena salah jawab!");
        }
        else
        {
            if (karenaWaktu && scriptTimer != null) scriptTimer.ResetTimer();
        }
    }

    private void Menang()
    {
        isGameSelesai = true;
        panelMenang.SetActive(true);
        
        PlayerPrefs.SetInt(kodeKategori + "_Level_" + levelAktif + "_Soal", indexSoalTerpilih);
        PlayerPrefs.SetInt("SisaNyawa", nyawaSaatIni); 
        PlayerPrefs.Save();
    }

    private void Kalah(string pesan)
    {
        isGameSelesai = true;
        if(scriptTimer != null) scriptTimer.enabled = false; 
        if (panelPause != null) panelPause.SetActive(false);
        
        // RESET DATA GAME OVER
        PlayerPrefs.SetInt("LevelAktif", 1);
        PlayerPrefs.SetInt("SisaNyawa", nyawaMaksimal);

        // LOGIKA BARU: Hapus riwayat soal yang sudah dijawab sebelumnya
        for (int i = 1; i <= batasMaksimalLevel; i++)
        {
            PlayerPrefs.DeleteKey(kodeKategori + "_Level_" + i + "_Soal");
        }

        PlayerPrefs.Save();
        
        panelKalah.SetActive(true);
    }

    public void PauseGame() { if (!isGameSelesai) { panelPause.SetActive(true); } }
    public void LanjutGame() { panelPause.SetActive(false); Time.timeScale = 1f; }
    
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
        PlayerPrefs.SetInt("LevelAktif", levelAktif + 1);
        PlayerPrefs.Save();
        Time.timeScale = 1f; 
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}