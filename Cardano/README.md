A [`secret.key`](https://github.com/input-output-hk/daedalus/blob/0b74fb81803f507ac859464bbadaed86c0769483/tests/wallets/e2e/documents/import-files/Secrets-1.0/secret.key) is a CBOR binary encoded deprecated format of key store for the Cardano's [Daedalus wallet](https://daedaluswallet.io/) (~v1.0.1 late 2017 and early 2018) containing old Byron era based encrypted secret keys.

The structure of the key file is defined [here in cardano-sl](https://github.com/input-output-hk/cardano-sl/blob/1499214d93767b703b9599369a431e67d83f10a2/lib/src/Pos/Util/UserSecret.hs#L107) node's code repository.


## Passwords

There are six wallets stored in the secret.key file but only one, the first, has a valid decryption password which is: "Secret1234"
