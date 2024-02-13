def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


if __name__ == "__main__":
    while True:
        print('Enter number:')
        num = collatz(int(input()))
        if num == 1:
            print(num)
            break
        else:
            print(num)
