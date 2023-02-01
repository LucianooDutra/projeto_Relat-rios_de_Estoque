# Projeto Relatorios de Estoque!

## Sobre o projeto:

  Neste projeto foi utilizando a Programação Orientada a Objetos. Foi desenvolvido um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque foi obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possui duas versões: **simples** e **completa**.

# Técnologias utilizadas:

 - Python;
 - Flask;
 - Flake8;
 - Pytest;

# Habilidades trabalhadas:

 - terminal interativo do Python;
 - Aplicar conceitos de Orientação a Objetos em Python;
 - Aplicar padrões de projeto;
 - Leitura e escrita de arquivos (XML, CSV, JSON);
 - manipulação de arquivos;
 - testes com Pytest;

## Instalando as dependências

<details>

  ```json
    # Clone o repositório:
    git clone git@github.com:LucianooDutra/projeto_Relat-rios_de_Estoque.git
    
    # Entre no diretório:
    cd projeto_Job_Insights_python
    
    # Crie o ambiente virtual para o projeto:
    python3 -m venv .venv && source .venv/bin/activate
    
    # Instale as dependências:
    python3 -m pip install -r dev-requirements.txt
  ```

</details>


## Executando os testes

<details>
 <summary><strong>Testes</strong></summary><br />

 Foi utilizado o Pytest para a realização dos testes;

- Para rodar todos os testes:

Para executar todos os testes digite o seguinte comando no terminal a partir da raiz do projeto:

  ```json
    python3 -m pytest
  ```
  
Obs: Nem todos os testes ainda não foram implementados.

</details>

