# One-Time-Pad-Algorithm
This work is a simple implementation of the One Time Pad algorithm written in Python.

One Time Pad algorithm also known as Vernam Cipher, is a method of encrypting alphabetic plain text. It is one of the substitution techniques which converts plain text into ciphertex, meaning we assign a number to each character of the plaintext.

![otp](https://user-images.githubusercontent.com/93947087/163680487-bb76cffa-424c-49be-8fa9-69996b6b7fc6.png)

Relation between the key and plain text: 
In this algorithm, the length of the key should be equal to that of plain text.

When using an OTP, a string of random numbers is generated and shared between two or more individuals who want to communicate securely. Each letter of the message is then shifted by the corresponding number within the OTP, so each letter has its own individual key.

## Using our program
The program is fairly easy to use, the options are presented in a list as shown below.

![cmd](https://user-images.githubusercontent.com/93947087/163680750-65f740d9-bca9-4642-8752-2980596ccde4.PNG)


[1] In order to encrypt any data you may want to communicate in a secure fashion you must generate one or several One Time Pads. After choosing the first option you will be required to input the number of pads you want to generate, as well as the maximum length which should be equal or longer than the length of the plaintext.
This way you have generated your One Time Pad and are now ready to encrypt some data.

[2] When selecting the second option consequently you also need to select which One Time Pad you want to use. You will do so by typing otp_.txt.
The way our program works is that when it asks you how many One Time Pads you want to generate, if for example you want to generate 3 One Time Pads then it will create 3 text files named otp0.txt, otp1.txt, otp2.txt respectively. 
Next the program will ask for the message/data you want to encrypt.
The last step for encrypting will be assigning a name for the encrypted data file in accordance to the enc_.txt format.

[3] In case you may want to decrypt a message it is implied that you have first of all, the encrypted message (ciphertext) and also the One Time Pad that was used to encrypt that message. So you will need to define the enc_.txt and also the otp_.txt

Note: The One Time Pad used to decrypt the message should be the same as the One Time Pad that was used to do the encryption.

[4] This option enables the user to delete all One Time Pad text files (otp.txt) that were generated during the process.

[5] By selecting this last option, you will be quitting the program.

## Project creators:
① Blend Gashi

② Blendi Povataj

③ Bleona Jashari

④ Blerande Azemi
