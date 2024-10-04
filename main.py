import logging
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from src.services.dashboard import (
    plot_directors_as_actors,
    plot_longest_movies,
    plot_longest_series,
    plot_movies_and_series,
    plot_titles_by_country,
    plot_titles_by_rating,
    plot_titles_by_year,
    plot_top_directors,
)
from src.services.report_generator import generate_reports
from src.services.download_data import download_file
from src.models.model import read_csv_to_dto
from src.utils.list_columns import (
    directors_as_actors,
    list_columns,
    list_longest_movies,
    list_longest_series,
)
from src.utils.count import (
    count_items_by_year,
    count_movies,
    count_series,
    count_titles_by_country,
    count_titles_by_rating,
    top_directors,
)

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do logger
logging.basicConfig(
    filename='./logs/app.log',  # Log será salvo no arquivo 'app.log'
    level=logging.DEBUG,         # Nível mínimo de log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem de log
)

def main():
    # Definir Timestamp
    timestamp = time.time()
    timestamp_formatted = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')

    # Definir URL de download e o diretório de saída com o nome do arquivo
    download_url = os.getenv('LINK_DATA_SET')
    output_dir = './data/raw/'
    output_file = os.path.join(output_dir, f'DataSetNetflix_{timestamp_formatted}.csv')

    # Verifica se os diretórios existem
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs('./data/processed/excel/', exist_ok=True)
    os.makedirs('./data/processed/csv/', exist_ok=True)
    os.makedirs('./data/processed/pdf/', exist_ok=True)
    os.makedirs('./data/processed/txt/', exist_ok=True)

    try:
        # Executar o download
        download_file(download_url, output_file)

        # Ler e processar o dataset
        dataset = read_csv_to_dto(output_file)

        # 1. Quais colunas estão presentes no dataset?
        columns = list_columns(dataset)

        # 2. Quantos filmes estão disponíveis na Netflix?
        total_movies = count_movies(dataset)

        # 3. Quem são os 5 diretores com mais filmes e séries na plataforma?
        directors = top_directors(dataset)

        # 4. Quais diretores também atuaram como atores em suas próprias produções?
        directors_actors = directors_as_actors(dataset)

        # 5. Quantas séries estão disponíveis na Netflix?
        total_series = count_series(dataset)

        # 6. Quantos títulos foram adicionados por ano?
        total_by_years = count_items_by_year(dataset)

        # 7. Quantos títulos existem de cada classificação?
        titles_by_rating = count_titles_by_rating(dataset)

        # 8. Maiores filmes em duração?
        longest_movies = list_longest_movies(dataset)

        # 9. Maiores séries em temporada?
        longest_series = list_longest_series(dataset)

        # 10. Títulos por país
        titles_by_country = count_titles_by_country(dataset)

        # Gerar relatórios
        generate_reports(
            columns=columns,
            total_movies=total_movies,
            directors=directors,
            directors_actors=directors_actors,
            total_series=total_series,
            total_by_years=total_by_years,
            titles_by_rating=titles_by_rating,
            longest_movies=longest_movies,
            longest_series=longest_series,
            titles_by_country=titles_by_country,
            date=timestamp_formatted
        )

        # Visualizar os dados
        plot_movies_and_series(total_movies, total_series)
        plot_titles_by_year(total_by_years)
        plot_titles_by_rating(titles_by_rating)
        plot_top_directors(directors)
        plot_titles_by_country(titles_by_country)
        plot_directors_as_actors(directors_actors)
        plot_longest_movies(longest_movies)
        plot_longest_series(longest_series)

    except Exception as e:
        logging.error(f"Ocorreu um erro: {str(e)}")
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
