import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello Stream")


# Display a simple Text
df = pd.DataFrame({
    'first Column ': [1, 2, 3, 4, 5],
    'second column': [10, 20, 30, 40, 50]
})

# Display the DataFrame
st.write("Here is the DataFrame")
st.write(df)


# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
