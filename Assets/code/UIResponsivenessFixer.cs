using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Script pembantu untuk memastikan Canvas Scaler selalu diset ke 1920x1080 (Scale With Screen Size).
/// Tidak akan mengubah atau mereset ukuran / posisi objek anak yang sudah kamu atur di editor.
/// </summary>
[RequireComponent(typeof(Canvas))]
public class UIResponsivenessFixer : MonoBehaviour
{
    [Header("Pengaturan Standar Resolusi")]
    public Vector2 referenceResolution = new Vector2(1920, 1080);
    [Range(0f, 1f)]
    public float matchWidthOrHeight = 0.5f;

    private void Awake()
    {
        FixCanvasScaler();
    }

    public void FixCanvasScaler()
    {
        CanvasScaler scaler = GetComponent<CanvasScaler>();
        if (scaler == null)
        {
            scaler = gameObject.AddComponent<CanvasScaler>();
        }

        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = referenceResolution;
        scaler.screenMatchMode = CanvasScaler.ScreenMatchMode.MatchWidthOrHeight;
        scaler.matchWidthOrHeight = matchWidthOrHeight;
    }
}
