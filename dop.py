from math import sqrt
import re

string1 = "$31x^2+13x+78=0$"
string2 = "$x^2+1=0$"
string3 = "$13x+78=0$"
string4 = "$31x^2+13x=0$"
string5 = "$21=0$"

pattern1 = r"([-]*\d*)x\^2"
pattern2 = r"([-]*\d*)x[^\^]"
pattern3 = r"([-]*\d*)="


def solution(string: str) -> None:
    rez1 = re.findall(pattern1, string)
    rez2 = re.findall(pattern2, string)
    rez3 = re.findall(pattern3, string)

    if rez1:
        if rez1[0]:
            A = int(rez1[0]); print(A)
        else:
            A = 1; print(A)
    else:
        A = 0; print(A)

    if rez2:
        if rez2[0]:
            B = int(rez2[0]); print(B)
        else:
            B = 1; print(B)
    else:
        B = 0; print(B)

    if rez3:
        if rez3[0]:
            C = int(rez3[0]); print(C)
        else:
            C = 0; print(C)
    else:
        C = 0; print(C)


    if not(A) and B:
        print(f"X = {-C / B}")

    elif not(A) and not(B) and C:
        print(int(string[1:string.find("=")]) == int(string[string.rfind("=")+1:-1]))

    else:
        D = B**2 - 4 * A * C; print(D)

        if D <= 0:
            print("no solutions in R")
        elif D == 0:
            print(f"X = {(-B + sqrt(D))/(2 * A)}")
        else:
            print(f"X1 = {(-B + sqrt(D))/(2 * A)}")
            print(f"X2 = {(-B - sqrt(D))/(2 * A)}")



solution(string5)
