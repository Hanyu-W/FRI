def main():
    n = int(input())
    pts = 4
    squares = 1
    for i in range(n):
        pts += squares
        squares *= 4

main()