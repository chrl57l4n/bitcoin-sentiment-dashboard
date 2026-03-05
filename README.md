# ₿ Bitcoin Dashboard — Android App

Eine native Android-App, die das Bitcoin Dashboard als WebView-Wrapper verpackt.  
Daten kommen live von **Binance**, **CoinGecko**, **alternative.me** und **Blocktrainer**.

---

## Features

- **Live BTC/USD Preis** — Echtzeit-Kurs via Binance API
- **Preischart** — Zeitrahmen: Stunden / Tage / Wochen / Jahre
- **Marktsentiment** — Retail vs. Institutionell + BlackRock IBIT ETF
- **Fear & Greed Index** — Tageswert + 30-Tage-Verlauf
- **Blocktrainer News Feed** — Aktuelle Bitcoin-News mit Sentiment-Tags
- **Dark Mode** — Bitcoin-Orange Farbschema (`#070a0f` Hintergrund)
- **Hardware-Beschleunigt** — Optimiert für Snapdragon-Prozessoren

---

## Voraussetzungen

- Android Studio **Ladybug** (2024.2) oder neuer
- JDK **17**
- Android SDK **API 34** (compileSdk)
- Mindest-Android: **API 26** (Android 8.0)

---

## Installation & Build

### Option A — GitHub Actions (empfohlen)

Der Workflow baut automatisch eine APK bei jedem Push:

1. Repo auf GitHub erstellen und alle Dateien hochladen
2. Unter **Actions → Build APK → Run workflow** manuell starten (oder einfach pushen)
3. APK unter **Actions → letzter Workflow-Run → Artifacts** herunterladen

### Option B — Lokal mit Android Studio

```bash
# Projekt öffnen
File → Open → BitcoinDashboard2/

# Debug-APK bauen
Build → Build Bundle(s) / APK(s) → Build APK(s)
```

Die APK liegt danach unter:
```
app/build/outputs/apk/debug/app-debug.apk
```

### Option C — Kommandozeile

```bash
gradle assembleDebug
```

---

## Projektstruktur

```
BitcoinDashboard2/
├── .github/
│   └── workflows/
│       └── build.yml               # GitHub Actions CI/CD
├── app/
│   ├── build.gradle                # App-Konfiguration (compileSdk, dependencies)
│   └── src/main/
│       ├── AndroidManifest.xml     # App-Manifest (Permissions, Activity)
│       ├── assets/
│       │   └── dashboard.html      # Das komplette Bitcoin Dashboard (HTML/JS/CSS)
│       ├── java/com/bitcoin/dashboard/
│       │   └── MainActivity.java   # WebView-Wrapper
│       └── res/
│           ├── layout/
│           │   └── activity_main.xml
│           ├── mipmap-*/           # Launcher-Icons (alle Auflösungen)
│           └── values/
│               ├── strings.xml
│               └── styles.xml
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties
├── build.gradle                    # Root Build-Datei
├── gradle.properties               # AndroidX, JVM-Flags, Caching
└── settings.gradle
```

---

## Genutzte APIs

| Quelle | Daten | Authentifizierung |
|--------|-------|-------------------|
| `api.binance.com` | Kurshistorie, Ticker, Trades | Kein API-Key nötig |
| `api.alternative.me/fng` | Fear & Greed Index | Kein API-Key nötig |
| `blocktrainer.de/feed` | News RSS-Feed | Kein API-Key nötig |
| `query2.finance.yahoo.com` | IBIT ETF Kursdaten | Kein API-Key nötig |

---

## APK installieren

```bash
# Per ADB (USB-Debugging aktiviert)
adb install app-debug.apk

# Oder: APK auf das Gerät kopieren und direkt öffnen
# (Einstellung "Unbekannte Quellen" / "Apps aus unbekannten Quellen" erforderlich)
```

---

## Hinweise

- **Debug-Build**: Die APK ist unsigniert (Debug-Signatur). Für eine Play-Store-Veröffentlichung wird ein Release-Keystore benötigt.
- **CORS**: Einige APIs (z. B. Yahoo Finance) blockieren gelegentlich Anfragen — die App versucht automatisch mehrere Proxy-Fallbacks.
- **Netzwerk**: Alle Daten werden zur Laufzeit geladen. Eine aktive Internetverbindung ist erforderlich.
