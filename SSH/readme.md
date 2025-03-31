# Testing the SSH format

Using SSH samples from the `john-samples` repository, save them in your working folder:

```bash
cp "$SAMPLES_PATH"/aes-256-ctr/id_rsa-aes256-ctr                 ./key/id_rsa-aes256-ctr
cp "$SAMPLES_PATH"/aes-256-ctr/id_rsa-aes256-cbc                 ./key/id_rsa-aes256-cbc
cp "$SAMPLES_PATH"/openssh-new-format-keys/ssh-new-format-1.key  ./key/1.key
cp "$SAMPLES_PATH"/openssh-new-format-keys/ssh-new-format-2.key  ./key/2.key
cp "$SAMPLES_PATH"/openssh-new-format-keys/ssh-new-format-3.key  ./key/3.key
cp "$SAMPLES_PATH"/openssh-new-format-keys/ssh-default.key       ./key/ssh-default.key
cp "$SAMPLES_PATH"/sample_ssh_private_keys/dsa_test.key          ./key/dsa.key
cp "$SAMPLES_PATH"/sample_ssh_private_keys/rsa_test.key          ./key/rsa.key
```

The list of passwords that crack the files listed above:

```
12345
diesel
openwall
openwall@123
password
qwerty
TestPassword
```

And/or create random "keys":

```bash
for i in {1..115}; do
    echo "-- Iteration: $i"
    string=$(tr -dc 'A-Za-z0-9.,*-+%' </dev/urandom | head -c $i)
    echo $string >> ./passwords.lst
    echo $string > ./secret
    #
    openssl ecparam -name secp521r1 -genkey | openssl ec -aes256 -out ./key/"$i".ec_aes256-dbc -passout file:./secret
    #
    ssh-keygen -f ./key/"$i".default -N "$string"
    #
    ssh-keygen -t rsa -b 4096 -f ./key/"$i".id_rsa-aes256-cbc  -Z aes256-cbc -N "$string"
    #
    ssh-keygen -t rsa -b 4096 -f ./key/"$i".id_rsa-aes256-ctr  -Z aes256-ctr -N "$string"
    #
    ssh-keygen -t ed25519 -o  -f ./key/"$i".ed25519-aes256-cbc -Z aes256-cbc -N "$string"
    #
    ssh-keygen -t ed25519 -o  -f ./key/"$i".ed25519-aes256-ctr -Z aes256-ctr -N "$string"
done
```

Test John the Ripper:

```bash
python3 ssh2john.py ./key/* > ./ssh-hashes.txt
./john ./ssh-hashes.txt --format=ssh --wordlist=./passwords.lst -pot=./tmp-ssh.pot ./ssh-hashes.txt
```
