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

    [Header("Validasi Visual Level Selesai")]
    public Button[] arrayTombolLevel; 
    public Color warnaSelesai = new Color32(126, 217, 87, 255); 
    public Color warnaBelum = Color.white; 

    private void Start()
    {
        CekStatusLevel();
    }

    private void CekStatusLevel()
    {
        if (arrayTombolLevel == null || arrayTombolLevel.Length == 0) return;

        for (int i = 0; i < arrayTombolLevel.Length; i++)
        {
            int nomorLevel = i + 1; 

            // Cek memori yang udah dilabelin kategori
            int soalTersimpan = PlayerPrefs.GetInt(kodeKategori + "_Level_" + nomorLevel + "_Soal", -1);

            if (soalTersimpan != -1)
            {
                arrayTombolLevel[i].image.color = warnaSelesai;
            }
            else
            {
                arrayTombolLevel[i].image.color = warnaBelum;
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