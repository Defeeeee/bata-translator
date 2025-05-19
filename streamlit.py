import streamlit as st
from main import translate_mac_option_string  # Import the function from main.py

# --- Streamlit App Layout ---
st.set_page_config(page_title="BATA Translator", layout="wide")

st.title("BATA Translator")
st.caption("Translate strings typed with Option-key combinations (US ANSI Layout) back to standard characters.")

st.markdown("""
    **How to use:**
    1. Type or paste your Option-key modified string into the textbox below.
    2. The translated (standard) text will appear underneath.

    For example, the input `˙´¬¬ø` should translate to `hello`.
    Your example `´¨ ∫å†å` should translate to `eu bata`.
""")

# Input Text Box
default_input = "˙´¬¬ø"
input_text = st.text_input("Enter your Option-modified string here:", value=default_input)

if input_text:
    # Perform the translation using the function from main.py
    # This assumes translate_mac_option_string in main.py uses its own global MAC_US_OPTION_KEY_MAP
    try:
        translated_text = translate_mac_option_string(input_text)

        st.subheader("Translated String:")
        # Using a text area for the output makes it easy to copy and handles multiline better
        st.text_area("Output", value=translated_text, height=100, disabled=True,
                     help="This is the translated text based on the US Mac ANSI keyboard map.")
    except Exception as e:
        st.error(f"An error occurred during translation: {e}")
        st.error(
            "Please ensure your `main.py` file and the `translate_mac_option_string` function are set up correctly and the Option Map is complete.")

else:
    st.info("Please enter a string in the textbox above to see the translation.")

st.markdown("---")
st.markdown(
    "Built with Streamlit. The translation logic and character map are imported from your `main.py` file, assuming a US Mac ANSI keyboard layout.")

