def raw_input(f_num,s_num):
    print("=====RESTART=====")
    sum=f_num+s_num
    print(f"The sum of {f_num} and {s_num} is:{sum}")
    subs=f_num-s_num
    print(f"The difference of {f_num} and {s_num} is:{subs}")
    product=f_num*s_num
    print(f"The product of {f_num} and {s_num} is:{product}")
    div=f_num//s_num
    rem=f_num%s_num
    print(f"The quotient of {f_num} and {s_num} is:{div} with remainder:{rem}")
raw_input(int(input("Enter the first number:")),int(input("Enter the second number:")))
