# Análise de dados do Catálogo da Netflix

![Netflix Logo]([https://upload.wikimedia.org/wikipedia/commons/6/67/Netflix_logo.png](https://upload.wikimedia.org/wikipedia/commons/7/75/Netflix_icon.svg))

## Descrição do Projeto

Este projeto realiza uma análise abrangente do catálogo da Netflix, utilizando dados disponíveis publicamente. Ele faz o download de um conjunto de dados e gera relatórios em diferentes formatos (CSV, Excel, PDF e TXT) para facilitar a análise e visualização. O projeto é projetado para ajudar a entender melhor o conteúdo disponível na plataforma, incluindo filmes e séries, suas classificações e diretores.

## Funcionalidades

- **Download de Dados**: Os dados são baixados automaticamente e armazenados em diretórios específicos.
- **Análises Realizadas**:
  - Identificação das colunas presentes no dataset.
  - Cálculo do total de filmes disponíveis na Netflix.
  - Listagem dos 5 diretores com mais filmes e séries.
  - Identificação de diretores que atuaram em suas próprias produções.
  - Cálculo do total de séries disponíveis na Netflix.
  - Contagem de títulos adicionados por ano.
  - Análise do número de títulos por classificação.
  - Listagem dos filmes mais longos.
  - Listagem das séries com maior número de temporadas.
  - Análise de títulos por país.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

### Passo a Passo para Inicialização

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/seu_projeto.git
   cd seu_projeto

2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate

3. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt

4. **Crie o Arquivo .env: No diretório raiz do projeto, crie um arquivo chamado .env e adicione a seguinte variável:**
    ```bash
    LINK_DATA_SET=http://eae.vexpens.es/files/deyin3ta4ffi7nta9xgsd7ksro/public?h=_kZmnFJZq56nRrPuHNcLXK0eLpl_US5ELfDw8sx69zM

5. **Execute o Projeto:**
    ```bash
    python main.py

### Relatórios Gerados

Os relatórios são salvos nos seguintes diretórios:

- data/raw/: contém o arquivo CSV original baixado.
- data/processed/excel/: contém os relatórios em formato Excel.
- data/processed/csv/: contém os relatórios em formato CSV.
- data/processed/pdf/: contém os relatórios em formato PDF.
- data/processed/txt/: contém os relatórios em formato TXT.

### Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

### Contato

Para mais informações, entre em contato com rafaelalmeid00@gmail.com.

