def simple_interest_accrued(interest_rate_per_period, number_of_periods, present_value):
    if not isinstance (interest_rate_per_period, float):
        interest_rate_per_period = float(interest_rate_per_period)
    elif interest_rate_per_period >= 1.0:
        interest_rate_per_period = interest_rate_per_period / 100.0
    pv = present_value
    r = interest_rate_per_period
    n = number_of_periods
    interest = pv * r * n
    return interest

def simple_interest_and_future_value(interest_rate_per_period, number_of_periods, present_value):
    if not isinstance (interest_rate_per_period, float):
        interest_rate_per_period = float(interest_rate_per_period)
    elif interest_rate_per_period >= 1.0:
        interest_rate_per_period = interest_rate_per_period / 100.0
    pv = present_value
    r = interest_rate_per_period
    n = number_of_periods
    interest = pv * r * n
    fv = pv + interest
    return interest, fv

def compound_interest_accrued(interest_rate_per_period, number_of_periods, present_value):
    if not isinstance (interest_rate_per_period, float):
        interest_rate_per_period = float(interest_rate_per_period)
    elif interest_rate_per_period >= 1.0:
        interest_rate_per_period = interest_rate_per_period / 100.0
    pv = present_value
    r = interest_rate_per_period
    n = number_of_periods
    fv = pv * (1 + r)**n
    interest = fv - pv
    return interest

def compound_interest_and_future_value(interest_rate_per_period, number_of_periods, present_value):
    if not isinstance (interest_rate_per_period, float):
        interest_rate_per_period = float(interest_rate_per_period)
    elif interest_rate_per_period >= 1.0:
        interest_rate_per_period = interest_rate_per_period / 100.0
    pv = present_value
    r = interest_rate_per_period
    n = number_of_periods
    fv = pv * (1 + r)**n
    interest = fv - pv
    return interest, fv