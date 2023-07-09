import numpy_financial as npf
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import hvplot.pandas as hvplot
import holoviews as hv
# Create a title:
st.title('Visualize Cashflows')

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

   

    




selection_choice = st.selectbox("Select a function:", ["Multiple Cashflow Returns", "Visualize Annuities"])

if selection_choice == "Multiple Cashflow Returns":
    # Initialize inputs
    par = st.number_input("Par Value ($):", min_value=0.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0)
    t = st.number_input("Maturity (years):", min_value=0.0)
    frequency = st.selectbox("Frequency", ['Annual', 'Semi-annual', 'Quarterly'])
    ytm = st.number_input("Yield to Maturity (%):", min_value=0.0)
    if frequency == 'Semi-annual':
        freq_per_anum = 2
    elif frequency == 'Annual':
        freq_per_anum = 1
    elif frequency == 'Quarterly':
        freq_per_anum = 4
    # Validate and normalize inputs
    if not isinstance(coupon_rate, float):
        coupon_rate = float(coupon_rate)
    elif coupon_rate >= 1.0:
        coupon_rate = coupon_rate / 100.0

    if not isinstance(ytm, float):
        ytm = float(ytm)
    elif ytm >= 1.0:
        ytm = ytm / 100.0
    n = int(t * freq_per_anum)
    result = list(range(1, n+ 1))
    
    st.markdown("""---""")
    topup_expander = st.expander("Topup values")
    topups = {}
    for period in range(1,n+1):
        topups[period] = topup_expander.number_input(f"Topup for period {period}:", min_value=0.0)
    ## Calculations:
    # Calculation remains mostly the same, but without checking if period is in selected_periods
    multiple_cashflows_dataframe = pd.DataFrame(index=result, columns=[ 'Deposit','Deposit FV', 'Topup','Topup FV', 'Topup FV Total', 'Total FV','Interest Accrued'])
    multiple_cashflows_dataframe.index.name = 'Period'
    multiple_cashflows_dataframe.loc[1, 'Deposit'] = par
    deposit = multiple_cashflows_dataframe.loc[1, 'Deposit']
    deposit_fv = deposit * (1 + ytm/freq_per_anum) ** n
    multiple_cashflows_dataframe['Deposit FV'] = deposit_fv

    topup_total = 0
    for period in result:
        topup = topups[period]
        topup = topups[period]
        topup_fv = topup * (1 + ytm/freq_per_anum) ** (n - period)
        multiple_cashflows_dataframe.loc[period, 'Topup FV'] = topup_fv
        multiple_cashflows_dataframe.loc[period, 'Topup'] = topup
        topup_fv_total = sum(multiple_cashflows_dataframe['Topup FV'][:period])
        multiple_cashflows_dataframe.loc[period, 'Topup FV Total'] = topup_fv_total
        # Add the topups
        topup_total += multiple_cashflows_dataframe.loc[period,'Topup']
        # Calculate total fv
        total_fv = deposit_fv + topup_fv_total
        multiple_cashflows_dataframe.loc[period,'Total FV'] = total_fv
        # Calculate interest accrued
        interest_accrued = total_fv - par - topup_total
        multiple_cashflows_dataframe.loc[period, 'Interest Accrued'] = interest_accrued
        # multiple_cashflows_dataframe.loc[period, 'Interest Accrued'] = interest_accrued
        # multiple_cashflows_dataframe.loc[period, 'Interest Accrued'] = interest_accrued[period]
    multiple_cashflows_dataframe = multiple_cashflows_dataframe.fillna(0)

        

    ##3

    st.dataframe(multiple_cashflows_dataframe)
    x = st.selectbox("Select the 'x' variable:", ['Deposit','Deposit FV', 'Topup','Topup FV', 'Topup FV Total', 'Total FV','Interest Accrued','Period'])
    y = st.selectbox("Select the 'y' variable:", ['Deposit','Deposit FV', 'Topup','Topup FV', 'Topup FV Total', 'Total FV','Interest Accrued'])
    graph_type = st.selectbox("Select a graph type:", ['Line', 'Bar', 'Scatter'])
    if graph_type == 'Line':
        ax = multiple_cashflows_dataframe.hvplot.line(
            x=x,
            y=y,
            colormap='viridis',
        )
    elif graph_type == 'Bar':
        ax = multiple_cashflows_dataframe.hvplot.bar(
            x=x,
            y=y,
            colormap='viridis',
        )
    elif graph_type == 'Scatter':
        ax = multiple_cashflows_dataframe.hvplot.scatter(
            x=x,
            y=y,
            colormap='viridis',
        )
    
    st.bokeh_chart(hv.render(ax, backend='bokeh'))


    # After 