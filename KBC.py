# KBC

question=[
    ["1. What is the output of the following code: System.out.println(""Hello "" + 5);","Hello 5","5","Hello 5","Error",3],
    ["2. What is the output of the following code: int x = 5; int y = x++; System.out.println(y);","5","6","4","Error",1],
    ["3. What is the output of the following code: System.out.println(""Hello"".substring(2));","Hello","llo","He","Error",2],
    ["4. What is the output of the following code: int x = 5; int y = x * 2; System.out.println(y);","5","10","2","Error",2],
    ["5. What is the time complexity of a linear search algorithm?","0(n)","0(n-1)","0(n!)","None",1],
    ["6. How many types of errors can occur in a Java program?","1","2","3","4",3],
]

levels=[1000,2000,4000,8000,16000,32000]
money=0
for i in range(0,len(levels)):
    print(f"\nQuestion for RS:{levels[i]}\n")
    print(question[i][0])
    print(f"a.{question[i][1]}               b.{question[i][2]}")
    print(f"c.{question[i][3]}               d.{question[i][4]}")

    inp=int(input("Enter Option from 1-4 = "))
   if inp>4:
        raise ValueError("Value error")
    else:
        if(inp==question[i][5]):
            print("Correct")
            money=money+levels[i]
            print(f"\nmoney won is RS {money}")

        else:
            print("Wrong")
            print(f"\nmoney won is RS {money}")
