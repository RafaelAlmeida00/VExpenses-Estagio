import logging
import requests
import os

# Função para baixar o arquivo
def download_file(url, output_path):
    try:
        logging.info(f"Iniciando download do arquivo de: {url}")
        
        # Verifica se o diretório de saída existe
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(f"Diretório {output_dir} criado.")
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Levanta uma exceção se a resposta tiver um erro HTTP

        # Escreve o conteúdo do arquivo
        with open(output_path, 'wb') as file:
            file.write(response.content)
        logging.info(f"Arquivo baixado com sucesso em: {output_path}")

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erro HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Erro de conexão: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Erro de timeout: {timeout_err}")
    except Exception as err:
        logging.error(f"Ocorreu um erro: {err}")
