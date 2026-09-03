import streamlit as st
import re
import torch
import time
import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Text Summarizer", page_icon="🧠")
st.title("🧠 AI Text Summarizer")

model_id = "AhmedSheta10/my-t5-summarizer"

# 2. تحميل الموديل (استخدام Caching لمنع إعادة التحميل مع كل ضغطة)
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained(model_id)
    model = T5ForConditionalGeneration.from_pretrained(model_id)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    
    return tokenizer, model, device

tokenizer, model, device = load_model()

# 3. دالة التنظيف
def clean_text(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", "", text)
    text = text.strip().lower()
    return text

# 4. دالة تأثير الكتابة (Streaming)
def stream_response(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.02)

# 5. بناء واجهة المستخدم
user_input = st.text_area("أدخل المحادثة المراد تلخيصها هنا:", height=200)

if st.button("تلخيص المحادثة (Summarize)"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            # تجهيز النص
            cleaned_message = clean_text(user_input)
            final_message = "summarize: " + cleaned_message
            
            inputs = tokenizer(
                final_message,
                return_tensors="pt",
                truncation=True,
                max_length=512
            ).to(device)
            
            # التوليد
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_length=175,
                    num_beams=4,
                    do_sample=True,
                    temperature=0.7
                )
                
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # عرض النتيجة بتأثير الكتابة
        st.write("### الملخص:")
        st.write_stream(stream_response(response))
    else:
        st.warning("رجاءً أدخل نصاً أولاً!")

