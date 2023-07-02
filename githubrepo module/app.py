import requests

import streamlit as st
from transformers import pipeline
import base64

# streamlit run app.py --server.clearCache

def main():
    
    st.set_page_config(page_title="Ask your GitHub Repository")
    st.header(" Mercor Hackathon - Ask your GitHub Repository 💬")

    # get GitHub repository link from user
    repo_link = st.text_input("Enter the GitHub repository link:")
    
    if repo_link:
        # extract owner and repository name from the link
        owner, repo = parse_github_link(repo_link)
        
        # fetch repository information using GitHub API
        repository_info = fetch_repository_info(owner, repo)
        
        if repository_info:
            # extract relevant information from repository API response
            description = repository_info["description"]
            readme_content = fetch_readme_content(owner, repo)
            
            if readme_content:
                # combine repository information into the context
                context = f"{description}\n\n{readme_content}"
                
                # show user input
                user_question = st.text_input("Ask a question about the repository:")
                
                if user_question:
                    # load the pre-trained Q&A model
                    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
                    qa_model = pipeline("question-answering", model=model_name)
                    
                    # ask a question and get the answer
                    answer = qa_model(question=user_question, context=context)
                    st.write(answer["answer"])

def parse_github_link(link):
    # extract owner and repository name from the GitHub repository link
    # example link: https://github.com/owner/repo
    parts = link.strip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo

def fetch_repository_info(owner, repo):
    # fetch repository information using GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.write("Failed to fetch repository information.")
        return None

def fetch_readme_content(owner, repo):
    # fetch README content from GitHub repository using GitHub API
    readme_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(readme_url, headers=headers)
    if response.status_code == 200:
        readme_info = response.json()
        readme_content = base64.b64decode(readme_info["content"]).decode("utf-8")
        return readme_content
    else:
        st.write("Failed to fetch README content.")
        return None

if __name__ == "__main__":
    main()
