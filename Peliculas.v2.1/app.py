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
    csv_path= 'tmdb_movies.csv'
    if os.path.exists(csv_path):
        return MovieRecommender(csv_path)
    else:
        st.warning("el archivo csv: 'tmdb_movies' no existe , usando datos de ejemplo")
    return MovieRecommender()

#carga/sube los archivos csv
with st.sidebar:
    st.header("configuración")
    uploaded_file = st.file_uploader("sube un archivo csv", type=["csv"])

if uploaded_file is not None:
    # Guardar el archivo subido en la carpeta actual
    with open("tmdb_movies.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Archivo subido correctamente!")

  #reiniciar el recomendador con un nuevo csv
    recommender = MovieRecommender("tmdb_movies.csv")
else:
    recommender = get_recommender()
    
    
# Sidebar para navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Recomendación por Película", "Recomendación por Categoría", 
     "Recomendación por Plataforma", "Visualizaciones", "ver Datos"]
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
        
        # SOLUCIÓN AL ERROR: Buscar la columna de rating correcta
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
    
    # Selector de película
    movie_title = st.selectbox(
        "Selecciona una película:",
        options=recommender.movies_df['title'].tolist()
    )
    
    #numero de las recomendaciones
    num_recommendations = st.slider("numero de recomendaciones", 1, 10, 5)
    
    if st.button("Obtener Recomendaciones"):
        # Obtener recomendaciones
        recommendations = recommender.get_movie_recommendations(movie_title)
        
        # Mostrar la película seleccionada
        st.subheader("Película seleccionada:")
        selected_movie = recommender.movies_df[recommender.movies_df['title'] == movie_title].iloc[0]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://via.placeholder.com/300x450?text=Movie+Poster", caption=selected_movie['title'])
        with col2:
            st.markdown(f"**Título:** {selected_movie['title']}")
            st.markdown(f"**Año:** {selected_movie['year']}")
            st.markdown(f"**Categorías:** {', '.join(selected_movie['categories'])}")
            st.markdown(f"**Plataformas:** {', '.join(selected_movie['platforms'])}")
            
            # Mostrar rating usando la columna correcta
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
                      st.image("https://via.placeholder.com/150x225?text=Movie+Poster", caption=movie['title'])
                      st.markdown(f"**Categorías:** {', '.join(movie['categories'])}")
                      st.markdown(f"**Plataformas:** {', '.join(movie['platforms'])}")
                      
                      # Mostrar rating usando la columna correcta
                      rating_col = find_rating_column(recommender.movies_df)
                      if rating_col:
                          st.markdown(f"**Calificación:** {movie[rating_col]}/10")
                      else:
                          st.markdown("**Calificación:** No disponible")

# Página de recomendación por categoría
elif page == "Recomendación por Categoría":
    st.header("Recomendación por Categoría")
    st.markdown("Encuentra las mejores películas de tu género favorito.")
    
    # Selector de categoría
    category = st.selectbox(
        "Selecciona una categoría:",
        options=recommender.get_all_categories()
    )
    
    #num. recomendaciones
    num_recommendations = st.slider("numero de recomendaciones", 1, 10, 5)
    
    
    # Botón para buscar películas
    if st.button("Buscar Películas"):
        # Obtener recomendaciones por categoría
        category_recommendations = recommender.get_recommendations_by_category(category)
        
        # Mostrar recomendaciones
        st.subheader(f"Mejores películas de {category}:")
        
        for _, movie in category_recommendations.iterrows():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150x225?text=Movie+Poster", caption=movie['title'])
            with col2:
                st.markdown(f"**Título:** {movie['title']}")
                st.markdown(f"**Año:** {movie['year']}")
                st.markdown(f"**Categorías:** {', '.join(movie['categories'])}")
                st.markdown(f"**Plataformas:** {', '.join(movie['platforms'])}")
                
                # Mostrar rating usando la columna correcta
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
    
    # Selector de plataforma
    platform = st.selectbox(
        "Selecciona una plataforma:",
        options=recommender.get_all_platforms()
    )
    
    if st.button("Buscar Películas"):
        # Obtener recomendaciones por plataforma
        platform_recommendations = recommender.get_recommendations_by_platform(platform)
        
        # Mostrar recomendaciones
        st.subheader(f"Mejores películas en {platform}:")
        
        for _, movie in platform_recommendations.iterrows():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150x225?text=Movie+Poster", caption=movie['title'])
            with col2:
                st.markdown(f"**Título:** {movie['title']}")
                st.markdown(f"**Año:** {movie['year']}")
                st.markdown(f"**Categorías:** {', '.join(movie['categories'])}")
                st.markdown(f"**Plataformas:** {', '.join(movie['platforms'])}")
                
                # Mostrar rating usando la columna correcta
                rating_col = find_rating_column(recommender.movies_df)
                if rating_col:
                    st.markdown(f"**Calificación:** {movie[rating_col]}/10")
                else:
                    st.markdown("**Calificación:** No disponible")
                    
                st.markdown(f"**Descripción:** {movie['description']}")
            st.markdown("---")

# Página de visualizaciones
elif page == "Visualizaciones":
    st.header("Visualizaciones")
    st.markdown("Explora la distribución de películas por categoría y plataforma.")
    
    # Visualización de categorías
    st.subheader("Distribución de Películas por Categoría")
    
    # Contar la frecuencia de cada categoría
    category_counts = {}
    for categories in recommender.movies_df['categories']:
        for category in categories:
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
    
    # Ordenar por frecuencia
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    categories, counts = zip(*sorted_categories)
    
    # Crear gráfico
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    bars = ax1.bar(categories, counts, color='skyblue')
    ax1.set_title('Distribución de Películas por Categoría', fontsize=15)
    ax1.set_xlabel('Categoría', fontsize=12)
    ax1.set_ylabel('Número de Películas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Añadir etiquetas de valor
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.0f}', ha='center', va='bottom')
    
    st.pyplot(fig1)
    
    # Visualización de plataformas
    st.subheader("Distribución de Películas por Plataforma")
    
    # Contar la frecuencia de cada plataforma
    platform_counts = {}
    for platforms in recommender.movies_df['platforms']:
        for platform in platforms:
            if platform in platform_counts:
                platform_counts[platform] += 1
            else:
                platform_counts[platform] = 1
    
    # Ordenar por frecuencia
    sorted_platforms = sorted(platform_counts.items(), key=lambda x: x[1], reverse=True)
    platforms, counts = zip(*sorted_platforms)
    
    # Crear gráfico
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.pie(counts, labels=platforms, autopct='%1.1f%%', startangle=90, 
            shadow=True, explode=[0.05] * len(platforms))
    ax2.set_title('Distribución de Películas por Plataforma', fontsize=15)
    ax2.axis('equal')
    plt.tight_layout()
    
    st.pyplot(fig2)

# Página para ver datos (nueva funcionalidad de debug)
elif page == "ver Datos":
    st.header("Información del Dataset")
    st.markdown("Explora la estructura de tus datos.")
    
    # Mostrar información básica del DataFrame
    st.subheader("Información General")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"Número de filas: {len(recommender.movies_df)}")
        st.info(f"Número de columnas: {len(recommender.movies_df.columns)}")
    with col2:
        rating_col = find_rating_column(recommender.movies_df)
        if rating_col:
            st.info(f"Columna de rating encontrada: {rating_col}")
        else:
            st.warning("No se encontró columna de rating")
    
    # Mostrar columnas disponibles
    st.subheader("Columnas Disponibles")
    st.write(list(recommender.movies_df.columns))
    
    # Mostrar muestra de datos
    st.subheader("Muestra de Datos")
    st.dataframe(recommender.movies_df.head())
    
    # Mostrar estadísticas de rating si existe
    rating_col = find_rating_column(recommender.movies_df)
    if rating_col:
        st.subheader(f"Estadísticas de {rating_col}")
        st.write(recommender.movies_df[rating_col].describe())

# Pie de página
st.markdown("---")
st.markdown("Desarrollado con ❤️ usando Python y Machine Learning")