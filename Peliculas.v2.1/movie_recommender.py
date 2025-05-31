import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para gráficos
plt.style.use('dark_background')
sns.set_theme(style="darkgrid")

class MovieRecommender:
    def __init__(self, csv_path='tmdb_movies.csv'):
        # Cargar datos de películas
        self.movies_df = self.load_movie_data(csv_path)
        # Crear matriz de características para el modelo
        self.tfidf_matrix, self.tfidf_features = self.create_feature_matrix()
        # Calcular matriz de similitud
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)
        
    def load_movie_data(self, csv_path):
        """
        Cargar los datos de películas desde el archivo CSV
        """
        try:
            # Verificar si el archivo existe
            if not os.path.exists(csv_path):
                print(f"El archivo {csv_path} no existe")
                print("Utilizando datos de ejemplo")
                return self.create_example_data()
            
            # Cargar el CSV
            df = pd.read_csv(csv_path)
            print(f"CSV cargado exitosamente: {len(df)} filas")
            
            # Procesar las columnas de categorías y plataformas
            if 'categories' in df.columns:
                if not isinstance(df['categories'].iloc[0], list):
                    df['categories'] = df['categories'].apply(
                        lambda x: x.split(',') if isinstance(x, str) and pd.notna(x) else []
                    )
            else:
                # Si no existe la columna, usar géneros o crear una por defecto
                if 'genres' in df.columns:
                    df['categories'] = df['genres'].apply(
                        lambda x: x.split(',') if isinstance(x, str) and pd.notna(x) else ['Sin categoría']
                    )
                else:
                    df['categories'] = [['Sin categoría']] * len(df)
        
            if 'platforms' in df.columns:
                if not isinstance(df['platforms'].iloc[0], list):
                    df['platforms'] = df['platforms'].apply(
                        lambda x: x.split(',') if isinstance(x, str) and pd.notna(x) else ['Desconocida']
                    )
            else:
                # Si no existe la columna platforms, crear una por defecto
                df['platforms'] = [['Netflix']] * len(df)
                
            # Verificar si existe columna de descripción
            if 'description' not in df.columns:
                if 'overview' in df.columns:
                    df['description'] = df['overview']
                else:
                    df['description'] = 'Sin descripción disponible'
                    
            # Verificar si existe columna de título
            if 'title' not in df.columns:
                if 'original_title' in df.columns:
                    df['title'] = df['original_title']
                else:
                    df['title'] = 'Título desconocido'
                    
            # Verificar si existe columna de año
            if 'year' not in df.columns:
                if 'release_date' in df.columns:
                    df['year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
                else:
                    df['year'] = 2000  # Año por defecto
                    
            # Buscar columna de rating
            rating_column = self.find_rating_column(df)
            if rating_column and rating_column != 'rating':
                df['rating'] = df[rating_column]
            elif 'rating' not in df.columns:
                df['rating'] = 7.0  # Rating por defecto
        
            # Convertir las categorías y plataformas a strings para el procesamiento de texto
            df['categories_str'] = df['categories'].apply(
                lambda x: ' '.join(x) if isinstance(x, list) else ''
            )
            df['platforms_str'] = df['platforms'].apply(
                lambda x: ' '.join(x) if isinstance(x, list) else ''
            )
        
            # Crear una columna de características combinadas para el modelo
            df['features'] = df['categories_str'] + ' ' + df['description'].astype(str)
            
            return df
        
        except Exception as e:
            print(f"Error al cargar el archivo CSV: {e}")
            print("Utilizando datos de ejemplo...")
            return self.create_example_data()
    
    def find_rating_column(self, df):
        """Encontrar la columna de rating en el DataFrame"""
        possible_names = ['rating', 'vote_average', 'imdb_rating', 'score', 'user_rating', 'tmdb_rating']
        
        # Buscar nombres exactos
        for name in possible_names:
            if name in df.columns:
                return name
        
        # Buscar por patrones en nombres de columnas
        for col in df.columns:
            if any(pattern in col.lower() for pattern in ['rating', 'vote', 'score']):
                return col
        
        return None
        
    def create_example_data(self):
        """
        Crear un DataFrame de ejemplo con películas
        """
        
        data = {
            'id': range(1, 13),
            'title': [
                'Matrix', 'Inception', 'Interstellar', 'The Dark Knight',
                'Pulp Fiction', 'The Godfather', 'Forrest Gump', 'Gladiator',
                'The Shawshank Redemption', 'Fight Club', 'The Social Network', 
                'The Avengers'
            ],
            'description': [
                'Un hacker descubre la verdad sobre su realidad.',
                'Un ladrón especializado en el robo de secretos.',
                'Un viaje a través del tiempo y el espacio.',
                'El caballero oscuro lucha contra el crimen en Gotham.',
                'Una historia de crimen y redención.',
                'La historia de una familia mafiosa.',
                'La vida de un hombre con un pasado extraordinario.',
                'Un general romano busca venganza.',
                'La esperanza y la amistad en una prisión.',
                'Un hombre lucha contra su propia mente.',
                'La creación de una red social revolucionaria.',
                'Los héroes se unen para salvar el mundo.'
            ],
            'categories': [
                ['Ciencia Ficción', 'Acción'],
                ['Ciencia Ficción', 'Acción'], 
                ['Ciencia Ficción', 'Drama'],
                ['Acción', 'Crimen'], 
                ['Crimen', 'Drama'],
                ['Drama', 'Crimen'], 
                ['Drama', 'Romance'],
                ['Acción', 'Drama'],
                ['Drama', 'Crimen'], 
                ['Drama', 'Acción'],
                ['Drama', 'Biografía'], 
                ['Acción', 'Aventura']
            ],
            'rating': [8.7, 8.8, 8.6, 9.0, 8.9, 9.2, 8.8, 8.5, 9.3, 8.7, 7.7, 8.0],
            'platforms': [
                ['Netflix', 'HBO'], 
                ['Amazon Prime', 'Netflix'], 
                ['Disney+', 'Netflix'],
                ['HBO', 'Amazon Prime'], 
                ['Netflix', 'Hulu'],
                ['HBO', 'Disney+'], 
                ['Netflix', 'Amazon Prime'],
                ['HBO', 'Disney+'],
                ['Netflix', 'Hulu'], 
                ['Amazon Prime', 'Netflix'],
                ['Disney+', 'HBO'], 
                ['Netflix', 'Amazon Prime']
            ],
            'year': [1999, 2010, 2014, 2008, 1994, 1972, 1994, 2000, 1994, 1999, 2010, 2012],
        }
        
        df = pd.DataFrame(data)
        
        # Convertir las columnas de categorías y plataformas a strings
        df['categories_str'] = df['categories'].apply(lambda x: ' '.join(x))
        df['platforms_str'] = df['platforms'].apply(lambda x: ' '.join(x))
        
        # Crear una columna de características combinadas para el modelo
        df['features'] = df['categories_str'] + ' ' + df['description']
        return df
    
    def create_feature_matrix(self):
        """Crear una matriz TF-IDF para las características de las películas"""
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies_df['features'])
        
        return tfidf_matrix, tfidf.get_feature_names_out()
    
    def get_movie_recommendations(self, movie_title, n=5):
        """
        Obtener recomendaciones basadas en una película
        """
        # Encontrar el índice de la película en el DataFrame
        try:
            idx = self.movies_df[self.movies_df['title'] == movie_title].index[0]
        except IndexError:
            return pd.DataFrame()  # Retornar DataFrame vacío si no se encuentra
        
        # Obtener puntuaciones de similitud para todas las películas
        similarity_scores = list(enumerate(self.similarity_matrix[idx]))
        
        # Ordenar las películas según la puntuación de similitud
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Obtener los índices de las películas más similares (excluyendo la propia película)
        similar_movie_indices = [i[0] for i in similarity_scores[1:n+1]]
        
        # Devolver las películas recomendadas
        return self.movies_df.iloc[similar_movie_indices]
    
    def get_recommendations_by_category(self, category, n=5):
        """
        Obtener recomendaciones basadas en una categoría
        """
        # Filtrar películas que contienen la categoría
        category_movies = self.movies_df[self.movies_df['categories_str'].str.contains(category, case=False, na=False)]
        
        if category_movies.empty:
            return pd.DataFrame()  # Retornar DataFrame vacío
        
        # Ordenar por calificación
        return category_movies.sort_values('rating', ascending=False).head(n)
    
    def get_recommendations_by_platform(self, platform, n=5):
        """
        Obtener recomendaciones disponibles en una plataforma específica
        """
        # Filtrar películas disponibles en la plataforma
        platform_movies = self.movies_df[self.movies_df['platforms_str'].str.contains(platform, case=False, na=False)]
        
        if platform_movies.empty:
            return pd.DataFrame()  # Retornar DataFrame vacío
        
        # Ordenar por calificación
        return platform_movies.sort_values('rating', ascending=False).head(n)
    
    def get_all_categories(self):
        """
        Obtener todas las categorías únicas
        """
        all_categories = []
        for categories in self.movies_df['categories']:
            if isinstance(categories, list):
                all_categories.extend(categories)
        return sorted(list(set(all_categories)))
    
    def get_all_platforms(self):
        """
        Obtener todas las plataformas únicas
        """
        all_platforms = []
        for platforms in self.movies_df['platforms']:
            if isinstance(platforms, list):
                all_platforms.extend(platforms)
        return sorted(list(set(all_platforms)))
    
    def visualize_category_distribution(self):
        """
        Visualizar la distribución de películas por categoría
        """
        # Contar la frecuencia de cada categoría
        category_counts = {}
        for categories in self.movies_df['categories']:
            if isinstance(categories, list):
                for category in categories:
                    if category in category_counts:
                        category_counts[category] += 1
                    else:
                        category_counts[category] = 1
        
        # Ordenar por frecuencia
        sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
        categories, counts = zip(*sorted_categories)
        
        # Crear gráfico
        plt.figure(figsize=(12, 6))
        bars = plt.bar(categories, counts, color='skyblue')
        plt.title('Distribución de Películas por Categoría', fontsize=15)
        plt.xlabel('Categoría', fontsize=12)
        plt.ylabel('Número de Películas', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Añadir etiquetas de valor
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.0f}', ha='center', va='bottom')
        
        plt.show()
    
    def visualize_platform_distribution(self):
        """
        Visualizar la distribución de películas por plataforma
        """
        # Contar la frecuencia de cada plataforma
        platform_counts = {}
        for platforms in self.movies_df['platforms']:
            if isinstance(platforms, list):
                for platform in platforms:
                    if platform in platform_counts:
                        platform_counts[platform] += 1
                    else:
                        platform_counts[platform] = 1
        
        # Ordenar por frecuencia
        sorted_platforms = sorted(platform_counts.items(), key=lambda x: x[1], reverse=True)
        platforms, counts = zip(*sorted_platforms)
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.pie(counts, labels=platforms, autopct='%1.1f%%', startangle=90, 
                shadow=True, explode=[0.05] * len(platforms))
        plt.title('Distribución de Películas por Plataforma', fontsize=15)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    
    def print_movie_info(self, movie_row):
        """
        Imprimir información detallada de una película
        """
        print(f"\n{'=' * 50}")
        print(f"Título: {movie_row['title']}")
        print(f"Año: {movie_row['year']}")
        print(f"Categorías: {', '.join(movie_row['categories']) if isinstance(movie_row['categories'], list) else movie_row['categories']}")
        print(f"Plataformas: {', '.join(movie_row['platforms']) if isinstance(movie_row['platforms'], list) else movie_row['platforms']}")
        print(f"Calificación: {movie_row['rating']}/10")
        print(f"Descripción: {movie_row['description']}")
        print(f"{'=' * 50}\n")

# Ejemplo de uso del sistema de recomendación
if __name__ == "__main__":
    # Inicializar el recomendador
    recommender = MovieRecommender()
    
    print("\n===== SISTEMA DE RECOMENDACIÓN DE PELÍCULAS CON MACHINE LEARNING =====\n")
    
    # Mostrar todas las categorías disponibles
    print("Categorías disponibles:")
    print(", ".join(recommender.get_all_categories()))
    print("\nPlataformas disponibles:")
    print(", ".join(recommender.get_all_platforms()))
    
    print("\n1. Recomendaciones basadas en una película:")
    movie_title = "Matrix"
    recommendations = recommender.get_movie_recommendations(movie_title)
    print(f"\nSi te gustó '{movie_title}', te recomendamos:")
    for _, movie in recommendations.iterrows():
        recommender.print_movie_info(movie)
    
    print("\n2. Recomendaciones por categoría:")
    category = "Ciencia Ficción"
    category_recommendations = recommender.get_recommendations_by_category(category)
    print(f"\nMejores películas de '{category}':")
    for _, movie in category_recommendations.iterrows():
        recommender.print_movie_info(movie)
    
    print("\n3. Recomendaciones por plataforma:")
    platform = "Netflix"
    platform_recommendations = recommender.get_recommendations_by_platform(platform)
    print(f"\nMejores películas en '{platform}':")
    for _, movie in platform_recommendations.iterrows():
        recommender.print_movie_info(movie)
    
    print("\n4. Visualizaciones:")
    print("\nDistribución de películas por categoría:")
    recommender.visualize_category_distribution()
    
    print("\nDistribución de películas por plataforma:")
    recommender.visualize_platform_distribution()