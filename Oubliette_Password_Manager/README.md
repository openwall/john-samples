Oubliette Password Manager - Sample files
=========================================

Hash creation example:
```
    for f in *.oub ; do echo $f ; echo -n '  ' ; ./oubliette2john.py $f ; done
    oubliette-blowfish-12345678.oub
      $oubliette-blowfish$16c863009dbc7a89fa26520aeeae5543beda0bbf41622be472d7c7320c8ea66f
    oubliette-blowfish-complex.oub
      $oubliette-blowfish$82ea2c652362c380349d6ac0d5a06d2ae9b164becc5a75103c2744b4d27fe35d
    oubliette-blowfish-complex-withdata-v15.oub
      $oubliette-blowfish$82ea2c652362c380349d6ac0d5a06d2ae9b164becc5a75103c2744b4d27fe35d
    oubliette-idea-12345678.oub
      $oubliette-idea$e82bb8b871ed9a2b7d77afce662325a2c522844e0e91bde104b8e4f68044e991
    oubliette-idea-complex.oub
      $oubliette-idea$9c846ab8c1dc703330521e7ca77489beded5d23b3aa821edea8f0324fbdb9f08
    oubliette-idea-complex-withdata-v15.oub
      $oubliette-idea$9c846ab8c1dc703330521e7ca77489beded5d23b3aa821edea8f0324fbdb9f08
```
Testing the passwords:
```
    john -w:oubliette-passwords.txt *.hash
```
The complex test vector is originally made in ISO-8859-1 and thus `--target-encoding=iso-8859-1` would be needed. In order to avoid that, the hint file `oubliette-passwords.txt` now contains two versions of it, one in UTF-8 and one in ISO-8859-1, so that extra option is not needed.

See `docs/ENCODINGS` in the john tree for more information.
