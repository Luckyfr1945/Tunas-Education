using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Script pembantu otomatis untuk menjaga UI dan Anchor tetap presisi dan responsif
/// saat game dijalankan (Play Mode) di berbagai ukuran layar / rasio.
/// </summary>
[RequireComponent(typeof(Canvas))]
public class UIResponsivenessFixer : MonoBehaviour
{
    [Header("Pengaturan Standar Resolusi")]
    public Vector2 referenceResolution = new Vector2(1920, 1080);
    [Range(0f, 1f)]
    public float matchWidthOrHeight = 0.5f;

    [Header("Opsi")]
    [Tooltip("Jika dicentang, hanya akan merapikan saat game dimainkan")]
    public bool autoFixOnPlay = true;

    private void Awake()
    {
        if (Application.isPlaying && autoFixOnPlay)
        {
            FixCanvasScaler();
            FixAnchors();
        }
    }

    [ContextMenu("Rapikan UI & Scaler Sekarang")]
    public void ManualFix()
    {
        FixCanvasScaler();
        FixAnchors();
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

    public void FixAnchors()
    {
        RectTransform[] allTransforms = GetComponentsInChildren<RectTransform>(true);

        foreach (RectTransform rt in allTransforms)
        {
            if (rt == null || rt == transform) continue;
            string objName = rt.gameObject.name.ToLower();

            // 1. Backgrounds & Fullscreen Overlays
            if (objName == "main" || objName == "background" || objName == "bg" || objName.StartsWith("panel_") || objName.Contains("overlay") || objName.Contains("readypopup"))
            {
                // Jika objek ini adalah latar belakang layar penuh atau panel popup utama
                if (rt.parent == transform || rt.parent.GetComponent<Canvas>() != null)
                {
                    rt.anchorMin = Vector2.zero;
                    rt.anchorMax = Vector2.one;
                    rt.offsetMin = Vector2.zero;
                    rt.offsetMax = Vector2.zero;
                }
            }

            // 2. Sosmed / Tombol Pojok Kanan Atas
            else if (objName.Contains("tiktok") || objName.Contains("ig") || objName.Contains("sosmed"))
            {
                // Kunci ke Top-Right
                if (rt.anchorMin != Vector2.one || rt.anchorMax != Vector2.one)
                {
                    Vector2 currentAnchored = rt.anchoredPosition;
                    rt.anchorMin = Vector2.one;
                    rt.anchorMax = Vector2.one;
                    rt.pivot = new Vector2(0.5f, 0.5f);
                }
            }

            // 3. Tombol Kembali / Back (Pojok Kiri Atas)
            else if (objName.Contains("back") || objName.Contains("kembali") || objName == "btn_back")
            {
                if (rt.anchorMin != new Vector2(0, 1) || rt.anchorMax != new Vector2(0, 1))
                {
                    rt.anchorMin = new Vector2(0, 1);
                    rt.anchorMax = new Vector2(0, 1);
                    rt.pivot = new Vector2(0.5f, 0.5f);
                }
            }
        }
    }
}
