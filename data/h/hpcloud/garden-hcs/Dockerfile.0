# Dockerfile to build the garden rootfs image
#
# Build the image with this command:
#  docker build -t garden-rootfs .
#
# Use the following PS snippet to get the -baseImagePath argument for garden:
#  (docker inspect garden-rootfs | ConvertFrom-Json).GraphDriver.Data.Dir

FROM microsoft/windowsservercore

# Install VC Redist and features
RUN powershell.exe -Command \
  $ErrorActionPreference = 'Stop'; \
  mkdir -Force "c:\vc2013"; \
  iwr -Verbose -UseBasicParsing  -OutFile "c:\vc2013\vcredist_x86.exe"  https://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x86.exe ; \
  iwr -Verbose -UseBasicParsing  -OutFile "c:\vc2013\vcredist_x64.exe"  https://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x64.exe ; \
  start -Wait "c:\vc2013\vcredist_x86.exe"  -ArgumentList '/install /passive /norestart' ; \
  start -Wait "c:\vc2013\vcredist_x64.exe"  -ArgumentList '/install /passive /norestart' ; \
  rm .\vc2013 -Force -Recurse; \

  Install-WindowsFeature  Web-Server, Web-WebServer ; \
  Install-WindowsFeature  -IncludeAllSubFeature Web-Common-Http ; \
  Install-WindowsFeature  Web-App-Dev, Web-Net-Ext45, Web-AppInit, Web-ASP, Web-Asp-Net45, Web-CGI, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Includes, Web-WebSockets ; \
  Install-WindowsFeature  -IncludeAllSubFeature Web-Health ; \
  Install-WindowsFeature  -IncludeAllSubFeature Web-Performance ; \
  Install-WindowsFeature  Web-Security, Web-Filtering, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Cert-Auth, Web-IP-Security, Web-Url-Auth, Web-Windows-Auth ;
