import logging
import pandas as pd
from typing import List
import os
from fpdf import FPDF 
from fpdf.enums import XPos, YPos

from src.models.model import CsvDto

def clean_text(text: str) -> str:
    # Limpa e substitui caracteres problemáticos
    return text.encode('latin-1', 'replace').decode('latin-1')

def create_pdf_report(data_dict: dict, pdf_path: str) -> None:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Definir a fonte personalizada para suporte a Unicode
    pdf.add_font("ArialUnicode", "", "./arial-font/Arial-Unicode-Regular.ttf", uni=True)  # Certifique-se de que o caminho da fonte esteja correto
    pdf.set_font("ArialUnicode", "", 12)

    # Iterar pelos DataFrames e adicionar ao PDF
    for title, df in data_dict.items():
        pdf.cell(0, 10, title, ln=True, align='C')  # Adiciona o título centralizado
        pdf.ln(5)  # Espaçamento entre título e conteúdo

        # Adiciona os dados do DataFrame
        for index, row in df.iterrows():
            row_str = ' | '.join(str(item) for item in row)
            pdf.cell(0, 10, clean_text(row_str), ln=True)  # Usa clean_text para caracteres não suportados

        pdf.ln(10)  # Espaçamento entre seções

    pdf.output(pdf_path)

def generate_reports(
    columns: List[str],
    total_movies: int,
    directors: List[str],
    directors_actors: List[str],
    total_series: int,
    total_by_years: dict,
    titles_by_rating: dict,
    longest_movies: List[str],
    longest_series: List[str],
    titles_by_country: dict,
    date: str
) -> None:
    try:
        # Criação de DataFrames para cada relatório
        df_columns = pd.DataFrame({'Columns': columns})
        df_total_movies = pd.DataFrame({'Total Movies': [total_movies]})  # Corrigido para lista
        df_directors = pd.DataFrame({'Directors': directors})
        df_directors_actors = pd.DataFrame({'Directors as Actors': directors_actors})
        df_total_series = pd.DataFrame({'Total Series': [total_series]})  # Corrigido para lista
        df_total_by_years = pd.DataFrame(total_by_years)
        df_titles_by_rating = pd.DataFrame(titles_by_rating)
        df_longest_movies = pd.DataFrame({'Longest Movies': longest_movies})
        df_longest_series = pd.DataFrame({'Longest Series': longest_series})
        df_titles_by_country = pd.DataFrame(titles_by_country)

        # Salvar em Excel
        excel_path = f'./data/processed/excel/dataAnalysis_{date}.xlsx'
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df_columns.to_excel(writer, sheet_name='Colunas', index=False)
            df_total_movies.to_excel(writer, sheet_name='Total Movies', index=False)
            df_directors.to_excel(writer, sheet_name='Top Directors', index=False)
            df_directors_actors.to_excel(writer, sheet_name='Directors as Actors', index=False)
            df_total_series.to_excel(writer, sheet_name='Total Series', index=False)
            df_total_by_years.to_excel(writer, sheet_name='Titles by Year', index=False)
            df_titles_by_rating.to_excel(writer, sheet_name='Titles by Rating', index=False)
            df_longest_movies.to_excel(writer, sheet_name='Longest Movies', index=False)
            df_longest_series.to_excel(writer, sheet_name='Longest Series', index=False)
            df_titles_by_country.to_excel(writer, sheet_name='Titles by Country', index=False)

        logging.info(f"Análise de dados salva em: {excel_path}")

        # Salvar em CSV
        csv_path = f'./data/processed/csv/dataAnalysis_{date}.csv'
        df_combined = pd.concat([
            df_columns, df_total_movies, df_directors, df_directors_actors, df_total_series,
            df_total_by_years, df_titles_by_rating, df_longest_movies, df_longest_series, df_titles_by_country
        ], axis=1)
        df_combined.to_csv(csv_path, index=False)
        logging.info(f"Análise de dados salva em: {csv_path}")

        # Salvar em PDF
        pdf_path = f'./data/processed/pdf/dataAnalysis_{date}.pdf'
        create_pdf_report({
            'Colunas': df_columns,
            'Total Movies': df_total_movies,
            'Top Directors': df_directors,
            'Directors as Actors': df_directors_actors,
            'Total Series': df_total_series,
            'Titles by Year': df_total_by_years,
            'Titles by Rating': df_titles_by_rating,
            'Longest Movies': df_longest_movies,
            'Longest Series': df_longest_series,
            'Titles by Country': df_titles_by_country
        }, pdf_path)
        logging.info(f"Análise de dados salva em: {pdf_path}")

        # Salvar em TXT
        txt_path = f'./data/processed/txt/dataAnalysis_{date}.txt'
        with open(txt_path, 'w', encoding='utf-8') as f:
            for title, df in {
                'Colunas': df_columns,
                'Total Movies': df_total_movies,
                'Top Directors': df_directors,
                'Directors as Actors': df_directors_actors,
                'Total Series': df_total_series,
                'Titles by Year': df_total_by_years,
                'Titles by Rating': df_titles_by_rating,
                'Longest Movies': df_longest_movies,
                'Longest Series': df_longest_series,
                'Titles by Country': df_titles_by_country
            }.items():
                f.write(f"{title}\n")
                f.write(df.to_string(index=False))
                f.write("\n\n")  # Duas linhas em branco entre seções

        logging.info(f"Análise de dados salva em: {txt_path}")

    except Exception as e:
        logging.error(f"Ocorreu um erro ao gerar os relatórios: {e}")
