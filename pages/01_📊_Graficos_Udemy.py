import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

if st.checkbox('¿Qué es Udemy?'):
    st.write('Tienda virtual de aprendizaje y enseñanza con más de 213000 cursos y 62 millones de estudiantes')

#carga de datos
udemy_courses=pd.read_csv('Datasets/df_uc.csv')
df_uc=pd.DataFrame(udemy_courses) 

#Presentación datos
if st.checkbox('Datos en tabla'):
    st.dataframe(df_uc)
    if st.checkbox('Vista de los primeras ó últimas 5 filas'):
        if st.button('Mostrar primeras 5 filas'):
            st.write(df_uc.head())
        if st.button('Mostrar últimas 5 filas'):
            st.write(df_uc.tail())

if st.checkbox('Nube de palabras'):
    if st.button('Títulos'):
        all_titles_uc = ' '.join(df_uc['course_title'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_titles_uc)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusiones de Títulos de Udemy: Se favorece la presencia de cursos introductorios, principalmente enfocados en ciencias computacionales, a diferencia de Edx y Coursera, se observa la presencia de cursos de arte como piano y Guitar y de diseño como Photoshop y Adobe Illustrator.')

    if st.button('Temática'):
        all_subject_uc = ' '.join(df_uc['subject'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_subject_uc)

        # Configura y muestra la figura
        fig= plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusiones de Nube de Palabras Subject de Udemy: Es posible observar un mejor comportamiento mediante un gráfico de columnas. Se observan 3 grandes tópicos en la oferta de Udemy: Web Development (que en la imagen aparece separado a Development Web), Finance Business (equiparable a Business Finance) y Musical Instruments')

if st.checkbox('Gráficos de Relaciones y Frecuencia de variables'):
    if st.button('Frecuencia de Subjects'):
        # Obtener el recuento de valores únicos en la columna 'subject'
        subject_counts_uc = df_uc['subject'].value_counts()

        # Ordenar los valores de mayor a menor
        subject_counts_sorted_uc = subject_counts_uc.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(subject_counts_sorted_uc.index, subject_counts_sorted_uc.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Subject')
        plt.ylabel('Cantidad')
        plt.title('Freciencia de Subjects en Udemy')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfico de Barras de Subject de Udemy: Únicamente se observa la presencia de 4 grandes ramas, donde predomina el Web Development equiparado con Business Finance. ')
    
    if st.button('Frecuencia de Niveles en el catálogo'):
        # Obtener el recuento de valores únicos en la columna 'subject'
        level_counts_uc = df_uc['level'].value_counts()

        # Ordenar los valores de mayor a menor
        level_counts_sorted_uc = level_counts_uc.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(level_counts_sorted_uc.index, level_counts_sorted_uc.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Level')
        plt.ylabel('Cantidad')
        plt.title('Freciencia de Level en Udemy')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfica de Barras de Level en Udemy: La variable All Levels es ambigüa, por experiencia previa en cursos puedo decir, que se trata de cursos que te brindan información básica con posibilidad de generar proyectos más avanzados como retos adicionales. Sin embargo, lo más importante es la la frecuencia predominante de Beginner Level, siendo la más frecuente. ')

    if st.button('Diagrama de Dispersión Ingreso por Curso por Número de Lectures dividido por Temática'):
        # Crear el diagrama de dispersión con subdivisión por 'subject'
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_uc, x='ingreso_por_curso', y='num_lectures', hue='subject')

        # Título del gráfico
        plt.title('Diagrama de Dispersión: Ingreso por Curso vs. Num Lectures')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones de Diagrama de Dispersión entre Ingreso por curso y Número de Lecturas en Udemy: La mayoría de los cursos de Web Development generan poco ingreso (número de suscriptores multiplicado por precio de curso), sin embargo, debido a la gran cantidad de ellos parece ser que ante una gran oferta de ellos, se puede concluir que el mayor aporte monetario a Udemy viene de este subject. Por otro lado, existen cursos que generan mayor ingreso que en su mayoría son del mismo tema, tal vez, a raíz de la gran diversidad de cursos enfocados en esta área. ')
    
    if st.button('Diagrama de Dispersión Ingreso por Curso por Número de Lectures dividido por Temática eliminando Web Development'):
        # Crear el diagrama de dispersión con subdivisión por 'subject'
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_uc, x='ingreso_por_curso', y='num_lectures', hue='level')

        # Título del gráfico
        plt.title('Diagrama de Dispersión: Ingreso por Curso vs. Num Lectures')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones de Diagrama de Dispersión de Ingreso por curso contra Número de lectures subidivido por Temática eliminando Web Development: Se comprueba la misma tendencia que con Web Development, una gran cantidad de cursos con pocas lecturas que a pesar de diferencias sustanciales en el número de lecturas generan un ingreso similar. Es importante considerar la escala presente en el eje X, por su magnitud podría contarse que un movimiento de 0.25 a 0.5 representa (tomando en cuenta un contexto de pequeña empresa) una ganancia tal vez, significativa. ')

    if st.button('Diagrama de Dispersión Ingreso por Curso por Número de Lectures dividido por Nivel'):
        # Filtrar los datos para excluir la categoría 'All Levels'
        filtered_data = df_uc[df_uc['level'] != 'All Levels']

        # Crear el diagrama de dispersión sin la categoría 'All Levels'
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_data, x='ingreso_por_curso', y='num_lectures', hue='level')

        # Título del gráfico
        plt.title('Diagrama de Dispersión: Ingreso por Curso vs. Num Lectures')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Diagrama de Dispersión Ingreso por Curso y Número de Conferencias dividido por nivel: se observa que la gran mayoría de cursos pertenecen al área de All Levels, sin embargo en el gráfico donde se discrimina tal valor, se observa que los cursos de nivel Beginner predominan en la cantidad de ingreso por curso generado, se observa una tendencia donde aquellos cursos con mayor éxito económico (traducido como Ingreso por curso) son de nivel Beginner y con una cantidad de conferencias bajas.')

    if st.button('Gráfica de barras de las Temáticas con su Ingreso promedio por curso'):

        # Calcular el promedio de ingreso por curso por cada categoría de 'subject'
        avg_income_by_subject = df_uc.groupby('subject')['ingreso_por_curso'].mean().reset_index()

        # Crear el diagrama de barras
        fig=plt.figure(figsize=(10, 6))
        sns.barplot(data=avg_income_by_subject, x='subject', y='ingreso_por_curso')

        # Título del gráfico
        plt.title('Promedio de Ingreso por Curso por Categoría de Subject')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones del Gráfico de Columnas de Promedio de Ingreso por Curso y Subject: Se observa que los cursos enfocados en Web Development generan un mayor ingreso promedio, muy por encima de los otros subject, siguiendo por debajo Graphic Design a pesar de que Business Finance es el segundo con mayor presencia en Udemy. ')

    if st.button('Gráfica de barras de Niveles con su Ingreso promedio por curso'):

        # Calcular el promedio de ingreso por curso por cada categoría de 'subject'
        avg_income_by_subject = df_uc.groupby('level')['ingreso_por_curso'].mean().reset_index()

        # Crear el diagrama de barras
        fig=plt.figure(figsize=(10, 6))
        sns.barplot(data=avg_income_by_subject, x='level', y='ingreso_por_curso')

        # Título del gráfico
        plt.title('Promedio de Ingreso por Curso por Categoría de Level')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones de gráfico de Promedio de Ingreso por Curso dividido por categoría de Level: Se observa un ingreso promedio mayor por cursos de All Levels seguido de Beginner Level y posteriormente Intermediate Level, concordante con la tasa de frecuencia de los cursos.')

if st.checkbox('Conclusión de catálogo Udemy'):
    st.write('Los datos provisto por Udemy son muy útiles para establecer seguimiento mediante temática por la existencia de únicamente 4 subjects y los niveles, se observa una predominancia de Web Development en el catálogo que puede deberser al auge en la decada de 2010s de la programación orientada a sitios web y el nacimiento de esta plataforma educativa.')
