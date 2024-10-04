from collections import defaultdict
import logging
from typing import Any, Dict, List

from src.models.model import CsvDto

def list_columns(dtos: List[CsvDto]) -> List[str]:
    """
    Retorna uma lista com os nomes das colunas de um objeto DTO.
    """
    if not dtos:
        logging.warning("A lista de DTOs está vazia.")
        return []

    columns = list(vars(dtos[0]).keys())
    logging.info(f"Colunas do objeto: {columns}")
    return columns

def list_longest_movies(dtos: List[CsvDto], top_n: int = 5) -> List[Dict[str, Any]]:
    """
    Retorna uma lista dos filmes com as maiores durações, limitando-se ao top_n especificado.
    """
    movie_durations = []

    for dto in dtos:
        if dto.type == "Movie":
            try:
                duration_str = dto.duration
                if "min" in duration_str:
                    minutes = int(duration_str.split()[0])
                    movie_durations.append({'title': dto.title, 'duration': minutes})
            except (ValueError, AttributeError) as e:
                logging.warning(f"Erro ao processar a duração do filme '{dto.title}': {e}")
                continue

    # Ordenar os filmes pela duração em ordem decrescente
    longest_movies = sorted(movie_durations, key=lambda movie: movie['duration'], reverse=True)

    logging.info(f"Top {top_n} filmes mais longos: {longest_movies[:top_n]}")
    return longest_movies[:top_n]

def list_longest_series(dtos: List[CsvDto], top_n: int = 5) -> List[Dict[str, Any]]:
    """
    Retorna uma lista das séries com o maior número de temporadas, limitando-se ao top_n especificado.
    """
    series_seasons_count = []

    for dto in dtos:
        if dto.type == "TV Show":
            try:
                duration_str = dto.duration
                if "Seasons" in duration_str:
                    seasons = int(duration_str.split()[0])
                    series_seasons_count.append({'title': dto.title, 'seasons': seasons})
            except (ValueError, AttributeError) as e:
                logging.warning(f"Erro ao processar a quantidade de temporadas da série '{dto.title}': {e}")
                continue

    # Ordenar as séries pelo número de temporadas em ordem decrescente
    longest_series = sorted(series_seasons_count, key=lambda series: series['seasons'], reverse=True)

    logging.info(f"Top {top_n} séries mais longas: {longest_series[:top_n]}")
    return longest_series[:top_n]

def list_directors_as_actors(dtos: List[CsvDto]) -> List[Dict[str, Any]]:
    """
    Retorna uma lista de diretores que também atuaram em suas próprias produções, com a contagem de aparições e títulos.
    """
    directors_with_roles = defaultdict(lambda: {"director": "", "count": 0, "titles": []})

    for dto in dtos:
        if dto.director and dto.director in dto.cast:
            director_info = directors_with_roles[dto.director]
            director_info["director"] = dto.director
            director_info["count"] += 1
            director_info["titles"].append(dto.title)

    result = list(directors_with_roles.values())
    logging.info(f"Diretores que atuaram em suas próprias produções: {result}")
    return result
