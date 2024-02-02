def main():
    n = int(input())
    for i in range(n):
        input_list = [int(x) for x in input().split()]
        sum = 0
        for i in range(1, input_list[0] + 1):
            sum += input_list[i] - 1
        sum += 1
        print(sum)

main()

