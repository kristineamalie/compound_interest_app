import streamlit as st
from calc import monthly_compound


#documenttion found here: https://docs.streamlit.io/library

st.title('How Rich Will I Be?')

initial = st.number_input(label='Initial value (£)', min_value=(0), max_value=(1000000000))

monthly = st.number_input(label='Monthly contribution (£)', min_value=(0), max_value=(1000000000))

years = st.number_input(label='Duration (years)', min_value=(0), max_value=(1000000000))

#to run app go to command line and run: streamlit run app.py
#to stop it running close command line or click ctr c continously 
#app found on this url: http://localhost:8501/

annual_rate = st.slider(label = 'Annual interest rate (%)', min_value=1, max_value=12, step=1)

final_sum = monthly_compound(initial, monthly, annual_rate, years)

st.markdown(f'After {int(years)} years you would have £{round(final_sum, 2)} :sunglasses:')
