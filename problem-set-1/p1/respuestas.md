# Problem Set 1

## Parte 1

### Análisis de Michelangelo desde CRISP-DM y Martínez-Plumed et al. (2019)

La plataforma Michelangelo de Uber puede explicarse en gran parte mediante CRISP-DM, metodología que organiza los proyectos de minería de datos en seis fases: entendimiento del negocio, entendimiento de los datos, preparación de los datos, modelamiento, evaluación y despliegue. En el caso de UberEATS, por ejemplo, se parte de un objetivo de negocio concreto: predecir el tiempo de preparación y entrega de una orden. A partir de ello, Michelangelo administra datos históricos y en tiempo casi real, utiliza pipelines y un Feature Store, entrena distintos modelos, compara sus resultados y finalmente los despliega en producción.

Las fases de modelamiento, evaluación y despliegue también están claramente representadas. Michelangelo permite definir hiperparámetros, probar múltiples configuraciones, generar métricas de desempeño y seleccionar los mejores modelos. Luego, estos pueden ser desplegados para predicciones *online* u *offline*. Además, la plataforma monitorea continuamente el desempeño de los modelos en producción, lo que se relaciona con la etapa de mantenimiento contemplada en CRISP-DM.

Sin embargo, CRISP-DM no explica completamente una plataforma moderna como Michelangelo. Martínez-Plumed et al. (2019) señalan que los proyectos actuales de ciencia de datos son más exploratorios y flexibles, por lo que proponen el modelo Data Science Trajectories (DST). Este amplía CRISP-DM mediante actividades de exploración de objetivos, fuentes de datos, valor de los datos, resultados y productos, además de actividades de gestión de datos.

Esta perspectiva permite entender mejor la evolución de Michelangelo. Uber no solo desarrolla modelos para problemas ya definidos, sino que también explora nuevas aplicaciones de Machine Learning, prioriza proyectos según su impacto en el negocio y analiza qué datos o características pueden generar mayor valor. Asimismo, Michelangelo incorpora infraestructura para gestionar datos, características, modelos y metadatos de manera continua, además de herramientas como control de versiones, CI/CD, reentrenamiento y monitoreo.

En conclusión, CRISP-DM permite explicar el flujo principal de Michelangelo, desde la definición del problema hasta el despliegue del modelo**, mientras que la propuesta de **Martínez-Plumed permite comprender mejor sus componentes exploratorios, su gestión continua de datos y su carácter iterativo y flexible.
