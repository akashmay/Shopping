import random
import string



def Random_string(size=10,chars = string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for x in range(size))