import streamlit as st
import os

# NLP packages
import spacy
from textblob import TextBlob
from gensim.summarization import summarize

# pcks
from sumy.parsers.plaintext import PlainTextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docx):
    parser = PlainTextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary] 
    result = ' '.join(summary_list)
    return result


@st.cache
def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    return tokens




def main():
    st.title("Explore NLP")
    st.subheader("NLP on the go")
    # Tokenisation
    if st.checkbox("show tokkens and lemma"):
        st.subheader("Tokenize your text : ")
        message = st.text_area("Enter your text" , "Type here")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.success(nlp_result)
    # text Analysis
    if st.checkbox("show sentiment analyses"):
        st.subheader("Lets check the sentence how it is sounded")
        message = st.text_area("Enter your text","type here")
        if st.button("Analyze"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    # text summarization
    if st.checkbox("Show Text summarization"):
        message = st.button("Enter your text here", "Type here")
        summary_options = st.select_box("choose your summarization tech",("gensim",'sumy'))
        if st.button("Summarise"):
            if summary_options == 'gensim':
                st.text("using Gensi..")
                summary_result = summarize(message)
            elif summary_options == 'sumy':
                st.text("using sumy..")
                summary_result = sumy_summrizer(message)
            else:
                st.warning("using default summarizer")
                st.text("using gensim..")
                summary_result = summarize(message)
            st.success(summary_result)
    st.sidebar.subheader("About app")
    st.sidebar.text("NLP")
    st.sidebar.info("begining of deployment")


if __name__ == '__main__':
    main()