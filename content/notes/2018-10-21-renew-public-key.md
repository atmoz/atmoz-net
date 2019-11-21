---
tags: [pgp]
---

# Renew public key

* Save public key to external storage
* Have the private key handy (yubikey or other storage)
* Boot Tails in offline mode
  * Remove any existing keys from GPG: `gpg --delete-keys <key>`
  * Import public and private keys: `gpg --import key.asc`
  * Renew subkeys:
    * `gpg --edit-key <key>`
    * `key 1`, `key 2`, etc.
    * `expire`
    * `save`
  * Export new public key: `gpg --export --armor > key.asc`
  * Save public key to external storage
* Boot back to normal OS
  * Copy new public key to disk and import: `gpg --import key.asc`
  * Send keys to key servers: `gpg --send-keys <key>`
  * Keybase public key can be updated via the webpage
* Add a reminder in your calendar a couple of weeks before the expiration date
