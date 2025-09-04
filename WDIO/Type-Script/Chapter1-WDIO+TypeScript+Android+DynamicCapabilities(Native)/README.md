# WebdriverIO pCloudy Test Setup for Type Script

## 1. Node Version

Ensure you are using the Node version specified in `.nvmrc`:

```bash
nvm use
```

## 2. Install Dependencies

Install project dependencies:

```bash
npm install
```

## 3. Update Configuration

Update the `config/config.json` file according to your environment:

### a. Credentials

Update your pCloudy credentials:

```json
"pcloudy:options": {
  "pCloudy_Username": "<your-username>",
  "pCloudy_ApiKey": "<your-api-key>"
}
```

### b. Application

* If `uploadApp` is `false`, provide the app name directly in:

```json
"pCloudy_ApplicationName": "YourAppName.apk"
```

* If `uploadApp` is `true`, ensure `AppPath` points to a valid `.apk` or `.ipa` file.

### c. Dynamic Name & Build

* If `dynamicName` or `dynamicBuild` is `false`, make sure:

```json
"appium:name": "SomeTestName",
"appium:build": "SomeBuildID"
```

have valid values.

## 4. Run Tests

Run the WebdriverIO tests:

```bash
npm run wdio
```

---

**Notes:**

* All configurations are loaded from `config/config.json`.
* Dynamic test name and build ID will override static values if `dynamicName` or `dynamicBuild` is `true`.
* If `uploadApp` fails, the WDIO run will abort to avoid invalid app configuration.
