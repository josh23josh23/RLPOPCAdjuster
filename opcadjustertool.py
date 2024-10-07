import streamlit as st
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

hide_st_style = """
    <style>
    /* Initially hide header and footer */
    header, footer {
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
        background-color: rgba(255, 255, 255, 0.95); /* White background with slight transparency */
        color: black !important; /* Black text color for visibility */
        padding: 10px; /* Add some padding for better visibility */
        border-radius: 5px; /* Optional: Rounded corners */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Optional: Subtle shadow */
    }

    /* Show header and footer on hover */
    header:hover, footer:hover {
        opacity: 1;
    }

    /* Styling specifically for Streamlit's header menu */
    .css-1v0mbdj, .css-1q8dd3e, .stDropdown-menu {
        background-color: rgba(255, 255, 255, 0.95) !important; /* White background for the menu */
        color: black !important; /* Black text inside the menu */
    }

    /* Styling for dropdown menu items */
    .stDropdown-item, .css-1q8dd3e * {
        background-color: rgba(255, 255, 255, 0.95) !important; /* White background */
        color: white !important; /* White text for the items */
    }

    /* Additional styles to ensure the deploy button and text are visible */
    .stButton button {
        color: black !important;
        background-color: white !important;
        border: 2px solid #ddd !important;
        border-radius: 5px;
    }

    .stButton button:hover {
        background-color: #e0e0e0 !important; /* Lighter background on hover */
        border-color: #ccc !important;
    }
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

def add_bg_image():
    st.markdown(
        """
        <style>
        /* Apply background image to the full Streamlit app container */
        .stApp {
            background-image: url("https://raw.githubusercontent.com/josh23josh23/FEASO/refs/heads/main/peakpx%20(1).jpg");
            background-size: cover; /* Ensure background covers the entire container */
            background-position: center; /* Center the background */
            background-repeat: no-repeat; /* Prevent repeating */
            background-attachment: scroll; /* Background moves when scrolling */
        }

        /* Styling for the main content container */
        .stApp .block-container {
            background-color: rgba(255, 255, 255, 1); /* Light transparent white background for readability */
            color: black; /* Black text for better contrast */
            border-radius: 15px; /* Rounded corners for the container */
            padding: 2rem; /* Padding inside the container */
            width: 80%; /* Set the width of the container */
            max-width: 900px; /* Set a maximum width */
            margin: 5rem auto; /* Center the container and add space on top */
            box-shadow: 0 4px 35px rgba(0,0,0,0.8); /* Add subtle shadow for depth */
        }

        /* Logo container styling */
        .logo-img-container {
            display: flex;
            justify-content: center; /* Center the logo horizontally */
            position: relative;
            width: 100%;
            z-index: 2; /* Keep the logo on top */
        }

        /* Logo image styling */
        .logo-img-container img {
            width: 350px; /* Set a fixed size for the logo */
            margin-top: 1rem; /* Add space on top */
            z-index: 2; /* Ensure the logo stays on top */
        }

        /* Markdown text container styling */
        .markdown-text-container {
            padding: 2rem 1rem;
            border-radius: 15px; /* Add rounded corners to the text box */
            background-color: rgba(255, 255, 255, 0.9); /* Add a light transparent background */
            position: relative;
            top: -3rem; /* Adjust the vertical position */
            z-index: 1; /* Ensure the text is layered properly */
        }

        /* Center the title */
        .title-container {
            text-align: center; /* Center the title text */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

# Logo at the top center with increased size
st.markdown("""
    <div class="logo-img-container">
        <img src="https://raw.githubusercontent.com/josh23josh23/RLPOPCAdjuster/refs/heads/main/grange-dark-blue-no-bg.png">
    </div>
""", unsafe_allow_html=True)

# Title in a container to ensure it's centered
st.markdown("""
    <div class="title-container">
        <h1>Tuning Tool</h1>
    </div>
""", unsafe_allow_html=True)


# Set custom CSS for styling
def load_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        /* Set global font style */
        html, body, div, h1, h2, h3, h4, h5, h6, p, a, span, label, button, textarea, select, input {
            font-family: 'Poppins', sans-serif !important;
        }

        /* Center the table title */
        .table-title {
            text-align: center;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        /* Style for the dataframe to give it an Excel-like look */
        .dataframe-table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }

        .dataframe-table th, .dataframe-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }

        .dataframe-table th {
            background-color: #E8F4FA;
            font-weight: 600;
        }
        
        .dataframe-table td {
            background-color: white;
        }

        /* Adjust spacing between labels and inputs */
        .input-label {
            margin-bottom: -50px; /* Reduce the space between label and input */
            font-size: 18px;
            font-weight: bold;
            text-align: center; /* Center the text */
        }

        /* Set font and alignment for number inputs */
        input[type=number] {
            font-family: 'Poppins', sans-serif !important;
            text-align: center; /* Center the text in the input */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Load CSS for the app
load_custom_css()

# Title for the app
st.markdown("<div class='table-title'>OPC Tuner</div>", unsafe_allow_html=True)

# Define the initial data for OPC adjuster
opc_data = {
    "OPC ($)": [115000],
    "OPC Default Land Size": [450],
    "Desired Lot Size": [500],
    "Adjusted OPC": [0],
}

# Create a DataFrame for OPC
opc_df = pd.DataFrame(opc_data)

# Create columns for OPC inputs
col1, col2, col3 = st.columns([1, 1, 1])

# Editable number inputs for OPC with styled labels
with col1:
    st.markdown("<div class='input-label'>Default OPC</div>", unsafe_allow_html=True)
    opc = st.number_input("", value=int(opc_df.at[0, "OPC ($)"]), step=1000, format="%d", key="opc")

with col2:
    st.markdown("<div class='input-label'>OPC Default Land Size</div>", unsafe_allow_html=True)
    opc_default_land_size = st.number_input("", value=int(opc_df.at[0, "OPC Default Land Size"]), step=1, key="opc_default_land_size")

with col3:
    st.markdown("<div class='input-label'>Desired Lot Size</div>", unsafe_allow_html=True)
    desired_lot_size = st.number_input("", value=int(opc_df.at[0, "Desired Lot Size"]), step=1, key="opc_desired_lot_size")

# Calculate the "Adjusted OPC" value based on the new formula
if desired_lot_size >= 1200:
    adjusted_opc = Decimal(opc) * Decimal('1.38')
else:
    percent_change_in_land = Decimal((desired_lot_size - opc_default_land_size) / opc_default_land_size)
    adjustment_factor = (percent_change_in_land * Decimal('0.15')) / Decimal('0.4')
    adjusted_opc = Decimal(opc) + (Decimal(opc) * adjustment_factor)

# Update the Adjusted OPC in the DataFrame
opc_df.at[0, "Adjusted OPC"] = round(adjusted_opc)

# Format Adjusted OPC as currency
opc_df["OPC ($)"] = opc_df["OPC ($)"].apply(lambda x: "${:,.0f}".format(x))
opc_df["Adjusted OPC"] = opc_df["Adjusted OPC"].apply(lambda x: "${:,.0f}".format(x))

# Display the Adjusted OPC table
st.markdown(f"""
    <table class="dataframe-table">
        <tr>
            <th>Adjusted OPC at {desired_lot_size}</th>
        </tr>
        <tr>
            <td>{opc_df.at[0, "Adjusted OPC"]}</td>
        </tr>
    </table>
""", unsafe_allow_html=True)


# Title for the RLP adjuster section
st.markdown("<div class='table-title'>RLP Tuner</div>", unsafe_allow_html=True)

# Define the initial data for RLP adjuster
rlp_data = {
    "RLP ($)": [115000],
    "RLP Default Land Size": [450],
    "Desired Lot Size": [500],
    "Adjusted RLP": [0],
}

# Create a DataFrame for RLP
rlp_df = pd.DataFrame(rlp_data)

# Create columns for RLP inputs
col4, col5, col6 = st.columns([1, 1, 1])

# Editable number inputs for RLP with styled labels
with col4:
    st.markdown("<div class='input-label'>Default RLP</div>", unsafe_allow_html=True)
    rlp = st.number_input("", value=int(rlp_df.at[0, "RLP ($)"]), step=1000, format="%d", key="rlp")

with col5:
    st.markdown("<div class='input-label'>RLP Default Land Size</div>", unsafe_allow_html=True)
    rlp_default_land_size = st.number_input("", value=int(rlp_df.at[0, "RLP Default Land Size"]), step=1, key="rlp_default_land_size")

with col6:
    st.markdown("<div class='input-label'>Desired Lot Size</div>", unsafe_allow_html=True)
    rlp_desired_lot_size = st.number_input("", value=int(rlp_df.at[0, "Desired Lot Size"]), step=1, key="rlp_desired_lot_size")

# Create the RLP adjustment lookup table (mimicking Excel's VLOOKUP)
rlp_adjustment_table = [
    (0, 0.09, Decimal('0')),
    (0.1, 0.1, Decimal('0.022')),
    (0.11, 0.2, Decimal('0.054')),
    (0.21, 0.3, Decimal('0.126')),
    (0.31, 0.4, Decimal('0.174')),
    (0.41, 0.5, Decimal('0.244')),
    (0.51, 0.6, Decimal('0.387')),
    (0.61, 0.7, Decimal('0.475')),
    (0.71, 0.8, Decimal('0.518')),
    (0.81, 0.9, Decimal('0.594')),
    (0.91, 1, Decimal('0.67'))
]

# Calculate the "Adjusted RLP" value using the provided logic
percent_change_in_land_rlp = Decimal((rlp_desired_lot_size - rlp_default_land_size) / rlp_default_land_size)

def get_adjustment(percent_change):
    for min_val, max_val, adjustment in rlp_adjustment_table:
        if min_val <= percent_change <= max_val:
            return adjustment
    return None

if percent_change_in_land_rlp == 0:
    adjusted_rlp = Decimal(rlp)
elif percent_change_in_land_rlp > 1:
    adjusted_rlp = "Not Supported"
else:
    adjustment = get_adjustment(abs(percent_change_in_land_rlp))
    if adjustment is not None:
        adjusted_rlp = Decimal(rlp) + (Decimal(rlp) * adjustment) if percent_change_in_land_rlp >= 0 else Decimal(rlp) - (Decimal(rlp) * adjustment)
    else:
        adjusted_rlp = Decimal(rlp)

# Update the Adjusted RLP in the DataFrame
rlp_df.at[0, "Adjusted RLP"] = adjusted_rlp if isinstance(adjusted_rlp, str) else round(adjusted_rlp)

# Format Adjusted RLP as currency if it's a number
if not isinstance(adjusted_rlp, str):
    rlp_df["RLP ($)"] = rlp_df["RLP ($)"].apply(lambda x: "${:,.0f}".format(x))
    rlp_df["Adjusted RLP"] = rlp_df["Adjusted RLP"].apply(lambda x: "${:,.0f}".format(x))

# Display the Adjusted RLP table
st.markdown(f"""
    <table class="dataframe-table">
        <tr>
            <th>Adjusted RLP at {rlp_desired_lot_size}</th>
        </tr>
        <tr>
            <td>{rlp_df.at[0, "Adjusted RLP"]}</td>
        </tr>
    </table>
""", unsafe_allow_html=True)
