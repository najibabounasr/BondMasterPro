def calculate_bond_present_value(coupon_rate, face_value, ytm, n):
    pv_selection = st.selectbox("Would you like to use the simple or complex present value formula?", ['Bond Master Pro', 'Annuities Only', 'Lump Sum Only'])
    if pv_selection == 'Full Payment':
        if coupon_rate == 0:
            return face_value / (1 + ytm)**n
        elif ytm == 0:  # No discounting
            return (coupon_rate * face_value) + face_value
        else:  # Regular case
            coupon_payment = face_value * (coupon_rate / freq_per_anum)
            present_value_paid_at_maturity = face_value / (1 + ytm/freq_per_anum)**(n)
            present_value_of_regular_payments = coupon_payment * (1 - (1 + ytm/freq_per_anum)**(-n)) / (ytm/freq_per_anum)
            present_value = present_value_paid_at_maturity + present_value_of_regular_payments
            return present_value
    elif pv_selection == 'Annuities Only':
        if coupon_rate == 0:
            return 0
        elif ytm == 0:  # No discounting
            coupon_payment = face_value * (coupon_rate / freq_per_anum)
            return coupon_payment * n
        else:  # Regular case
            coupon_payment = face_value * (coupon_rate / freq_per_anum)
            present_value_of_regular_payments = coupon_payment * (1 - (1 + ytm/freq_per_anum)**(-n)) / (ytm/freq_per_anum)
            present_value =  present_value_of_regular_payments
            return present_value
    elif pv_selection == 'Lump Sum Only':
        if coupon_rate == 0:
            return face_value / (1 + ytm)**n
        elif ytm == 0:  # No discounting
            return (coupon_rate * face_value) + face_value
        else:  # Regular case
            coupon_payment = face_value * (coupon_rate / freq_per_anum)
            present_value_paid_at_maturity = face_value / (1 + ytm/freq_per_anum)**(n)
            present_value = present_value_paid_at_maturity
            return present_value
        
        