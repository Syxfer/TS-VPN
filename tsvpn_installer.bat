@echo off
set owner=syxfer
set repo=TS-VPN
set branch=main

echo Downloading TSVPN.exe...
curl -s -L "https://raw.githubusercontent.com/%owner%/%repo%/%branch%/TSVPN.exe" -o "TSVPN.py"
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
pause