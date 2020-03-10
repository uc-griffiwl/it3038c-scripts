# Lab 7 - Posh-SSH

I had trouble finding a decent module / addin to use for this lab but I ended up finding this
cool tool that allows you to ssh from within the powershell console and do a bunch of different things.

Link to the github for the module - github.com/darkoperator/Posh-SSH

# Install


```javascript

Install-Module -Name posh-ssh -force
```

After the install to ensure it downloaded sucessfully, lets make sure it is there run:

```javascript
Get-Module -ListAvailable -Name Posh-SSH
```

To get an SSH session started, you must enter the command below
```javascript
new-sshsession -computername -acceptkey -credential 
```

Example of what I used and worked
```javascript
new-sshsession -computername 192.168.33.108 -acceptkey -credential cechuser
```

Now that we are connected, we can run commands / do whatever we really need to from within powershell.


