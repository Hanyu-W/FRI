def main():
    n = int(input())
    sum = 0
    for i in range(n):
        num = int(input())
        pow = num % 10
        num //= 10
        num **= pow
        sum += num
    print(sum)

main()