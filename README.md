# KawaiiXOR / ~~Sp~~litXOR / ~~Secur~~eXOR
[![wakatime](https://wakatime.com/badge/github/Special-Rocket-Agents/KawaiiXOR.svg)](https://wakatime.com/badge/github/Special-Rocket-Agents/KawaiiXOR)

Tax-writeoff encryption algorithm to send confidental messages


# How does it work?
The plaintext is split into __3__ chunks of 256 bits

1. XORize the first chunk with the selected password

2. XORize the second chunk with hash of unencrypted first chunk

3. XORize the third chunk with hash of unencrypted 2nd chunk

## Interface?

When you run `main.py`, You are greeted with a choice of encrypting or decrypting a text.

For encryption, you will need to provide your plain text, and then provide your password to encrypt your text.

The Program will then spit out the encrypted text and it should look like this:
```00000000000000000000000000537065636961353d1a430a17116114080f0607```

Try figuring that out now ;)

The Decryption process is dangrously the same as the encryption one.

The program will ask your for the encrypted hex, then will ask you for the passphrase that was used to encrypt the text. It will then get out the correct text if done correctly.

**Side Note: If you and your encrypting partner plan on having the same password, Edit the main.py file and scroll to the bottom. Then remove the `input()` field on password and replace it with your choosing password, You can do this same process on the decrypt section too.**

# Side Notes
- When you forget a password, that message is **GONE**
- Using KawaiiXOR for simple messages such as `hi` is not healthy, use it when you are in secretive environments such as telling people that a certain someone is an alt of a banned person
- Avoid encrypting long sentences, something even as much as `uwutastic` will generate a lot of zeros at the beginning, Passphrases have little effect on this
- Should you enter the Encryption Hex or the Passphrase wrong during the decryption process, the program will not notify you of it being incorrect but rather result in a bunch of symbols and letters. For now the only way of telling the decryption was succesful is to receive a fluent sentence or word instead of blabs.
- Don't go too easy on the passphrase part, so even if someone snitches to the admins and shows them this algorithm, they still need to figure out the password to decrypt it fully.
- When pronouncing KawaiiXOR, Pronounce it as KawaiiZOR and not KawaiiExo-Ar, Same goes for SplitXOR but not SecureXOR. When pronouncing SecureXOR, pronounce it as SecureExor (not SecureX-O-R)

# Credits?

Arezalgamer89 - the python implementation

[Breadtard](https://github.com/breadtard) - for making this encryption algorithm

NarratingSince86 (specialrocketagents@gmail.com) - Emotional Support

# License and PR
MIT, MIT just do whatever you want with the code

I tested this a lot on sensitive servers and they did not work (banned)
feel free to smash a PR in if you made any fixes or anything good basically honestly
