# Mosquitto passwd file examples

Three Eclipse Mosquitto passwd files are included, the passwords for all users
are included in *password.txt*. 

The passwd files included were all generated using the stock Eclipse software
[mosquitto_passwd](https://mosquitto.org/man/mosquitto_passwd-1.html), from 
Mosquitto version 2.0.5. In this version, the user is permitted to specify 
the hash type for each user added to the passwd file, so to reflect this, 
there are passwd files including hashes of each type (sha512 and sha512-pbkdf2),
plus one where the hash types are mixed.
