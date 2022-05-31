fuel = 19
power = [40, 30, 20, 10]
distances = [1000, 2000, 3000, 4000]


def solution(fuel, powers, distances):
    print(fuel)
    print(powers)
    print(distances)

    barrel = [0] * len(powers)
    times = [0] * len(powers)
    # visited = [0] * len(powers)

    # 배분 초기화
    equal_size = fuel // len(powers)

    for i, power in enumerate(powers):
        if i + 1 == len(powers):
            barrel[i] = fuel
        else:
            barrel[i] = equal_size
            fuel -= equal_size

    print("배분 초기화: ", barrel)

    check = 0
    result = 1e9

    while (True):
        check += 1
        count = 0

        times = [0] * len(powers)

        while (True):
            count += 1
            if 0 in times:
                for i, data in enumerate(barrel):
                    print("cal")
                    if times[i] != 0:
                        continue
                    else:
                        if count > data:
                            dist = ((data * data * powers[i]) / 2) + ((count - data) * data * powers[i])
                        else:
                            dist = (count * count * powers[i]) / 2

                        if dist >= distances[i]:
                            times[i] = count

            else:
                break
        print("times : ", times)

        temp_result = max(times)
        print("result : ", result, temp_result)

        if result == temp_result:
            print("nothing change")
            break
        else:
            result = temp_result

        if max(times) - min(times) > 1:
            maxi = max(times)
            index1 = times.index(maxi)

            mini = min(times)
            index2 = times.index(mini)

            barrel[index1] += 1
            barrel[index2] -= 1
        else:
            break

        if check == 8:
            break

    return max(times)

print(solution(fuel, power, distances))




