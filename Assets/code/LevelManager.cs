using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelSelection : MonoBehaviour
{
    [Header("Pengaturan Scene")]
 
    public string namaSceneGameplay = "GameplayScene"; 
    public string namaSceneKembali = "Category"; 

    // Fungsi ini akan dipasang ke SEMUA tombol level (1-20)
    public void PilihLevel(int nomorLevel)
    {
        Debug.Log("Pemain memilih Level: " + nomorLevel);

        // Simpan nomor level ke memori Unity
        // Ini kuncinya! Scene Gameplay nanti akan membaca data "LevelAktif" ini
        PlayerPrefs.SetInt("LevelAktif", nomorLevel);
        PlayerPrefs.Save();

        // Pindah ke scene Gameplay
        SceneManager.LoadScene(namaSceneGameplay);
    }

    // Fungsi untuk tombol X (Close/Back) warna pink di pojok kanan atas
    public void KembaliKeKategori()
    {
        SceneManager.LoadScene(namaSceneKembali);
    }
}