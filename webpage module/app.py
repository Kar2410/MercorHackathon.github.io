import requests

import streamlit as st
from transformers import pipeline

# streamlit run app.py --server.clearCache

def main():
    
    st.set_page_config(page_title="Ask your Webpage")
    st.header("Ask your Webpage 💬")
    
    # Get webpage link from user
    webpage_link = st.text_input("Enter the webpage link:")
    
    if webpage_link:
        # Fetch webpage content
        webpage_content = fetch_webpage_content(webpage_link)
        
        if webpage_content:
            # Show user input
            user_question = st.text_input("Ask a question about the webpage:")
            
            if user_question:
                # Load the pre-trained Q&A model
                model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
                qa_model = pipeline("question-answering", model=model_name)
                
                # Ask a question and get the answer
                answer = qa_model(question=user_question, context=webpage_content)
                st.write(answer["answer"])

def fetch_webpage_content(webpage_link):
    # Fetch webpage content
    response = requests.get(webpage_link)
    
    if response.status_code == 200:
        return response.text
    else:
        st.write("Failed to fetch webpage content.")
        return None

if __name__ == "__main__":
    main()
