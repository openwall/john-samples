This repository contains all files from https://openwall.info/wiki/john/sample-non-hashes
unpacked and somewhat cleaned up.

Normally, the password to crack a sample is included in the file name (e.g.
`zip1_testpassword#.zip` has a password of `testpassword#`) or in a file
near it, such as `password.txt` which can be used directly as a wordlist.

If all else fails, try really simple passwords including `openwall` and
`hashcat`.  Or if you're lucky, the latest John Jumbo has the sample as a test
vector. To dump all such test vectors' passwords to a wordlist, try this:

    ./john --format=cpu --list=format-tests | cut -f4 | ./unique all_tests.lst
