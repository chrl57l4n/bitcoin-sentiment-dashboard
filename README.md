# Bitcoin Dashboard – Android App

Android-WebView-Wrapper für das Bitcoin Sentiment Dashboard.  
Optimiert für **Snapdragon 8** (arm64-v8a, Adreno GPU Hardware-Acceleration).

---

## Voraussetzungen

| Tool | Version |
|------|---------|
| Android Studio | Hedgehog 2023.1.1+ |
| JDK | 17 |
| Android SDK | API 34 |
| NDK (optional) | nicht erforderlich |

---

## Projekt-Struktur

```
bitcoin-dashboard-android/
├── app/
│   ├── src/main/
│   │   ├── assets/
│   │   │   └── bitcoin-enhanced.html   ← Dashboard-HTML hier ablegen!
│   │   ├── java/com/bitcoin/dashboard/
│   │   │   └── MainActivity.java
│   │   └── res/
│   │       ├── layout/activity_main.xml
│   │       ├── values/strings.xml
│   │       ├── values/themes.xml
│   │       └── xml/network_security_config.xml
│   ├── build.gradle
│   └── proguard-rules.pro
├── gradle/wrapper/
├── .github/workflows/android.yml
├── build.gradle
├── gradle.properties
└── settings.gradle
```

---

## Dashboard-HTML einbinden

1. `bitcoin-enhanced.html` in den Ordner `app/src/main/assets/` kopieren.
2. Falls du den Dateinamen änderst, in `MainActivity.java` anpassen:
   ```java
   webView.loadUrl("file:///android_asset/DEIN_DATEINAME.html");
   ```

---

## Lokal bauen

```bash
# Debug-APK
./gradlew assembleDebug

# Release-APK (Keystore erforderlich, siehe unten)
./gradlew assembleRelease

# Release-AAB für Play Store
./gradlew bundleRelease
```

APK-Ausgabe: `app/build/outputs/apk/`

---

## Keystore erstellen (einmalig)

```bash
keytool -genkey -v \
  -keystore bitcoin-dashboard.jks \
  -alias bitcoin \
  -keyalg RSA -keysize 2048 \
  -validity 10000
```

Anschließend mit `base64` kodieren für GitHub Secrets:

```bash
base64 -i bitcoin-dashboard.jks | pbcopy   # macOS
base64 bitcoin-dashboard.jks               # Linux
```

---

## GitHub Actions – Secrets einrichten

In deinem GitHub-Repo unter **Settings → Secrets and variables → Actions**:

| Secret | Inhalt |
|--------|--------|
| `KEYSTORE_BASE64` | Base64-kodierter Keystore (s.o.) |
| `KEYSTORE_PASS`   | Passwort des Keystores |
| `KEY_ALIAS`       | Key-Alias (z. B. `bitcoin`) |
| `KEY_PASS`        | Key-Passwort |

Der CI-Workflow baut bei jedem Push auf `main`/`master`:
- **Debug-APK** (immer)
- **Release-APK** + **AAB** (nur bei push, nicht bei PR)
- **GitHub Release** (automatisch bei Tags `v*`)

---

## Snapdragon 8 – Optimierungen

- `ndk { abiFilters "arm64-v8a" }` – nur natives ABI, kein x86-Overhead
- `android:hardwareAccelerated="true"` – Adreno GPU für Canvas/WebGL
- `LAYER_TYPE_HARDWARE` im Java-Code – GPU-beschleunigte Darstellung
- Immersive Fullscreen – maximale Displayfläche für Charts
- `resumeTimers()` / `pauseTimers()` – sauber pausieren wenn App im Hintergrund

---

## Schnellstart mit Android Studio

1. Repo klonen: `git clone https://github.com/chri57i4n/bitcoin-sentiment-dashboard-android`
2. `bitcoin-enhanced.html` → `app/src/main/assets/`
3. **File → Open** → Projektordner wählen
4. **Run ▶** auf verbundenem Gerät oder Emulator

---

## Lizenz

MIT
