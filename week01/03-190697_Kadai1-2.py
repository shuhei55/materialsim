import random

sum=0
million=1000000
test_file=open('03-190697_kadai1-2.result.txt','w')

for i in range(million):
    r1=random.random()
    r2=random.random()
    ans=r1**2+r2**2
    if ans < 1:
        sum+=1

print((sum / million)*4)
test_file.write(str((sum/million)*4))
test_file.flush()
test_file.close()
