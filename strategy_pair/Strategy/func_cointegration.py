from statsmodels.tsa.stattools import coint
import statsmodels.api as sm
import pandas as pd
import numpy as np
from tqdm import tqdm


def calculate_spread(series1, series2, hedge_ratio):
    spread = pd.Series(series1) - (pd.Series(series2) + hedge_ratio)
    return spread


def calculate_cointegration(series1, series2):

    try:
        coint_flag = 0
        coint_res = coint(series1, series2)
        coint_t = coint_res[0]
        p_value = coint_res[1]
        critical_value = coint_res[2][1]
        model = sm.OLS(series1, series2).fit()
        hedge_ratio = model.params[0]
        spread = calculate_spread(series1, series2, hedge_ratio)
        zero_crossings = len(np.where(np.diff(np.sign(spread)))[0])
        if p_value < 0.5 and coint_t < critical_value:
            coint_flag = 1
        return (coint_flag, round(p_value, 2), round(coint_t, 2), round(critical_value, 2), round(hedge_ratio, 2), zero_crossings)
    except:
        return 0, 0, 0, 0, 0, 0


# Calculate cointegrated pairs
def get_cointegrated_pairs(prices):
    # Loop through coins and check for co-integration
    coint_pair_list = []
    included_list = []
    for sym_1 in tqdm(prices.keys()):

        # check each coin against the first coin (sym_1)
        for sym_2 in prices.keys():
            if sym_2 != sym_1:

                # Get unique combination id and ensure one off check
                sorted_characters = sorted(sym_1 + sym_2)
                unique = ''.join(sorted_characters)
                if unique in included_list:
                    break

                # Get Close price data
                series1 = prices[sym_1]
                series2 = prices[sym_2]

                # check for cointegration and add cointegrated pair
                coin_flag, p_value, t_value, c_value, hedge_ratio, zero_crossings = calculate_cointegration(series1,
                                                                                                            series2)
                if coin_flag == 1:
                    included_list.append(unique)
                    coint_pair_list.append({
                        'sym_1': sym_1,
                        'sym_2': sym_2,
                        'p_value': p_value,
                        't_value': t_value,
                        'c_value': c_value,
                        'hedge_ratio': hedge_ratio,
                        'zero_crossings': zero_crossings
                    })
    # Output results
    df_coint = pd.DataFrame(coint_pair_list)
    df_coint = df_coint.sort_values('zero_crossings', ascending=False)
    df_coint.to_csv('2_cointegrated_pairs.csv')
    return df_coint
