Hidden TC volumes are just a second volume inside the same
file. You could give up the password to the "normal" one, and a
keep the hidden password secret still. Hidden volumes do not
require the password of the "non-hidden" volume.
-rich
(Made using TC 7.1a)
===============================================================================
TrueCrypt/TC-Volume/TC-Normal-Volume.txt
*NOTES:
  3 Keyfiles used, each had it's own algorythm to choose from
*Properties:
  Crypt : AES (keyfiles=*keyfile-1,2,3 | pass=truecrypt [all-lower])
  PriKey: 256
  SecKey: 256 (XTS)
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-RIPEMD-160
  Fmt Ver: 2

-Hidden- (also in TC-Normal-Volume.txt)
*NOTES:
  1 Keyfile used, same text file TC-Normal-Volume.txt
*Properties:
  Crypt:  AES (keyfile=RIPEMD-160-hidden-kf pass=TRUECRYPT [all-caps])
  PriKey: 256
  SecKey: 256
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-Whirlpool
  Fmt Ver: 2
===============================================================================

TrueCrypt/TC-Volume-2/TC-Hidden-2.txt
*NOTES:
  1 Keyfile used (RIPEMD-160-Keyfile)
*Properties:
  Crypt:  Serpent-Twofish-AES (keyfile=RIPEMD-160-Keyfile | pass=truecrypt [all-lower])
  PriKey: 768
  SecKey: 768
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-RIPEMD-160
  Fmt Ver: 2

-Hidden- (also in TC-Hidden-2.txt)
*NOTES:
  1 Keyfile used, same text file as above
*Properties:
  Crypt:  AES-Twofish (keyfile=RIPEMD-160-hidden-kf pass=TRUECRYPT [all-caps])
  PriKey: 512
  SecKey: 512
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-SHA-512
  Fmt Ver: 2
===============================================================================

TrueCrypt/TC-STD-Volume/TC-STD-Volume.txt
	Serpent (encryption), SHA-512 (hash), truecrypt(pwd), RIPEMD-160-keyfile
*NOTES:
  1 Keyfile used (RIPEMD-160-Keyfile)
*Properties:
  Crypt:  Serpent (keyfile=RIPEMD-160-Keyfile | pass=truecrypt [all-lower])
  PriKey: 256
  SecKey: 256
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-SHA-512
  Fmt Ver: 2
===============================================================================

TrueCrypt/TC-STD-Volume-2/TC-STD-Volume-2.txt
	AES (encryption), Whirlpool (hash), truecrypt(pwd), Whirlpool-keyfile
*NOTES:
  1 Keyfile used (Whirlpool-Keyfile)
*Properties:
  Crypt:  AES (keyfile=Whirlpool-keyfile | pass=truecrypt [all-lower])
  PriKey: 256
  SecKey: 256
  Blk Sz: 128
  Mode:   XTS
  PKCS-5 PRF: HMAC-Whirlpool
  Fmt Ver: 2
Rand pool  71464ba54bfd6246e9a1c0fb4c3679b6 (I was able to write these down when making the file, they may or maynot be correct)
Header key 3a61391f53d83c58d6066986355cc72e
Master key 183495c6e214742efb96a433d0af5f28
===============================================================================
