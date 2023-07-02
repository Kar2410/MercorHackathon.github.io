# Team NeuronX - Ask Anything 💬

This is a Python application that allows you to load a PDF, Video, Web Pages, Github Repo and ask questions about it using natural language. The application uses a LLM to generate a response about your PDF. The LLM will not answer questions unrelated to the document.

## How it works

The application reads the PDF and splits the text into smaller chunks that can be then fed into a LLM. It uses OpenAI embeddings to create vector representations of the chunks. The application then finds the chunks that are semantically similar to the question that the user asked and feeds those chunks to the LLM to generate a response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.


## Installation

To install the repository, please clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to add your OpenAI API/ Hugging Face API  key to the `.env` file.

## Usage

To use the application, run the `app.py` file with the streamlit CLI (after having installed streamlit): 

```
streamlit run app.py
```
## Demo Link
https://kar2410.github.io/MercorHackathon.github.io/

## Video Link
https://drive.google.com/file/d/1IgmyAjczCknHr_aEvylIJ9J6G8_cK4HI/view?usp=drive_link

## Screenshots

## Homepage

![image](https://github.com/Kar2410/MercorHackathon.github.io/assets/89201634/029d7800-8272-403b-8e4b-bb0d5c2209c5)

## PDF Module

![image](https://github.com/Kar2410/MercorHackathon.github.io/assets/89201634/d2973c57-ed4d-4a90-a0ca-e0596a68272d)

## Video Module

![video](https://github.com/Kar2410/MercorHackathon.github.io/assets/89201634/95f5f75b-fec0-4521-8af6-e99ad6ee98bb)

## Github Repository Module

![githubrepo](https://github.com/Kar2410/MercorHackathon.github.io/assets/89201634/5c22cf22-6c77-43e9-8d96-05a92b3e41b3)

## Webpage Module

![webpage](https://github.com/Kar2410/MercorHackathon.github.io/assets/89201634/6d9bd6bd-8012-4518-b45c-3edc0df6438d)

## Contributing

If you are thinking of contributing to this repository (hooray! 🎉), please make sure you gone through project idea
Fork repo, add changes, pull-request. Please update both: app.py & requirements.txt file





