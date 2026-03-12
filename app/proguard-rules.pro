# Bitcoin Dashboard – ProGuard rules
# Keep the Activity entry point
-keep class com.bitcoin.dashboard.MainActivity { *; }

# WebView JavaScript interface (falls du später einen @JavascriptInterface hinzufügst)
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}

# AndroidX / Material
-keep class androidx.** { *; }
-dontwarn androidx.**
