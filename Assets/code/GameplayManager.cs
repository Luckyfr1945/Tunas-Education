using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameplayManager : MonoBehaviour
{
    [Header("Identitas Kategori")]
    [Tooltip("Ketik: IPA, MATH, atau SARKASME")]
    public string kodeKategori = "IPA"; 

    [Header("Mode Pameran")]
    [Tooltip("Jumlah total soal dalam 1 sesi permainan di pameran")]
    public int totalSoalPameran = 5;

    [Header("Sistem Countdown (3 Detik di Awal)")]
    public GameObject panelCountdown;
    public TMP_Text teksCountdown;
    [Tooltip("Ukuran font countdown (bisa kamu atur agar pas dan besar)")]
    public float ukuranFontCountdown = 140f;

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
    
    private int batasMaksimalLevel = 50; 

    [Header("UI Teks")]
    public TMP_Text teksPertanyaan;
    public TMP_Text[] teksPilihanJawaban; 
    [Tooltip("Masukkan TextMeshPro untuk tampilan tulisan Level / Soal di sini")]
    public TMP_Text teksLevelUI;

    [Header("Komponen Timer")]
    public TimerBar scriptTimer; 

    [Header("Pengaturan Kesulitan Waktu")]
    public float waktuDasar = 30f; 
    public float potonganWaktu = 3f; 

    [Header("UI Panel")]
    public GameObject panelMenang;
    public GameObject panelKalah;
    public GameObject panelPause; 

    private bool isGameSelesai = false; 
    private bool isCountingDown = false;

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
        if (teksLevelUI != null) 
            teksLevelUI.text = "SOAL " + levelAktif + " / " + totalSoalPameran;
            
        UpdateUIHati();

        if (panelMenang != null) panelMenang.SetActive(false);
        if (panelKalah != null) panelKalah.SetActive(false);
        if (panelPause != null) panelPause.SetActive(false);
        
        isGameSelesai = false;

        // Pilih soal dulu agar teks pertanyaan siap
        PilihSoalRandom();

        // Jalankan countdown 3 detik HANYA saat pertama kali mulai game (Soal 1)
        if (levelAktif == 1)
        {
            StartCoroutine(StartCountdownRoutine());
        }
        else
        {
            // Untuk Soal 2, 3, 4, dst: Langsung mulai tanpa countdown
            isCountingDown = false;
            SetVisibilitySoalDanJawaban(true);
            SetPilihanJawabanInteractable(true);
            if (teksCountdown != null) teksCountdown.gameObject.SetActive(false);
            if (panelCountdown != null) panelCountdown.SetActive(false);

            if (scriptTimer != null)
            {
                scriptTimer.ResetTimer();
                scriptTimer.enabled = true;
            }
        }
    }

    private IEnumerator StartCountdownRoutine()
    {
        isCountingDown = true;
        SetPilihanJawabanInteractable(false);
        SetVisibilitySoalDanJawaban(false); // Sembunyikan teks soal & jawaban selama countdown agar tidak kelihatan

        if (scriptTimer != null) 
        {
            scriptTimer.enabled = false;
        }

        // Matikan word wrapping agar kata 'MULAI!' tidak terpotong turun ke bawah
        if (teksCountdown != null)
        {
            teksCountdown.textWrappingMode = TextWrappingModes.NoWrap;
            teksCountdown.overflowMode = TextOverflowModes.Overflow;
            if (teksCountdown.rectTransform != null)
            {
                teksCountdown.rectTransform.sizeDelta = new Vector2(1600f, 450f);
            }
        }

        // Tentukan objek backdrop blur / gelap di belakang countdown
        GameObject autoBackdrop = null;
        if (panelCountdown != null)
        {
            panelCountdown.SetActive(true);
        }
        else if (teksCountdown != null)
        {
            Canvas canvas = teksCountdown.GetComponentInParent<Canvas>();
            if (canvas != null)
            {
                autoBackdrop = new GameObject("Countdown_FrostedBackdrop", typeof(RectTransform), typeof(Image));
                autoBackdrop.transform.SetParent(canvas.transform, false);
                autoBackdrop.transform.SetSiblingIndex(teksCountdown.transform.GetSiblingIndex());

                RectTransform rt = autoBackdrop.GetComponent<RectTransform>();
                rt.anchorMin = Vector2.zero;
                rt.anchorMax = Vector2.one;
                rt.offsetMin = Vector2.zero;
                rt.offsetMax = Vector2.zero;

                Image img = autoBackdrop.GetComponent<Image>();
                img.color = new Color(0.04f, 0.07f, 0.1f, 0.90f); // Frosted dark blur overlay 90%

                // Coba pasang shader blur jika ada
                Shader blurShader = Shader.Find("UI/FrostedBlurUI");
                if (blurShader != null)
                {
                    img.material = new Material(blurShader);
                }
            }
            teksCountdown.gameObject.SetActive(true);
        }

        if (teksCountdown != null)
        {
            // 3 (Oranye)
            yield return StartCoroutine(PlayStepCountdown("3", new Color32(255, 140, 0, 255), 1f));

            // 2 (Kuning)
            yield return StartCoroutine(PlayStepCountdown("2", new Color32(255, 215, 0, 255), 1f));

            // 1 (Hijau Muda)
            yield return StartCoroutine(PlayStepCountdown("1", new Color32(144, 238, 144, 255), 1f));

            // MULAI! (Hijau Cerah)
            yield return StartCoroutine(PlayStepCountdown("MULAI!", new Color32(50, 205, 50, 255), 0.7f));

            if (panelCountdown != null) panelCountdown.SetActive(false);
            if (autoBackdrop != null) Destroy(autoBackdrop);
            teksCountdown.gameObject.SetActive(false);
        }
        else
        {
            yield return new WaitForSeconds(0.2f);
        }

        // Tampilkan kembali soal & jawaban saat game dimulai
        SetVisibilitySoalDanJawaban(true);
        isCountingDown = false;
        SetPilihanJawabanInteractable(true);

        if (scriptTimer != null)
        {
            scriptTimer.ResetTimer();
            scriptTimer.enabled = true;
        }
    }

    private void SetVisibilitySoalDanJawaban(bool visible)
    {
        if (teksPertanyaan != null) teksPertanyaan.gameObject.SetActive(visible);
        if (teksPilihanJawaban != null)
        {
            foreach (var teks in teksPilihanJawaban)
            {
                if (teks != null) teks.gameObject.SetActive(visible);
            }
        }
    }

    private IEnumerator PlayStepCountdown(string text, Color color, float duration)
    {
        if (teksCountdown == null) yield break;

        teksCountdown.text = text;
        teksCountdown.color = color;
        
        // Buat teks otomatis besar, tebal (bold), dan di tengah
        if (ukuranFontCountdown > 0)
        {
            teksCountdown.fontSize = ukuranFontCountdown;
        }
        teksCountdown.fontStyle = FontStyles.Bold;
        teksCountdown.alignment = TextAlignmentOptions.Center;
        teksCountdown.textWrappingMode = TextWrappingModes.NoWrap;
        teksCountdown.overflowMode = TextOverflowModes.Overflow;

        Transform tf = teksCountdown.transform;
        Vector3 baseScale = Vector3.one;

        float elapsed = 0f;
        while (elapsed < duration)
        {
            elapsed += Time.deltaTime;
            float t = elapsed / duration;

            // Efek Pop Membal Lebih Besar (Punch Zoom Out)
            float scaleMultiplier;
            if (t < 0.25f)
            {
                scaleMultiplier = Mathf.Lerp(2.2f, 0.95f, t / 0.25f);
            }
            else
            {
                scaleMultiplier = Mathf.Lerp(0.95f, 1f, (t - 0.25f) / 0.75f);
            }

            tf.localScale = baseScale * scaleMultiplier;
            yield return null;
        }

        tf.localScale = baseScale;
    }

    private void SetPilihanJawabanInteractable(bool state)
    {
        if (teksPilihanJawaban == null) return;
        foreach (var teks in teksPilihanJawaban)
        {
            if (teks != null)
            {
                Button btn = teks.GetComponentInParent<Button>();
                if (btn != null) btn.interactable = state;
            }
        }
    }

    private void Update()
    {
        if (!isGameSelesai && !isCountingDown && scriptTimer != null && scriptTimer.timerSlider != null && scriptTimer.timerSlider.value <= 0f)
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

    private int indeksTombolBenarSaatIni; 

    private void TampilkanSoal()
    {
        if (soalSaatIni == null) return;

        if (teksPertanyaan != null) teksPertanyaan.text = soalSaatIni.teksPertanyaan;
        
        int jumlahPilihan = soalSaatIni.pilihanJawaban != null ? soalSaatIni.pilihanJawaban.Length : 0;
        
        // Buat list indeks pilihan (0, 1, 2, 3) lalu diacak (Fisher-Yates Shuffle)
        List<int> listIndexAcak = new List<int>();
        for (int i = 0; i < jumlahPilihan; i++)
        {
            listIndexAcak.Add(i);
        }

        for (int i = 0; i < listIndexAcak.Count; i++)
        {
            int rnd = Random.Range(i, listIndexAcak.Count);
            int temp = listIndexAcak[i];
            listIndexAcak[i] = listIndexAcak[rnd];
            listIndexAcak[rnd] = temp;
        }

        // Tampilkan teks jawaban yang sudah diacak ke tombol A, B, C, D
        for (int i = 0; i < teksPilihanJawaban.Length; i++)
        {
            if (teksPilihanJawaban[i] != null)
            {
                if (i < listIndexAcak.Count)
                {
                    int indexJawabanAsli = listIndexAcak[i];
                    teksPilihanJawaban[i].text = soalSaatIni.pilihanJawaban[indexJawabanAsli];

                    // Catat tombol ke berapa yang memegang jawaban benar
                    if (indexJawabanAsli == soalSaatIni.indeksJawabanBenar)
                    {
                        indeksTombolBenarSaatIni = i;
                    }
                }
                else
                {
                    teksPilihanJawaban[i].text = "-";
                }
            }
        }

        if (scriptTimer != null) 
        {
            int kelipatanKesulitan = (levelAktif - 1);
            float waktuLevelIni = waktuDasar - (kelipatanKesulitan * potonganWaktu);
            if (waktuLevelIni < 8f) waktuLevelIni = 8f;

            scriptTimer.maxTime = waktuLevelIni; 
            scriptTimer.ResetTimer();
        }
    }

    public void CekJawaban(int indeksPilihan)
    {
        if (isGameSelesai || isCountingDown || soalSaatIni == null) return; 

        // Cocokkan apakah tombol yang diklik adalah tombol yang menyimpan jawaban benar saat ini
        if (indeksPilihan == indeksTombolBenarSaatIni) 
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
        if (scriptTimer != null) scriptTimer.enabled = false;
        
        PlayerPrefs.SetInt(kodeKategori + "_Level_" + levelAktif + "_Soal", indexSoalTerpilih);
        PlayerPrefs.SetInt("SisaNyawa", nyawaSaatIni); 
        PlayerPrefs.Save();

        if (panelMenang != null)
        {
            panelMenang.SetActive(true);
        }
    }

    private void Kalah(string pesan)
    {
        isGameSelesai = true;
        if (scriptTimer != null) scriptTimer.enabled = false; 
        if (panelPause != null) panelPause.SetActive(false);
        
        ResetDataPameran();
        
        if (panelKalah != null) panelKalah.SetActive(true);
    }

    public void ResetDataPameran()
    {
        PlayerPrefs.SetInt("LevelAktif", 1);
        PlayerPrefs.SetInt("SisaNyawa", nyawaMaksimal);

        for (int i = 1; i <= batasMaksimalLevel; i++)
        {
            PlayerPrefs.DeleteKey(kodeKategori + "_Level_" + i + "_Soal");
        }
        PlayerPrefs.Save();
    }

    public void PauseGame() 
    { 
        if (!isGameSelesai && !isCountingDown) 
        { 
            if (panelPause != null) panelPause.SetActive(true); 
            Time.timeScale = 0f;
        } 
    }

    public void LanjutGame() 
    { 
        if (panelPause != null) panelPause.SetActive(false); 
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
        ResetDataPameran();
        SceneManager.LoadScene("MainMenu"); 
    }
    
    public void LanjutLevelBerikutnya()
    {
        Time.timeScale = 1f;
        if (levelAktif >= totalSoalPameran)
        {
            // Jika sudah 5 soal dan menekan lanjut/selesai -> Kembali ke Main Menu
            KeMenuUtama();
        }
        else
        {
            PlayerPrefs.SetInt("LevelAktif", levelAktif + 1);
            PlayerPrefs.Save();
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
    }
}