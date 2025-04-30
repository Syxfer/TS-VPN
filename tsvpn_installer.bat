@echo off
set owner=syxfer
set repo=TS-VPN
set branch=main

echo Checking for Python installation...
where python > nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Attempting to download and install...
    REM You might need to adjust the download link based on the Python version you want
    bitsadmin /transfer python_download /priority normal "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe" "%TEMP%\python-installer.exe"
    if exist "%TEMP%\python-installer.exe" (
        echo Running Python installer...
        start /wait "%TEMP%\python-installer.exe" /quiet InstallAllUsers=1 Include_launcher=1 Shortcut=0
        if exist "C:\Python312\python.exe" (
            echo Python installed successfully. Make sure 'C:\Python312\' and 'C:\Python312\Scripts\' are in your PATH.
        ) else (
            echo Python installation may have failed. Please check the installer output.
            echo You might need to add Python to your PATH manually.
        )
        del "%TEMP%\python-installer.exe"
    ) else (
        echo Failed to download Python installer. Please install Python manually.
        goto :download_files
    )
) else (
    echo Python is already installed.
)
echo.

:download_files
echo Downloading TSVPN.exe...
curl -s -L "https://raw.githubusercontent.com/%owner%/%repo%/%branch%/TSVPN.exe" -o "TSVPN.exe"
if errorlevel 1 (
    echo Error downloading TSVPN.exe
) else (
    echo TSVPN.exe downloaded successfully.
)
echo.

echo Downloading tsvpn_gui.py...
curl -s -L "https://raw.githubusercontent.com/%owner%/%repo%/%branch%/tsvpn_gui.py" -o "tsvpn_gui.py"
if errorlevel 1 (
    echo Error downloading tsvpn_gui.py
) else (
    echo tsvpn_gui.py downloaded successfully.
)
echo.

echo Downloading tsvpn_server_client.py...
curl -s -L "https://raw.githubusercontent.com/%owner%/%repo%/%branch%/tsvpn_server_client.py" -o "tsvpn_server_client.py"
if errorlevel 1 (
    echo Error downloading tsvpn_server_client.py
) else (
    echo tsvpn_server_client.py downloaded successfully.
)

echo.
echo All files downloaded.
pauses
