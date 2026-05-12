using UnityEngine;
using UnityEngine.UI;

public class TimerBar : MonoBehaviour
{
    [Header("Slider References")]
    public Slider timerSlider;
    public Image fillImage;

    [Header("Timer Settings")]
    public float maxTime = 30f;

    [Header("Timer Colors")]
    public Color greenColor = new Color32(126, 217, 87, 255);   // Hijau
    public Color yellowColor = new Color32(255, 217, 61, 255);  // Kuning
    public Color redColor = new Color32(255, 77, 77, 255);      // Merah

    private float currentTime;

    void Start()
    {
        currentTime = maxTime;

        timerSlider.maxValue = maxTime;
        timerSlider.value = currentTime;

        fillImage.color = greenColor;
    }

    void Update()
    {
        currentTime -= Time.deltaTime;
        currentTime = Mathf.Max(currentTime, 0f);

        timerSlider.value = currentTime;

        float percent = currentTime / maxTime;

        if (percent > 0.6f)
        {
            fillImage.color = greenColor;
        }
        else if (percent > 0.3f)
        {
            fillImage.color = yellowColor;
        }
        else
        {
            fillImage.color = redColor;
        }

        if (currentTime <= 0f)
        {
            Debug.Log("Time's Up!");
            enabled = false;
        }
    }

    public void ResetTimer()
    {
        currentTime = maxTime;
        timerSlider.value = currentTime;
        fillImage.color = greenColor;
        enabled = true;
    }
}