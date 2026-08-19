using UnityEngine;
using UnityEditor;
using System.IO;

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
    [MenuItem("Game Kuis/Import Soal IPA")]
    public static void ImportSoalIPA()
    {
        string pathJSON = "Assets/banksoal/IPA/soal.json";
        if (!File.Exists(pathJSON)) pathJSON = "Assets/banksoal/soalipa/soal_ipa.json";
        ImportDariFile(pathJSON, "Assets/banksoal/soalipa/");
    }

    [MenuItem("Game Kuis/Import Soal Math")]
    public static void ImportSoalMath()
    {
        ImportDariFile("Assets/banksoal/Math/soal_math.json", "Assets/banksoal/Math/");
    }

    [MenuItem("Game Kuis/Import Soal Sarkas")]
    public static void ImportSoalSarkas()
    {
        ImportDariFile("Assets/banksoal/SARKAS/soalsarkes.json", "Assets/banksoal/SARKAS/");
    }

    public static void ImportDariFile(string pathJSON, string folderTujuan)
    {
        if (!File.Exists(pathJSON))
        {
            Debug.LogError("File JSON tidak ditemukan di: " + pathJSON);
            EditorUtility.DisplayDialog("Error", "File JSON tidak ditemukan di:\n" + pathJSON, "OK");
            return;
        }

        string isiJSON = File.ReadAllText(pathJSON);
        WrapperJSON data = JsonUtility.FromJson<WrapperJSON>(isiJSON);

        if (data == null || data.kumpulanData == null || data.kumpulanData.Length == 0)
        {
            Debug.LogError("Format JSON salah atau data soal kosong!");
            EditorUtility.DisplayDialog("Error", "Format JSON salah atau data soal kosong!", "OK");
            return;
        }

        if (!Directory.Exists(folderTujuan))
        {
            Directory.CreateDirectory(folderTujuan);
        }

        int counter = 1;
        foreach (StrukturSoal soal in data.kumpulanData)
        {
            string namaFile = folderTujuan + "Soal_Otomatis_" + counter.ToString("000") + ".asset";
            DataSoal asset = AssetDatabase.LoadAssetAtPath<DataSoal>(namaFile);

            if (asset == null)
            {
                asset = ScriptableObject.CreateInstance<DataSoal>();
                asset.teksPertanyaan = soal.teksPertanyaan;
                asset.pilihanJawaban = soal.pilihanJawaban;
                asset.indeksJawabanBenar = soal.indeksJawabanBenar;
                AssetDatabase.CreateAsset(asset, namaFile);
            }
            else
            {
                asset.teksPertanyaan = soal.teksPertanyaan;
                asset.pilihanJawaban = soal.pilihanJawaban;
                asset.indeksJawabanBenar = soal.indeksJawabanBenar;
                EditorUtility.SetDirty(asset);
            }
            
            counter++;
        }

        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();
        Debug.Log("Sukses import " + data.kumpulanData.Length + " soal ke " + folderTujuan);
        EditorUtility.DisplayDialog("Sukses!", "Berhasil mengimpor " + data.kumpulanData.Length + " soal ke folder " + folderTujuan, "OK");
    }
}