import bcrypt

def encrypt(input):
    text=input.encode('utf-8')

    salt = bcrypt.gensalt()
    #Hashing
    hashed = bcrypt.hashpw(text, salt)

    #printing the salt
    #print("Salt :",salt)

    # printing the hashed
    #print("Hashed",hashed)
    return hashed

with open("text.txt","r") as f:
    text=f.read()
    result=str(encrypt(text))


print(str(result))

print("Success! \nFile has been encrypted")
