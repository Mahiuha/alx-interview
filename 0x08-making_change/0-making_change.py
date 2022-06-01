#!/usr/bin/python3
""" MakeChange module"""


def makeChange(coins, total):
    """
    find the minimum number of coins that meets the total number
    """
    if total <= 0:
        return 0

    if not coins or min(coins) > total:
        return -1

    INT_MAX = 1 << 32
    totalSize = [INT_MAX] * (total + 1)

    totalSize[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                totalSize[i] = min((totalSize[i-coin] + 1), totalSize[i])

    return totalSize[total] if totalSize[total] != INT_MAX else -1
