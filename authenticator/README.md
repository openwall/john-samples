authenticator is a CLI analog to the Google Authenticator phone app, or the LastPass Authenticator phone app. It is a TOTP/HOTP client that can generate the numeric codes needed for authentication with sites that support Two-Factor Authentication (TFA) or Multi-Factor Authentication (MFA).

https://github.com/JeNeSuisPasDave/authenticator

sample password: pass123
Google Authenticator (googleauth) shared secret: WSLRETXRDKXNR4AN

```
$ authenticator add googleauth
No data file was found. Do you want to create your data file? (yes|no) [yes]: 
Enter passphrase: 
Confirm passphrase: 
Enter shared secret: WSLRETXRDKXNR4AN
OK
X@XXX:~$ authenticator gen
Enter passphrase: 
googleauth: 309615 (expires in 20 seconds)
```
