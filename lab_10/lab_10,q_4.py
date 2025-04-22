import os
import shutil
sd = "C:/college/sem2"
fc= "C:/college/sem2/ee"
dd = "C:/college/sem2/maths"
os.makedirs(dd)
p1 = os.path.join(sd,fc)
p2 =os.path.join(dd,fc)
shutil.copy(p1,p2)
print("file copied")
