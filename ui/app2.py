import streamlit as st

st.title('sasta calculator')
st.write('This is a simple calculator  app')

c1,c2=st.columns(2)
c1.number_input('Number 1',key='num1')
c2.number_input('Number 2',key='num2')

if st.button('Addition'):
        num1=st.session_state.num1
        num2=st.session_state.num2
        ans=num1+num2
        st.info(f'{num1}+{num2}={ans}')


if st.button('Subtract'):
        num1=st.session_state.num1
        num2=st.session_state.num2
        ans=num1-num2
        st.info(f'{num1}-{num2}={ans}')




if st.button('multiply'):
        num1=st.session_state.num1
        num2=st.session_state.num2
        ans=num1*num2
        st.info(f'{num1}*{num2}={ans}')