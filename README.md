# pandas-ai-streamlit
A streamlit interface for pandas-ai

## Installation & Running:

```
git clone https://github.com/straussmaximilian/pandas-ai-streamlit.git
conda create --name pandasai python=3.10
conda activate pandasai
pip install pandasai streamlit BeautifulSoup4
cd pandas-ai-streamlit
streamlit run app.py
```

Check requirements in case there are compatibility issues. Tested with `pandasai==1.2.8`.

## Streamlit Share

Running [here](https://pandas-ai-gui.streamlit.app)
Note: This is the stable version with pandas-ai version 0.2.2. 

## Notes
- Updated to pandasai==1.2.8. Charts are stored as `temp_chart.png` and now they are loaded from there. The implementation is not perfect an might cause issues when having multiple concurrent users.
