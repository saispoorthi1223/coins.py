'''
you are given an integer array coims representing coins of different denominations and an integer amount representing
a total amount of money
return the fewest number of coins that you need to makeup that amount. if that amount of money cannot be made up by any
combination of coins, return -1:
you may assume that you have initfinite number of each kind of coins.
input: coins=[1,2,5],amount=11
output: 3      111=5+5+1
input: coins=[2].amount=3
output:-1
'''
def coinCharge(coins,amount):
    n=len(coins)
    dp=[amount+1]*(amount+1)
    dp[0]=0
    for i in coins:
        for j in range(i,amount+1):
            dp[i]=min(dp[j],dp[j-1]+1)
    if dp[amount]!=amount+1:
        return dp[amount]
    else:
        return -1

coins=[1,2,5]
amount=11
print(coinCharge(coins,amount))