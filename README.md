# KawaiiXOR
Tax-writeoff encryption algorithm to send confidental messages


# How does it work?
The plaintext is split into __3__ chunks of 256 bits

1. XORize the first chunk with the selected password

2. XORize the second chunk with hash of unencrypted first chunk

3. XORize the third chunk with hash of unencrypted 2nd chunk

## Interface?

When you run `main.py`, You are greeted with a choice of encrypting or decrypting a text.

For encryption, you will need to provide your plain text, and then provide your password to encrypt your text.

**Side Note: If you and your encrypting partner plan on having the same password, Edit the main.py file and scroll to the bottom. Then remove the `input()` field on password and replace it with your choosing password, You can do this same process on the decrypt section too.**

# Side Notes
- When you forget a password, that message is **GONE**
- Using KawaiiXOR for simple messages such as `hi` is not healthy, use it when you are in secretive environments such as telling people that a certain someone is an alt of a banned person
- Avoid encrypting long sentences, something even as much as `uwutastic` will generate a lot of zeros at the beginning, Passphrases have little effect on this
