#Write a program to count remaining mobile data daily.

data = 2000   # MB

while True:
    used = int(input("Enter how much u used: "))

    if used <= data:
        data = data - used
        print("Show data remaining:", data)

        if data <= 0:
            print("Data finished!!")

    else:
        print("Wrong input!! Used is higher than original data!!")

    if input("Continue(yes/no)? ") != "yes":
        break
