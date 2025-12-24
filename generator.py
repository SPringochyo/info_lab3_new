from random import randint

cmplx = []

for _ in range(100):
    A = randint(2,123)
    B = randint(2,123)
    C = randint(2,123)

    string1 = f"${A}x^2+{B}x+{C}=0$"
    string2 = f"${A}x^2+{C}=0$"
    string3 = f"${B}x+{C}=0$"
    string4 = f"${A}x^2+{B}x=0$"
    string5 = f"${A}x^2-{B}x+{C}=0$"
    string6 = f"${A}x^2+{C}=0$"
    string7 = f"${A}x^2+{B}x-{C}=0$"
    string8 = f"${B}x-{C}=0$"
    string9 = f"${A}x^2-{B}x=0$"
    stringA = f"${C}=0$"

    cmplx.append(string1)
    cmplx.append(string2)
    cmplx.append(string3)
    cmplx.append(string4)
    cmplx.append(string5)
    cmplx.append(string6)
    cmplx.append(string7)
    cmplx.append(string8)
    cmplx.append(string9)
    cmplx.append(stringA)

flag = 0
v_flag = 1

for i in range(1000):
    a = cmplx[randint(0, 999 - i)]
    del cmplx[cmplx.index(a)]

    if flag != 5:
        print("\t" + a)
        flag += 1
    else:
        print(f"\nВариант {v_flag}")
        print("\t" + a)
        flag = 1
        v_flag += 1
