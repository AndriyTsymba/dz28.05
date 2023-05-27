##3
import random
class PasswordGenerator:
    def __init__(self,length,characters):
        self.length = length
        self.characters = characters

    def generate_password(self):
        password = ''.join(random.choice(self.characters) for i in range(self.length))
        return password
password_gen = PasswordGenerator(length = 10 , characters = "aftrwddt455@#!%^%))_*SJHfdge")
print(password_gen.generate_password())
print(password_gen.generate_password())
print(password_gen.generate_password())