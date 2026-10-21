import streamlit as st
import os

# Method 1: Streamlit secrets (recommended for deployment)
def get_api_key():
    """Get API key from Streamlit secrets or user input."""
    # Try to get from Streamlit secrets first
    try:
        api_key = st.secrets["ANTHROPIC_API_KEY"]
        return api_key
    except (FileNotFoundError, KeyError):
        # Fall back to user input
        st.sidebar.warning("⚠️ API key not configured")
        api_key = st.sidebar.text_input(
            "Enter your Anthropic API key:",
            type="password",
            help="Get your key from console.anthropic.com"
        )
        if not api_key:
            st.error("Please provide an API key to continue")
            st.stop()
        return api_key

# Method 2: Environment variables (for local development)
# from decouple 
# load_dotenv()  # Loads from .env file

api_key = os.getenv("ANTHROPIC_API_KEY")
