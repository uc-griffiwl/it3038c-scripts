# Lab 7 - Carbon

I decided to do the Powershell Module Carbon for Lab 7 and what the Module Carbon does is automate processes that are not included in the regular version of Powershell and will make System Administrators daily jobs much easier.

# Install
How to install and import Carbon into your Powershell.

```javascript

Install-Module -Name 'Carbon' -AllowClobber
Import-Module 'Carbon'
```
# Features

Get the information of Local users and information for the administrator of the machine.
```javascript
Get-User 
Get-WmiLocalUserAccount -Username Administrator
```
Get IPv4 and IPv6 IP addresses of the local machine.
```javascript
Get-IPAddress -V4
Get-IPAddress -V6
```
Zip and Unzip folders in Windows Directory (I used sample files to do this in the commands you will need to replace the locations with locations of files on your local machine).
```javascript
Compress-Item -Path 'C:\it3038c-scripts\Carbon\Lab7\Test1.txt' -OutFile 'C:\it3038c-scripts\Carbon\Lab7\Test1.zip'
Expand-Item -Path 'C:\it3038c-scripts\Carbon\Lab7\Test1.zip' -OutDirectory 'C:\it3038c-scripts\Carbon\Lab7' -Force
```



