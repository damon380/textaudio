import streamlit as st
import pyttsx3
import pdfplumber
import requests

st.set_page_config(layout="wide")

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
        

def extract_data(feed):
    data = ""
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        for p in pages:
            data = data + p.extract_text()
    return data 

def main():
    st.header('Text and Audio Extractor with Streamlit')
    st.sidebar.title("Text and Audio Extractor")
    st.sidebar.header("Extract from PDF")
    page = st.sidebar.selectbox("Tool", ["Text Extractor", "Audio Extractor"])

    if  page == 'Text Extractor':
        st.title('Text Extractor')
        uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
        if uploaded_file is not None:
            df = extract_data(uploaded_file)

            st.write(df)

    elif page == 'Audio Extractor':
        st.title('Audio Extractor')
        free = st.text_area("Enter your text here ",max_chars=5000)
        speaker = pyttsx3.init()
        newrate=200
        speaker.setProperty('rate', newrate)
        newvolume=200
        speaker.setProperty('volume', newvolume)
        speaker.say(free)
        speaker.save_to_file(free , r'C:\users\public\freetextaudio.mp3')
        speaker.runAndWait()

        
        uploaded_file1 = st.file_uploader('Alternatively, choose your .pdf file', type="pdf")
        if uploaded_file1 is not None:
            df1 = extract_data(uploaded_file1)
            speaker.say(df1)
            speaker.save_to_file(df1 , r'C:\users\public\pdftextaudio.mp3')
            speaker.runAndWait()

                    
    else:
        st.write( 'Error404')
    
if __name__ == '__main__':
    main()

