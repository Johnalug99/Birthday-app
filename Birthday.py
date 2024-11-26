
import streamlit as st

def birthday_game():
    st.title("Guess Your Birthday Game!")
    name = st.text_input("It's good to have you on this game.\n"
                         "What is your name?", "")
    
    if name:
        st.write(f"Hello, {name}! Let's find out your birthday!")
        day = 0
        if st.checkbox("Is your birthday in this set?\n1  3  5  7\n9  11  13  15\n17  19  21 23\n25  27  29 31"):
            day += 1
        if st.checkbox("Is your birthday in this set?\n2  3  6  7\n10  11  14  15\n18  19  22 23\n26  27  30 31"):
            day += 2

        if st.checkbox("Is your birthday in this set?\n4  5  6  7\n12  13  14  15\n20  21  22 23\n28  29  30 31"):
            day += 4

        if st.checkbox("Is your birthday in this set?\n8  9  10  11\n12  13  14  15\n24  25  26 27\n28  29  30 31"):
            day += 8

        if st.checkbox("Is your birthday in this set?\n16  17  18  19\n20  21  22 23\n24  25  26 27\n28  29  30 31"):
            day += 16
        if day > 0:
            suffix = "th"
            if day in [1, 21, 31]:
                suffix = "st"
            elif day in [2, 22]:
                suffix = "nd"
            elif day in [3, 23]:
                suffix = "rd"
            st.success(f"Your birthday is on the {day}{suffix}!")
