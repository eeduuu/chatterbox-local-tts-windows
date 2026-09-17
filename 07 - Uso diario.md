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
video_nana.txt
```

Puedes guardarlo en cualquier carpeta de Windows.

No es necesario copiarlo dentro del repositorio.

---

# 2. Formato recomendado del guion

Puedes utilizar texto normal:

```text
Lo raro de Nana es que casi nunca te sorprende.

Tú sabes lo que hace.

Y aun así, cuando aparece la oportunidad... ahí vas.
```

También puedes conservar timestamps:

```text
[0:00–0:51]

Lo raro de Nana es que casi nunca te sorprende.

Tú sabes lo que hace.

[0:51–1:41]

Por eso Nana funciona tan bien en SoloQ.
```

El generador reconoce líneas con este formato y no las pronuncia:

```text
[0:00–0:51]
```

Los tiempos sirven para organizar el guion.

No obligan a Chatterbox a producir exactamente esa duración.

---

# 3. Preparar el texto para TTS

Chatterbox puede leer correctamente un texto normal, pero la puntuación influye mucho en:

- velocidad;
- respiraciones;
- pausas;
- intención;
- naturalidad.

Por ejemplo:

```text
Lo sabes. Lo has vivido. Y aun así, ahí vas.
```

puede sonar diferente a:

```text
Lo sabes... Lo has vivido... Y aun así, ahí vas.
```

No es necesario llenar el guion de puntos suspensivos.

Úsalos únicamente donde tenga sentido dejar una pausa perceptible.

Las comas también pueden ayudar a evitar que una frase larga se lea demasiado seguida.

---

# 4. No intentes controlar la duración exacta con puntuación

La puntuación puede ralentizar ligeramente la lectura, pero no debe utilizarse para intentar convertir artificialmente:

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

El objetivo debe ser mejorar el ritmo, no alcanzar una duración matemática.

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

Selecciona tu:

```text
.txt
```

Por ejemplo:

```text
video_nana.txt
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

Por ejemplo:

```text
D:\Voces\otra_voz.wav
```

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

El programa mostrará:

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
Texto...
```

después:

```text
[2/8]
Texto...
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

No representa el porcentaje total del vídeo.

Representa la generación del bloque actual.

---

# 13. Tiempo de espera

Esta configuración utiliza CPU.

Por tanto, la generación no es en tiempo real.

Es completamente normal que:

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
video_nana.txt
```

produce:

```text
video_nana_voz.wav
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
video_nana.txt
```

la salida volverá a llamarse:

```text
video_nana_voz.wav
```

Por tanto, la nueva generación puede sustituir la anterior.

Si quieres conservar varias versiones:

```text
video_nana_v1.txt
video_nana_v2.txt
```

o renombra/mueve el WAV anterior antes de volver a generar.

---

# 19. La misma configuración no produce siempre exactamente la misma interpretación

El generador utiliza una seed controlada para hacer el comportamiento más reproducible.

La configuración inicial es:

```text
BASE_SEED = 12345
```

Cada bloque utiliza una seed derivada de esa base.

Aun así, cambios en:

- texto;
- puntuación;
- bloques;
- modelo;
- dependencias;
- voz;

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

Esta configuración fue elegida como un punto de partida útil para narración en español.

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

De esta forma sabrás qué parámetro produjo realmente el cambio.

---

# 23. Utiliza textos cortos para probar configuraciones

No generes un vídeo entero cada vez que quieras comparar parámetros.

Crea un `.txt` corto con varias frases representativas.

Por ejemplo:

```text
Esta es una prueba de voz.

Quiero comprobar cómo cambia el ritmo, la entonación y la naturalidad.

También quiero escuchar cómo termina una frase más larga.
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

También pueden modificar el ritmo y la estabilidad.

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

afecta al comportamiento de la generación y puede influir en el ritmo.

Reducirlo puede hacer que algunas voces se sientan diferentes o algo menos rígidas.

No existe un valor universal.

---

# 26. Temperature

El parámetro:

```text
TEMPERATURE
```

afecta a la variabilidad de la generación.

Valores diferentes pueden cambiar:

- entonación;
- estabilidad;
- forma de pronunciar algunas frases.

Si una configuración ya funciona bien, no es necesario modificarla constantemente.

---

# 27. Tamaño de los bloques

El generador utiliza:

```python
TARGET_CHARS = 500
HARD_MAX = 650
```

No es un límite propio del modelo de 300 caracteres.

El programa agrupa varias frases para dar a Chatterbox suficiente contexto.

Esto ayuda a conservar:

- continuidad;
- ritmo;
- intención.

---

# 28. No reduzcas demasiado los bloques

Generar una frase de pocos segundos de forma independiente puede producir una voz muy buena.

Sin embargo, generar cada frase de un guion por separado puede provocar:

- cambios de voz;
- diferencias de volumen;
- entonación inconsistente;
- sensación de audio pegado.

Por eso el programa intenta trabajar con bloques relativamente largos.

---

# 29. Bloques demasiado largos

Tampoco conviene enviar varios minutos completos en una sola generación.

Los bloques excesivamente largos pueden aumentar la posibilidad de:

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

No pongas pausas enormes esperando compensar un guion demasiado corto.

Un exceso de silencios puede hacer que la narración parezca artificial.

---

# 32. Voz buena en pruebas cortas pero peor en textos largos

Puede ocurrir que una prueba de 10 segundos suene mejor que una narración de varios minutos.

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

Si el problema ocurre siempre en la misma frase, revisa primero su puntuación.

---

# 34. Si una palabra se pronuncia mal

Antes de modificar parámetros generales, prueba a cambiar únicamente la puntuación alrededor de esa palabra o frase.

No cambies la ortografía correcta sin comprobar antes que realmente sea necesario.

Palabras inglesas, nombres propios y términos de videojuegos pueden ser especialmente variables.

---

# 35. Si habla demasiado rápido

Primero revisa:

- frases extremadamente largas;
- falta de comas;
- falta de puntos;
- bloques de texto sin respiraciones naturales.

Puedes probar una puntuación más oral.

Por ejemplo:

```text
Sabes lo que ocurre y aun así sigues entrando porque crees que esta vez será diferente.
```

puede convertirse en:

```text
Sabes lo que ocurre... y aun así, sigues entrando, porque crees que esta vez será diferente.
```

No añadas pausas sin sentido únicamente para aumentar segundos.

---

# 36. Si necesitas una duración concreta

Chatterbox no está diseñado en esta configuración para garantizar que:

```text
un bloque de texto = exactamente X segundos
```

Si necesitas una sincronización exacta para vídeo, las opciones más seguras son:

- adaptar la cantidad de texto;
- ajustar el montaje del vídeo;
- insertar pausas naturales;
- cortar y colocar la narración dentro del editor.

Evita ralentizar agresivamente el WAV terminado.

Puede deteriorar mucho la naturalidad.

---

# 37. Preparación del guion antes de TTS

Si utilizas una IA para escribir el guion, puede ser útil tener dos fases distintas:

```text
Guion normal
        ↓
Preparación para TTS
        ↓
Chatterbox
```

La preparación para TTS puede modificar exclusivamente:

- puntuación;
- pausas;
- saltos;
- signos de interrogación;
- signos de exclamación;

sin cambiar necesariamente las palabras.

Esto permite conservar el contenido y mejorar la forma en que el TTS interpreta el ritmo.

---

# 38. No dependas de los saltos de línea

El generador actual procesa los bloques principalmente a partir de:

- timestamps;
- frases;
- puntuación;
- tamaño del texto.

Los saltos de línea sirven para que el guion sea legible, pero no deben ser la única herramienta para indicar pausas.

Utiliza puntuación explícita donde la pausa sea importante.

---

# 39. Cambiar permanentemente la voz predeterminada

Para cambiar la voz utilizada al pulsar:

```text
Sí
```

en la pregunta de voz predeterminada:

1. abre:

```text
voces/
```

2. elimina o mueve la referencia actual;

3. coloca la nueva referencia;

4. llámala:

```text
voz_predeterminada.mp3
```

La próxima generación utilizará esa voz cuando selecciones la opción predeterminada.

---

# 40. Probar una voz sin convertirla en predeterminada

No necesitas renombrarla.

Ejecuta:

```text
Generar voz.bat
```

Cuando pregunte por la voz predeterminada, pulsa:

```text
No
```

y selecciona el nuevo:

```text
.mp3
```

o:

```text
.wav
```

---

# 41. No es necesario reiniciar Chatterbox al cambiar de voz

Cada ejecución del BAT inicia una generación nueva.

Puedes utilizar:

```text
voz A
```

en una ejecución y:

```text
voz B
```

en la siguiente.

No necesitas reinstalar nada.

---

# 42. Organización recomendada de las salidas

La carpeta:

```text
salidas/
```

puede llenarse con el tiempo.

Puedes mover los WAV terminados a las carpetas de tus proyectos de vídeo.

Por ejemplo:

```text
Proyecto vídeo/
├── guion.txt
├── narracion.wav
└── ...
```

No es necesario conservar todos los resultados dentro del repositorio.

---

# 43. GitHub y archivos personales

Nunca hagas commit de:

```text
voces reales
audios generados
modelos
cachés
```

El repositorio está pensado para contener solamente:

- scripts;
- documentación;
- archivos de configuración;
- estructura vacía.

---

# 44. Utilizarlo en otro PC

Para utilizar el proyecto en otro ordenador:

1. clona o descarga el repositorio;
2. sigue desde `01_REQUISITOS.md`;
3. instala WSL2;
4. prepara el entorno;
5. instala Chatterbox;
6. descarga el modelo;
7. añade tu propia voz;
8. ejecuta el BAT.

No necesitas copiar:

```text
hf_cache
miniforge3
ChatterboxES
```

desde el ordenador antiguo.

Es más seguro reproducir la instalación siguiendo la documentación.

---

# 45. Qué debes guardar como copia de seguridad

Si quieres conservar únicamente lo importante, guarda:

```text
repositorio
voces personales
guiones
audios finales que quieras conservar
```

Los modelos pueden volver a descargarse.

El entorno Python también puede reconstruirse siguiendo el tutorial.

---

# 46. Flujo diario resumido

Después de instalar todo:

```text
1. Preparar guion .txt
2. Revisar puntuación
3. Doble clic en Generar voz.bat
4. Elegir guion
5. Elegir voz
6. Esperar
7. Recoger WAV en salidas
8. Llevar WAV al editor de vídeo
```

---

# 47. Cuándo tocar la configuración

No modifiques parámetros simplemente porque una frase aislada haya salido rara.

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

solo cuando quieras cambiar de forma general el comportamiento de la voz.

---

# 48. Cuándo dejar de ajustar

Si tienes una configuración que:

- suena natural;
- mantiene una voz estable;
- sirve para tus vídeos;
- no presenta errores graves;

es mejor conservarla.

Los modelos generativos tienen variabilidad.

Buscar indefinidamente una configuración perfecta puede producir resultados diferentes sin una mejora consistente.

---

# Siguiente paso

Continúa con:

```text
08_ERRORES_Y_SOLUCIONES.md
```

Ese documento reúne los errores más importantes que pueden aparecer y las soluciones que realmente necesita esta instalación.
