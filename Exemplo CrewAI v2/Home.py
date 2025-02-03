import streamlit as st
from pathlib import Path
import time
import asyncio
from mult_agents_run import multi_agent_system

FILE_FOLDER = Path(__file__).parent / "documents"

def sidebar():
    st.header(":red[Coloque seus documentos]")
    uploaded_document = st.file_uploader(
        "Coloque seu documento aqui",
        type=["pdf", "docx", "md", "txt"],
        accept_multiple_files=False
    )
    print(st.session_state)
    if uploaded_document is not None:
        # Limpa a pasta de documentos
        for document in FILE_FOLDER.glob("*"):
            document.unlink()
        
        # Salva o novo documento
        with open(FILE_FOLDER / uploaded_document.name, 'wb') as document_files:
            document_files.write(uploaded_document.read())
        
        label_button = "Inicializar Análise"
        
        if "chain" in st.session_state:
            label_button = "Atualizar Análise"
        if st.button(label_button, use_container_width=True):
            st.session_state["document"] = uploaded_document
            st.success("Gerando Novo Documento...")   
            time.sleep(2)
            asyncio.run(multi_agent_system())
            st.rerun()     
                
def home():
    st.header("🤖Análisador de Normas LGPD")
    if "document" not in st.session_state:
        st.error("Adicione arquivos para inicializar a Inteligência Artificial")
        st.stop()   
    # Exibir o conteúdo do arquivo atualizado
    with open("documento_atualizado.md", 'r', encoding='utf-8') as file:
        markdown_content = file.read()
        st.header("Seu contrato Atualizado com as Normas LGPD\n", divider=True)
        st.markdown(markdown_content)
    
def main():   
    with st.sidebar:
        sidebar()
    home() 
    
if __name__ == "__main__":
   main()
    
    