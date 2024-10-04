import matplotlib.pyplot as plt

def plot_movies_and_series(count_movies, count_series):
    categories = ['Filmes', 'Séries']
    counts = [count_movies['count'], count_series['count']]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, counts, color=['blue', 'orange'])
    plt.title('Total de Filmes e Séries')
    plt.ylabel('Contagem')
    plt.ylim(0, max(counts) + 50)  # Ajusta o limite do eixo Y
    plt.grid(axis='y')
    plt.show()

def plot_titles_by_year(titles_by_year):
    years = [item['year'] for item in titles_by_year]
    counts = [item['count'] for item in titles_by_year]

    plt.figure(figsize=(10, 5))
    plt.plot(years, counts, marker='o')
    plt.title('Títulos Adicionados por Ano')
    plt.xlabel('Ano')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def plot_titles_by_rating(titles_by_rating):
    ratings = [item['rating'] for item in titles_by_rating]
    totals = [item['total'] for item in titles_by_rating]

    plt.figure(figsize=(8, 8))
    plt.pie(totals, labels=ratings, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição de Títulos por Classificação')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def plot_top_directors(top_directors):
    directors = [item['director'] for item in top_directors]
    counts = [item['count'] for item in top_directors]

    plt.figure(figsize=(10, 6))
    plt.barh(directors, counts, color='green')
    plt.title('Top Diretores')
    plt.xlabel('Contagem de Títulos')
    plt.grid(axis='x')
    plt.show()

def plot_titles_by_country(titles_by_country):
    countries = [item['country'] for item in titles_by_country]
    totals = [item['total'] for item in titles_by_country]

    plt.figure(figsize=(12, 6))
    plt.bar(countries[:10], totals[:10], color='purple')  # Top 10 países
    plt.title('Títulos por País (Top 10)')
    plt.xlabel('País')
    plt.ylabel('Contagem de Títulos')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def plot_directors_as_actors(directors_actors):
    directors = [item['director'] for item in directors_actors]
    counts = [item['count'] for item in directors_actors]

    plt.figure(figsize=(10, 6))
    plt.barh(directors, counts, color='red')
    plt.title('Diretores que Atuaram em Suas Próprias Produções')
    plt.xlabel('Contagem de Títulos')
    plt.grid(axis='x')
    plt.show()

def plot_longest_movies(longest_movies):
    # Corrige para usar 'title' em vez de 'movie'
    movies = [item['title'] for item in longest_movies]
    durations = [item['duration'] for item in longest_movies]

    plt.figure(figsize=(10, 6))
    plt.barh(movies, durations, color='blue')
    plt.title('Top 5 Filmes Mais Longos')
    plt.xlabel('Duração (minutos)')
    plt.ylabel('Filmes')
    plt.grid(axis='x')
    plt.show()

def plot_longest_series(longest_series):
    # Corrige para usar 'title' em vez de 'series'
    series = [item['title'] for item in longest_series]
    seasons = [item['seasons'] for item in longest_series]

    plt.figure(figsize=(10, 6))
    plt.barh(series, seasons, color='green')
    plt.title('Top 5 Séries com Mais Temporadas')
    plt.xlabel('Número de Temporadas')
    plt.ylabel('Séries')
    plt.grid(axis='x')
    plt.show()

