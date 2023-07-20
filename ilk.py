liste = ["Demhat","EmreS","EmreG","Durmus","Cevaplar","Canberk"]
import os
import shutil
filename = "01_DeepLearning"
for item in liste:
    try:
        os.mkdir(f"/workspace/KordSADLPython/Exercises/{item}")
    except:
        pass 
    try:
        os.mkdir(f"/workspace/KordSADLPython/Exercises/{item}/data")
    except:
        pass
    cFile = "banknotes.csv"
    source = f"/workspace/KordSADLPython/Documents/data/{cFile}"
    target = f"/workspace/KordSADLPython/Exercises/{item}/data/{cFile}"
    shutil.copy(source,target)
    open(f"Exercises/{item}/{filename}.ipynb","ab+")



""" 
   Tip         kilo    fiyat
0  elma         10      12
1  armut        25      16
2  portakal     30      12
3  mandalina    12      35
"""

