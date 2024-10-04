from decimal import ROUND_DOWN, Decimal
import logging
from typing import Any, Dict, List
from collections import Counter, defaultdict
from datetime import datetime

from src.models.model import CsvDto

def count_movies(dtos: List[CsvDto]) -> Dict[str, Any]:
    movie_count = sum(1 for dto in dtos if dto.type == "Movie")
    total_items = len(dtos)

    # Calcula a porcentagem de filmes em relação ao total
    percentage = (movie_count / total_items * 100) if total_items > 0 else 0

    logging.info(f"Total de filmes: {movie_count} disponíveis no catálogo da Netflix")
    return {"count": movie_count, "percentage": round(percentage, 2)}

def count_series(dtos: List[CsvDto]) -> Dict[str, Any]:
    series_count = sum(1 for dto in dtos if dto.type == "TV Show")
    total_items = len(dtos)

    # Calcula a porcentagem de séries em relação ao total
    percentage = (series_count / total_items * 100) if total_items > 0 else 0

    logging.info(f"Total de séries: {series_count} disponíveis no catálogo da Netflix")
    return {"count": series_count, "percentage": round(percentage, 2)}

def count_titles_by_year(dtos: List[CsvDto]) -> List[Dict[str, Any]]:
    year_counts = Counter()

    for dto in dtos:
        try:
            if dto.date_added:
                date_obj = datetime.strptime(dto.date_added, "%B %d, %Y")
                year_counts[date_obj.year] += 1
        except ValueError as e:
            logging.error(f"Erro ao processar a data: {dto.date_added}. Detalhes: {e}")

    total_count = sum(year_counts.values())
    result = [
        {"year": year, "count": count, "percentage": round((count / total_count * 100), 2)}
        for year, count in year_counts.items()
    ]

    logging.info(f"Títulos adicionados por ano no catálogo: {result}")
    return result

def count_titles_by_rating(dtos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rating_data = defaultdict(lambda: {'total': 0, 'titles': []})

    for dto in dtos:
        rating = dto.rating
        if rating:
            rating_data[rating]['total'] += 1
            rating_data[rating]['titles'].append(dto.title)

    result = [
        {
            "rating": rating,
            "total": data['total'],
            "titles": {i: title for i, title in enumerate(data['titles'])}
        }
        for rating, data in rating_data.items()
    ]

    logging.info(f"Títulos por classificação: {result}")
    return result

def top_directors(dtos: List[CsvDto], top_n: int = 5) -> List[Dict[str, Any]]:
    director_counts = Counter(dto.director for dto in dtos if dto.director)

    most_common_directors = director_counts.most_common(top_n)

    result = [{"director": director, "count": count} for director, count in most_common_directors]
    logging.info(f"Top {top_n} diretores: {result}")
    return result

def count_titles_by_country(dtos: List[CsvDto]) -> List[Dict[str, Any]]:
    country_counts = Counter()
    country_titles = defaultdict(list)

    for dto in dtos:
        if dto.country.strip():
            countries = [country.strip() for country in dto.country.split(',')]
            for country in countries:
                country_counts[country] += 1
                country_titles[country].append(dto.title)

    total_titles = sum(country_counts.values())

    result = [
        {
            "country": country,
            "total": count,
            "percentage": round((count / total_titles * 100), 2),
            "titles": {i: title for i, title in enumerate(country_titles[country])}
        }
        for country, count in country_counts.items()
    ]

    result.sort(key=lambda x: x['total'], reverse=True)

    logging.info(f"Títulos por país: {result}")
    return result
