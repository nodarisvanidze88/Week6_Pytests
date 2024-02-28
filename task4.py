import random
import string

def main():
    while True:
        try:
            user = int(input("Give us the length of the password: "))
            print(pass_gen(user))
            break
        except:
            pass

def pass_gen(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(all_chars, k=length))
    return password


if __name__=="__main__":
    main()
