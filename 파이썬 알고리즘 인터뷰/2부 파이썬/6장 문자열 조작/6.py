data = input()
print("input : ",data)


while True:
    if data == "":
        print("nothing")
        break

    if data == data[::-1]:
        print(data)
        break

    else:
        data = data[:-2]