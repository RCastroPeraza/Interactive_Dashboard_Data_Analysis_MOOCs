import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np

if st.checkbox('¿Qué es Edx?'):
    st.write('Plataforma de cursos abiertos masivos en línea trabajando con universidades y organizaciones líderes mundiales para ofrecer cursos de alta calidad teniendo un catálogo de más de 3500 cursos disponibles')

#carga de datos
edx_courses=pd.read_csv('Datasets/df_ec.csv')
df_ec=pd.DataFrame(edx_courses) 

#nube de palabras
if st.checkbox('Nube de palabras'):
    if st.button('Títulos'):
        all_titles_ec = ' '.join(df_ec['title'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_titles_ec)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusión de Nube de Palabras de Títulos de Edx: Al igual que con Coursera, aquellos cursos que presentan introducción a temas parecen ser más relevantes, aunque es notable la importancia de un enfoque de negocio por la presencia de Business y de Management. También la relevante de la Data Science, Python, Analysis. Algo de importancia a tomar en cuenta es que presentan palabras en inglés y en español, algo que no se observó en coursera, esto genera ruido porque palabras como Introduction e Introducción pudieran estar juntas, aumentando su presencia en la nube de palabras. Edx a primera mano, tiene un enfoque más orientado a la ciencia de datos y negocios.')

    if st.button('Instituciones'):
        all_institution_ec = ' '.join(df_ec['institution'])
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_institution_ec)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusiones Nube de Palabras de Instituciones Edx: Se observa una mayor diversidad de nacionalidades en las instituciones a diferencia de Coursera, la Universidad Politécnica de Valencia (por su nombre en español, en la imagen está en valenciano), es conocida por su enfoque en energías, salud y recursos. Por otro lado se observa la gran presencia de Harvard escuela de negocios y leyes de EEUU. ')

    if st.button('Tematicas'):
        all_subject_ec = ' '.join(df_ec['subject'].astype(str))
        wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(all_subject_ec)

        # Configura y muestra la figura
        fig=plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)
        st.write('Conclusión de Nube de Palabras de Subjetcs de Edx: llama la atención la poca cantidad de palabras, esto significa que es posible filtrar por temas utilizando un diagrama de columnas. Corroborando la información anterior, Edx, parece ser una plataforma enfocada en las cienicas computaciones y el manejo de negocios, incorporando en su catálogoc otros cursos como la ingeniería, humanidades, educación y biología.')

#Gráficas
if st.checkbox('Gráficos de Relaciones y Frecuencia de variables'):
    if st.button('Frecuencia de Subjects'):
        # Obtener el recuento de valores únicos en la columna 'subject'
        subject_counts_ec = df_ec['subject'].value_counts()

        # Ordenar los valores de mayor a menor
        subject_counts_sorted_ec = subject_counts_ec.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(subject_counts_sorted_ec.index, subject_counts_sorted_ec.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Subject')
        plt.ylabel('Cantidad')
        plt.title('Freciencia de Subjects en Edx')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones gráfica de columnas de Subject para Edx: Se observa una tendencia a brindar cursos enfocados en tecnologías observable por la frecuencia de Computer Science y Data Analysis & Statistics, por otra lado también se observa una variedad donde predominan las ciencias sociales: Humanidades, Social Sciences y Comunicación. También, es importa la versatilidad de Data Analysis & Statistics siendo posible de vincular con la oferta de Business & Management y Econocmics & Finance.')

    if st.button('Frecuencia de Level'):

        # Obtener el recuento de valores únicos en la columna 'level'
        level_counts_ec = df_ec['Level'].value_counts()

        # Ordenar los valores de mayor a menor
        level_counts_sorted_ec = level_counts_ec.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(level_counts_sorted_ec.index, level_counts_sorted_ec.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Level')
        plt.ylabel('Cantidad')
        plt.title('Freciencia de Level en Edx')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones de Gráfico de Barras Level de Edx: La mayoría de los cursos pertenecen a un nivel introductorio. Por otro lado, se escasa de cursos especializados avanzados. ')
    if st.button('Frecuencia de Tipo de Curso'):
        # Obtener el recuento de valores únicos en la columna 'course_type'
        course_type_counts_ec = df_ec['course_type'].value_counts()

        # Ordenar los valores de mayor a menor
        course_type_counts_sorted_ec = course_type_counts_ec.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(course_type_counts_sorted_ec.index, course_type_counts_sorted_ec.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Course Type')
        plt.ylabel('Cantidad')
        plt.title('Freciencia de Course Type en Edx')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfico de Barras Course Type de Edx: Casi la totalidad de los cursos se enfocan en un contenido disponible para su consulta al tiempo del estudiante. Pareciera ser un mejor enfoque de negocio complementandolo con el level, podemos concluir que los cursos introductorios y de self-paced on your time son los más comunes de encontrar en el catálogo de Edx. ')
    if st.button('Frecuencia de Esfuerzo de Curso'):

        # Obtener el recuento de valores únicos en la columna 'course_effort'
        course_effort_counts_ec = df_ec['course_effort'].value_counts()

        # Obtener las 10 categorías más frecuentes
        top_10_categories_ec = course_effort_counts_ec.head(10)

        # Ordenar los valores de mayor a menor
        top_10_categories_sorted_ec = top_10_categories_ec.sort_values(ascending=False)

        # Crear el diagrama de columnas
        fig=plt.figure(figsize=(10, 6))
        plt.bar(top_10_categories_sorted_ec.index, top_10_categories_sorted_ec.values)

        # Rotar las etiquetas del eje x para una mejor legibilidad
        plt.xticks(rotation=90)

        # Etiquetas y título del gráfico
        plt.xlabel('Course Effort')
        plt.ylabel('Cantidad')
        plt.title('Frecuencia de las 10 categorías más frecuentes de Course Effort en Edx')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfico de Barras de  Course Effort de Edx: La mayoría de los cursos oscilan entre 2-4 h, 2-3 h y 3-5 h, a partir de este valor se observa un cambio más pronunciado que significa menor frecuencia. NOTA: Se limitaron a las 10 más frecuentes, debido a la gran cantidad de valores diferentes que tiene esta variable. ')
    #if st.button('Pairplot del Catálogo'):
        #course_type_list=df_ec['course_type'].unique().tolist()
        #level_type_list=df_ec['Level'].unique().tolist()
       # subject_list=df_ec['subject'].unique().tolist()
       # if st.button('Subdivido por Tipo de Curso'):
            #print('hola')
           # c_t=st.multiselect('Seleccione las categorías que desee analizar:', course_type_list)
            #df_ec_ct=df_ec[df_ec['course_type'].isin(c_t)]
            #fig=plt.figure(figsize=(10, 6))
           # sns.pairplot(data=df_ec,hue='course_type')
           # st.pyplot(fig)

    if st.button('Diagrama de Dispersión entre precio y número de inscritos'):
        # Crear el scatter plot
        fig=plt.figure(figsize=(10, 6))
        plt.scatter(df_ec['price_extracted'], df_ec['n_enrolled'])

        # Etiquetas de los ejes
        plt.xlabel('Precios')
        plt.ylabel('Inscritos')

        # Título del gráfico
        plt.title('Diagrama de Dispersión entre Precio y Número de Inscritos')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusión de Gráfico de Dispersión Precio e Inscritos y de Displot de Precio: La mayoría de los cursos se ubican por debajo de 100 dolares de precio, graficando contra inscritos también se observa que aquellos cursos por debajo o alrededor de este precio tienen una mayor cantidad de estudiantes inscritos. ')
    
    if st.button('Diagrama de Cajas y Bigotes de Esfuerzo total por curso'):

        # Crear el diagrama de cajas
        fig=plt.figure(figsize=(10, 6))
        sns.boxplot(data=df_ec, y='esfuerzo_total')

        # Título del gráfico
        plt.title('Diagrama de Cajas: Esfuerzo Total')

        # Etiqueta del eje y
        plt.ylabel('Esfuerzo Total')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Diagrama de Cajas y Bigotes de Esfuerzo total en Edx: Se observa que la mayoría de los cursos se ubican por debajo de los 50 h de esfuerzo total, siendo notable la presencia de outliers. ')

    if st.button('Diagrama de Columnas de Esfuerzo Total agrupado por Intérvalos'):

        # Definir los límites de los grupos
        bin_edges = [0, 10, 20, 30 ,40, 50,60,70,80,100,float('inf')]

        # Crear las categorías a partir de los límites
        categories = pd.cut(df_ec['esfuerzo_total'], bins=bin_edges)

        # Agregar las categorías al DataFrame
        df_ec['esfuerzo_group'] = categories

        # Crear el diagrama de barras
        fig=plt.figure(figsize=(10, 6))
        sns.countplot(data=df_ec, x='esfuerzo_group')

        # Título del gráfico
        plt.title('Distribución del Esfuerzo Total')

        # Etiquetas de los ejes
        plt.xlabel('Grupo de Esfuerzo')
        plt.ylabel('Cantidad')

        # Rotar las etiquetas del eje x para mayor legibilidad
        plt.xticks(rotation=45)

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfica de Barras de Esfuerzo Total (horas de dedicación por semana por longitud del curso en semanas): Se observa una predominancia de cursos que requieren un esfuerzo de 10-20 y de 20-30 horas siendo predomintes en comparación al esfuerzo total de otros cursos. Esto puede servir de base para establecer una pauta de duración total de los cursos para la inversión.')
    
    if st.button('Diagrama de Dispersión del Esfuerzo Total (h totales) contra logaritmo base 10 del número de inscritos'):
        # Calcular el logaritmo de 'n_enrolled'
        df_ec['log_n_enrolled'] = np.log(df_ec['n_enrolled'])

        # Crear el gráfico de dispersión
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_ec, x='esfuerzo_total', y='log_n_enrolled')

        # Título del gráfico
        plt.title('Gráfico de Dispersión: Esfuerzo Total vs. Log(N Enrolled)')

        # Etiquetas de los ejes
        plt.xlabel('Esfuerzo Total')
        plt.ylabel('Log(N Enrolled)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfica de Dispersión del Logaritmo de Número de Inscritos contra el Esfuerzo total: La presencia de la mayoría de los cursos está ubicado a valores bajos de Esfuerzo total. Lo cual es comprobable en el Gráfico Diagrama de Barras de Esfuerzo Total. ')

    if st.button('Diagrama de Dispersión del Esfuerzo Total (h totales) contra logaritmo base 10 del número de inscritos aplicando regla de 3 sigmas (desviación estándar a Esfuerzo Total)'):
        # Calcular el logaritmo de 'n_enrolled'
        df_ec['log_n_enrolled'] = np.log(df_ec['n_enrolled'])

        # Calcular la desviación estándar y el percentil 75% de 'esfuerzo_total'
        std = df_ec['esfuerzo_total'].std()
        percentile_75 = df_ec['esfuerzo_total'].quantile(0.75)

        # Definir el límite superior del filtro
        upper_limit = percentile_75 + 3 * std

        # Filtrar los puntos con 'esfuerzo_total' por debajo del límite superior
        filtered_data = df_ec[df_ec['esfuerzo_total'] < upper_limit]

        # Crear el gráfico de dispersión
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_data, x='esfuerzo_total', y='log_n_enrolled')

        # Título del gráfico
        plt.title('Gráfico de Dispersión: Esfuerzo Total (< 3 Desviaciones Estándar al Percentil 75%) vs Log(N Enrolled)')

        # Etiquetas de los ejes
        plt.xlabel('Esfuerzo Total')
        plt.ylabel('Log(N Enrolled)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones de Diagrama de Dispersión del Logaritmo del número de inscritos contra el esfuerzo total aplicando la regla de las 3 sigmas: Se percibe levemente una baja en la tasa de inscritos a mayor esfuerzo total, es decir. Los cursos más "ofertados" son aquellos con bajo esfuerzo total, sin embargo, es notable una curvatura con pendiente negativa a partir de una cima en el valor de esfuerzo total de 60 h, a partir de este valor, el comportamiento baja, lo que puede sugerir que a mayor esfuerzo total el número de inscritos no aumenta como sucedía previo al pico.')

    if st.button('Diagrama de Dispersión del Esfuerzo medio por curso contra el logaritmo base de 10 del número de inscritos'):

        # Crear el gráfico de dispersión con logaritmo de 'n_enrolled'
        fig=plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_ec, x='media_course_effort', y=np.log(df_ec['n_enrolled']))

        # Título del gráfico
        plt.title('Gráfico de Dispersión: Media Course Effort vs Log(N Enrolled)')

        # Etiquetas de los ejes
        plt.xlabel('Media de esfuerzo de curso (h por semana)')
        plt.ylabel('Log(N Enrolled)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusión Gráfica de Dispersión del esfuerzo medio por curso contra el logartimo de número de suscritos: Se observa una clara tendencia a mayor esfuerzo en horas por semana, existe un menor número de personas suscritas a ellos. siendo notable la presencia de 0 a 5 con un crecimiento de suscritos (tendencia positiva)')

    if st.button('Diagrama de Columnas de Ingreso por curso de acuerdo a la variable Grupo de Esfuerzo'):

        # Agrupar los datos por 'esfuerzo_group' y calcular el promedio de 'ingreso_por_curso'
        grupo_ingreso = df_ec.groupby('esfuerzo_group_str')['ingreso_por_curso'].mean()

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.bar(grupo_ingreso.index, grupo_ingreso.values)

        # Etiquetas y título del gráfico
        plt.xlabel('Esfuerzo Group')
        plt.ylabel('Ingreso por Curso')
        plt.title('Diagrama de Columnas: Ingreso por Curso según Esfuerzo Group')

        # Rotar las etiquetas del eje x a 90 grados
        plt.xticks(rotation=90)

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('Conclusiones Gráfica de Barras de Esfuerzo Total de Curso contra Ingreso por Curso: Se observa un patron predominante en cursos con tiempo de esfuerzo de 80 a 100 horas. Lo que podría confimrar que aquellos cursos extensos son de mayor remuneración económica para la empresa.')

if st.checkbox('Conclusión'):
    st.write('Los datos de Edx son útiles por su cantidad de variables numéricas, la creación de marca de clase para el tiempo de esfuerzo de curso multiplicando por el tiempo en semanas previsto permitió la generación de la variable esfuerzo total, los precios fueron extráidos y con el número de suscriptores fue posible obtener la cantidad de ingreso por curso y filtrando por temática, permitió la evaluación de diversas KPI. Cabe resaltar que a pesar de ser un gran rango de variables numéricas, muchas de ellas fueron incorporadas en otras para permitir análisis más sencillos (Tal es el caso de las antes mencionadas, números inscritos y precio, por brindar un ejemplo).')


