def trib_seq(n, result, start):
    if n < 2:
        return n
    else:
        x = 0
        if len(result) > 3:
            start[0] += 1
        for i in result[start[0]:]:
            x += i
        return x


def tribonacci_sequence(number):
    result = []
    start = [0]
    for i in range(1, number + 1):
        result.append(trib_seq(i, result, start))
    return print(* result, sep=" ")


numb = int(input())

tribonacci_sequence(numb)
