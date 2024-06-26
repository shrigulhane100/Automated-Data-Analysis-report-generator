import streamlit as st
import pandas as pd
from io import StringIO
import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title = 'Online data analyse report',layout='wide')


# Web App Title
st.markdown(
    """
    <div style='text-align:center; background-color:#1abc9c; padding: 20px'>
        <h1>Online Data Analysis report generator</h1>
        <h3>Download your interactive report in seconds</h3>
        <div style='background-color:#1abc9c; padding: 10px'>
            <p style='margin-bottom: 0;'><b>Developer :</b> <a href='https://github.com/shrigulhane100'>Shriyash Gulhane</a> </p>
            <p style='margin-top: 0;'>Unleash the power of your data</p>
        </div>
    </div>
    <div style='height: 5px'></div>
    """,
    unsafe_allow_html=True)


# Upload CSV data
with st.sidebar.header('Upload Your CSV Dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example Of CSV input file](https://github.com/shrigulhane100/Automated-Data-Analysis-report-generator/blob/main/CSV%20files%20for%20website%20demo/automobile_data.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
    export=pr.to_html()
    st.download_button(label="Download Report", data=export.encode(), file_name='report.html', mime='text/html')

else:
    st.markdown(
        """
        <div style='background-color: #occ9bc; padding: 10px;'>
            <h3 style='margin-top: 0;'>Awaiting CSV file upload</h3>
            <p style='margin-bottom: 0;'>Please upload a CSV file to begin the analysis.</p>
            <p style='margin-top: 0;'>Alternatively, click the button below to use an example dataset.</p>
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown(
        """
        <div style='height:5px'></div>
        """,
        unsafe_allow_html=True)
    if st.button('Press to use Example Dataset'):
        st.markdown(
            """
            <div style='background-color: #4b8b3b; padding: 10px; margin-top: 5px;'>
                <p style='margin-bottom: 0;'>Using example dataset.</p>
            </div>
            """,
            unsafe_allow_html=True)

        
        # Example data
        @st.cache_data
        def load_data():
            url = 'https://raw.githubusercontent.com/shrigulhane100/Automated-Data-Analysis-report-generator/main/CSV%20files%20for%20website%20demo/phone_data.csv'
            df = pd.read_csv(url)
            return df
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
        export=pr.to_html()
        st.download_button(label="Download Report", data=export.encode(), file_name='report.html', mime='text/html')
      
        

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
