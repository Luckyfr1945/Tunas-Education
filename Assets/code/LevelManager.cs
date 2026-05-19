using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI; // Wajib ditambahkan untuk memanipulasi warna Button

public class LevelSelection : MonoBehaviour
{
    [Header("Pengaturan Scene")]
    public string namaSceneGameplay = "gameplay_ipa"; // Pastikan namanya sesuai
    public string namaSceneKembali = "Category"; 

    [Header("Validasi Visual Level Selesai")]
    [Tooltip("Masukkan tombol level 1 sampai 20 ke sini secara berurutan")]
    public Button[] arrayTombolLevel; 
    
    // Warna untuk membedakan status level
    public Color warnaSelesai = new Color32(126, 217, 87, 255); // Hijau (kayak timer kamu)
    public Color warnaBelum = Color.white; // Warna asli gambar tombol (orange)

    private void Start()
    {
        // Langsung cek status semua level saat scene ini baru dibuka
        CekStatusLevel();
    }

    private void CekStatusLevel()
    {
        // Jaga-jaga kalau array-nya lupa diisi di Inspector
        if (arrayTombolLevel == null || arrayTombolLevel.Length == 0) return;

        // Looping (mengecek) satu per satu tombol dari array
        for (int i = 0; i < arrayTombolLevel.Length; i++)
        {
            int nomorLevel = i + 1; // Array mulai dari 0, sedangkan level mulai dari 1

            // Intip memori: apakah level ini sudah ada kuncian soalnya? (Artinya sudah tamat)
            int soalTersimpan = PlayerPrefs.GetInt("Level_" + nomorLevel + "_Soal", -1);

            if (soalTersimpan != -1)
            {
                // LEVEL SUDAH SELESAI: Ubah warna tombol jadi hijau
                arrayTombolLevel[i].image.color = warnaSelesai;
            }
            else
            {
                // LEVEL BELUM SELESAI: Biarkan warna aslinya
                arrayTombolLevel[i].image.color = warnaBelum;
            }
        }
    }

    // Fungsi ini akan dipasang ke SEMUA tombol level (1-20)
    public void PilihLevel(int nomorLevel)
    {
        Debug.Log("Pemain memilih Level: " + nomorLevel);

        PlayerPrefs.SetInt("LevelAktif", nomorLevel);
        PlayerPrefs.Save();

        SceneManager.LoadScene(namaSceneGameplay);
    }

    // Fungsi untuk tombol X (Close/Back)
    public void KembaliKeKategori()
    {
        SceneManager.LoadScene(namaSceneKembali);
    }
}