import random
import streamlit as st
import time 

st.markdown("""
    <style>
    .big-label {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([4,4]) # make them as columns

with col1: #place them in columns here
    st.header(" Random Sample Generator ", divider='rainbow')
    with st.expander("Click here for more info"):
        st.write("Our Random Sample Generator gives you 5 hand-picked items from your list in seconds.  Skip the ad-infested randomizer websites and unreliable chatbots! ")

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
    if st.button("Generate"):
    # this line will split the IDs and strip any extra whitespace
        items = [item.strip() for item in text.split('\n') if item.strip()]

        if len(items) < 5:
            st.warning("Oops, please enter more than 5 Ids!")
        else:
            # select 5 items randomly from the list
            random_selection = random.sample(items, 5)

        # Progress bar here
            progress_text = "Hang on..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty() 
        # show results here
            with col2:
                st.markdown("### Here you go:")
                st.write("""
                <style>
                .sample-output {
                    font-family: 'Courier New', Courier, monospace;
                    font-size: 1em;
                    color: #4CAF50;
                }
                </style>
                """, unsafe_allow_html=True)

                for i, item in enumerate(random_selection, 1):
                    st.markdown(f'<div class="sample-output">{i}: {item}</div>', unsafe_allow_html=True)
