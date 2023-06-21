import streamlit as st
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

#Carga y Tratamiento de los datos
udemy_courses=pd.read_csv('Datasets/df_uc.csv')
df_uc=pd.DataFrame(udemy_courses) 

edx_courses=pd.read_csv('Datasets/df_ec.csv')
df_ec=pd.DataFrame(edx_courses) 

coursera_courses=pd.read_csv('Datasets/df_cc.csv')
df_cc=pd.DataFrame(coursera_courses) 

coursera_reviews=pd.read_csv('Datasets/df_cr.csv')
df_cr=pd.DataFrame(coursera_reviews)

# Combinar las columnas 'course_title' de df_uc y 'title' de df_ec en la columna 'Curso' de df_mezcla
df_mezcla = pd.DataFrame({
    'Curso': df_uc['course_title'].tolist() + df_ec['title'].tolist(),
    'Precio': df_uc['price'].tolist() + df_ec['price_extracted'].tolist(),
    'Inscritos': df_uc['num_subscribers'].tolist()+df_ec['n_enrolled'].tolist()
})

# Ordenar el dataframe por el precio de forma descendente
df_mezcla = df_mezcla.sort_values('Precio', ascending=False)

# Filtrar los cursos con 'media_rating' más alta y 'num_rating' mayor a 1071
cursos_filtrados = df_cc[(df_cc['num_ratings'] > 1071)]

# Ordenar los cursos por 'num_rating' de forma descendente
cursos_filtrados = cursos_filtrados.sort_values('media_rating', ascending=False)

st.title('Proyecto Individual 02: Análisis de MOOCs')
st.markdown('***')
st.markdown(' Nombre: Ricardo Castro')
st.markdown(' Github: RCastroPeraza')
st.markdown(' Cohorte: 11')
st.markdown('***')
st.write('### Hipótesis de análisis')
st.write('Los cursos cortos, introductorios, gratuitos y de temática TI generan ganancias mayores medibles a través del ingreso total generado')
st.write('### Objetivo General')
st.write('Enmarcar las características identificables de cursos para la inversión en el catálogo tales como longitud, precio, tema posibilitando mayores ganancias o retornos a menor plazo empleando los datos de Udemy, Coursera y Edx y generar KPI capaces de contrastar estas carcterísticas como medida del desempeño de los cursos seleccionados')
st.write('### Objetivos Específicos')
st.write('* Generar el KPI Tasa de Conversión que evalúe el desempeño de cursos pagados contra cursos gratuitos en la fidelidad del consumidor')
st.write('* Obtener el KPI Tasa de Subscripción por temática donde se determina el tópico más popular y su pendiente de crecimiento en comparación a otros temas')
st.write('* Mediante el KPI Tasa de Ingreso por Curso Promedio de acuerdo a nivel, tasar el nivel que genera mayor ganancias')
st.write('* Establecer el KPI Tasa de Ingreso por Curso Promedio de acuerdo a esfuerzo total en horas para delimitar la característica longitud, esfuerzo de curso (ó horas por semana) y lecturas')

st.markdown('***')

st.sidebar.markdown('Gráficos de Análisis de MOOcs')

st.markdown('# KPI')
if st.checkbox('Tasa de conversión por condición de pago o contenido gratuito'):

    # Obtener el numerador: num_subscribers cuando is_paid es True
    num_paid = df_uc.loc[df_uc['is_paid'] == True, 'num_subscribers'].sum()

    # Obtener el denominador: num_subscribers cuando is_paid es False
    num_free = df_uc.loc[df_uc['is_paid'] == False, 'num_subscribers'].sum()

    # Calcular la tasa de conversión
    tasa_conversion_pago = num_paid / num_free *100

    st.write('Tasa de Conversión Pago en Udemy en porcentaje es: ', tasa_conversion_pago, fontsize=35)

    st.write('* Conclusión KPI Tasa de Conversión: Los contenidos de pago atraen a 2 personas por cada 1 inscrita en algún contenido gratuito en Udemy. Lo que puede sugerir que la inversión en contenido de pago representaría el mejor acercamiento al área de negocio. A continuación se evalúa el mismo KPI evaluado al siguiente año con un crecimiento del 15%. ')

    tasa_conversion_pago_futura = num_paid / num_free *115

    st.write('Tendencia a esperar para un óptimo crecimiento en un año: ', tasa_conversion_pago_futura)

    st.write('* Conclusión KPI Tasa de Conversión Futura: Se espera que el número de suscriptores de contenido de paga aumente de un 2.28 (entendiendose como 2.28 personas que consumen contenido de paga por cada 1 de contenido gratuito) a 2.63. Para conseguirlo se debe de incrementar la media de retención de clientes de consumo pagado o bien, bajar la tasa de consumidores de contenido gratuito. ')
    st.write('Nota: Para este KPI se utilizó la información de Udemy')

if st.checkbox('### Tasa de suscripción en cursos por Tematica'):

    web_dev_mean = df_uc.loc[df_uc['subject'] == 'Web Development', 'num_subscribers'].mean()
    other_mean = df_uc.loc[df_uc['subject'] != 'Web Development', 'num_subscribers'].mean()
    ratio = web_dev_mean / other_mean
    st.write('Tasa de subscripción de TI en Udemy es: ', ratio)
    st.write('* Conclusión KPI Tasa de Subscripción de TI: Este KPI se construye de la razón de la media los cursos con el subject "Web Development" sobre la media de los cursos de las otras áreas. Se comprueba que el rendimiento promedio de suscriptores en cursos de TI (en este caso, Web Development) es de 4 personas por cada 1 persona inscrita en alguna de los otros cursos. Podría significar que debido a tendencias sociales el consumo de productos enfocados en tecnologías son sustancialmente mayores en comparación a otros tópicos. A continuación se evalúa la perspectiva futura del KPI donde se espera una tasa de crecimiento 20%.')

    ratio_futuro= web_dev_mean / other_mean *1.2
    st.write('Tasa de subscripción futura de TI en Udemy es: ', ratio_futuro)

    st.write('* Conclusión KPI Tasa de Susbcripción Futura de TI: Se espera que halla 5 personas suscritas por cada persona suscrita a algún tópico diferente a TI en Udemy. ')
    st.write('Nota: Para este KPI se utilizó la información de Udemy')

if st.checkbox('Tasa de Ingreso por curso evaluado el nivel del mismo'):
    advanced_courses_uc = df_uc[df_uc['level'] == 'Expert Level']
    non_advanced_courses_uc = df_uc[(df_uc['level'] != 'Expert Level') & (df_uc['level'] != 'All Levels')]
    advanced_income_mean_uc = advanced_courses_uc['ingreso_por_curso'].mean()
    non_advanced_income_mean_uc = non_advanced_courses_uc['ingreso_por_curso'].mean()


    advanced_courses_ec = df_ec[df_ec['Level'] == 'Advanced']
    non_advanced_courses_ec = df_ec[(df_ec['Level'] != 'Advanced')]
    advanced_income_mean_ec = advanced_courses_ec['ingreso_por_curso'].mean()
    non_advanced_income_mean_ec = non_advanced_courses_ec['ingreso_por_curso'].mean()


    #Establecimiento de KPI
    kpi_level = (advanced_income_mean_uc+advanced_income_mean_ec) / (non_advanced_income_mean_uc + non_advanced_income_mean_ec)

    #Imprimir valor
    st.write('Tasa de Ingreso por Curso Avanzado en comparación a otros niveles es :', kpi_level)

    st.write('* Conclusión KPI Tasa de Ingreso por Curso de Nivel Avanzado: Los cursos de nivel avanzado a pesar de tener un número de suscritos menor que otros niveles como Introductorio y por su especialidad ser menos frecuentes, parece que comparandolos con otras tasas obtenidas es la única con un cociente positivo, indicando que por cada dolar obtenido (entendiendose de la multiplicación de inscritos por precio) de cursos de otro nivel, el nivel avanzado obtiene 68% más en comparación con los demás. Cabe recalcar la posiblidad de enmarcar este valor dado su alto precio a raíz de la especialidad brindada.')

        
    #Establecimiento de KPI futura
    kpi_level_futuro = 1.15*(advanced_income_mean_uc+advanced_income_mean_ec) / (non_advanced_income_mean_uc + non_advanced_income_mean_ec)

    #Imprimir valor
    st.write('Tasa de Ingreso por Curso Avanzado Futura con un 15% de crecimiento es en comparación a otros niveles es :', kpi_level_futuro)

    st.write('* Conclusión KPI Tasa de Ingreso por Curso de Nivel Avanzado Futuro: Tras un año, el crecimiento, se espera de del 15%, lo que acercaría demasiado el valor de ingreso de cursos avanzados en comparación con otros en 200%. Parece que la inversión en cursos de nivel avanzado a pesar de ser de un posible riesgo por su poca frecuencia y por ende, subpopularidad en comparación con otros niveles, representa mayores ganancias monetarias. ')
    st.write('Nota: Para este KPI se utilizó la información de Udemy y Edx, tomando como Expert level sinónimo de Advanced')

if st.checkbox('Tasa de Ingreso por curso de acuerdo al esfuerzo total del curso'):

    filtro = df_ec['esfuerzo_group_str'].isin(['(100.0, inf]','(80.0, 100.0]'])
    df_filtered = df_ec[filtro]

    # Calcular el promedio de ingreso_por_curso para los grupos filtrados
    promedio_filtered = df_filtered['n_enrolled'].mean()

    # Filtrar los grupos excluyendo los rangos (['(100,inf]','(80.0,100]'])
    filtro_excluido = ~df_ec['esfuerzo_group_str'].isin(['(100.0, inf]','(80.0, 100.0]'])
    df_excluido = df_ec[filtro_excluido]

    # Calcular el promedio de ingreso_por_curso para los grupos excluidos
    promedio_excluido = df_excluido['n_enrolled'].mean()

    # Calcular el KPI como la división entre los promedios
    kpi_esfuerzo = promedio_filtered / promedio_excluido
    st.write("La tasa del promedio de Ingreso por cursos largos (más de 80 h en total) en comparación a cursos regulares y cortos es de: ", kpi_esfuerzo)

    st.write('* Conclusión KPI Tasa de Ingreso por Curso de acuerdo al esfuerzo total: Aquellos cursos que se ubican en los grupos de 80 h por delante, representan un mayor ingreso para la empresa en comparación a cursos menos exigentes. Esto podría deberse al precio de los cursos más extensos, a que es atractivo para el consumidor el comprar un producto amplio con conocimiento que puede ser explotado en un mayor espacio temporal. Cabe recalcar que a pesar de que no son los cursos más frecuentes representan el mayor ingreso por curso de los grupos de esfuerzo divididos. ')

    # Calcular el KPI como la división entre los promedios
    kpi_esfuerzo_futuro = promedio_filtered / promedio_excluido *1.1
    st.write("El crecimiento del KPI basado en el esfuerzo de curso para un 10% debe de ser de: ", kpi_esfuerzo_futuro)

    st.write('* Conclusión KPI Tasa de Ingreso por Curso por Esfuerzo de cursos futuro: Se espera un crecimiento que pueda ser traducido en que aproximadametne 2.6 dolares sean percibidos por la empresa por cada curso largo en comparación a cursos promedio (de 40-80 h) y cursos cortos (menores a 40 h)')
    st.write('Nota: Para este KPI se utilizó la información de Edx')

st.markdown('***')

st.markdown('# Nube de palabras')

st.write('Para la generación de estas nubes de palabras se combinaron los títulos de los cursos, nombres de instituciones y temáticas de cursos de Udemy, Edx y Coursera. ')

if st.checkbox('Títulos de Cursos'):
    all_titles_uc = ' '.join(df_uc['course_title'])
    all_titles_ec = ' '.join(df_ec['title'])
    all_titles_cc = ' '.join(df_cc['name'])
    combined_titles = all_titles_uc + ' ' + all_titles_ec + ' ' + all_titles_cc
    wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(combined_titles)

    # Configura y muestra la figura
    fig=plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)
    st.write('* Conclusión de Oferta Completa de Títulos: Los Títulos que parecen ser más populares para ofertar en MOOCs provistas son los introductorios, enfatizando la inclusión de palabras como Beginner, Course, Trading y Basic.')
    st.write('Nota: Para la generación de esta nube de palabras se utilizó datos de Udemy, Edx y Coursera')
if st.checkbox('Instituciones'):
    all_institution_ec = ' '.join(df_ec['institution'])
    all_institution_cc = ' '.join(df_cc['institution'])

    combined_instituion =all_institution_ec + ' ' + all_institution_cc
    wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(combined_instituion)

    # Configura y muestra la figura
    fig=plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)
    st.write('* Conclusiones de Oferta de Instituciones Completa: De acuerdo a la frecuencia completa, parece ser que la predominancia es de universidades estadounidenses: Harvard, Pennsylvania, Micigan. En un segundo plano, se encuentra IBM, la universidad de Valencia, el MIT y llama la atención la oferta de universidades extranjeras como Indian Institute (India), Universidades Anahuac (México) y el Tecnológico de Monterrey (México).')
    st.write('Nota: Para la generación de esta nube de palabras se utilizó datos de Coursera y Edx')
if st.checkbox('Temática'):
    all_subject_uc = ' '.join(df_uc['subject'])
    all_subject_ec = ' '.join(df_ec['subject'].astype(str))
    combined_subject = all_subject_uc + ' ' + all_subject_ec + ' '
    wordcloud = WordCloud(width=800, height=400, max_font_size=150, random_state=42).generate(combined_subject)

    # Configura y muestra la figura
    fig=plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)
    st.write('* Conclusiones de Oferta completa de Subject: Podríamos concluir que existen 3 grandes áreas del conocimiento obtenido por las MOOCs: Ciencias Computaciones, Enfoque de Negocios y Diseño y Arte. ')
    st.write('Nota: Para la generación de esta nube de palabras se utilizó datos de Edx y Udemy')
st.markdown('***')


st.markdown('# Gráficas')
st.write('### Gráficas de Ventas (Número de alumnado inscrito)')
filtro=st.radio('Seleccione el filtro a aplicar',('Precio', 'Idioma','Rating','Nivel'))

if filtro=='Precio':
    if st.checkbox('Top 10 cursos y su alumnado inscrito con mayor precio'):
        st.write('### Top 10 cursos y su alumnado inscrito con mayor precio')
        # Filtrar los cursos con mayor precio
        cursos_mayor_precio = df_mezcla.head(10)

        # Ordenar los cursos por el número de inscritos de forma descendente
        cursos_mayor_precio = cursos_mayor_precio.sort_values('Inscritos', ascending=True)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.barh(cursos_mayor_precio['Curso'], cursos_mayor_precio['Inscritos'],color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Inscritos')
        plt.ylabel('Curso')
        plt.title('Cursos con Mayor Precio y sus Inscritos (Ordenado por Inscritos)')

        # Mostrar el gráfico
        st.pyplot(fig) 

        st.write('* Conclusión de Diagrama de Barras de Cursos con 10 cursos de mayor precio y con mayor cantidad de alumnado inscrito')
        st.write('Se observa una gran presencia de tópicos enfocados en TI y tecnologías, podría inlcuir tópicos de estádistica como una herramienta en la formación de científicos de datos de manera que la formación con mayor alumnado inscrito 5 de los primeros 6 serían enfocados en la matrícula convencional de un estudiante en formación de TI.')
    
    if st.checkbox('Top 10 cursos y su alumnado inscrito con menor precio'):
        st.write('### Top 10 cursos y su alumnado inscrito con mayor precio')
        #Cursos más baratos top 10
        cursos_menor_precio = df_mezcla.tail(10)

        # Ordenar los cursos por el número de inscritos de forma descendente
        cursos_menor_precio = cursos_menor_precio.sort_values('Inscritos', ascending=False)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.barh(cursos_menor_precio['Curso'], cursos_menor_precio['Inscritos'],color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Inscritos')
        plt.ylabel('Curso')
        plt.title('Cursos con Menor Precio y sus Inscritos (Ordenado por Inscritos)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('* Conclusión Cursos más baratos con mayor cantidad de inscritos')
        st.write('Se observa que varios de los cursos pertenecen a la rama de diseño,algunos de TI, sin embargo, lo más llamativo es su escala en el eje x, de entre los 10 cursos con menor precio (incluídos aquellos que son gratuitos) el que mayor número de inscritos tienes es de 12 mil. Muy diferentes a comparación de los cursos de paga. Esto puede justificar el comportamiento del KPI tasa de conversión donde se confirmó que los cursos pagados captan mayor número de inscritos en comparación con los gratuitos.')

    if st.checkbox('Selección de precios a evaluar'):
        # Obtener el rango de precios utilizando un st.slider
        precio_minimo = st.slider('Precio mínimo', min_value=0, max_value=450, value=0)
        precio_maximo = st.slider('Precio máximo', min_value=0, max_value=450, value=450)

        # Filtrar los cursos dentro del rango de precios
        cursos_filtrados_pre = df_mezcla[(df_mezcla['Precio'] >= precio_minimo) & (df_mezcla['Precio'] <= precio_maximo)]

        # Ordenar los cursos por el número de inscritos de forma descendente
        cursos_filtrados=cursos_filtrados_pre.head(10)
        cursos_filtrados = cursos_filtrados.sort_values('Inscritos', ascending=True)

        # Crear el gráfico de barras
        fig = plt.figure(figsize=(10, 6))
        plt.barh(cursos_filtrados['Curso'], cursos_filtrados['Inscritos'], color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Inscritos')
        plt.ylabel('Curso')
        plt.title('Cursos con Mayor Precio dentro del rango arbitrario y sus Inscritos (Ordenado por Inscritos)')

        st.write('El siguiente gráfico filtra los datos de acuerdo a los límites brindados tomando los 10 con mayor precio, posteriormente organiza los cursos de mayor cantidad de inscritos a menor')
        st.write('En caso de haber cursos con 0 inscritos, significa que tienen un precio elevado entre los límites establecidos pero tiene 0 personas inscritas')
        # Mostrar el gráfico
        st.pyplot(fig)

if filtro=='Idioma':

    # Obtener los idiomas únicos del DataFrame df_ec['language']
    idiomas_disponibles = df_ec['language'].unique()

    # Permitir que el usuario seleccione los idiomas a graficar usando st.multiselect
    idiomas_seleccionados = st.multiselect('Selecciona los idiomas:', idiomas_disponibles,default=['English','Español'])

    # Filtrar el DataFrame original según los idiomas seleccionados
    df_filtrado = df_ec[df_ec['language'].isin(idiomas_seleccionados)]

    # Agrupar los datos filtrados por 'language' y calcular la suma de 'n_enrolled'
    grouped_data = df_filtrado.groupby('language')['n_enrolled'].sum().reset_index()

    # Ordenar los datos por 'n_enrolled' de forma descendente
    grouped_data = grouped_data.sort_values('n_enrolled', ascending=False)

    # Crear el gráfico de barras
    fig = plt.figure(figsize=(10, 6))
    plt.bar(grouped_data['language'], grouped_data['n_enrolled'], color='red')

    # Etiquetas y título del gráfico
    plt.xlabel('Idiomas')
    plt.ylabel('Log del número de alumnado inscrito')
    plt.title('Top 4 Idiomas con mayor cantidad de ventas en Edx')

    # Escala logarítmica en el eje y
    plt.yscale('log')

    # Mostrar el gráfico
    st.pyplot(fig)

    st.write('* Conclusión del Gráfico de Barras de los Idiomas con más cursos vendidos en Edx')
    st.write('El idioma inglés es sustancialmente mayor a los demás idiomas, la escala logarítmica se aplica para facilitar la visualización de valores más pequeños como los otros 3 idiomas. Con base en el fundamento del idioma universal, el inglés parece ser el idioma predilecto para tener un curso disponible en línea. ')

if filtro=='Nivel':
    if st.checkbox('Niveles en Udemy'):

        # Obtener los niveles únicos en el DataFrame
        niveles_disponibles = df_uc['level'].unique()

        # Selección de niveles con st.multiselect
        niveles_seleccionados = st.multiselect('Seleccionar niveles', niveles_disponibles, default=niveles_disponibles)

        # Filtrar el DataFrame original según los niveles seleccionados
        df_filtrado = df_uc[df_uc['level'].isin(niveles_seleccionados)]

        # Agrupar los datos por 'level' y calcular la suma de 'num_subscribers'
        grouped_data = df_filtrado.groupby('level')['num_subscribers'].sum().reset_index()

        # Ordenar los datos por 'num_subscribers' de forma descendente
        grouped_data = grouped_data.sort_values('num_subscribers', ascending=False)
        
        # Crear el gráfico de pie
        fig=plt.figure(figsize=(12, 8))
        colors = ['#d62728','#1f77b4', '#ff7f0e', '#2ca02c']  # Colores por default de python
        plt.pie(grouped_data['num_subscribers'], labels=grouped_data['level'], autopct='%1.1f%%',colors=colors)

        # Título del gráfico
        plt.title('Porcentaje de alumnos inscritos por nivel en Udemy')

        # Mostrar el gráfico
        st.pyplot(fig)

        #mostrar df
        # Cambiar el nombre de las columnas
        grouped_data.columns = ['Nivel', 'Inscritos']
        st.dataframe(grouped_data)
        st.write('* Conclusión de Gráfico de Barras de cantidad de alumnados por nivel en Udemy')
        st.write('La cantidad de alumnado por nivel es muy diferente, siendo el All Levels el nivel predominante, mientrás que Expert Level es significativamente inferior. Esto corresponde a la ley de oferta y demanda, la cantidad de cursos ofertados de All Levels son algo ambíguos, pero al haber una mayor cantidad de cursos de niveles introductorios, el alumnado inscrito en ellos es superior al de niveles avanzados. También esto pueda deberse a que cuando se accede a niveles de conocimiento más avanzados se buscan sitios más especializados en la materia como universidades convencionales o clubes del área. ')

    if st.checkbox('Niveles en Edx'):
        # Obtener los niveles únicos en el DataFrame
        niveles_disponibles = df_ec['Level'].unique()

        # Selección de niveles con st.multiselect
        niveles_seleccionados = st.multiselect('Seleccionar niveles', niveles_disponibles, default=niveles_disponibles)

        # Filtrar el DataFrame original según los niveles seleccionados
        df_filtrado = df_ec[df_ec['Level'].isin(niveles_seleccionados)]
        
        # Agrupar los datos por 'Level' y calcular la suma de 'n_enrolled'
        grouped_data = df_filtrado.groupby('Level')['n_enrolled'].sum().reset_index()

        # Ordenar los datos por 'n_enrolled' de forma descendente
        grouped_data = grouped_data.sort_values('n_enrolled', ascending=False)

        # Crear el gráfico de pie
        fig=plt.figure(figsize=(10, 6))
        plt.pie(grouped_data['n_enrolled'], labels=grouped_data['Level'], autopct='%1.1f%%')

        # Título del gráfico
        plt.title('Porcentaje de alumnado inscrito por Nivel en Edx')

        # Mostrar el gráfico
        st.pyplot(fig)
        grouped_data.columns = ['Nivel', 'Inscritos']
        st.dataframe(grouped_data)
        st.write('* Conclusión de cantidad de alumnado inscrito por nivel en Edx')
        st.write('Los niveles introductorios acaparan la mayor cantidad de alumnos inscritos en la plataforma, alrededor de un 1/5 de los alumnos inscritos pertenecen a cursos intermedios y unicamente un 6% a cursos avanzados. Esta información es también congruente con la cantidad de cursos ofertados por la plataforma donde se observa que la mayoría son de nivel introductorio. ')

if filtro=='Rating':
    st.write('Nota: Para la generación de los gráficos se utilizaron aquellos cursos que tuvieron un número de consumidores (entendiéndose como número de reviews obtenidos) mayor a 1071 siendo la mediana de esta variable, es decir, se tomaron en consideración aquellos cursos con mayor o menor rating que superarán las 1071 revisiones.')
    if st.checkbox('Top 10 Cursos con Mayor Rating en Coursera'):
        top_cursos = cursos_filtrados.head(10)
        top_cursos = top_cursos.sort_values('num_ratings', ascending=True)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.barh(top_cursos['name'], top_cursos['num_ratings'],color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Alumnado Inscrito')
        plt.ylabel('Curso')
        plt.title('Top 10 Cursos con Rating más alto y Número de calificaciones mayor a 1071 (mediana del conjunto)')

        # Mostrar el gráfico
        st.write('El siguiente gráfico filtra los datos de acuerdo a los límites brindados tomando los 10 con mayor rating, posteriormente organiza los cursos de mayor cantidad de inscritos a menor')
        st.write('En caso de haber cursos con 0 inscritos, significa que tienen un rating elevado entre los límites establecidos pero tiene 0 personas inscritas')
        st.pyplot(fig)
        st.write('* Conclusión de Cursos con mayor calificación')
        st.write('Se observa que los cursos tienen una diversidad de temáticas, algunas se enfocan en ciencias biológicas como la neurobiología, otras en estudios de pinturas enfocadas a épocas postguerra y alguna a lenguajes de programación. La información concluyente del gráfico afirma que existe una gran atracción hacia cursos enfocadas en humanidades en la plataforma de Coursera siendo calificado bastante alto y teniendo una gran cantidad de alumnado más del doble con el segundo lugar. ')
    if st.checkbox('Top 10 Cursos con Menor Rating en Coursera'):
        top_cursos = cursos_filtrados.tail(10)
        top_cursos = top_cursos.sort_values('num_ratings', ascending=False)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.barh(top_cursos['name'], top_cursos['num_ratings'],color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Número de Inscritos')
        plt.ylabel('Curso')
        plt.title('Top 10 Cursos con Rating más bajo y Número de calificaciones mayor a 1071 (mediana del conjunto)')

        # Mostrar el gráfico
        st.pyplot(fig)
        st.write('* Conclusiones de Cursos con menor rating')
        st.write('Es notable la presencia de un curso con un nombre que utiliza carácteres disitntos al español e inglés llamando la atención por ser un curso que tiene más de 1071 revisiones pero que tiene un rating que lo ubica entre los peores 10 cursos de Coursera, también es notable la presencia de cursos enfocados en tecnologías, por la presencia de Data Visualization with Python, Convolutional Neural Networks, Tools for Data Science, entre otros, para este último a pesar de ubicarse entre los cursos con menor calificación de Coursera, la cantidad de inscritos es bastante alta de 8000, ignorando este caso aíslado, la información indica que los cursos que obtienen una menor calificación tienen pocos inscritos en comparación a aquellos que tienen una calificación más alta, visible de forma sencilla por la escala presente en los ejes x de los gráficos.')

    if st.checkbox('Selección de ratings a evaluar'):
        # Obtener el rango de precios utilizando un st.slider
        rating_minimo = st.slider('Rating Mínimo', min_value=1, max_value=5, value=1)
        rating_maximo = st.slider('Precio máximo', min_value=1, max_value=5, value=5)

        # Filtrar los cursos dentro del rango de precios
        cursos_filtrados_pre = cursos_filtrados[(cursos_filtrados['media_rating'] >= rating_minimo) & (cursos_filtrados['media_rating'] <= rating_maximo)]
        top_cursos=cursos_filtrados_pre.head(10)
        top_cursos = top_cursos.sort_values('num_ratings', ascending=True)

        # Crear el gráfico de barras
        fig=plt.figure(figsize=(10, 6))
        plt.barh(top_cursos['name'], top_cursos['num_ratings'],color='red')

        # Etiquetas y título del gráfico
        plt.xlabel('Número de Inscritos')
        plt.ylabel('Curso')
        plt.title('Top 10 Cursos con el rating establecido y Número de calificaciones mayor a 1071 (mediana del conjunto)')

        # Mostrar el gráfico
        st.pyplot(fig)

#########
st.write('### Top 5 Cursos más calificados de Coursera')
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
plt.title('Los 5 Cursos con mayor número de calificaciones en Coursera')

# Etiquetas del eje x
plt.xlabel('ID del Curso')
plt.xticks(rotation=45, ha='right') 

# Etiquetas del eje y
plt.ylabel('Número de Calificaciones')

# Mostrar el gráfico
st.pyplot(fig)
st.write('* Conclusiones del Gráfico de Columnas de los cursos más calificados de Coursera:')
st.write('Se observa la presencia predominante de tópicos enfocados en TI como python, python-data, machine-learning y deep learning. Con base en lo anterior, ante la falta de una variable subscriptores en Coursera y entendiendose como aquellas personas que calificaron el curso sean únicamente consumidores del producto, podemos aseverar que los cursos TI en Coursera tienen una mayor demanda en comparación a otros tópicos. ')

##########
st.write('### Gráfica de Barras de Temática contra Ingreso promedio por curso en Udemy')

# Calcular el promedio de ingreso por curso por cada categoría de 'subject'
avg_income_by_subject = df_uc.groupby('subject')['ingreso_por_curso'].mean().reset_index()

# Obtener las categorías únicas de 'subject'
categorias_subject = avg_income_by_subject['subject'].tolist()

# Multiselect para que el usuario seleccione una o varias categorías
categorias_seleccionadas = st.multiselect("Seleccione la(s) temática(s) que desee analizar", categorias_subject,default=['Web Development'])

# Crear una lista de colores personalizada
colores = ['red' if categoria in categorias_seleccionadas else 'gray' for categoria in categorias_subject]

# Crear el gráfico de barras con colores personalizados
fig = plt.figure(figsize=(12, 6))
sns.barplot(data=avg_income_by_subject, x='subject', y='ingreso_por_curso', palette=colores)

# Cambiar las etiquetas de los ejes
plt.xlabel('Temática')
plt.ylabel('Ingreso Promedio por Curso (USD)')

# Título del gráfico
plt.title('Promedio de Ingreso por Curso por Temática en Udemy')

# Mostrar el gráfico
st.pyplot(fig)
st.write('* Conclusiones del Gráfico de Columnas de Promedio de Ingreso por Curso y Temática')
st.write('Se observa que los cursos enfocados en Web Development generan un mayor ingreso promedio, muy por encima de los otros subject, siguiendo por debajo Graphic Design a pesar de que Business Finance es el segundo con mayor presencia en Udemy. ')
##########
st.write('### Diagrama de Columnas del Ingreso Promedio por curso y el nivel del mismo')
col3,col4=st.columns(2)
with col3:
    # Crear la gráfica de barras
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=df_ec, x='Level', y='ingreso_por_curso', errorbar=None)

    # Configurar los ejes y el título
    plt.xlabel('Nivel de Curso')
    plt.ylabel('Ingreso Promedio por Curso (USD)')
    plt.title('Diagrama de Columnas de Ingreso por Curso de acuerdo al Nivel en Edx')

    # Mostrar la gráfica
    st.pyplot(fig)

with col4:
    # Filtrar las filas con nivel diferente a 'All Levels'
    filtered_df_uc = df_uc[df_uc['level'] != 'All Levels']

    # Calcular el promedio de ingreso por curso por cada categoría de 'subject'
    avg_income_by_level = filtered_df_uc.groupby('level')['ingreso_por_curso'].mean().reset_index()
    fig=plt.figure(figsize=(12, 6))

    # Crear el diagrama de barras
    sns.barplot(data=avg_income_by_level, x='level', y='ingreso_por_curso',order=['Beginner Level','Intermediate Level','Expert Level'])

    # Título del gráfico
    plt.title('Promedio de Ingreso por Curso por Categoría de Nivel en Udemy')
    plt.xlabel('Nivel del Curso')
    plt.ylabel('Ingreso Promedio por Curso (USD)')


    # Mostrar el gráfico
    st.pyplot(fig)
st.write('* Conclusiones de Gráficas de acuerdo a Nivel')
st.write('En la gráfica de la izquierda perteneciente a Edx se observa que el ingreso promedio por curso es bastante mayor en cursos nivel avanzado que otros niveles, por otra parte, en la veficación de Udemy, aquel que genera mayor ingreso promedio son los de nivel introductorio, sin embargo, al momento de evaluar el impacto en conjunto de ambos en el desempeño del KPI, se observa que las ganancias generadas por cursos avanzados son sustancialmente mayores')
st.write('Nota: Para la evaluación de Udemy se retiró aquellos cursos con nivel All Levels para simplificar el análisis, debido a la ambigüedad del valor')

#########
st.write('### Cantidad e Ingreso por curso a partir de la segmentación de los cursos en intérvalos de esfuerzo total (horas totales)')
col1,col2=st.columns(2)
with col1:
    # Definir los límites de los grupos
    bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 100, float('inf')]

    # Crear las categorías a partir de los límites
    categories = pd.cut(df_ec['esfuerzo_total'], bins=bin_edges)

    # Agregar las categorías al DataFrame
    df_ec['esfuerzo_group'] = categories

    # Ordenar los grupos de esfuerzo de menor a mayor
    order = sorted(df_ec['esfuerzo_group'].unique())

    # Crear el diagrama de barras con el orden especificado
    fig = plt.figure(figsize=(10, 6))

    # Obtener la paleta de colores con los tonos grises
    color_palette = sns.color_palette('Greys', len(order))

    # Definir los colores para las últimas dos barras
    color_palette[-2:] = ['red', 'red']

    # Crear el gráfico de barras con la paleta de colores
    sns.countplot(data=df_ec, x='esfuerzo_group', order=order, palette=color_palette)

    # Título del gráfico
    plt.title('Distribución del Esfuerzo Total')

    # Etiquetas de los ejes
    plt.xlabel('Grupo de Esfuerzo')
    plt.ylabel('Cantidad')

    # Rotar las etiquetas del eje x para mayor legibilidad
    plt.xticks(rotation=45)

    # Mostrar el gráfico
    st.pyplot(fig)
with col2:
    grupo_ingreso = df_ec.groupby('esfuerzo_group_str')['ingreso_por_curso'].mean()
    grupo_ingreso = grupo_ingreso.sort_values().reset_index()

    # Renombrar la columna de los índices
    grupo_ingreso = grupo_ingreso.rename(columns={'esfuerzo_total_group': 'esfuerzo_total_group'})

    grupo_ingreso.iloc[[2, 3]] = grupo_ingreso.iloc[[3, 2]]
    grupo_ingreso.iloc[[5, 7]] = grupo_ingreso.iloc[[7, 5]]
    grupo_ingreso.iloc[[6, 7]] = grupo_ingreso.iloc[[7, 6]]
    grupo_ingreso.iloc[[8, 9]] = grupo_ingreso.iloc[[9, 8]]

    # Definir la lista de colores para cada columna en el gráfico de columnas
    colores = sns.color_palette('Greys', len(grupo_ingreso))

    # Definir los colores para las últimas dos barras
    colores[-2:] = ['red', 'red']

    # Crear el gráfico de columnas con la paleta de colores
    fig = plt.figure(figsize=(10, 6))
    plt.bar(grupo_ingreso['esfuerzo_group_str'], grupo_ingreso['ingreso_por_curso'], color=colores)

    # Etiquetas y título del gráfico
    plt.xlabel('Grupos de Esfuerzo')
    plt.ylabel('Ingreso promedio por curso (USD)')
    plt.title('Diagrama de Columnas: Ingreso promedio por Curso contra Esfuerzo total (en horas)')

    # Rotar las etiquetas del eje x a 90 grados
    plt.xticks(rotation=45)

    # Mostrar el gráfico
    st.pyplot(fig)
st.write('* Conclusión de gráficas de esfuerzo total')
st.write('La cantidad de cursos baja considerablemente al aumentar el tiempo de esfuerzo total medido en h, sin embargo, el ingreso por curso resulta ser sustancialmente mayor en cursos largos (mayores a 80 h totales)')

st.markdown('***')

st.markdown('# Conclusión')
st.write('Las características que precisan un mayor desempeño para la longitud de un curso, son aquellos que resultan ser más extensos, esto es posible debido a la seguridad de encontrar información por parte del consumidor, distinto a la idea inicial de un contenido más ligero. Se espera que cursos largos, puedan brindar una mayor perspectiva, también cabe resaltar que cursos brindados por empresas como Google y IBM son ofertados en algunas plataformas de las analizadas, mismas que te capacitan para ejercer como analista de datos mediante un curso intensivo de 6 meses, siendo uno de los más populares del áreas para la preparación profesional. Por otra parte, la evaluación del KPI de tasa de conversión de suscritos es útil para evaluar la fidelidad del cliente, debido a la tendencia de consumidores de contenido de gratis es a casi no terminar el producto mientras que la existencia de un intercambio comercial por él, asegura fidelidad y esto aumenta la posibilidad de consumir un segundo curso. Los cursos que parecen ser más eficientes en términos de alumnos inscritos son los de TI como Web Development o Data Analysis, mismos que sobrepasan a otras temáticas casi 500%. Para concluir, la evaluación del nivel a pesar de tener una hipótesis inicial de cursos introductorios, parece que la oferta tiende a contar con una gran cantidad de cursos para principiantes disponibles en múltiples plataformas, mientras que la oferta de contenido especializado es más escasa y por ello, es posible que la demanda sea alta, asegurando un pago consideradable por ese contenido comprobado por el ingreso por curso.')
st.write('Se puede concluir que la mejor combinación de inversión en cursos serían aquellos de temática de TI, con una duración larga mayor a 80 h en total de contenido siendo posible percibir ganancias a partir de la subscripción a él.')


st.markdown('***')

st.markdown('# Invitación')
st.write('En la parte izquierda de esta página se encuentran los análisis detallados de cada gráfica de las diferentes plataformas utilizadas para construir este análisis, te invito a revisar la información.')