#!/usr/bin/python3

'''prime game'''


def isWinner(x, nums):
    '''function that is used in the prime game '''
    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_prime = [True for _ in range(max(max_num + 1, 2))]

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    is_prime[0] = is_prime[1] = False

    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    maria_score = 0
    for n in nums:
        maria_score += is_prime[n] % 2 == 1

    if maria_score * 2 == len(nums):
        return None
    elif maria_score * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
