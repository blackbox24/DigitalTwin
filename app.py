import time

import anthropic
import pandas as pd
import streamlit as st
from decouple import config

from utils.llm import get_llm_response

# Page configuration
st.set_page_config(
    page_title="Digital Twin Assistant",
    page_icon="🤖",
    layout="centered"
)

# Method 1: Streamlit secrets (recommended for deployment)
def get_api_key():
    """Get API key from Streamlit secrets or user input."""
    # Try to get from Streamlit secrets first
    api_key = config("ANTHROPIC_API_KEY", cast=str);
    if not api_key:
        try:
            api_key = st.secrets["ANTHROPIC_API_KEY"]
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

# def main():
#     st.title("🤖 Digital Twin Assistant")
#     st.write("An AI-powered personal assistant built for fast and reliable deployment.")

#     # Secure API key retrieval
#     api_key = get_api_key()

#     # Chat interface input
#     user_input = st.text_input("Ask your digital twin anything:")
    

#     if user_input:
#         with st.spinner("Thinking..."):
#             try:
#                 client = anthropic.Anthropic(api_key=api_key)
#                 message = client.messages.create(
#                     model="claude-3-5-sonnet-20241022",
#                     max_tokens=1024,
#                     messages=[{"role": "user", "content": user_input}]
#                 )
#                 response_text = message.content[0].text
#                 st.success("Response:")
#                 st.write(response_text)
#             except Exception as e:
#                 st.error(f"An error occurred while connecting to the API: {e}")

# Requirement 1: Use @st.cache_data for expensive data loading operations
@st.cache_data(show_spinner=False)
def load_large_dataset():
    """Simulate an expensive database query or heavy file load."""
    time.sleep(2) # Simulating latency
    # Generating a dummy dataset with 100 rows
    data = {
        "ID": range(1, 101),
        "Item_Name": [f"Product Alpha {i}" if i % 2 == 0 else f"Product Beta {i}" for i in range(1, 101)],
        "Category": ["Electronics" if i % 3 == 0 else "Apparel" for i in range(1, 101)],
        "Price": [round(10.0 + (i * 1.5), 2) for i in range(1, 101)],
        "Stock": [50 - (i % 20) for i in range(1, 101)]
    }
    return pd.DataFrame(data)

# Requirement 2 & 4: Implement Pagination for large datasets
def paginate_dataframe(df: pd.DataFrame, page_size: int = 10):
    """Split dataframe into manageable chunks for pagination."""
    total_rows = len(df)
    total_pages = (total_rows // page_size) + (1 if total_rows % page_size > 0 else 0)
    
    # Sidebar pagination controls
    st.sidebar.markdown("### 📄 Pagination Controls")
    page_number = st.sidebar.number_input(
        "Select Page", 
        min_value=1, 
        max_value=max(1, total_pages), 
        value=1, 
        step=1
    )
    
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    
    st.sidebar.text(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")
    return df.iloc[start_idx:end_idx]

def main():
    st.title("⚡ Optimized Data Explorer & Analytics")
    st.write("This application demonstrates caching, loading indicators, and pagination for high performance.")

    # Requirement 3: Add loading indicators during expensive actions
    with st.spinner("🔄 Loading dataset into memory... (Cached after first load)"):
        df = load_large_dataset()

    # Sidebar Filter Options
    st.sidebar.markdown("### 🔍 Filters")
    selected_category = st.sidebar.selectbox(
        "Filter by Category", 
        ["All"] + list(df["Category"].unique())
    )

    # Filter data based on user input
    filtered_df = df if selected_category == "All" else df[df["Category"] == selected_category]

    # Apply Pagination
    paginated_data = paginate_dataframe(filtered_df, page_size=10)

    # Display Metrics & Results
    col1, col2 = st.columns(2)
    col1.metric(label="Total Matching Records", value=len(filtered_df))
    col2.metric(label="Average Price", value=f"${filtered_df['Price'].mean():.2f}")

    st.markdown("### 📊 Dataset View")
    st.dataframe(paginated_data, use_container_width=True)

if __name__ == "__main__":
    main()