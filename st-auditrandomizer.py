import random
import streamlit as st
import time
st.set_page_config(layout="wide")

# Apply custom styling
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


col1, col2, col3 = st.columns([8, 8, 8])  # Create columns for layout

# Left column: Header and description
with col1:
    st.header("CE Ticket Randomizer", divider='rainbow')
    with st.expander("Click here for more info"):
        st.write("Our Random Sample Generator provides you with randomly hand-picked items from your list. "
                 "This tool ensures that your samples are completely random. Ideal for quality assurance and data "
                 "analysis, our generator allows you to confidently rely on the integrity of your sample data, making "
                 "your decision-making process more efficient and accurate.")

# Right column: Text area for input and controls
with col2:
    st.markdown('<div class="big-label">Copy IDs from Airtable then click Generate:</div>', unsafe_allow_html=True)
    text = st.text_area(
        label='Hidden Label',
        label_visibility='collapsed',
        height=200,
        help="Paste the audit IDs you'd like to choose from."
    )

    # Add a numeric input for selecting the number of items to output
    num_outputs = st.number_input(
        label="Number of outputs you want",
        min_value=1,
        max_value=100,
        value=5,
        step=1,
        help="Select the number of random IDs to generate."
    )

    # Generate button
    if st.button("Generate"):
        items = [item.strip() for item in text.split('\n') if item.strip()]

        if len(items) < num_outputs:
            st.warning(f"Oops, please enter at least {num_outputs} IDs!")
        else:
            # Select the specified number of items randomly
            random_selection = random.sample(items, num_outputs)
            st.session_state['random_selection'] = random_selection  # Save to session state

            # Progress bar
            progress_text = "Hang on..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            my_bar.empty()

# Display the results
if 'random_selection' in st.session_state:
    with col3:
        st.markdown("### Here are the tickets for your today's audit:")
        for i, item in enumerate(st.session_state['random_selection'], 1):
            st.markdown(f'<div class="sample-output">{i}: {item}</div>', unsafe_allow_html=True)
