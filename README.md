# emailscrapper

## IMPORTANT:
  The versions of Google Chrome and Chrome Driver need to be compatible and match each other.
## Step 1, Installing and get the path of Google Chrome on Windows and macOS is straightforward. Here are the steps for each operating system:

### macOS:
Download Chrome Installer:

1. Open Safari or your preferred web browser and go to the official Google Chrome download page.
Click on the "Download Chrome" button.

2. Run the Installer:

3. Once the download is complete, open the downloaded disk image file (usually in the Downloads folder).
4. Drag the Chrome icon to the "Applications" folder.
Complete Installation:

5. Open the "Applications" folder, locate Google Chrome, and double-click on it to launch the browser.
6. Chrome may ask if you want to set it as your default browser; choose according to your preference.
7. Alternatively, you can find the path manually:

Open the "Applications" folder.
Right-click (or control-click) on "Google Chrome."
Select "Show Package Contents."
Navigate to the "Contents/MacOS" directory.
The executable file is named "Google Chrome."
The full path is usually something like /Applications/Google Chrome.app/Contents/MacOS/Google Chrome. This path is subject to change based on the installation directory and version of Google Chrome.

### Windows:
Download Chrome Installer:

Open your current web browser and go to the official Google Chrome download page.
Click on the "Download Chrome" button.
Run the Installer:

Once the download is complete, locate the downloaded file (usually in the Downloads folder) and double-click on it.
Follow the on-screen instructions in the installer.
Complete Installation:

Chrome will be installed on your system. Ensure that the option to set Chrome as your default browser is selected if you want to make it your default browser.
Launch Chrome:

After installation, you can launch Google Chrome from your desktop or Start menu.

## Step 2, To install ChromeDriver on macOS and Windows, you can follow these steps:

### macOS:
Using Homebrew:

Open Terminal.
Run the following commands:
```
brew update
```
```
brew install chromedriver
```

Manual Installation:

Visit the ChromeDriver downloads page.
Download the appropriate version of ChromeDriver for macOS.
Extract the downloaded ZIP file.
Move the chromedriver executable to a directory included in your system's PATH, like /usr/local/bin/.


### Windows:
Download ChromeDriver:

Visit the ChromeDriver downloads page.
Download the appropriate version of ChromeDriver for Windows.
Extract the downloaded ZIP file.
Add ChromeDriver to System PATH:

Move the chromedriver.exe executable to a directory included in your system's PATH. You can add the directory containing chromedriver.exe to your system's PATH.
Example:

If you place chromedriver.exe in the C:\Program Files\ChromeDriver directory, add this directory to your PATH.
Verifying Installation:
After installation, you can verify that ChromeDriver is accessible from the command line by opening a terminal or command prompt and running:

### for all (masOS/Windows/Linux)
```
chromedriver --version
```
This command should display the version of ChromeDriver, indicating that the installation was successful.

Now, you can use ChromeDriver with automation tools or libraries like Selenium for web testing or scraping. Make sure to update ChromeDriver periodically to match the version of your Chrome browser for compatibility.

## macOS:
To get the path of ChromeDriver on macOS, you can use the which command in the Terminal after installing ChromeDriver via Homebrew or another method. Open the Terminal and run:

```
which chromedriver
```
This command will output the path to the installed ChromeDriver executable.

## Windows:
If you've manually added ChromeDriver to a directory in your system's PATH, you can open a Command Prompt and run:

```
where chromedriver
```

This command will display the path to the ChromeDriver executable if it's in the system's PATH.

Alternatively, if you know the directory where you placed the ChromeDriver executable, you can navigate to that directory using the cd command in the Command Prompt, and then run:

```
echo %cd%
```
This command will print the current working directory, which is the directory containing the ChromeDriver executable.


## Step 3, install python: Installing Python on macOS, Windows, and Linux involves slightly different steps. Here's a general guide for each operating system:

### macOS:
Using Homebrew (recommended):
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
```
brew install python
```

### Windows:
Using the Official Python Installer:

Download the latest Python installer for Windows from the official Python website.
Run the installer and make sure to check the box that says "Add Python to PATH" during installation.

## Step 3,Install python libraries
### macOS:

1. Open the terminal.

2. Navigate to the directory containing your requirements.txt file using the cd command:
```
cd /path/to/your/project
```
3. Install the requirements using pip:
```
pip install -r requirements.txt
```

### Windows:
1.) Open the command prompt or PowerShell.

2.) Navigate to the directory containing your requirements.txt file using the cd command:
```
cd \path\to\your\project
```
3.) Install the requirements using pip:
```
pip install -r requirements.txt
```
This assumes that Python and pip are added to your system's PATH. If you encounter issues, make sure that the Python scripts directory (usually C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts on Windows) is in your system's PATH.


## Specify the paths for the Chrome driver and Google browser in the configuration file (config.txt).

### for windowsOS (sample path)
```
chrome_driver_path=D:\bin\google\Chrome\Application\chrome.exe
google_browser_path=D:\bin\driver\chromedriver.exe
```
### for macOS (sample path)
```
chrome_driver_path=/path/to/bin/google/Chrome/Application/chrome
google_browser_path=/path/to/bin/driver/chromedriver
```
### for linux (sample path)
```
chrome_driver_path=/path/to/bin/google/Chrome/Application/chrome
google_browser_path=/path/to/bin/driver/chromedriver
```
