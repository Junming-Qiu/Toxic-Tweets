import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


models = ["cardiffnlp/twitter-xlm-roberta-base-sentiment", "nlptown/bert-base-multilingual-uncased-sentiment", "Tatyana/rubert-base-cased-sentiment-new"]



st.title('Sentiment Analysis Demo')
st.markdown("Junming Qiu")
with st.form("form"):
    selection = st.selectbox('Select Transformer', models)
    text = st.text_input('Enter text: ', "I do not like to walk")
    submitted = st.form_submit_button('Submit')

    if submitted:
        model_name = models[models.index(selection)]
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        st.write(classifier(text))