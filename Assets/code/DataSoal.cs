using UnityEngine;

// Baris ini membuat menu baru saat kamu klik kanan di folder Project Unity
[CreateAssetMenu(fileName = "SoalBaru", menuName = "Game Kuis/Data Soal")]
public class DataSoal : ScriptableObject
{
    [Header("Pertanyaan")]
    [TextArea(3, 5)] // Membuat kolom teks di Inspector jadi lebih lebar
    public string teksPertanyaan;

    [Header("Pilihan Jawaban")]
    public string[] pilihanJawaban = new string[4]; // Array 4 untuk A, B, C, D

    [Header("Kunci Jawaban")]
    [Tooltip("Isi 0 untuk A, 1 untuk B, 2 untuk C, 3 untuk D")]
    public int indeksJawabanBenar; 
}