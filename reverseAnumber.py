def main():
    num = int(input())
    temp_copy = num
    result = 0

    while temp_copy > 0:
        digit = temp_copy % 10
        result = result * 10 + digit
        temp_copy = temp_copy // 10

    print(result)

main()
