import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from movie_recommender import MovieRecommender

# Configuración de la página
st.set_page_config(
    page_title="Recomendador de Películas ML",
    page_icon="🎬",
    layout="wide"
)

# Estilo personalizado
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #ff4b4b;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
    }
    .stSelectbox>div>div {
        background-color: #262730;
    }
</style>
""", unsafe_allow_html=True)

# Función para encontrar la columna de rating
def find_rating_column(df):
    """Encuentra la columna de rating en el DataFrame"""
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

# Título de la aplicación
st.title("🎬 Recomendador de Películas con Machine Learning")
st.markdown("### Encuentra tu próxima película favorita con IA")

# Inicializar el recomendador
@st.cache_resource
def get_recommender():
    csv_path = 'tmdb_movies.csv'
    if os.path.exists(csv_path):
        return MovieRecommender(csv_path)
    else:
        st.warning("El archivo CSV 'tmdb_movies.csv' no existe. Usando datos de ejemplo.")
        return MovieRecommender()

# Cargar/subir archivos CSV
with st.sidebar:
    st.header("Configuración")
    uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

# Variable para el recomendador
if uploaded_file is not None:
    # Guardar el archivo subido en la carpeta actual
    with open("tmdb_movies.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("¡Archivo subido correctamente!")
    
    # Reiniciar el recomendador con el nuevo CSV
    try:
        recommender = MovieRecommender("tmdb_movies.csv")
        st.success(f"CSV procesado: {len(recommender.movies_df)} películas cargadas")
    except Exception as e:
        st.error(f"Error al procesar el CSV: {e}")
        recommender = get_recommender()
else:
    recommender = get_recommender()

# Sidebar para navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Recomendación por Película", "Recomendación por Categoría", 
     "Recomendación por Plataforma", "Visualizaciones", "Ver Datos"]
)

# Página de inicio
if page == "Inicio":
    st.markdown("""
    ## Bienvenido al Recomendador de Películas con Machine Learning
    
    Este sistema utiliza técnicas avanzadas de procesamiento de lenguaje natural y aprendizaje automático 
    para recomendarte películas basadas en tus preferencias.
    
    ### Características principales:
    
    - **Recomendación basada en películas similares**: Encuentra películas parecidas a tus favoritas
    - **Filtrado por categorías**: Descubre las mejores películas de tu género preferido
    - **Filtrado por plataformas**: Encuentra qué ver en tus servicios de streaming
    - **Visualizaciones**: Explora la distribución de películas por categoría y plataforma
    - **Carga de datos CSV**: Puedes personalizar el sistema con tu propia base de datos de películas
    
    Usa el menú de navegación para explorar las diferentes funcionalidades.
    """)
    
    # Mostrar algunas estadísticas
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📊 Total de películas: {len(recommender.movies_df)}")
        st.info(f"🏷️ Categorías disponibles: {len(recommender.get_all_categories())}")
    with col2:
        st.info(f"📺 Plataformas disponibles: {len(recommender.get_all_platforms())}")
        
        # Buscar la columna de rating correcta
        rating_col = find_rating_column(recommender.movies_df)
        if rating_col:
            avg_rating = recommender.movies_df[rating_col].mean()
            st.info(f"⭐ Calificación promedio: {avg_rating:.1f}/10")
        else:
            st.info("⭐ Información de calificación no disponible")

# Página de recomendación por película
elif page == "Recomendación por Película":
    st.header("Recomendación basada en una película")
    st.markdown("Selecciona una película que te guste y te recomendaremos películas similares.")
    
    # Verificar que hay películas disponibles
    if len(recommender.movies_df) == 0:
        st.error("No hay películas disponibles. Por favor, carga un archivo CSV.")
    else:
        # Selector de película
        movie_title = st.selectbox(
            "Selecciona una película:",
            options=recommender.movies_df['title'].tolist()
        )
        
        # Número de recomendaciones
        num_recommendations = st.slider("Número de recomendaciones", 1, 10, 5)
        
        if st.button("Obtener Recomendaciones"):
            # Obtener recomendaciones
            recommendations = recommender.get_movie_recommendations(movie_title, num_recommendations)
            
            if recommendations.empty:
                st.error("No se pudieron encontrar recomendaciones para esta película.")
            else:
                # Mostrar la película seleccionada
                st.subheader("Película seleccionada:")
                selected_movie = recommender.movies_df[recommender.movies_df['title'] == movie_title].iloc[0]
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image("https://via.placeholder.com/300x450?text=Poster+Pelicula", caption=selected_movie['title'])
                with col2:
                    st.markdown(f"**Título:** {selected_movie['title']}")
                    st.markdown(f"**Año:** {selected_movie['year']}")
                    
                    # Mostrar categorías de forma segura
                    if isinstance(selected_movie['categories'], list):
                        st.markdown(f"**Categorías:** {', '.join(selected_movie['categories'])}")
                    else:
                        st.markdown(f"**Categorías:** {selected_movie['categories']}")
                    
                    # Mostrar plataformas de forma segura
                    if isinstance(selected_movie['platforms'], list):
                        st.markdown(f"**Plataformas:** {', '.join(selected_movie['platforms'])}")
                    else:
                        st.markdown(f"**Plataformas:** {selected_movie['platforms']}")
                    
                    # Mostrar rating
                    rating_col = find_rating_column(recommender.movies_df)
                    if rating_col:
                        st.markdown(f"**Calificación:** {selected_movie[rating_col]}/10")
                    else:
                        st.markdown("**Calificación:** No disponible")
                        
                    st.markdown(f"**Descripción:** {selected_movie['description']}")
                
                # Mostrar recomendaciones
                st.subheader("Películas recomendadas:")
                
                # Crear columnas para las recomendaciones
                num_rows = (len(recommendations) + 2) // 3
                for row in range(num_rows):
                    cols = st.columns(3)
                    for col_idx in range(3):
                        movie_idx = row * 3 + col_idx
                        if movie_idx < len(recommendations):
                            movie = recommendations.iloc[movie_idx]
                            with cols[col_idx]:
                                st.image("https://via.placeholder.com/150x225?text=Poster+Pelicula", caption=movie['title'])
                                
                                # Mostrar categorías de forma segura
                                if isinstance(movie['categories'], list):
                                    st.markdown(f"**Categorías:** {', '.join(movie['categories'])}")
                                else:
                                    st.markdown(f"**Categorías:** {movie['categories']}")
                                
                                # Mostrar plataformas de forma segura
                                if isinstance(movie['platforms'], list):
                                    st.markdown(f"**Plataformas:** {', '.join(movie['platforms'])}")
                                else:
                                    st.markdown(f"**Plataformas:** {movie['platforms']}")
                                
                                # Mostrar rating
                                rating_col = find_rating_column(recommender.movies_df)
                                if rating_col:
                                    st.markdown(f"**Calificación:** {movie[rating_col]}/10")
                                else:
                                    st.markdown("**Calificación:** No disponible")

# Página de recomendación por categoría
elif page == "Recomendación por Categoría":
    st.header("Recomendación por Categoría")
    st.markdown("Encuentra las mejores películas de tu género favorito.")
    
    # Obtener categorías disponibles
    categories = recommender.get_all_categories()
    
    if not categories:
        st.error("No hay categorías disponibles.")
    else:
        # Selector de categoría
        category = st.selectbox(
            "Selecciona una categoría:",
            options=categories
        )
        
        # Número de recomendaciones
        num_recommendations = st.slider("Número de recomendaciones", 1, 10, 5)
        
        # Botón para buscar películas
        if st.button("Buscar Películas"):
            # Obtener recomendaciones por categoría
            category_recommendations = recommender.get_recommendations_by_category(category, num_recommendations)
            
            if category_recommendations.empty:
                st.error(f"No se encontraron películas para la categoría '{category}'.")
            else:
                # Mostrar recomendaciones
                st.subheader(f"Mejores películas de {category}:")
                
                for _, movie in category_recommendations.iterrows():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image("https://via.placeholder.com/150x225?text=Poster+Pelicula", caption=movie['title'])
                    with col2:
                        st.markdown(f"**Título:** {movie['title']}")
                        st.markdown(f"**Año:** {movie['year']}")
                        
                        # Mostrar categorías de forma segura
                        if isinstance(movie['categories'], list):
                            st.markdown(f"**Categorías:** {', '.join(movie['categories'])}")
                        else:
                            st.markdown(f"**Categorías:** {movie['categories']}")
                        
                        # Mostrar plataformas de forma segura
                        if isinstance(movie['platforms'], list):
                            st.markdown(f"**Plataformas:** {', '.join(movie['platforms'])}")
                        else:
                            st.markdown(f"**Plataformas:** {movie['platforms']}")
                        
                        # Mostrar rating
                        rating_col = find_rating_column(recommender.movies_df)
                        if rating_col:
                            st.markdown(f"**Calificación:** {movie[rating_col]}/10")
                        else:
                            st.markdown("**Calificación:** No disponible")
                            
                        st.markdown(f"**Descripción:** {movie['description']}")
                    st.markdown("---")

# Página de recomendación por plataforma
elif page == "Recomendación por Plataforma":
    st.header("Recomendación por Plataforma")
    st.markdown("Descubre qué ver en tus servicios de streaming favoritos.")
