from helper import Util

class Farm():
    def alcxInfo(contract, poolIndex, account):

        rewardsPerWeek = round(contract.functions.getPoolRewardRate(poolIndex).call() / 1e18 * 604800 / 13.5, 2)
        totalDeposited = round(contract.functions.getPoolTotalDeposited(poolIndex).call() / 1e18, 2)
        userStaked = round(contract.functions.getStakeTotalDeposited(account, poolIndex).call() / 1e18, 2)
        userUnclaimed = round(contract.functions.getStakeTotalUnclaimed(account, poolIndex).call() / 1e18, 2)

        weeklyAPY = round(rewardsPerWeek / totalDeposited * 100, 2)
        dailyAPY = round((weeklyAPY / 7), 2)
        yearlyAPY = round((weeklyAPY * 52), 2)

        dailyEarnings = round(dailyAPY * userStaked / 100,2)
        weeklyEarnings = round(weeklyAPY * userStaked / 100, 2)
        yearlyEarnings = round(yearlyAPY * userStaked / 100, 2)

        price = Util.getPrice(token='alchemix')
    
        dailyEarningsUSD = round(dailyEarnings * price, 2)
        weeklyEarningsUSD = round(weeklyEarnings * price, 2)
        yearlyEarningsUSD = round(yearlyEarnings * price, 2)

        poolDict = {
            'name': 'ALCX',
            'rewardsPerWeek': rewardsPerWeek,
            'totalDeposited': totalDeposited,
            'userStaked': userStaked,
            'userUnclaimed': userUnclaimed,
            'weeklyAPY': weeklyAPY,
            'dailyAPY': dailyAPY,
            'yearlyAPY': yearlyAPY,
            'dailyEarnings': dailyEarnings,
            'weeklyEarnings': weeklyEarnings,
            'yearlyEarnings': yearlyEarnings,
            'dailyEarningsUSD': dailyEarningsUSD,
            'weeklyEarningsUSD': weeklyEarningsUSD,
            'yearlyEarningsUSD': yearlyEarningsUSD,
            'price': price
        }

        return poolDict


    def bdpiInfo(contract, account):

        rewardsPerWeek = round(contract.functions.basketPerBlock().call() / 1e18 * 604800 / 13.5 * 0.6, 2)
        totalDeposited = round(contract.functions.getPoolTotalDeposited(poolIndex).call() / 1e18, 2)
        userStaked = round(contract.functions.getStakeTotalDeposited(account, poolIndex).call() / 1e18, 2)
        userUnclaimed = round(contract.functions.getStakeTotalUnclaimed(account, poolIndex).call() / 1e18, 2)

        weeklyAPY = round(rewardsPerWeek / totalDeposited * 100, 2)
        dailyAPY = round((weeklyAPY / 7), 2)
        yearlyAPY = round((weeklyAPY * 52), 2)

        dailyEarnings = round(dailyAPY * userStaked / 100,2)
        weeklyEarnings = round(weeklyAPY * userStaked / 100, 2)
        yearlyEarnings = round(yearlyAPY * userStaked / 100, 2)

        price = Util.getPrice(token='interest-bearing-dpi')
    
        dailyEarningsUSD = round(dailyEarnings * price, 2)
        weeklyEarningsUSD = round(weeklyEarnings * price, 2)
        yearlyEarningsUSD = round(yearlyEarnings * price, 2)

        poolDict = {
            'name': 'ALCX',
            'rewardsPerWeek': rewardsPerWeek,
            'totalDeposited': totalDeposited,
            'userStaked': userStaked,
            'userUnclaimed': userUnclaimed,
            'weeklyAPY': weeklyAPY,
            'dailyAPY': dailyAPY,
            'yearlyAPY': yearlyAPY,
            'dailyEarnings': dailyEarnings,
            'weeklyEarnings': weeklyEarnings,
            'yearlyEarnings': yearlyEarnings,
            'dailyEarningsUSD': dailyEarningsUSD,
            'weeklyEarningsUSD': weeklyEarningsUSD,
            'yearlyEarningsUSD': yearlyEarningsUSD,
            'price': price
        }

        return poolDict