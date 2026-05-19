using UnityEngine;
using UnityEditor; // Wajib pakai ini untuk bikin file .asset
using System.IO;

// Kelas pembungkus struktur JSON
[System.Serializable]
public class StrukturSoal
{
    public string teksPertanyaan;
    public string[] pilihanJawaban;
    public int indeksJawabanBenar;
}

[System.Serializable]
public class WrapperJSON
{
    public StrukturSoal[] kumpulanData;
}

public class ImportSoalJSON : MonoBehaviour
{
    // Ini akan bikin menu baru di bar atas Unity
    [MenuItem("Game Kuis/Import Soal Dari JSON")]
    public static void ImportSoal()
    {
        // Ganti path ini sesuai lokasi kamu menaruh file JSON di Unity
        string pathJSON = "Assets/banksoal/soalipa/soal_ipa.json"; 
        
        // Folder tujuan tempat file .asset akan dicetak (pastikan foldernya sudah kamu buat!)
        string folderTujuan = "Assets/banksoal/soalipa/";

        if (!File.Exists(pathJSON))
        {
            Debug.LogError("File JSON tidak ditemukan di: " + pathJSON);
            return;
        }

        string isiJSON = File.ReadAllText(pathJSON);
        WrapperJSON data = JsonUtility.FromJson<WrapperJSON>(isiJSON);

        int counter = 1;
        foreach (StrukturSoal soal in data.kumpulanData)
        {
            // Bikin cetakan kosong di memori
            DataSoal assetBaru = ScriptableObject.CreateInstance<DataSoal>();
            
            // Isi data dari JSON ke cetakan
            assetBaru.teksPertanyaan = soal.teksPertanyaan;
            assetBaru.pilihanJawaban = soal.pilihanJawaban;
            assetBaru.indeksJawabanBenar = soal.indeksJawabanBenar;

            // Cetak jadi file fisik .asset
            string namaFile = folderTujuan + "Soal_Otomatis_" + counter.ToString("000") + ".asset";
            AssetDatabase.CreateAsset(assetBaru, namaFile);
            
            counter++;
        }

        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();
        Debug.Log("Sukses import " + data.kumpulanData.Length + " soal!");
    }
}