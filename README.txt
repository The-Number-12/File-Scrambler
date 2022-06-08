This program can encrypt and decrypt files with a password of the users choice. 
I made this as a way to safely store private data in places where other people might see it. 
There are lots of other programs that do similar things, but I wanted to mess around with encryption.

How to use:
1. Make a new directory and put FileScrambler.py and any files/folders you want to encrypt into it.
2. Run  FileScrambler.py.
3. Type 3 to Set and confirm your password.
4. Type 1 to Encrypt your files.
5. When you want to decrypt your files Run FileScrambler.py again and type 2 then enter the password you picked to decrypt those files.

There are a few things you should be careful with when using this program.
Don't forget your password.
Don't try to edit encrypted files, always decrypt them first.
Don't try to manually edit the password.txt file that FileScrambler generates. 
	if you want to change your password run FileScrambler.py and type 3 (the text in that file is a salted version of your password not the password it's self, it might also be encrypted).
Don't edit the trackEncryptionState.txt file that the program generates.
Do keep the  password.txt and trackEncryptionState.txt files in the same directory as the files that you encrypted (it is probably a good idea to keep FileScrambler.py in that directory also)

The encryption is done using Fernet, and the password salting uses PBKDF2HMAC with SHA256.