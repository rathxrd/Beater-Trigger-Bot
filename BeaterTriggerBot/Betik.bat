@echo off
echo Running script...
cd /d "%~dp0"

:: Betik dosyasını yönetici olarak çalıştır
powershell -Command "Start-Process 'python' -ArgumentList 'betik.py' -WorkingDirectory '%~dp0' -Verb RunAs"
