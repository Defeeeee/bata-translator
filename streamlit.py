import streamlit as st
from urllib.parse import urlencode, quote_plus
from main import translate_mac_option_string  # Import the function from main.py

APP_BASE_URL = "https://bataaa.streamlit.app/"

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

# --- 1) Read query params (so shared links restore state) ---
qp = st.query_params  # for older Streamlit: st.experimental_get_query_params()
default_input = qp.get("text", "˙´¬¬ø")

# Input Text Box
input_text = st.text_input("Enter your Option-modified string here:", value=default_input)

translated_text = ""
if input_text:
    try:
        translated_text = translate_mac_option_string(input_text)

        st.subheader("Translated String:")
        st.text_area(
            "Output",
            value=translated_text,
            height=100,
            disabled=True,
            help="This is the translated text based on the US Mac ANSI keyboard map.",
        )
    except Exception as e:
        st.error(f"An error occurred during translation: {e}")
        st.error(
            "Please ensure your `main.py` file and the `translate_mac_option_string` function are set up correctly and the Option Map is complete."
        )
else:
    st.info("Please enter a string in the textbox above to see the translation.")

# --- 2) Share link (plain URL; visible params) ---
st.markdown("---")
st.subheader("Share")

# Build a shareable URL that restores the input via ?text=...
params = {"text": input_text} if input_text else {"text": default_input}
share_url = APP_BASE_URL.rstrip("/") + "/?" + urlencode(params, quote_via=quote_plus)

st.text_input("Shareable link", share_url)

# Optional: convenient button to sync the browser URL to current input
if st.button("Update page URL to match current input"):
    st.query_params.update(params)
    st.rerun()

st.markdown("---")
st.markdown(
    "Built with Streamlit. The translation logic and character map are imported from your `main.py` file, assuming a US Mac ANSI keyboard layout."
)
