import math #imports more complex mathematics

p = 257 #creates variable p and assigns value of 257
q = 53 #creates variable q and assigns value of 53
e = 65537 #creates variable e and assigns value of 65537
d = 1 #creates variable d and assigns value of 1
check = False #creates variable check and assigns value of False
temp = 0 #creates variable temp and assigns value of 0
CipherText = 0 #creates variable CipherText and assigns value of 0
PlainText = 0 #creates variable PlainText and assigns value of 0
Hex_Hash = hex(0x14959484) #creates variable Hex_Hash and assigns hex value of 0x14959484
Int_Hash = int(Hex_Hash, 16) #creates variable Int_Hash and assigns integer value of Hex_Hash
Mod_Num = 1048575 #creates variable Mod_Num and assigns value of 1048575
Hash = 0 #creates variable Hash and assigns value of 0
Digital_Sign = 0
DS_Undo = 0

n = p*q #calculates the value of n
phi_n = (p-1) * (q-1) #calculates the value of phi_n

print ("Prime Number p = ", p) #displays prime number p
print ("Prime Number q = ", q) #displays prime number q

while check == False: #while check has the boolean value of False, loop
    temp = (e * d) % phi_n #temp is equal to e multiplied by d, mod phi_n
    if temp == 1: #if temp is equal to 1, continue
        check = True #assign True to check, breaking out the loop
    else: #if temp is not equal to 1, continue
        d = d + 1 #add 1 to the value of d

print("Public Key = (", e,", ", n,")") #displays the values of the public key

print("Private Key = (", d,", ", n,")") #displays the values of the private key
print ("HI encoded = 0809\nTherefore the plaintext is 809")
CipherText = (809 ** e) % n #encrypts the plaintext
print ("Ciphertext = ", CipherText) #displays the ciphertext
PlainText = (CipherText ** d) % n #decrypts the ciphertext
print ("Decrypted cipher text = ", PlainText, "\n") #displays the plaintext

print("To digitally sign the message, alice needs to use her private key to encrypt") #displays the message in the bracket
print("Private Key = (6613, 12709)\nPublic Key = (65537, 12709)") #displays the message in the bracket
print("HI in plaintext will be used to sign instead of the hash") #displays the message in the bracket
Digital_Sign = (809 ** 6613) % 12709 #creates the digital signature
print("Digital Signature = ", Digital_Sign) #displays the digital signature
DS_Undo = (Digital_Sign ** e) % 12709 #decrypts the digital signature
print ("Undone digital signature is: ", DS_Undo, "\n") #displays the decrypted digital signature

print("For hashing, HIYA into hex is 48 49 59 41") #displays the message in the bracket
print("Reversed makes it 14959484") #displays the message in the bracket
print("Converting into decimal creates ", Int_Hash) #displays the message in the bracket
Int_Hash = Int_Hash % Mod_Num #mods Int_Hash by Mod_Num
print ("Modding by ", Mod_Num, " gets the answer: ", Int_Hash) #displays the message in the bracket
Hash = hex(Int_Hash) #converts Int_Hash into a hex number
print("After converting into hex, the hash value is: ", Hash) #displays the hash value