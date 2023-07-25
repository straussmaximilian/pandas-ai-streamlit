import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt


def gen_prompt(prompt):
    if 'plot' in prompt.lower():
        prompt = f"""
        {prompt}.
        Show the plot, and return the data in the following
        JSON format: {{"x": , "y": , "plot_type":, "plot_title": }}
        """
    return prompt

st.title("pandas-ai streamlit interface")

st.write("A demo interface for [PandasAI](https://github.com/gventuri/pandas-ai)")

if "openai_key" not in st.session_state:
    with st.form("API key"):
        key = st.text_input("OpenAI Key", value="", type="password")
        if st.form_submit_button("Submit"):
            if not len(key):
                key = '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'
            st.session_state.openai_key = key
            st.session_state.prompt_history = []
            st.session_state.df = None

examples = f"""
Here are some example queries:
- Plot the number of customer by country in a pie chart
- Plot the mean total over time for Germany
- How many customers are there in Oslo
"""
with st.sidebar:
    st.markdown(examples)

if "openai_key" in st.session_state:
    if st.session_state.df is None:
        uploaded_file = st.file_uploader(
            "Choose a CSV file. This should be in long format (one datapoint per row).",
            type="csv",
        )
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
    if st.session_state.df is not None:
        st.subheader("Current dataframe:")
        st.write(st.session_state.df)
    with st.form("Question"):
        question = st.text_input("Question", value="", type="default")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner():
                llm = OpenAI(api_token=st.session_state.openai_key)
                pandas_ai = PandasAI(llm)
                x = pandas_ai(st.session_state.df, prompt=gen_prompt(question))
                fig = plt.gcf()
                if fig.get_axes():
                    st.pyplot(fig)
                st.write(x)
                st.session_state.prompt_history.append(question)

    st.subheader("Prompt history:")
    st.write(st.session_state.prompt_history)


if st.button("Clear"):
    st.session_state.prompt_history = []
    st.session_state.df = None
