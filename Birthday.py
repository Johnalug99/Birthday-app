import streamlit as st

def birthday_game():
    st.title("Guess Your Birthday Game!")
    
    name = st.text_input("It's good to have you on this game.\nWhat is your name?", "")
    if name.strip() == "":
        st.warning("Please enter your name to start the game!")
        return

    st.write("Hello", name,",", "Let's find out your birthday.!\n"
    "\nTick all the boxes that applies.")
    day = 0

    birthday_sets = [
        "1  3  5  7\n9  11  13  15\n17  19  21 23\n25  27  29 31",
        "2  3  6  7\n10  11  14  15\n18  19  22 23\n26  27  30 31",
        "4  5  6  7\n12  13  14  15\n20  21  22 23\n28  29  30 31",
        "8  9  10 11\n12  13  14  15\n24  25  26 27\n28  29  30 31",
        "16  17  18 19\n20  21  22 23\n24  25  26 27\n28  29  30 31"
    ]
    values = [1, 2, 4, 8, 16]

    for i, set_text in enumerate(birthday_sets):
        if st.checkbox(f"Is your birthday in this set?\n\n{set_text}"):
            day += values[i]
            if day > 0:
                suffix = "th"
                if day in [1, 21, 31]:
                 suffix = "st"
                elif day in [2, 22]:
                 suffix = "nd"
                elif day in [3, 23]:
                 suffix = "rd"
        st.success(f"Yippie! {name}Your birthday is on the {day}{suffix}!")
        st.balloons()
    else:
        st.error("It seems you didn't select any options. Try again!")

birthday_game()
