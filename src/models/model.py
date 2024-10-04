import csv
import logging
from typing import List, Any

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Define a classe DTO
class CsvDto:
    def __init__(self, **kwargs):
        """
        Inicializa um objeto CsvDto com os dados fornecidos.

        Args:
            **kwargs: Parâmetros nomeados que representam os atributos do DTO.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        # Converte a string de elenco em uma lista, se houver
        if hasattr(self, 'cast'):
            self.cast = self.cast.split(", ") if self.cast else []

    def __repr__(self):
        """Retorna uma representação da instância do DTO."""
        return str(self.__dict__)

# Função para ler o arquivo CSV e retornar uma lista de objetos DTO
def read_csv_to_dto(file_path: str) -> List[CsvDto]:
    """
    Lê um arquivo CSV e converte cada linha em um objeto CsvDto.

    Args:
        file_path (str): O caminho do arquivo CSV.

    Returns:
        List[CsvDto]: Uma lista de objetos CsvDto.
    """
    dtos = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Lê o CSV como dicionário
            for row in reader:
                dto = CsvDto(**row)  # Cria um objeto DTO com os dados da linha
                dtos.append(dto)  # Adiciona o objeto à lista
    except FileNotFoundError:
        logging.error(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao ler o arquivo: {e}")
    
    logging.info(f"Retorno DTO: {dtos}")
    return dtos