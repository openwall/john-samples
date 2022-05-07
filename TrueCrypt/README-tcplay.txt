Info from tcplay in addition to README.txt

----------------------------------------------------------------------
  General info about tcplay and usage

tcplay uses devices. losetup can be used to make loop device from a
regular file. Option --info prints information about the volume if
passphrase is correct (tcplay decrypts header).

Option --keyfile= is used to specify a keyfile. It can be used
multiple times to specify multiple keyfiles.

It is possible to use tcplay --info without root if user has read
permissions on (loop) device. Debian provides tcplay as
/usr/sbin/tcplay that is not in default PATH for users. So the full
path should be used.

Both losetup and tcplay give informative feedback on misuse.

'TrueCrypt# ' below is a prompt of root shell standing in
john-samples/TrueCrypt folder. Most of the other text is output.
Comments are indented. losetup commands for individual files are
omitted.

  Tested version of tcplay:
TrueCrypt# tcplay --version
tcplay v1.1

  Setup a loop device:
TrueCrypt# losetup /dev/loop1 tc-hackthis

  Repeated attempt would result in error:
TrueCrypt# losetup /dev/loop1 tc-hackthis
losetup: tc-hackthis: failed to set up loop device: Device or resource busy

  Trying wrong password:
TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: asdf

Incorrect password or not a TrueCrypt volume
  [... asked again for password ...]

  Trying correct password:
TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: hackthis

Device:			/dev/loop1
  [... more info ...]

  Revert the setup of the loop device:
TrueCrypt# losetup --detach /dev/loop1

  Attempt to run tcplay again without setup loop device:
TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: asdf

Error reading from file /dev/loop1
error read hdr_enc: /dev/loop1

  Repeated attempt to revert the setup:
TrueCrypt# losetup --detach /dev/loop1
losetup: /dev/loop1: detach failed: No such device or address

----------------------------------------------------------------------
  File: tc-hackthis

TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: hackthis

Device:			/dev/loop1
PBKDF2 PRF:		SHA512
PBKDF2 iterations:	1000
Cipher:			SERPENT-256-XTS,TWOFISH-256-XTS,AES-256-XTS
Key Length:		1536 bits
CRC Key Data:		0x4dcab528
Sector size:		512
Volume size:		1536 sectors
IV offset:		256 sectors
Block offset:		256 sectors

----------------------------------------------------------------------
  File: tc-openwall

TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: openwall

Device:			/dev/loop1
PBKDF2 PRF:		RIPEMD160
PBKDF2 iterations:	2000
Cipher:			AES-256-XTS
Key Length:		512 bits
CRC Key Data:		0xab4903e7
Sector size:		512
Volume size:		1536 sectors
IV offset:		256 sectors
Block offset:		256 sectors

----------------------------------------------------------------------
  File: tc-password

TrueCrypt# tcplay --info -d /dev/loop1
Passphrase: password

Device:			/dev/loop1
PBKDF2 PRF:		SHA512
PBKDF2 iterations:	1000
Cipher:			AES-256-XTS
Key Length:		512 bits
CRC Key Data:		0xfc4dd18c
Sector size:		512
Volume size:		1536 sectors
IV offset:		256 sectors
Block offset:		256 sectors

----------------------------------------------------------------------
  File: TC-STD-Volume/TC-STD-Volume.txt

TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-STD-Volume/RIPEMD-160-Keyfile
Passphrase: truecrypt

Device:			/dev/loop1
PBKDF2 PRF:		SHA512
PBKDF2 iterations:	1000
Cipher:			SERPENT-256-XTS
Key Length:		512 bits
CRC Key Data:		0x338ac7c6
Sector size:		512
Volume size:		5632 sectors
IV offset:		256 sectors
Block offset:		256 sectors

----------------------------------------------------------------------
  File: TC-STD-Volume-2/TC-STD-Volume-2.txt

TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-STD-Volume-2/Whirlpool-Keyfile
Passphrase: truecrypt

Device:			/dev/loop1
PBKDF2 PRF:		whirlpool
PBKDF2 iterations:	1000
Cipher:			AES-256-XTS
Key Length:		512 bits
CRC Key Data:		0xeec847f2
Sector size:		512
Volume size:		5632 sectors
IV offset:		256 sectors
Block offset:		256 sectors

----------------------------------------------------------------------
  File: TC-Volume/TC-Normal-Volume.txt

TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-Volume/RIPEMD-160-Keyfile-1 --keyfile=TC-Volume/SHA-512-Keyfile-2 --keyfile=TC-Volume/Whirlpool-Keyfile-3
Passphrase: truecrypt

Device:			/dev/loop1
PBKDF2 PRF:		RIPEMD160
PBKDF2 iterations:	2000
Cipher:			AES-256-XTS
Key Length:		512 bits
CRC Key Data:		0x6a69b1df
Sector size:		512
Volume size:		5632 sectors
IV offset:		256 sectors
Block offset:		256 sectors


TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-Volume/RIPEMD-160-hidden-kf
Passphrase: TRUECRYPT

Device:			/dev/loop1
PBKDF2 PRF:		whirlpool
PBKDF2 iterations:	1000
Cipher:			AES-256-XTS
Key Length:		512 bits
CRC Key Data:		0x917cb0f4
Sector size:		512
Volume size:		3840 sectors
IV offset:		1792 sectors
Block offset:		1792 sectors

----------------------------------------------------------------------
  File: TC-Volume-2/TC-Hidden-2.txt

TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-Volume-2/RIPEMD-160-Keyfile
Passphrase: truecrypt

Device:			/dev/loop1
PBKDF2 PRF:		RIPEMD160
PBKDF2 iterations:	2000
Cipher:			AES-256-XTS,TWOFISH-256-XTS,SERPENT-256-XTS
Key Length:		1536 bits
CRC Key Data:		0x432ca8dc
Sector size:		512
Volume size:		5632 sectors
IV offset:		256 sectors
Block offset:		256 sectors


TrueCrypt# tcplay --info -d /dev/loop1 --keyfile=TC-Volume-2/SHA-512-kf
Passphrase: TRUECRYPT

Device:			/dev/loop1
PBKDF2 PRF:		SHA512
PBKDF2 iterations:	1000
Cipher:			TWOFISH-256-XTS,AES-256-XTS
Key Length:		1024 bits
CRC Key Data:		0xa5d3eb2a
Sector size:		512
Volume size:		3840 sectors
IV offset:		1792 sectors
Block offset:		1792 sectors
