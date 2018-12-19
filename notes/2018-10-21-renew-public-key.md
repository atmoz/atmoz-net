---
tags: [pgp]
---

# Renew public key

* Save public key to external storage
* Boot Tails in offline mode
* Make private key available for use
* Renew subkeys:
** `gpg --edit-key <key>`
** `key 1`, `key 2`, etc.
** `expire`
** `save`
* Export new public key: `gpg --export --armor > key.asc`
* Save public key to external storage
* Boot back to normal OS
* Copy new public key to disk and import: `gpg --import key.asc`
* Send keys to key servers: `gpg --send-keys <key>`
