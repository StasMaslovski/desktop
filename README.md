# This repository  is a sample test project for Windows desktop application [Reverso](https://context.reverso.net/).
**Requirements:**
- Windows 10 or Windows 11
- Python v2.7 or higher
- Use Python package manager (PIP) to install the following dependencies:
     - Appium-Python-Client (tested version 0.24)
     - selenium (tested version 3.5.0)
     - setuptools (tested version 28.8.0)

1. Download Windows Application Driver installer from [here](https://github.com/Microsoft/WinAppDriver/releases)
2. Run the installer on a Windows 10 machine where your application under test is installed and will be tested
3. Enable [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) in Windows settings
4. Run WinAppDriver.exe from the installation directory (for example: Windows Application Driver>WinAppDriver.exe 127.0.0.1 4723/wd/hub)
5. Download and install [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/) (Windows Development Kit)


Command for running tests with generating allure report: `pytest --alluredir=allure-result/ tests/reverso_context_test.py`

For watching the tests results execute following command: `allure serve allure-result`
