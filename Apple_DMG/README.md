UDIF
====
```
Sample Apple Disk Image files

Disk images created with OSX 10.84
Disk Utility version: 13 (450)
HSFJ Filesystem (HFS+ Journaled)
No partition map
Password "qwerty54"

Image formats are:
UDRW - udif read/write disk image // default type
UDSP - udif sparse disk image // grows along with contents
UDSB - udif sprase bundle disk image / and re-joined // see below

Encrypted and unencrypted.
Files have been zipped to conserve space, if they don't unzip correctly let me know.

--

UDRW and UDSP are single file formats, while UDSB is a folder/bundle appearing as a file in OSX.

This is a bundle directory layout:
name.sparsebundle/
name.sparsebundle/token
name.sparsebundle/bands/<0...ff> (up to 10,000 files or more)

A unencrypted bundle that has been re-joined (.sparsebundle/bands/ topped off by .sparsebundle/token) is
apparently identical to a .dmg file and is mounted by the system without a hitch. Encrypted,
the system will authenticate the disk image correctly but gives a "Not Recognized" error.
The following is from the log:

diskimages-helper[46907]: CEncryptedEncoding: need to repair aj.dmg
diskimages-helper[46907]: expected length: 122368, actual length: 15953408

Joining .sparsebundle/bands/... while leaving token in place didn't give any errors,
it mounted normally.

The following are byte positions/length of various data chunks within the disk images. 

Encrypted disk image:
+--------------------+-------------------+------------------+------------------------+
|                    | DMG               | Sparse Image     | Sparse Bundle (joined) |
+--------------------+-------------------+------------------+------------------------+
| "encrcdsa" header  | 0...122368        | 0...122368       | 0...122368             |
| <encrypted data>   | 122368...<EOF>    | 122368...<EOF>   | 122368...<EOF>         |
| Ending block       | <encrypted data>  | <null>           | <encrypted data>       |
+--------------------+-------------------+------------------+------------------------+

Unencrypted disk image:
+--------------------+-------------------+------------------+------------------------+
|                    | DMG               | Sparse Image     | Sparse Bundle (joined) |
+--------------------+-------------------+------------------+------------------------+
| Beginning block    | <null>            | sprs             | <null>                 |
| HFS+ signature     | 1024              | 5120             | 1024                   |
| Ending block       | <null>            | <null>           | <null>                 |
+--------------------+-------------------+------------------+------------------------+

In many aspects a sparse seems more different than the other two.
```
