import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

if st.checkbox('¿Qué es Coursera?'):
    st.write('Es una plataforma educativa virtual que ofrece cursos diversos en temáticas disponibles en distintos idiomas y desarrollada por la Universidad de Stanford.')

#carga de datos
coursera_courses=pd.read_csv('Datasets/df_cc.csv')
df_cc=pd.DataFrame(coursera_courses) 

coursera_reviews=pd.read_csv('Datasets/df_cr.csv')
df_cr=pd.DataFrame(coursera_reviews)

#Presentación datos
if st.checkbox('Datos en tabla'):
    st.dataframe(df_cc)
    if st.checkbox('Vista de los primeras ó últimas 5 filas'):
        if st.button('Mostrar primeras 5 filas'):
            st.write(df_cc.head())
        if st.button('Mostrar últimas 5 filas'):
            st.write(df_cc.tail())

#nube de palabras
if st.checkbox('Nube de palabras'):
    if st.button('Títulos'):
        all_titles_cc = ' '.join(df_cc['name'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_titles_cc)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusión de Nube de Palabras de Títulos Coursera: Parece ser que existe una mezcla de palabras más comunes, aquellas de índole de las ciencias computaciones tales como JavaScript, Web Development, HTML y otras de música como Piano, Guitarra. También resulta relevante la importante de la cursos introductorios y de entrenamiento para llamar la atención. El título es el primer acercamiento del posible consumidor con el producto.')

    if st.button('Instituciones'):
        all_institution_cc = ' '.join(df_cc['institution'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_institution_cc)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusiones Nube de palabras Instituciones de Coursera: Las universidades estadounidenses parecen liderar la oferta de cursos brindados, Duke University conocida por su enfoque de negocios, Business School, University of Pennsylvania son algunas de las más enfocadas en el ámbito empresarial. También llama la atención la presencia de Google Cloud y de IBM dos empresa que han ofertados cursos en el área de informática. ')

if st.checkbox('Gráficos de Relaciones y Frecuencia de variables'):
    if st.button('Top 5 cursos por número de calificaciones brindadas'):

        # Realizar el merge entre df_cr y df_cc
        merged_df = df_cr.merge(df_cc, on='course_id')

        # Contar el número de ocurrencias de cada course_id
        course_counts = merged_df['course_id'].value_counts()

        # Seleccionar los 10 cursos con el mayor número de ocurrencias
        top_5_courses = course_counts.head(5)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(12, 6))
        sns.barplot(x=top_5_courses.index, y=top_5_courses.values)

        # Título del gráfico
        plt.title('Los 5 Cursos con mayor número de calificaciones')

        # Etiquetas del eje x
        plt.xlabel('Course ID')

        # Etiquetas del eje y
        plt.ylabel('Número de Calificaciones en Coursera')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Diagrama de Columnas de Los cursos con mayor número de calificaciones de Coursera: Se observa la presencia predominante de tópicos enfocados en TI como python, python-data, machine-learning y deep learning. Con base en lo anterior, ante la falta de una variable subscriptores en Coursera y entendiendose como aquellas personas que calificaron el curso sean únicamente consumidores del producto, podemos aseverar que los cursos TI en Coursera tienen una mayor demanda en comparación a otros tópicos. ')
    
    if st.button('Top 5 cursos por Rating (Mínimo de calificaciones obtenidas de 1071)'):   
        # Filtrar los cursos con 'num_ratings' mayor a 1071
        filtered_courses = df_cc[df_cc['num_ratings'] > 1071]

        # Ordenar los cursos filtrados por 'media_rating' de manera descendente
        top_10_courses = filtered_courses.nlargest(10, 'media_rating')

        # Crear el gráfico de columnas
        fig=plt.figure(figsize=(12, 6))
        sns.barplot(x='media_rating', y='course_id', data=top_10_courses)

        # Título del gráfico
        plt.title('Los 10 Mejores Cursos con el Rating más Alto (Número de Calificaciones mínima de 1071)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Diagrama de Barras de los cursos con mayor rating que tienen al menos 1071 número de calificaciones: Se observa una predominancia de 2 áreas TI observable con el tópico build-a-computer y programming-language, al igual que otros cursos enfocados en humanides como painting, educación, introclassicmusic. NOTA: La condición fue establecida para poder filtrar aquellos que tuvieran un mínimo de 1071 calificaciones, este número representa la mediana del número de calificaciones. ')

if st.checkbox('Conclusión de catálogo Coursera'):
    st.write('Coursera provee de 3 caracteríticas muy relevantes, el número de calificaciones obtenidas, rating y las instituciones que los brindan. Las 2 primeras pueden ser utilizadas para trazar una línea de tendencia a encontrar la popularidad de centros educativos para poder cotizar aquellos cursos que son más populares y estén disponibles de ellos. Cabe resaltar que la falta de temática complico el análisis por otras áreas como subject o nivel. ')
