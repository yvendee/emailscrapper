# emailscrapper

##Step1, install python: Installing Python on macOS, Windows, and Linux involves slightly different steps. Here's a general guide for each operating system:

### macOS:
Using Homebrew (recommended):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

### Windows:
Using the Official Python Installer:

Download the latest Python installer for Windows from the official Python website.
Run the installer and make sure to check the box that says "Add Python to PATH" during installation.

##Step2,Install python libraries
##macOS:

1. Open the terminal.

2. Navigate to the directory containing your requirements.txt file using the cd command:

cd /path/to/your/project

3. Install the requirements using pip:
pip install -r requirements.txt


##Windows:
1.) Open the command prompt or PowerShell.

2.) Navigate to the directory containing your requirements.txt file using the cd command:

cd \path\to\your\project

3.) Install the requirements using pip:

pip install -r requirements.txt

This assumes that Python and pip are added to your system's PATH. If you encounter issues, make sure that the Python scripts directory (usually C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts on Windows) is in your system's PATH.


## Specify the paths for the Chrome driver and Google browser in the configuration file (config.txt).

### for windowsOS (sample path)
chrome_driver_path=D:\bin\google\Chrome\Application\chrome.exe
google_browser_path=D:\bin\driver\chromedriver.exe

### for macOS (sample path)
chrome_driver_path=/path/to/bin/google/Chrome/Application/chrome
google_browser_path=/path/to/bin/driver/chromedriver

### for linux (sample path)
chrome_driver_path=/path/to/bin/google/Chrome/Application/chrome
google_browser_path=/path/to/bin/driver/chromedriver

