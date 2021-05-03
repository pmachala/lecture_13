def recursive_nth_fibo(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)



def main():
    n = int(input("Zadejte pocet prvku n ="))
    n_th = recursive_nth_fibo(n)

    fib_seq = []
    for num in range(n + 1):
        fib_seq.append(recursive_nth_fibo(num))

    print(fib_seq)



if __name__ == '__main__':
    main()
