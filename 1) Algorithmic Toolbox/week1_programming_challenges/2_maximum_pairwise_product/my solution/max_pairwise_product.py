# python3

def max_pairwise_product(numbers):
    a = 0
    b = 0
    for x in numbers:
        if x > a: 
            a = x
	    elif x > b: 
            b = x
    return a*b


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
