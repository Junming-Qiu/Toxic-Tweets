import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification
from huggingface_hub.inference_api import InferenceApi
import os

models = ["cardiffnlp/twitter-xlm-roberta-base-sentiment", "nlptown/bert-base-multilingual-uncased-sentiment", "Tatyana/rubert-base-cased-sentiment-new", "junming-qiu/BertToxicClassifier"]



st.title('Sentiment Analysis Demo')
with st.form("form"):
    selection = st.selectbox('Select Transformer:', models)
    text = st.text_input('Enter text: ', "I do not like to walk")
    submitted = st.form_submit_button('Submit')

    if submitted:
        model_name = models[models.index(selection)]

        if model_name == "junming-qiu/BertToxicClassifier":
            API_TOKEN=os.environ['API-KEY']
            inference = InferenceApi(repo_id=model_name, token=API_TOKEN)
            predictions = inference(inputs=text)[0]
            predictions = sorted(predictions, key=lambda x: x['score'], reverse=True)
            st.write(predictions[0]['label']+":", predictions[0]['score'])
            st.write(predictions[1]['label']+":", predictions[1]['score'])
        else:

            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
            result = classifier(text)
            st.write("Label:", result[0]["label"])
            st.write('Score: ', result[0]['score'])
        