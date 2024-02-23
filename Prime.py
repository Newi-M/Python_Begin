value = int(input('Enter max value up to which you want to find prime: '))


def prime(num):

    primes = ""
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j != 1 and j != num:
                if i % j == 0:
                    break
                else:
                    if i != 1:
                        primes += ", "
                    primes += str(i)
                    break

            j += 1

        i += 1

    return primes


prime_numbers = prime(value)
print('The prime numbers are: ', prime_numbers)
