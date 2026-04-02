# Dashboard FIFA 2023 — Análise de Dados com Streamlit

![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52.1-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Educacional-yellow?style=flat-square)
![Curso](https://img.shields.io/badge/Curso-Asimov%20Academy-blueviolet?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-Não%20definida-lightgrey?style=flat-square)

> Aplicação web de análise de dados desenvolvida com Streamlit, construída como projeto prático do curso *Criando Aplicativos Web com Streamlit* da [Asimov Academy](https://hub.asimov.academy/curso/criando-aplicativos-web-com-streamlit/). O projeto explora o dataset do FIFA 2023 por meio de um dashboard interativo com múltiplas páginas.

---

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos de Aprendizagem](#objetivos-de-aprendizagem)
- [Arquitetura da Aplicação](#arquitetura-da-aplicação)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Execução](#instalação-e-execução)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Contexto Acadêmico](#contexto-acadêmico)
- [Considerações Finais](#considerações-finais)

---

## Sobre o Projeto

O **Dashboard FIFA 2023** é uma aplicação web de análise de dados construída integralmente em Python utilizando o framework Streamlit. O projeto tem como base os dados públicos do jogo FIFA 2023, permitindo a exploração interativa de informações sobre jogadores e clubes por meio de uma interface dinâmica e multipáginas.

O desenvolvimento foi realizado como atividade prática do curso de Streamlit da Asimov Academy, cujo módulo central abrange a construção de um *Dash FIFA 2023* com visualização de jogadores e times. O objetivo não é replicar o jogo, mas sim demonstrar as capacidades do Streamlit como ferramenta de comunicação de dados.

---

## Objetivos de Aprendizagem

Este projeto foi desenvolvido com foco nos seguintes tópicos do curso:

- Estruturação de aplicações Streamlit com **múltiplas páginas** (Multipage Apps)
- Leitura e manipulação de conjuntos de dados tabulares com **Pandas**
- Exibição de tabelas, métricas e gráficos interativos com **Streamlit**
- Uso de **widgets de entrada** (filtros, seletores, sliders) para interação do usuário
- Técnicas de **cacheamento** (`@st.cache_data`) para otimização de performance
- Carregamento e exibição de **imagens dinâmicas** de jogadores e clubes
- Preparação de aplicações para **deploy no Streamlit Cloud**

---

## Arquitetura da Aplicação

A aplicação segue o padrão de múltiplas páginas nativo do Streamlit, em que cada arquivo dentro da pasta `pages/` é automaticamente registrado como uma rota navegável na barra lateral da interface:

```
projeto-fifa-streamlit/
│
├── 1_home.py            ← Página principal (ponto de entrada)
│
├── pages/               ← Páginas adicionais do dashboard
│   ├── 2_players.py     ← Visualização e análise de jogadores
│   └── 3_teams.py       ← Visualização e análise de times/clubes
│
├── datasets/            ← Conjunto de dados do FIFA 2023 (CSV)
│
├── requeriments.txt     ← Dependências do projeto
└── .gitignore
```

> **Nota sobre convenção de nomenclatura:** O Streamlit utiliza o prefixo numérico nos nomes dos arquivos (`1_`, `2_`, `3_`) para definir a ordem de exibição das páginas na barra lateral de navegação.

---

## Tecnologias Utilizadas

| Biblioteca | Versão | Finalidade |
|---|---|---|
| Python | 3.10+ | Linguagem principal |
| Streamlit | 1.52.1 | Framework de criação da interface web |
| Pandas | 2.3.3 | Leitura, filtragem e manipulação dos dados |
| NumPy | 2.2.6 | Operações numéricas auxiliares |
| Altair | 6.0.0 | Visualizações declarativas e gráficos interativos |
| Pillow | 12.0.0 | Manipulação e exibição de imagens |
| PyArrow | 22.0.0 | Serialização e performance na leitura de dados |

> As demais dependências listadas em `requeriments.txt` são pacotes internos do ecossistema Streamlit e não requerem configuração adicional por parte do usuário.

---

## Funcionalidades

A aplicação oferece as seguintes visualizações e interações:

- **Página Inicial (Home):** visão geral do projeto com métricas de alto nível sobre o dataset do FIFA 2023
- **Análise de Jogadores:** tabela filtrável com atributos individuais dos jogadores (posição, clube, nacionalidade, overall, potencial, entre outros)
- **Análise de Times:** agrupamento e comparação de estatísticas por clube
- **Filtros interativos:** seletores de posição, clube, nacionalidade e faixas de atributos via widgets nativos do Streamlit
- **Exibição de imagens:** carregamento dinâmico de fotos de jogadores e escudos de clubes

---

## Pré-requisitos

Antes de executar o projeto localmente, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- Git

A criação de um ambiente virtual é fortemente recomendada para evitar conflitos entre dependências.

---

## Instalação e Execução

Siga os passos abaixo para executar a aplicação em ambiente local:

**1. Clone o repositório**

```bash
git clone https://github.com/felipemonsef10/projeto-fifa-streamlit.git
cd projeto-fifa-streamlit
```

**2. Crie e ative um ambiente virtual**

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**

```bash
pip install -r requeriments.txt
```

**4. Execute a aplicação**

```bash
streamlit run 1_home.py
```

**5. Acesse no navegador**

```
http://localhost:8501
```

A navegação entre as páginas do dashboard é realizada pela barra lateral gerada automaticamente pelo Streamlit.

---

## Estrutura de Diretórios

```
projeto-fifa-streamlit/
│
├── 1_home.py            # Página inicial — ponto de entrada do Streamlit
├── requeriments.txt     # Dependências do projeto
├── .gitignore
│
├── datasets/            # Dados brutos do FIFA 2023 (formato CSV)
│
└── pages/               # Páginas adicionais (roteamento automático)
    ├── 2_players.py     # Dashboard de jogadores
    └── 3_teams.py       # Dashboard de times
```

---

## Contexto Acadêmico

Este projeto foi desenvolvido como atividade prática do **Módulo 3** do curso *Criando Aplicativos Web com Streamlit*, oferecido pela [Asimov Academy](https://hub.asimov.academy). O curso abrange desde a introdução ao framework até o deploy completo de aplicações na plataforma Streamlit Cloud.

O módulo específico que originou este projeto contempla:

- Aula 3.1 — Dash FIFA 2023
- Aula 3.2 — View de jogadores e times
- Aula 3.3 — Ajustes no carregamento de imagens

Para reproduzir integralmente o ambiente do curso ou aprofundar os conceitos aplicados, recomenda-se consultar a [documentação oficial do Streamlit](https://docs.streamlit.io/) e o material didático da Asimov Academy.

---

## Considerações Finais

O projeto demonstra como o Streamlit permite transformar scripts de análise de dados em aplicações web interativas com poucas linhas de código Python, dispensando o uso de frameworks de frontend tradicionais. A escolha do dataset do FIFA 2023 ilustra bem o potencial da ferramenta para exploração de dados tabulares ricos em atributos categóricos e numéricos.

---

_Desenvolvido por [felipemonsef10](https://github.com/felipemonsef10) · Projeto educacional — Asimov Academy_
