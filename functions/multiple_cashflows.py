import numpy_financial as npf
import pandas as pd
def compounding_frequency_calculation(coupon_rate, par, ytm, n):
    if not isinstance (coupon_rate, float):
        coupon_rate = float(coupon_rate)
    elif coupon_rate >= 1.0:
        coupon_rate = coupon_rate / 100.0
    if not isinstance (ytm, float):
        ytm = float(ytm)
    elif ytm >= 1.0:
        ytm = ytm / 100.0
    coupon = coupon_rate * par
    coupon_payment = coupon/n
    coupon_payments = np.repeat(coupon_payment, n)
    coupon_payments[-1] += par
    return npf.npv(ytm, coupon_payments)


def visualize_annuities(coupon_rate, par, ytm, n):
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i += 1
    #######
    if not isinstance (coupon_rate, float):
        coupon_rate = float(coupon_rate)
    elif coupon_rate >= 1.0:
        coupon_rate = coupon_rate / 100.0
    if not isinstance (ytm, float):
        ytm = float(ytm)
    elif ytm >= 1.0:
        ytm = ytm / 100.0
    ######
    deposit_fv = par * (1 + ytm)**n

    data = []
    for j in range(num_topups):
        data.append([j+1, deposit_fv])



def multiple_cashflow_returns(coupon_rate, par, ytm, n):

    # Validate and normalize inputs
    if not isinstance(coupon_rate, float):
        coupon_rate = float(coupon_rate)
    elif coupon_rate >= 1.0:
        coupon_rate = coupon_rate / 100.0

    if not isinstance(ytm, float):
        ytm = float(ytm)
    elif ytm >= 1.0:
        ytm = ytm / 100.0

    # Initialize dataframe to hold deposit, topup and interest data
    df = pd.DataFrame(columns=['Period', 'Deposit', 'Topup', 'Compound Interest'])

    
    # The initial deposit
    deposit_fv = par * (1 + ytm) ** n
    df = df.append({'Period': n, 'Deposit': deposit_fv, 'Topup': 0, 'Compound Interest': deposit_fv}, ignore_index=True)

    # Calculate topups
    total_topups = 0
    for j in range(1, num_topups+1):
        topup_fv = 100 * (1 + ytm) ** (n - j)
        total_topups += topup_fv
        compound_interest_with_multiple_cashflows = deposit_fv + total_topups
        df = df.append({'Period': n-j, 'Deposit': 0, 'Topup': topup_fv, 'Compound Interest': compound_interest_with_multiple_cashflows}, ignore_index=True)

    return df.sort_values(by='Period').reset_index(drop=True)