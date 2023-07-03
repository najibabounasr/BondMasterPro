import streamlit as st
import numpy as np
import pandas as pd
from scipy import optimize

# Initialize streamlit 
st.title("Bond Calculator")

st.warning("Please note that zeros entered into the inputs may result in errors.")
# Initialize the functions
def calculate_bond_present_value(coupon_rate, future_value, ytm, n):
    coupon_payment = (coupon_rate * future_value) / n
    present_value = (coupon_payment * (1 - (1 + ytm/n)**(-n))) / (ytm/n) + future_value / (1 + ytm/n)**n
    return present_value

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



# Metric selection
metric = st.selectbox("Select a bond metric to calculate", ['Present Value', 'Yield to Maturity', 'Coupon Yield', 'Market Discount Rate'])

# Collect user inputs

# Calculation and output based on metric
if metric == 'Present Value':
    # Collect user inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    t = st.number_input("Maturity (years):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])

    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4

    n = t * freq_per_anum
    ytm = st.number_input("Yield to Maturity (%):", min_value=0.0)
    present_value = calculate_bond_present_value(coupon_rate/100, par, ytm/100, t * freq_per_anum)
    st.write(f"The Present Value of the bond is: ${present_value:.2f}")
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Coupon Rate (%)': [coupon_rate],
        'Years': [t],
        'YTM (%)': [ytm],
        'Par Value ($)': [par],
        'Frequency': [frequency],
        'Total Payments': [n],
        'Bond Price ($)': [present_value]
    })
    st.dataframe(bonds_dataframe)
elif metric == 'Yield to Maturity':
    # Collect user inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    t = st.number_input("Maturity (years):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])

    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4

    n = t * freq_per_anum
    price = st.number_input("Market Price ($):", min_value=0.0)
    ytm = calculate_bond_ytm(price, par, t, coupon_rate, freq_per_anum)
    market_discount_rate = calculate_market_discount_rate(price, par, t, coupon_rate, freq_per_anum)
    
    st.write(f"The Yield to Maturity (YTM) of the bond is: {ytm*100:.2f}%")
    
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Coupon Rate (%)': [coupon_rate],
        'Years': [t],
        'YTM (%)': [ytm],
        'Market Discount Rate (%)': [market_discount_rate],
        'Par Value ($)': [par],
        'Frequency': [frequency],
        'Total Payments': [n],
    })
    st.dataframe(bonds_dataframe)
elif metric == 'Coupon Yield':
    # Collect user inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    coupon_yield = (coupon_rate / par) * 100
    st.write(f"The Coupon Yield (I/Y) of the bond is: {coupon_yield:.2f}%")
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Coupon Rate (%)': [coupon_rate],
        'Par Value ($)': [par],
        'Coupon Yield (%)': [coupon_yield],
    })
    st.dataframe(bonds_dataframe)
elif metric == 'Coupon Payment (PMT)':
    # Collect user inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])

    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4
    # calculate PMT
    pmt = (coupon_rate * par) / freq_per_anum
    st.write(f"The Coupon Payment (PMT) of the bond is: ${pmt:.2f}")
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Coupon Rate (%)': [coupon_rate],
        'Par Value ($)': [par],
        'Frequency': [frequency],
        'Coupon Payment ($)': [pmt],
    })
    st.dataframe(bonds_dataframe)
elif metric == 'Total Payments':
    # Collect user inputs
    t = st.number_input("Maturity (years):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])

    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4

    n = t * freq_per_anum 
    st.write(f"The Total Payments of the bond is: {n:.2f}")
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Years': [t],
        'Frequency': [frequency],
        'Total Payments': [n],
    })
    st.dataframe(bonds_dataframe)
elif metric == 'Market Discount Rate':
    # Collect user inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    t = st.number_input("Maturity (years):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])

    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4

    n = t * freq_per_anum
    price = st.number_input("Market Price ($):", min_value=0.0)
    market_discount_rate = calculate_market_discount_rate(price, par, t, coupon_rate, freq_per_anum)
    st.write(f"The Market Discount Rate (YTM) of the bond is: {market_discount_rate*100:.2f}%")
    ## Display dataframe
    bonds_dataframe = pd.DataFrame({
        'Coupon Rate (%)': [coupon_rate],
        'Years': [t],
        'Market Discount Rate (%)': [market_discount_rate],
        'Par Value ($)': [par],
        'Frequency': [frequency],
        'Total Payments': [n],
    })
    st.dataframe(bonds_dataframe)




