using UnityEngine;
using UnityEngine.SceneManagement;

public class ResetManager : MonoBehaviour
{
    public void HapusSemuaProgress()
    {
        // Sapu bersih semua data PlayerPrefs (termasuk level dan riwayat soal)
        PlayerPrefs.DeleteAll();
        PlayerPrefs.Save();
        
        Debug.Log("Semua data progress udah bersih coy!");

        // Langsung refresh scene biar efek resetnya kelihatan
        SceneManager.LoadScene(SceneManager.GetActiveScene().name); 
    }
}