import streamlit as st
from pathlib import Path
from IPython.display import Markdown, display
import time
from mult_agents_run import multi_agent_system

FILE_FOLDER = Path(__file__).parent / "documents"

def home():
    st.header("Coloque os documentos que você deseja verificar se estão de acordo com as normas LGPD")
    uploaded_document = st.file_uploader(
        "Coloque seu documento aqui",
        type=["pdf", "docx", "md", "txt"],
        accept_multiple_files=False
    )
    
    if uploaded_document is not None:
        # Limpa a pasta de documentos
        for document in FILE_FOLDER.glob("*"):
            document.unlink()
        
        # Salva o novo documento
        with open(FILE_FOLDER / uploaded_document.name, 'wb') as document_files:
            document_files.write(uploaded_document.read())
        with open(FILE_FOLDER / uploaded_document.name, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        st.header("Seu contrato Atual\n", divider=True)
        st.markdown(markdown_content)
        
        if st.button(
            "Clique para gerar novo documento de acordo com as normas da LGPD!!!",
            use_container_width=True):
            st.success("Gerando Novo Documento...")
            time.sleep(2)
            import asyncio
            asyncio.run(multi_agent_system())
                   
            
if __name__ == "__main__":
    home()
    
    