# 🚀 Multi AI Agent Systems com CrewAI

Este repositório contém exercícios e projetos desenvolvidos durante os cursos introdutório e avançado da CrewAI. Além disso, inclui um caso de uso próprio para a aplicação prática dos conceitos aprendidos.

## 📂 Estrutura do Repositório

### 📌 **Multi AI Agent Systems — with CrewAI!**
Essa pasta contém os exercícios do curso introdutório da CrewAI:

- **L2_research_write_article** → Pesquisa e Redação de Artigo
- **L3_customer_support** → Suporte ao Cliente
- **L4_tools_customer_outreach** → Ferramentas para Contato com Clientes
- **L5_tasks_event_planning** → Planejamento de Eventos
- **L6_collaboration_financial_analysis** → Colaboração para Análise Financeira
- **L7_job_application_crew** → Candidatura para Vagas com CrewAI

### 📌 **Practical Multi AI Agents and Advanced Use Cases with CrewAI**
Essa pasta contém os exercícios do curso mais avançado da CrewAI. Alguns códigos podem não estar funcionando e serão corrigidos futuramente.

- **L1**: Projeto Automatizado: Planejamento, Estimativa e Alocação
- **L2**: Interação Externa: Relatório de Progresso do Projeto
- **L3**: Pipeline de Vendas
- **L4**: Suporte à Análise de Insights de Dados
- **L5**: Criação de Conteúdo em Escala

### 📌 **Exemplo CrewAI**
Caso de uso de minha autoria para treinar conceitos abordados no curso.

#### **🛠️ Problema**
Muitos clientes desejam revisar seus documentos de forma automatizada para garantir conformidade com as normas da **LGPD (Lei Geral de Proteção de Dados).**

#### **💡 Solução**
Desenvolvimento de um **sistema multiagente** capaz de:
1. **Verificar documentos** para garantir conformidade com as normas da LGPD.
2. **Tratar documentos não conformes**, anonimizando dados sensíveis.
3. **Devolver os documentos revisados** e tratados aos clientes.

#### **🤖 Agentes Utilizados**
- **Agente 1: Especialista em LGPD**
  - **Função:** Verificar e analisar trechos do documento que não estão em conformidade com a LGPD.
  - **Responsabilidade:** Identificar dados sensíveis e apontar ajustes necessários para atender às regulamentações.

- **Agente 2: Anonimizador de Dados**
  - **Função:** Anonimizar dados sensíveis presentes no documento, substituindo-os por caracteres genéricos (ex: "XXX").
  - **Responsabilidade:** Garantir que todos os dados identificados pelo Agente 1 sejam devidamente tratados.

- **Agente 3: Revisor e Formalizador**
  - **Função:** Verificar se o Agente 2 anonimizou corretamente os dados conforme a análise do Agente 1. Além disso, aprimorar o texto, tornando-o mais formal e adequado ao ambiente jurídico.
  - **Responsabilidade:** Assegurar que o documento final esteja em conformidade com a LGPD, com texto claro, formal e profissional.

### 📌 **Exemplo CrewAI v2**
Essa pasta contém melhorias no **Exemplo CrewAI**, incluindo o desenvolvimento de uma **interface gráfica** e a futura implementação de funcionalidades avançadas do curso avançado da CrewAI.

## 📦 Instalação das Dependências
Para instalar todas as dependências do projeto, basta executar o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

Isso garantirá que todas as bibliotecas essenciais sejam instaladas corretamente, incluindo:

- **CrewAI**: Biblioteca para criação e gerenciamento de sistemas multiagentes baseados em IA.
- **Streamlit**: Framework para criação de interfaces gráficas interativas para aplicações Python.
- **FastAPI**: Framework para desenvolvimento de APIs rápidas e eficientes.
- **SQLAlchemy**: Biblioteca para manipulação de banco de dados utilizando ORM.
- **Pandas**: Ferramenta essencial para manipulação e análise de dados.

Certifique-se de ter o Python instalado e atualizado antes de rodar o comando.

---
📌 **Tecnologias utilizadas:** CrewAI, Python e Inteligência Artificial 🤖

