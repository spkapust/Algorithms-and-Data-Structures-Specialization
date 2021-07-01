# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    a = 0
    b = 0
    for i in range(n):
        if(numbers[i] > a):
            b = a 
            a = numbers[i]
        elif(numbers [i] > b): b = numbers[i]

    return a*b


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
