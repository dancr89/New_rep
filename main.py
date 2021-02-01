def rec_sums(n):
    if n == 0:
        return 0, 0, 0

    #return n + rec_sums(n - 1)
    total_sum, even_sum, odd_sum = rec_sums(n - 1)

    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum


total_sum, even_sum, odd_sum = rec_sums(5)
print(rec_sums(5)) #total_sum = 15, even_sum=6, odd_sum=9