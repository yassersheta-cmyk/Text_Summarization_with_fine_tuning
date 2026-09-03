# 🧠 AI Text Summarizer

An abstractive text summarization web application built with **Streamlit** and a custom fine-tuned **T5 model**. 

To optimize performance and bypass GitHub's storage limitations (Git LFS) for large AI models, this project uses a decoupled architecture: the lightweight application code is hosted here on GitHub, while the heavy model weights are dynamically loaded from the Hugging Face Model Hub during runtime.

## 🚀 Live Demo
You can try the live application here: **[https://nlpprojects-dyuij8jwbhhgdhtiozzfwb.streamlit.app/]**

## 🛠️ Tech Stack
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Machine Learning:** PyTorch, Hugging Face `transformers`
* **Model:** Fine-tuned `t5-small/base`
* **Model Hosting:** Hugging Face Model Hub

## 🏗️ Architecture
1. **GitHub Repository:** Contains only the application logic (`app.py`) and dependencies (`requirements.txt`), keeping the repo lightweight and fast to deploy.
2. **Hugging Face Hub:** Hosts the fine-tuned model weights and tokenizer (`AhmedSheta10/my-t5-summarizer`).
3. **Inference:** Upon running, the app automatically fetches the model from Hugging Face and caches it in memory for fast text summarization.


## 💻 Local Installation

If you want to run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yassersheta-cmyk/NLP_Projects.git
   cd NLP_Projects




2.Install the required dependencies:

```Bash
pip install -r requirements.txt

3.Run the application:

```Bash
streamlit run app.py

👨‍💻 Author: Ahmed Sheta

🌐 Hugging Face: AhmedSheta10 | GitHub: yassersheta-cmyk

   


