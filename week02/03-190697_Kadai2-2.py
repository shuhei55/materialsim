import matplotlib.pyplot as plt

def f(x):
    return x**4-2.65*x**2-0.66*x+0.4284

def diff_f(x):
    return 4*x**3-2*2.65*x-0.66

def calc(s,delta=0.001):
    x = s
    num = 0
    while abs(f(x)) > delta:
        x = x - f(x) / diff_f(x)
        num += 1
    return s,x, num

result_file=open('result.txt','w')
result_file.write(str(calc(-2.0))+"\n")
result_file.write(str(calc(-0.5))+"\n")
result_file.write(str(calc(0.0))+"\n")
result_file.write(str(calc(1.5)))
result_file.flush()
result_file.close()
