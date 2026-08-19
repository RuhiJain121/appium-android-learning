# Appium Android Automation — Learning Project

A minimal Android app (login screen + list screen) automated end-to-end with
[Appium](https://appium.io) + Python, wired into GitHub Actions CI.

## Structure

- `SampleApp/` — the Android app under test (Kotlin, plain Views, Gradle wrapper)
- `pages/` — Page Object classes (`LoginPage`, `WelcomePage`) wrapping element locators
- `tests/` — pytest test cases
- `conftest.py` — Appium driver fixture (starts/stops a session per test)
- `.github/workflows/ui-tests.yml` — CI pipeline: build APK → boot emulator → run tests

## Run locally

Prerequisites: JDK 17, Android SDK cmdline-tools + an AVD, Node.js, Appium
(`npm install -g appium && appium driver install uiautomator2`).

```bash
# 1. Build the APK
cd SampleApp && ./gradlew assembleDebug && cd ..

# 2. Start an emulator (adjust AVD name if different)
emulator -avd Pixel6_API34 &

# 3. Start Appium
appium --port 4723 &

# 4. Run tests
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Login credentials (sample app)

- Username: `admin`
- Password: `password123`

## CI

Every push/PR to `main` triggers `.github/workflows/ui-tests.yml`, which builds
the APK, boots a Pixel 6 / API 34 emulator via
[reactivecircus/android-emulator-runner](https://github.com/reactivecircus/android-emulator-runner),
and runs the full pytest suite against it.
