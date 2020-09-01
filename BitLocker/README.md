===== OpenCL BitLocker =====

BitLocker is a full-disk encryption feature available in recent Windows versions (Vista, 7, 8.1 and 10) Ultimate, Pro and Enterprise.\\
BitLocker-OpenCL format attacks memory units encrypted using the User Password  (see the following picture) or the Recovery Password authentication methods.\\
Our attack has been tested on several memory devices encrypted with BitLocker on Windows 7, 8.1 and 10 (both compatible and not compatible mode).\\
You can find the standalone CUDA implementation here: https://github.com/e-ago/bitcracker\\

===== User Password authentication method =====

With this authentication method, the user can choose to encrypt a memory device by means of a password.

{{:john:bitcracker_img1.png?direct&400|}}

To find the password used during the encryption, see [[#Step 2: Extract the hash|Step 2: Extract the hash]]

===== Recovery Password authentication method =====

During the encryption of a memory device, (regardless the authentication method) BitLocker asks the user to store somewhere a Recovery Password that can be used to restore the access to the encrypted memory unit in the event that she/he can't unlock the drive normally. Thus the Recovery Password is a common factor for all the authentication methods and it consists of a 48-digit key like this:

<code>
236808-089419-192665-495704-618299-073414-538373-542366
</code>

To find the correct Recovery Password, see [[#Step 2: Extract the hash|Step 2: Extract the hash]].
For further details, see also [[https://docs.microsoft.com/en-us/windows/device-security/bitlocker/bitlocker-recovery-guide-plan|Microsoft docs]].

===== Step 1: Get the image of your encrypted memory device =====

In order to start the attack, you need to extract the image of your memory device encrypted with BitLocker.
For example, you can use the dd command:

<code bash>
sudo dd if=/dev/disk2 of=/path/to/imageEncrypted conv=noerror,sync
4030464+0 records in
4030464+0 records out
2063597568 bytes transferred in 292.749849 secs (7049013 bytes/sec)
</code>

===== Step 2: Extract the hash =====

In order to use the BitLocker-OpenCL format, you must produce a well-formatted hash of your encrypted image.
Use the //bitlocker2john// tool (john repo) to extract the hash from the password protected BitLocker encrypted volumes.

<code>
$ ../run/bitlocker2john -i /path/to/imageEncrypted
Opening file /path/to/imageEncrypted

Signature found at 0x00010003
Version: 8
Invalid version, looking for a signature with valid version...

Signature found at 0x02110000
Version: 2 (Windows 7 or later)

VMK entry found at 0x021100d2
VMK encrypted with user password found!
VMK encrypted with AES-CCM

VMK entry found at 0x021101b2
VMK encrypted with Recovery key found!
VMK encrypted with AES-CCM

$bitlocker$0$16$a149a1c91be871e9783f51b59fd9db88$1048576$12$b0adb333606cd30103000000$60$c1633c8f7eb721ff42e3c29c3daea6da0189198af15161975f8d00b8933681d93edc7e63f36b917cdb73285f889b9bb37462a40c1f8c7857eddf2f0e
$bitlocker$1$16$a149a1c91be871e9783f51b59fd9db88$1048576$12$b0adb333606cd30103000000$60$c1633c8f7eb721ff42e3c29c3daea6da0189198af15161975f8d00b8933681d93edc7e63f36b917cdb73285f889b9bb37462a40c1f8c7857eddf2f0e
$bitlocker$2$16$2f8c9fbd1ed2c1f4f034824f418f270b$1048576$12$b0adb333606cd30106000000$60$8323c561e4ef83609aa9aa409ec5af460d784ce3f836e06cec26eed1413667c94a2f6d4f93d860575498aa7ccdc43a964f47077239998feb0303105d
$bitlocker$3$16$2f8c9fbd1ed2c1f4f034824f418f270b$1048576$12$b0adb333606cd30106000000$60$8323c561e4ef83609aa9aa409ec5af460d784ce3f836e06cec26eed1413667c94a2f6d4f93d860575498aa7ccdc43a964f47077239998feb0303105d

</code>

As shown in the example, it returns 4 output hashes with different prefix:
  * If the device was encrypted using the User Password authentication method, bitlocker2john prints those 2 hashes:
    * $bitlocker$0$... : it starts the User Password fast attack mode (see [[#User Password authentication method|User Password Section]])
    * $bitlocker$1$... : it starts the User Password attack mode with MAC verification (slower execution, no false positives)
  * In any case, bitlocker2john prints those 2 hashes:
    * $bitlocker$2$... : it starts the Recovery Password fast attack mode (see [[#Recovery Password authentication method|Recovery Password Section]])
    * $bitlocker$3$... : it starts the Recovery Password attack mode with MAC verification (slower execution, no false positives)

Samples BitLocker images for testing are available here:
  * https://github.com/e-ago/bitcracker/tree/master/Images
  * https://github.com/kholia/libbde/tree/bitlocker2john/samples

===== Step 3: Attack! =====

Use the BitLocker-OpenCL format specifying the hash file:
<code>
./john --format=bitlocker-opencl --wordlist=wordlist target_hash
</code>

Currently, this format is able to evaluate passwords having length between 8 (minimum password length) and 55 characters (implementation reasons).
We will increase the max passwords size in the next release.

The mask you can use to generate Recovery Password is:
<code>
-mask=?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d[-]?d?d?d?d?d?d
</code>

Samples of User Password/Recovery Passwords dictionaries you can user are available here: https://github.com/e-ago/bitcracker/tree/master/Dictionary
===== Output =====

An output example is:

<code>

./john --format=bitlocker-opencl --wordlist=wordlist hash
Device 0: Tesla K80
Using default input encoding: UTF-8
Loaded 1 password hash (bitlocker-opencl [SHA-256 AES OpenCL])
Note: minimum length forced to 8
Press 'q' or Ctrl-C to abort, almost any other key for status
password@123 (?)

</code>

This OpenCL implementation has been tested on a GPU NVIDIA GeForce Titan X (Openwall), GPU AMD Radeon HD 7990 Malta and an Intel Core i7 CPU.
For additional information about performance, see https://github.com/e-ago/bitcracker#performance

===== Updates and changelog =====

12/19/2017
  * Now BitLocker-OpenCL supports 4 different attack modes: User Password fast attack, User Password with MAC verification (performance decreased), Recovery Password, Recovery Password with MAC verification (performance decreased)
  * Max password length increased to 55

Next Update:
  * Provide a Recovery Password dictionary

===== References, license and contacts =====

BitCracker OpenCL version developed by Elenago <elena dot ago at gmail dot com> in 2015\\
Copyright (c) 2015-2017 Elenago and Massimo Bernaschi (National Research Council of Italy), <massimo dot bernaschi at gmail dot com>\\
Licensed under GPLv2\\

You can find the standalone CUDA implementation here: https://github.com/e-ago/bitcracker\\
This is a research project; for any additional info or to report any bug please contact <elena dot ago at gmail dot com>
