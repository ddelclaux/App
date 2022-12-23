
import streamlit as st
import transformers
from transformers import pipeline


# Crea la interfaz de usuario con Streamlit
st.sidebar.title("Opciones")
opcion = st.sidebar.selectbox("Elige un modelo", ["Resumir", "Q & A"])


#Bienvenidos a la App
if opcion == "Resumir":
    st.title('Resumir')
    texto = st.text_area('Ingrese el texto a resumir', 'Escriba aquí el texto')
    longitud_resumen = st.slider('Seleccione la longitud del resumen', min_value=1, max_value=500, value=10)
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn', tokenizer='facebook/bart-large-cnn')
    if st.button('Generar Resumen'):
        resumen = summarizer(texto, max_length=longitud_resumen)
        st.success('Aquí está el resumen:')
        st.write(resumen[0]['summary_text'])
    

# Create the pipeline
q_and_a = pipeline('question-answering')

if opcion == "Q & A":
    st.title('Q & A')
    text_input = st.text_area("Please enter the text:")
    question_input = st.text_input("Please enter the question:")
    if st.button("Ask the model"):
        answer = q_and_a(context=text_input, question=question_input)
        st.write("Answer: ", answer['answer'])
