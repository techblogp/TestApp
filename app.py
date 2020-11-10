import spacy_streamlit
import spacy
nlp = spacy.load("en_core_web_sm")

# models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
# spacy_streamlit.visualize(models, default_text)