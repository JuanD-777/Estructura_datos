import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para gráficos
plt.style.use('dark_background')
sns.set_theme(style="darkgrid")

class MovieRecommender:
    def __init__(self):
        # Cargar datos de películas
        self.movies_df = self.load_movie_data()
        # Crear matriz de características para el modelo
        self.tfidf_matrix, self.tfidf_features = self.create_feature_matrix()
        # Calcular matriz de similitud
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)
        
    def load_movie_data(self):
        # Crear un DataFrame de ejemplo con películas
        data = {
            'id': range(1, 13),
            'title': [
                'El Padrino', 'El Caballero Oscuro', 'Pulp Fiction', 
                'El Señor de los Anillos: El Retorno del Rey', 'El Rey León', 'Interestelar',
                'El Resplandor', 'Parásitos', 'Coco', 'Matrix', 'Titanic', 'Jurassic Park'
            ],
            'description': [
                'La historia de la familia Corleone, una de las más poderosas dinastías criminales de Nueva York.',
                'Batman se enfrenta al Joker, un criminal psicópata que busca sumir a Ciudad Gótica en el caos.',
                'Las vidas de dos mafiosos, un boxeador, la esposa de un gángster y un par de bandidos se entrelazan en cuatro historias de violencia y redención.',
                'Gandalf y Aragorn lideran el mundo de los hombres contra la armada de Sauron para distraer su atención de Frodo y Sam.',
                'Un joven príncipe león huye de su reino solo para aprender el verdadero significado de la responsabilidad y la valentía.',
                'Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento de asegurar la supervivencia de la humanidad.',
                'Una familia se aísla en un hotel para el invierno donde una presencia siniestra influye en el padre hacia la violencia.',
                'La familia Kim, todos desempleados, se interesa por el estilo de vida de la adinerada familia Park.',
                'Aspirante a músico Miguel, confrontado con la prohibición de su familia de la música, entra en la Tierra de los Muertos.',
                'Un hacker descubre la verdadera naturaleza de su realidad y su papel en la guerra contra sus controladores.',
                'Una aristócrata de diecisiete años se enamora de un amable pero pobre artista a bordo del lujoso y desafortunado R.M.S. Titanic.',
                'Un paleontólogo pragmático que visita un parque temático casi completo es enviado a proteger a un par de niños después de que un corte de energía provoque que los dinosaurios clonados del parque se suelten.'
            ],
            'categories': [
                ['Drama', 'Crimen'],
                ['Acción', 'Crimen', 'Drama'],
                ['Crimen', 'Drama'],
                ['Aventura', 'Fantasía', 'Acción'],
                ['Animación', 'Aventura', 'Drama'],
                ['Aventura', 'Drama', 'Ciencia Ficción'],
                ['Terror', 'Drama'],
                ['Comedia', 'Drama', 'Thriller'],
                ['Animación', 'Aventura', 'Comedia'],
                ['Acción', 'Ciencia Ficción'],
                ['Drama', 'Romance'],
                ['Aventura', 'Ciencia Ficción', 'Thriller']
            ],
            'rating': [9.2, 9.0, 8.9, 8.9, 8.5, 8.6, 8.4, 8.6, 8.4, 8.7, 7.8, 8.1],
            'platforms': [
                ['Netflix', 'Amazon Prime'],
                ['HBO Max', 'Amazon Prime'],
                ['Netflix', 'Amazon Prime'],
                ['HBO Max', 'Amazon Prime'],
                ['Disney+'],
                ['Netflix', 'Amazon Prime'],
                ['HBO Max', 'Amazon Prime'],
                ['Netflix', 'Amazon Prime'],
                ['Disney+'],
                ['HBO Max', 'Amazon Prime'],
                ['Disney+', 'Amazon Prime'],
                ['Netflix', 'Amazon Prime']
            ],
            'year': [1972, 2008, 1994, 2003, 1994, 2014, 1980, 2019, 2017, 1999, 1997, 1993]
        }
        
        df = pd.DataFrame(data)
        
        # Convertir las categorías y plataformas a strings para el procesamiento de texto
        df['categories_str'] = df['categories'].apply(lambda x: ' '.join(x))
        df['platforms_str'] = df['platforms'].apply(lambda x: ' '.join(x))
        
        # Crear una columna de características combinadas para el modelo
        df['features'] = df['categories_str'] + ' ' + df['description']
        
        return df
    
    def create_feature_matrix(self):
        # Crear una matriz TF-IDF para las características de las películas
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
        except:
            return "Película no encontrada. Por favor, verifica el título."
        
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
        category_movies = self.movies_df[self.movies_df['categories_str'].str.contains(category, case=False)]
        
        if category_movies.empty:
            return "Categoría no encontrada. Las categorías disponibles son: " + ", ".join(self.get_all_categories())
        
        # Ordenar por calificación
        return category_movies.sort_values('rating', ascending=False).head(n)
    
    def get_recommendations_by_platform(self, platform, n=5):
      """
        Obtener recomendaciones disponibles en una plataforma específica
      """
    # Filtrar películas disponibles en la plataforma
      platform_movies = self.movies_df[self.movies_df['platforms_str'].str.contains(platform, case=False)]
    
      if platform_movies.empty:
          return "Plataforma no encontrada. Las plataformas disponibles son: " + ", ".join(self.get_all_platforms())
      if 'rating' not in platform_movies.columns:
          print("Advertencia: La columna 'rating' no se encontró. Mostrando sin ordenar.")
          return platform_movies.head(n)
      
    # Verificar que exista la columna 'rating' antes de ordenar
      if 'rating' in platform_movies.columns:
          return platform_movies.sort_values('rating', ascending=False).head(n)
      else:
          return platform_movies.head(n)
    

    
    def get_all_categories(self):
        """
        Obtener todas las categorías únicas
        """
        all_categories = []
        for categories in self.movies_df['categories']:
            all_categories.extend(categories)
        return sorted(list(set(all_categories)))
    
    def get_all_platforms(self):
        """
        Obtener todas las plataformas únicas
        """
        all_platforms = []
        for platforms in self.movies_df['platforms']:
            all_platforms.extend(platforms)
        return sorted(list(set(all_platforms)))
    
    def visualize_category_distribution(self):
        """
        Visualizar la distribución de películas por categoría
        """
        # Contar la frecuencia de cada categoría
        category_counts = {}
        for categories in self.movies_df['categories']:
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
        print(f"Categorías: {', '.join(movie_row['categories'])}")
        print(f"Plataformas: {', '.join(movie_row['platforms'])}")
        print(f"Calificación: {movie_row['rating']}/10")
        print(f"Descripción: {movie_row['description']}")
        print(f"{'=' * 50}\n")

def menu_principal():
    """
    Menú interactivo para el sistema de recomendación
    """
    recommender = MovieRecommender()
    
    while True:
        print("\n===== SISTEMA DE RECOMENDACIÓN DE PELÍCULAS CON MACHINE LEARNING =====\n")
        print("1. Ver todas las películas")
        print("2. Recomendaciones basadas en una película")
        print("3. Recomendaciones por categoría")
        print("4. Recomendaciones por plataforma")
        print("5. Visualizar distribución por categoría")
        print("6. Visualizar distribución por plataforma")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            print("\nLista de todas las películas:")
            for _, movie in recommender.movies_df.iterrows():
                recommender.print_movie_info(movie)
            
        elif opcion == "2":
            print("\nPelículas disponibles:")
            for i, title in enumerate(recommender.movies_df['title']):
                print(f"{i+1}. {title}")
            
            try:
                idx = int(input("\nSelecciona el número de la película: ")) - 1
                movie_title = recommender.movies_df.iloc[idx]['title']
                recommendations = recommender.get_movie_recommendations(movie_title)
                
                print(f"\nSi te gustó '{movie_title}', te recomendamos:")
                for _, movie in recommendations.iterrows():
                    recommender.print_movie_info(movie)
            except:
                print("Selección inválida. Volviendo al menú principal.")
            
        elif opcion == "3":
            print("\nCategorías disponibles:")
            categories = recommender.get_all_categories()
            for i, category in enumerate(categories):
                print(f"{i+1}. {category}")
            
            try:
                idx = int(input("\nSelecciona el número de la categoría: ")) - 1
                category = categories[idx]
                category_recommendations = recommender.get_recommendations_by_category(category)
                
                print(f"\nMejores películas de '{category}':")
                for _, movie in category_recommendations.iterrows():
                    recommender.print_movie_info(movie)
            except:
                print("Selección inválida. Volviendo al menú principal.")
            
        elif opcion == "4":
            print("\nPlataformas disponibles:")
            platforms = recommender.get_all_platforms()
            for i, platform in enumerate(platforms):
                print(f"{i+1}. {platform}")
            
            try:
                idx = int(input("\nSelecciona el número de la plataforma: ")) - 1
                platform = platforms[idx]
                platform_recommendations = recommender.get_recommendations_by_platform(platform)
                
                print(f"\nMejores películas en '{platform}':")
                for _, movie in platform_recommendations.iterrows():
                    recommender.print_movie_info(movie)
            except:
                print("Selección inválida. Volviendo al menú principal.")
            
        elif opcion == "5":
            recommender.visualize_category_distribution()
            
        elif opcion == "6":
            recommender.visualize_platform_distribution()
            
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema de recomendación de películas!")
            break
            
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()