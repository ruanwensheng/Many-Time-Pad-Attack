# Many Time Pad Attack Solution

In this project, I implemented a Many Time Pad (MTP) attack to recover a stream cipher key that was reused across multiple ciphertexts. The key idea is that when two ciphertexts use the same key, XORing them removes the key: `Ci ⊕ Cj = Pi ⊕ Pj`. I used this property to identify likely spaces in the plaintext and gradually reconstruct the key.

Here’s how I approached it:

1. I loaded 10 ciphertexts (`C1`–`C10`) and the target ciphertext `C11` from JSON files and converted them to bytes.  
2. For each ciphertext, I XORed it with all the others. I then checked each byte position: if the XOR produced a printable letter in at least 7 out of 9 comparisons, I considered that position likely to be a space.  
3. Using these detected spaces, I recovered the corresponding key bytes by XORing the ciphertext byte with the space character and stored them.  
4. After processing all ciphertexts, I applied the partially recovered key to `C11`. For positions where the key was known, the plaintext was revealed; unknown positions are shown as dots.  

The decrypted output reads:  
*"The secuet-mes.age.is: Wh.. usi|g ..str.am cipher, nev...use th. k.y .ore than onc."*  

From context and linguistic reasoning, the missing characters can be inferred.
