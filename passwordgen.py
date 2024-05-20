import string
import random

a = string.ascii_letters + string.punctuation +string.digits
lst = random.choices(a,k=16)
password = "".join(lst)

print("your new pasword is\n",password)