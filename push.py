from os import system as s 
import numpy as np
s("git add .")
s("git commit -m'{}'".format(np.random.uniform()))
s("git push robel master")
