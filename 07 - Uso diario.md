# 07 - Uso diario

Este documento explica cómo utilizar Chatterbox después de completar toda la instalación.

Si todavía no has terminado la instalación, completa primero:

```text
01_REQUISITOS.md
02_INSTALAR_WSL.md
03_PREPARAR_ENTORNO.md
04_INSTALAR_CHATTERBOX.md
05_PREPARAR_VOZ.md
06_INSTALAR_LANZADOR.md
```

Una vez configurado todo, no necesitas abrir Ubuntu ni escribir comandos para generar una narración.

---

# 1. Preparar el guion

Guarda el texto que quieres convertir a voz en un archivo:

```text
.txt
```

Por ejemplo:

```text
guion_video.txt
```

Puedes guardarlo en cualquier carpeta de Windows.

No es necesario copiarlo dentro del repositorio.

---

# 2. Formato recomendado del guion

Puedes utilizar texto normal:

```text
Esta es la primera idea del vídeo.

Después continúa la explicación.

Finalmente llega la siguiente parte.
```

También puedes conservar timestamps:

```text
[0:00–0:45]

Texto correspondiente a la primera parte.

[0:45–1:30]

Texto correspondiente a la segunda parte.
```

El generador reconoce líneas con este formato:

```text
[0:00–0:45]
```

y no las envía a Chatterbox como texto hablado.

Los timestamps sirven únicamente para organizar el guion.

No obligan al modelo a producir exactamente esa duración.

---

# 3. Preparar el texto para TTS

Chatterbox puede leer un texto normal, pero la puntuación influye bastante en:

- velocidad;
- respiraciones;
- pausas;
- intención;
- naturalidad.

Por ejemplo:

```text
Ya sabes lo que ocurre. Lo has visto antes. Aun así, sigues adelante.
```

puede tener un ritmo diferente a:

```text
Ya sabes lo que ocurre... Lo has visto antes... Aun así, sigues adelante.
```

No es necesario llenar el guion de puntos suspensivos.

Utilízalos únicamente cuando tenga sentido dejar una pausa perceptible.

Las comas también pueden ayudar a que una frase larga no se lea demasiado seguida.

---

# 4. No intentes controlar la duración exacta con puntuación

La puntuación puede modificar ligeramente el ritmo, pero no debe utilizarse para intentar transformar artificialmente:

```text
30 segundos
```

en:

```text
50 segundos
```

Si se fuerza demasiado, la lectura puede sonar:

- artificial;
- exageradamente dramática;
- entrecortada;
- poco natural.

El objetivo es mejorar el ritmo y la naturalidad, no alcanzar una duración matemática.

---

# 5. Ejecutar el programa

Abre la carpeta:

```text
chatterbox-local-tts-windows
```

y haz doble clic en:

```text
Generar voz.bat
```

No necesitas:

- abrir PowerShell;
- abrir Ubuntu;
- activar Conda;
- ejecutar Python manualmente.

---

# 6. Seleccionar el guion

Aparecerá una ventana para elegir un archivo.

Selecciona el `.txt` que quieras convertir a voz.

Por ejemplo:

```text
guion_video.txt
```

Si cancelas esta ventana, el programa se cerrará sin generar nada.

---

# 7. Seleccionar la voz

Si existe:

```text
voces/voz_predeterminada.mp3
```

el programa preguntará si quieres utilizarla.

Pulsa:

```text
Sí
```

para utilizar la voz predeterminada.

Pulsa:

```text
No
```

para elegir otra referencia.

---

# 8. Utilizar otra voz

Puedes seleccionar cualquier archivo compatible:

```text
.mp3
.wav
```

No es necesario copiar previamente esa voz dentro de:

```text
voces/
```

El selector puede abrir un archivo situado en cualquier carpeta de Windows.

El lanzador convertirá automáticamente esa ruta para que WSL pueda utilizarla.

---

# 9. Qué ocurre después

Después de seleccionar guion y voz aparecerá la consola.

Verás algo parecido a:

```text
========================================
 CHATTERBOX LOCAL TTS
========================================
```

El programa mostrará información como:

```text
Guion:
...

Voz:
...

Generando...
```

Después Chatterbox cargará los modelos.

---

# 10. Carga del modelo

Cada nueva ejecución necesita cargar Chatterbox en memoria.

Puedes ver mensajes como:

```text
Fetching files
loaded PerthNet
```

o diferentes avisos de Python.

Si la generación continúa, no cierres la ventana.

---

# 11. Generación por bloques

Un guion largo no se envía completo a Chatterbox.

El programa lo divide automáticamente en bloques.

La configuración inicial utiliza aproximadamente:

```text
TARGET_CHARS = 500
HARD_MAX = 650
```

El programa intenta mantener frases completas.

Durante la generación verás:

```text
[1/8]
Texto del bloque...
```

después:

```text
[2/8]
Texto del bloque...
```

y así sucesivamente.

---

# 12. Barra `Sampling`

Durante cada bloque aparecerá:

```text
Sampling:
```

seguido de una barra de progreso.

Por ejemplo:

```text
Sampling: 57% ...
```

Es normal.

No representa el porcentaje total del guion.

Representa la generación del bloque actual.

---

# 13. Tiempo de espera

Esta configuración utiliza CPU.

Por tanto, la generación no es en tiempo real.

Es normal que:

```text
30 segundos de audio
```

necesiten bastante más de:

```text
30 segundos de cálculo
```

Un guion de varios minutos puede tardar muchos minutos en terminar.

Mientras la barra de `Sampling` avance, el programa sigue funcionando.

---

# 14. No cierres la ventana

No cierres la consola mientras Chatterbox esté generando.

Espera hasta ver:

```text
LISTO
```

Si cierras la ventana antes, la generación se interrumpirá.

---

# 15. Archivo final

Cuando termine, el programa crea un único:

```text
.wav
```

dentro de:

```text
salidas/
```

El nombre se basa en el archivo del guion.

Por ejemplo:

```text
guion_video.txt
```

produce:

```text
guion_video_voz.wav
```

---

# 16. La carpeta se abre automáticamente

Cuando la generación termina correctamente, Windows abre:

```text
salidas/
```

automáticamente.

Ahí encontrarás el WAV terminado.

---

# 17. Archivos temporales

Durante la generación se utilizan archivos internos dentro de WSL.

Se almacenan temporalmente en:

```text
~/ChatterboxES/temp_generacion/
```

Cuando todo termina correctamente, el programa elimina esa carpeta.

Normalmente no tendrás que verla ni gestionarla.

---

# 18. Si vuelves a generar el mismo guion

Si utilizas otra vez:

```text
guion_video.txt
```

la salida volverá a llamarse:

```text
guion_video_voz.wav
```

La nueva generación puede sustituir la anterior.

Si quieres conservar varias versiones, puedes:

- renombrar el guion;
- renombrar el WAV anterior;
- mover el WAV anterior antes de generar de nuevo.

---

# 19. Reproducibilidad

El generador utiliza una seed controlada:

```text
BASE_SEED = 12345
```

Cada bloque utiliza una seed derivada de esa base.

Esto ayuda a mantener cierto grado de reproducibilidad.

Aun así, cambios en:

- texto;
- puntuación;
- tamaño de bloques;
- modelo;
- dependencias;
- voz;
- parámetros;

pueden producir diferencias audibles.

---

# 20. Configuración inicial de voz

En:

```text
generar_guion.py
```

la configuración inicial es:

```python
EXAGGERATION = 0.70
CFG_WEIGHT = 0.20
TEMPERATURE = 0.80
```

Esta configuración sirve como punto de partida.

No significa que sea la mejor para todas las voces.

---

# 21. Cambiar los parámetros

Si quieres probar otra configuración, abre:

```text
generar_guion.py
```

con Visual Studio Code.

Busca:

```python
EXAGGERATION = 0.70
CFG_WEIGHT = 0.20
TEMPERATURE = 0.80
```

Modifica únicamente los números.

Por ejemplo:

```python
EXAGGERATION = 0.70
CFG_WEIGHT = 0.30
TEMPERATURE = 0.80
```

Guarda el archivo.

La próxima generación utilizará esos valores.

---

# 22. Cambia un parámetro cada vez

Si estás buscando una voz mejor, evita modificar simultáneamente:

```text
Exaggeration
CFG
Temperature
```

Es mejor:

1. conservar el mismo texto;
2. conservar la misma voz;
3. cambiar un solo valor;
4. generar una prueba corta;
5. comparar.

Así podrás identificar qué parámetro produjo realmente el cambio.

---

# 23. Utiliza textos cortos para probar configuraciones

No generes un guion completo cada vez que quieras comparar parámetros.

Crea un `.txt` corto con varias frases representativas.

Por ejemplo:

```text
Esta es una prueba de voz.

Quiero comprobar el ritmo, la entonación y la naturalidad.

También quiero escuchar cómo termina una frase un poco más larga.
```

Genera ese archivo varias veces cambiando únicamente el parámetro que quieras comparar.

Cuando encuentres una configuración que te guste, úsala con el guion completo.

---

# 24. Exaggeration

El parámetro:

```text
EXAGGERATION
```

afecta a la expresividad de la generación.

Valores más altos pueden producir una interpretación más marcada.

También pueden modificar:

- ritmo;
- estabilidad;
- energía;
- entonación.

No asumas que:

```text
más alto = mejor
```

Comprueba siempre el resultado escuchándolo.

---

# 25. CFG

El parámetro:

```text
CFG_WEIGHT
```

puede influir en:

- ritmo;
- estabilidad;
- carácter de la voz;
- forma de interpretar el texto.

No existe un valor universal.

Una pequeña modificación puede cambiar el resultado de forma audible.

---

# 26. Temperature

El parámetro:

```text
TEMPERATURE
```

afecta a la variabilidad de la generación.

Valores diferentes pueden modificar:

- entonación;
- estabilidad;
- pronunciación;
- expresividad.

Si una configuración ya funciona bien, no es necesario modificarla continuamente.

---

# 27. Tamaño de los bloques

El generador utiliza:

```python
TARGET_CHARS = 500
HARD_MAX = 650
```

Esto no significa que Chatterbox tenga un límite real de 500 o 650 caracteres.

Son valores elegidos para dividir narraciones largas en fragmentos manejables.

El programa agrupa varias frases para dar al modelo suficiente contexto.

Esto ayuda a conservar:

- continuidad;
- ritmo;
- intención.

---

# 28. No reduzcas demasiado los bloques

Una frase corta generada de forma independiente puede sonar muy bien.

Sin embargo, generar cada frase por separado puede provocar:

- cambios de timbre;
- diferencias de volumen;
- entonación inconsistente;
- sensación de audio pegado;
- falta de continuidad.

Por eso el programa intenta trabajar con bloques relativamente largos.

---

# 29. Tampoco utilices bloques excesivamente largos

Enviar varios minutos completos en una sola generación puede aumentar la posibilidad de:

- cambios extraños de voz;
- ritmo irregular;
- degradación al final;
- pronunciaciones inesperadas;
- resultados menos consistentes.

La configuración incluida busca un equilibrio entre contexto y estabilidad.

---

# 30. Pausas entre bloques

El generador añade pequeñas pausas automáticamente.

Configuración inicial:

```python
PAUSA_NORMAL = 0.28
PAUSA_SECCION = 0.70
```

`PAUSA_NORMAL` se utiliza entre bloques pertenecientes a una misma sección.

`PAUSA_SECCION` se utiliza cuando termina una sección marcada por timestamps.

---

# 31. Cambiar las pausas

Puedes modificar estos valores dentro de:

```text
generar_guion.py
```

Por ejemplo:

```python
PAUSA_NORMAL = 0.35
PAUSA_SECCION = 0.80
```

No utilices pausas enormes para compensar un guion demasiado corto.

Un exceso de silencios puede hacer que la narración parezca artificial.

---

# 32. Voz buena en pruebas cortas pero peor en textos largos

Puede ocurrir que una prueba de pocos segundos suene mejor que una narración de varios minutos.

Esto no significa necesariamente que la instalación esté mal.

Las generaciones largas son más difíciles de mantener consistentes.

El sistema de bloques intenta reducir ese problema, pero no puede eliminarlo completamente.

---

# 33. Si un tramo sale raro

Si únicamente una pequeña parte del audio tiene:

- entonación extraña;
- pronunciación mala;
- cambio de timbre;
- ritmo extraño;

puedes generar nuevamente el guion.

Una nueva generación puede producir una interpretación diferente.

Si el problema ocurre siempre en la misma frase, revisa primero:

- puntuación;
- longitud de la frase;
- signos de interrogación;
- comas;
- puntos;
- puntos suspensivos.

---

# 34. Si una palabra se pronuncia mal

Antes de modificar parámetros generales, prueba a revisar la puntuación alrededor de esa palabra o frase.

Los siguientes elementos pueden ser especialmente variables:

- nombres propios;
- siglas;
- palabras inglesas;
- términos técnicos;
- nombres inventados;
- palabras poco frecuentes.

No cambies la ortografía correcta sin comprobar antes que sea necesario.

---

# 35. Si habla demasiado rápido

Primero revisa:

- frases demasiado largas;
- falta de comas;
- falta de puntos;
- falta de pausas naturales;
- fragmentos demasiado densos.

Una frase como:

```text
Todo ocurre muy rápido y cuando intentas reaccionar ya ha empezado la siguiente parte.
```

puede recibir más estructura:

```text
Todo ocurre muy rápido... y cuando intentas reaccionar, ya ha empezado la siguiente parte.
```

El objetivo es orientar mejor la lectura, no llenar el texto de signos.

---

# 36. Si necesitas una duración concreta

Chatterbox no está diseñado en esta configuración para garantizar:

```text
un bloque de texto = exactamente X segundos
```

Si necesitas sincronización con vídeo, las opciones más seguras son:

- adaptar la cantidad de texto;
- ajustar el montaje;
- insertar pausas naturales;
- colocar la narración dentro del editor;
- modificar ligeramente la estructura del guion.

Evita ralentizar agresivamente el WAV terminado.

Puede degradar mucho la naturalidad.

---

# 37. Preparar el guion específicamente para TTS

Puede ser útil tener dos versiones del mismo contenido:

```text
Guion normal
        ↓
Guion preparado para TTS
        ↓
Chatterbox
```

La versión preparada para TTS puede modificar únicamente:

- puntuación;
- comas;
- puntos;
- puntos suspensivos;
- interrogaciones;
- exclamaciones;
- saltos de línea;

sin alterar necesariamente las palabras.

Esto ayuda a conservar el contenido mientras se ofrecen mejores señales de ritmo al sintetizador.

---

# 38. Los saltos de línea no son suficientes

El generador procesa el texto principalmente utilizando:

- timestamps;
- frases;
- puntuación;
- tamaño del bloque.

Los saltos de línea ayudan a organizar el guion para una persona, pero no deben ser la única forma de indicar pausas.

Si una pausa es importante, utiliza también una puntuación adecuada.

---

# 39. Cambiar permanentemente la voz predeterminada

Para cambiar la voz utilizada cuando seleccionas:

```text
Sí
```

en la pregunta de voz predeterminada:

1. abre:

```text
voces/
```

2. elimina o mueve la referencia anterior;

3. coloca la nueva referencia;

4. llámala:

```text
voz_predeterminada.mp3
```

La próxima generación utilizará esa referencia.

---

# 40. Probar otra voz sin hacerla predeterminada

No necesitas renombrar el archivo.

Ejecuta:

```text
Generar voz.bat
```

Cuando pregunte por la voz predeterminada, selecciona:

```text
No
```

y elige el nuevo:

```text
.mp3
```

o:

```text
.wav
```

---

# 41. No es necesario reinstalar nada al cambiar de voz

Cada ejecución del BAT inicia una generación nueva.

Puedes utilizar una referencia diferente en cada ejecución.

No necesitas:

- reinstalar Chatterbox;
- descargar de nuevo el modelo;
- recrear el entorno;
- modificar WSL.

---

# 42. Organización de las salidas

La carpeta:

```text
salidas/
```

puede llenarse con el tiempo.

Puedes mover los WAV terminados a las carpetas donde organices tus proyectos.

No es necesario conservar todos los resultados dentro del repositorio.

---

# 43. No subas archivos personales a GitHub

Nunca hagas commit de:

```text
voces reales
audios generados
modelos
cachés
archivos temporales
```

El repositorio debe contener únicamente:

- scripts;
- documentación;
- archivos de configuración;
- estructura vacía necesaria.

---

# 44. Utilizar el proyecto en otro PC

Para utilizarlo en otro ordenador:

1. clona o descarga el repositorio;
2. sigue `01_REQUISITOS.md`;
3. instala WSL2;
4. prepara el entorno;
5. instala Chatterbox;
6. descarga el modelo;
7. añade una voz de referencia;
8. ejecuta el BAT.

No necesitas copiar desde el ordenador anterior:

```text
hf_cache
miniforge3
ChatterboxES
```

La instalación puede reproducirse desde cero siguiendo la documentación.

---

# 45. Qué conviene guardar como copia de seguridad

Si quieres conservar únicamente lo importante, guarda:

```text
repositorio
voces personales
guiones
audios finales importantes
```

Los modelos pueden volver a descargarse.

El entorno Python puede reconstruirse siguiendo el tutorial.

---

# 46. Flujo diario resumido

Después de instalar todo:

```text
1. Preparar guion .txt
2. Revisar puntuación
3. Ejecutar Generar voz.bat
4. Elegir guion
5. Elegir voz
6. Esperar
7. Recoger WAV en salidas
8. Utilizar el WAV donde sea necesario
```

---

# 47. Cuándo tocar la configuración

No modifiques parámetros generales simplemente porque una frase aislada haya salido rara.

Primero comprueba:

```text
texto
puntuación
voz de referencia
```

Toca:

```text
Exaggeration
CFG
Temperature
```

cuando quieras cambiar de forma general el comportamiento de la voz.

---

# 48. Cuándo dejar de ajustar

Si tienes una configuración que:

- suena natural;
- mantiene una voz suficientemente estable;
- sirve para tu uso;
- no presenta errores graves;

es mejor conservarla.

Los modelos generativos tienen variabilidad.

Buscar indefinidamente una configuración perfecta puede producir cambios sin una mejora consistente.

---

# Siguiente paso

Continúa con:

```text
08_ERRORES_Y_SOLUCIONES.md
```

Ese documento reúne los errores más importantes que pueden aparecer durante la instalación y el uso, junto con sus soluciones.
