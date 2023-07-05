def calculate_bond_ytm(price, par, t, coupon, freq):
    periods = t*freq
    coupon = coupon/100.*par/freq
    dt = [(i+1)/freq for i in range(int(periods))]
    ytm_func = lambda y : sum([coupon/(1+y/freq)**(freq*t) for t in dt]) + par/(1+y/freq)**(freq*t) - price
    return optimize.newton(ytm_func, 0.03)

def calculate_market_discount_rate(price, par, t, coupon, freq):
    periods = t * freq
    coupon = coupon / 100.0 * par / freq
    dt = [(i + 1) / freq for i in range(int(periods))]
    market_discount_rate_func = lambda y: sum([coupon / (1 + y / freq) ** (freq * t) for t in dt]) + par / (1 + y / freq) ** (freq * t) - price
    return optimize.newton(market_discount_rate_func, 0.03)
