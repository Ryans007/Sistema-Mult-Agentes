# type: ignore
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,FileReadTool,MDXSearchTool
import yaml
import os
from IPython.display import Markdown, display
import streamlit as st
from utils import get_openai_api_key, get_serper_api_key
import warnings
warnings.filterwarnings('ignore')

# Load environment variables
from utils import load_env
load_env()


async def multi_agent_system():
    openai_api_key = get_openai_api_key()
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
    os.environ["SERPER_API_KEY"] = get_serper_api_key()

    # Loading Tasks and Agents YAML files
    files = {
        'agents': 'configs/agents.yaml',
        'tasks': 'configs/tasks.yaml'
    }

    configs = {}
    for config_type, file_path in files.items():
        with open(file_path, 'r') as config_file:
            configs[config_type] = yaml.safe_load(config_file)
            
    agents_config = configs['agents']
    tasks_config = configs['tasks']

    # configure tools
    ferramenta_busca = SerperDevTool()
    ferramenta_aprofundamento = ScrapeWebsiteTool()
    ferramenta_leitura_arquivo = FileReadTool(file_path="./documents/fake_document.md")
    ferramenta_busca_semantica = MDXSearchTool(mdx="./documents/fake_document.md")

    # Creating Agents
    agente_especialista_classificador_lgpd = Agent(
        config=agents_config["agente_especialista_classificador_lgpd"],
        tools=[
            ferramenta_busca, 
            ferramenta_aprofundamento, 
            ferramenta_leitura_arquivo, 
            ferramenta_busca_semantica
        ]
    )

    agente_anonimizador = Agent(
        config=agents_config["agente_anonimizador"]
    )

    agente_revisador_lgpd = Agent(
        config=agents_config["agente_revisador_lgpd"],
        tools=[
            ferramenta_busca,
            ferramenta_aprofundamento
        ]
    )

    # Creating Tasks
    task_especialista_classificador_lgpd = Task(
        config=tasks_config["task_especialista_classificador_lgpd"],
        agent=agente_especialista_classificador_lgpd
    )

    task_anonimizador = Task(
        config=tasks_config["task_anonimizador"],
        agent=agente_anonimizador,
        context=[task_especialista_classificador_lgpd]
    )

    task_revisador_lgpd = Task(  
        config=tasks_config["task_revisador_lgpd"],
        agent=agente_revisador_lgpd,
        context=[task_especialista_classificador_lgpd, task_anonimizador],
        output_file="documento_atualizado.md" 
    )

    # Creating Crew
    crew = Crew(
        agents=[
            agente_especialista_classificador_lgpd,
            agente_anonimizador,
            agente_revisador_lgpd
        ],
        tasks=[
            task_especialista_classificador_lgpd,
            task_anonimizador,
            task_revisador_lgpd
        ]
    )
    
    await crew.kickoff_async()
    
    # Exibir o conteúdo do arquivo atualizado
    with open("documento_atualizado.md", 'r', encoding='utf-8') as file:
        markdown_content = file.read()
        st.header("Seu contrato Atualizado\n", divider=True)
        st.markdown(markdown_content)