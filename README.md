# File-Scrambler
Do you have files you dont want other people seeing? With this program you can scramble all your files into meninges spaghetti when you arent using then, then unscramble them when you want them back.

File Scrambler is encryption software that makes other people not able to read your files.
To ues file scrambler you will need to have python and the libraries listed at the top of the file (maybe ill make a .exe for it at some point to make this easier)

Move the script into the folder you want to encrypt. 

Run the python script. Set a password that you will remember. Only ever set/change your password through the script its self, editing the password file yourself will not work. 

To encrypt files just run the script and select the encrypt option. Everything in the same directory as the script will be encrypted (except for the script its self and the trackEncryptionState file it creates) anything in a sub directory below where the script is ran from will also be encrypted. 

To decrypt  files just run the script again, type in your password and all of the files will be decrypted.

 If you encrypt your files people with filescrambler people wont be able to find them in the recycle bin,  under deleted files, or be able to read them without the password. If you are just trying to  from other people who use the same computer as you this is fine. However some of the unencrypted data from your files might still be written into space on your hard drive that is now considered empty. If you want to be extra cautious you can overwrite the empty space on your hard drive with other data to ensure that no one can recover your files (there are a number of programs that do this or you can do it manually).

Please don't use fileScrambler to hide evidence of your illegal activity. If you are are doing anything illegal that you want to hide from the the FBI, you would be better off using other software that never saves unencrypted data to your hard drive. That will save you the time and effort of constantly overwriting the empty space on your hard drive (and save me from involvement in your evil deeds). Look for something that loads encrypted data from hard drive into ram, decrypts it in ram for you to use it, and encrypts it again before ever saving it back to hard drive. Also consider not doing anything illegal.
