'Documentation: https://ss64.com/vb/run.html and https://ss64.com/vb/shell.html 
'(didnt use msft official stuff since this one seemed pretty accurate and msft ones seemed to be talking about internet explorer)
'Create a new shell variable
Set WshShell = CreateObject("WScript.Shell") 
'Set the command to be run to >> "C:\Users\Prateek\Desktop\chrome proxy\ssh-tunnel.bat" and bWaitOnReturn=0 (wait for command to complete before continuing)
'This command starts a PuTTY socks tunnel to the remote server (configs are defined in PuTTY itself) and waits for the command to return/complete before continuing
WshShell.Run chr(34) & "D:\Practice Programs\Scripts\Socks tunnel\chrome proxy\ssh-tunnel.bat" & Chr(34), 0
'Set WshShell = Nothing
'Start a different shell which starts chrome with proxy settings defined in chrome-proxy.bat
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "D:\Practice Programs\Scripts\Socks tunnel\chrome proxy\chrome-proxy.bat" & Chr(34), 0
'Clear variable, not sure how GC is implemented in VB so..
Set WshShell = Nothing