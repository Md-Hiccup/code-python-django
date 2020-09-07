def sol1():
    expenses = [2200, 2350, 2600, 2130, 2190]

    # 1. In Feb, how many dollars you spent extra compare to Jan.
    cmp = expenses[1] - expenses[0]
    print("Extra spent in Feb:", cmp)

    # 2. Total Expense in first quarter (3 months) of the year
    quart = expenses[0] + expenses[1] + expenses[2]
    print("Total Expenses in 1st quarter:", quart)

    # 3. Find exactly 2k spent in any month
    print("Expense spent 2k in any month:", 2000 in expenses)

    # 4. Add 1980 to June month
    expenses.append(1980)
    print("After adding June expenses:", expenses)

    # 5. After returned item in April of 200$ worth
    expenses[3] = expenses[3] - 200
    print("After returned item in April:", expenses)

def sol2():
    heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

    # 1. Length of the list
    print("length:", len(heros))

    # 2. Add 'black panther' at end of the list
    heros.append('black panther')
    print("After adding black panther:", heros)

    # 3. Add 'black panther' before 'hulk'
    heros.remove('black panther')
    heros.insert(3, 'black panther')
    print("Add black panther after hulk:", heros)

    # 4. Replace 'thor' and 'hulk' with 'doctor strange' with one line of code
    heros[1:3] = ["doctor strange"]
    print("Replace thor and hulk with doctor strange:", heros)

    # 5. sort list use dir() for help
    heros.sort()
    print("Sort heros list:", heros)

def sol3():
    max_numb = int(input("Enter max number\n"))
    ls = []
    for i in range(0, max_numb):
        if i%2 != 0:
            ls.append(i)
    print("Odd number list:", ls)

if __name__ == "__main__":
    sol1()

    sol2()

    sol3()
