import random
import streamlit as st
import time 

st.markdown("""
    <style>
    .big-label {
        font-size: 22px;
        font-weight: bold;
    }
    .sample-output {
        font-family: 'Courier New', Courier;
        font-size: 1em;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([4,4]) # make them as columns

with col1: #place them in columns here
    st.header(" CE Ticket Randomizer ", divider='rainbow')
    with st.expander("Click here for more info"):
        st.write("Our Random Sample Generator provides you with 5 hand-picked items from your list in seconds.
                 This tool ensures that your samples are completely random. Ideal for quality assurance and data analysis,
                 our generator allows you to confidently rely on the integrity of your sample data, making your decision-making process more efficient and accurate." ")

# input from users, usually bulk data copied from Airtable
with col2:
    st.markdown('<div class="big-label">Copy Ids from Airtable then click Generate:</div>', unsafe_allow_html=True)
    text = st.text_area(
        label='Hidden Label',  # Provide a non-empty label
        label_visibility='collapsed',  # Hide the label
        height=200,  # Fixed height 
        help="Paste the audit IDs you'd like to choose from."
    )        

# generate button here
with col2:
    if st.button("Generate"):
    # this line will split the IDs and strip any extra whitespace
        items = [item.strip() for item in text.split('\n') if item.strip()]

        if len(items) < 5:
            st.warning("Oops, please enter more than 5 Ids!")
        else:
            # select 5 items randomly from the list
            random_selection = random.sample(items, 5)
            st.session_state['random_selection'] = random_selection  # Save to session state

            # Progress bar here
            progress_text = "Hang on..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty() 

# show results here
if 'random_selection' in st.session_state:
    with col2:
        st.markdown("### Here are the tickets for your today's audit:")
        for i, item in enumerate(st.session_state['random_selection'], 1):
            st.markdown(f'<div class="sample-output">{i}: {item}</div>', unsafe_allow_html=True)
