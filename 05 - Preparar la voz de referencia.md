# 05 - Preparar la voz de referencia

En este paso prepararemos el archivo de audio que Chatterbox utilizará como referencia de voz.

No instalaremos nada nuevo.

El objetivo es tener una muestra limpia que pueda reutilizarse después desde el lanzador de Windows.

---

# Qué es la voz de referencia

Chatterbox puede recibir un archivo de audio con una persona hablando y utilizarlo como referencia para generar una voz con características similares.

El archivo de referencia no contiene el guion.

Solo sirve como muestra de:

- timbre;
- forma de hablar;
- entonación;
- características de la voz.

Después podrás utilizar esa misma referencia con cualquier guion.

---

# Formatos que utilizaremos

Para esta instalación utilizaremos:

```text
.mp3
.wav
```

No es necesario convertir un `.mp3` a `.wav` solo para utilizarlo con este proyecto.

Si ya tienes una grabación original limpia en `.mp3`, puedes utilizarla directamente.

---

# No conviertas la referencia innecesariamente

Utiliza preferentemente el archivo original de mayor calidad que tengas.

No conviertas manualmente la grabación a:

```text
16 kHz
mono
baja calidad
```

salvo que tengas un motivo concreto para hacerlo.

Durante las pruebas de esta instalación, utilizar una copia previamente reducida a 16 kHz dio peores resultados que utilizar directamente la grabación original.

Para Chatterbox es preferible conservar la fuente original limpia y dejar que el propio sistema procese el audio cuando sea necesario.

---

# Duración recomendada

No necesitas grabar varios minutos.

Como punto de partida práctico, utiliza aproximadamente:

```text
10 - 30 segundos
```

de voz limpia.

Una muestra algo más larga no garantiza automáticamente un resultado mejor.

Lo importante es la calidad y claridad de la grabación.

---

# Cómo debe ser la grabación

Intenta utilizar una muestra que tenga:

- una sola persona;
- voz clara;
- volumen estable;
- pronunciación natural;
- poco ruido de fondo;
- poca reverberación;
- varias frases normales;
- algo de variación natural en la entonación.

La persona debería hablar como lo haría normalmente.

---

# Evita

Evita referencias con:

- música;
- gameplay de fondo;
- otras voces;
- televisión;
- ventiladores muy fuertes;
- eco excesivo;
- reverberación fuerte;
- micrófono saturado;
- distorsión;
- clipping;
- silencios muy largos;
- cambios extremos de volumen;
- filtros de voz;
- reducción de ruido agresiva;
- efectos;
- pitch modificado;
- velocidad alterada.

También es mejor evitar una grabación donde toda la muestra sea:

```text
susurrada
gritada
actuada de forma exagerada
```

salvo que ese sea exactamente el estilo que quieres obtener.

---

# El contenido de la grabación

No necesitas leer un texto específico.

Puedes utilizar varias frases naturales.

Es preferible que la muestra contenga habla continua y normal en lugar de palabras aisladas.

Por ejemplo, una grabación útil puede contener varias frases de conversación durante unos segundos.

No hace falta que el texto de referencia coincida con el futuro guion.

---

# Idioma y acento

Esta instalación utiliza el modelo:

```text
Spanish (Spain) / es-ES
```

Si vas a generar narraciones en español de España, es recomendable utilizar una referencia donde la persona también hable de forma natural en español.

No necesitas imitar ningún acento artificialmente.

Utiliza la pronunciación normal de la persona grabada.

---

# Calidad antes que duración

Una referencia corta y limpia suele ser más útil que una grabación larga llena de:

- ruido;
- música;
- pausas;
- cambios de micrófono;
- diferentes ambientes.

Si tienes que elegir entre:

```text
15 segundos limpios
```

y:

```text
2 minutos con ruido y música
```

utiliza la muestra limpia.

---

# Cómo grabar una nueva referencia

Si necesitas grabarla desde cero, puedes utilizar cualquier programa que produzca un archivo normal de audio.

Por ejemplo:

- Grabadora de sonido de Windows;
- Audacity;
- OBS;
- un teléfono móvil;
- un editor de audio.

No necesitas un micrófono profesional.

Prioriza:

```text
habitación silenciosa
distancia estable al micrófono
voz natural
sin saturación
```

---

# Volumen

No es necesario normalizar agresivamente la grabación.

La voz debe escucharse claramente sin:

```text
distorsión
saturación
volumen extremadamente bajo
```

Si la forma de onda ha sido recortada por haber grabado demasiado fuerte, es mejor repetir la grabación que intentar repararla después.

---

# Recortar el principio y el final

Puedes eliminar:

- varios segundos de silencio inicial;
- varios segundos de silencio final;
- ruidos antes de empezar a hablar;
- ruidos después de terminar.

No es necesario eliminar todas las pequeñas respiraciones naturales.

Una referencia demasiado procesada también puede sonar artificial.

---

# Una voz por archivo

Utiliza un archivo independiente para cada voz.

Por ejemplo:

```text
voz_1.mp3
voz_2.mp3
voz_3.wav
```

No combines varias personas dentro de un mismo archivo.

---

# Voz predeterminada del repositorio

El lanzador que configuraremos en el siguiente paso permitirá tener una voz predeterminada.

Para mantener el proyecto genérico utilizaremos el nombre:

```text
voz_predeterminada.mp3
```

La ubicación será:

```text
chatterbox-local-tts-windows/
└── voces/
    └── voz_predeterminada.mp3
```

Si tu referencia está en `.wav`, también podrás seleccionar manualmente ese archivo desde el lanzador.

---

# Si quieres utilizar siempre otra voz

No estás obligado a llamar a todos los archivos:

```text
voz_predeterminada.mp3
```

Puedes guardar varias referencias:

```text
voces/
├── voz_predeterminada.mp3
├── voz_secundaria.mp3
└── otra_voz.wav
```

Al generar un audio podrás:

1. utilizar la voz predeterminada;
2. elegir otro `.mp3`;
3. elegir otro `.wav`.

No será necesario modificar Chatterbox ni reinstalar los modelos para cambiar de voz.

---

# Si no quieres una voz predeterminada

También puedes dejar la carpeta:

```text
voces/
```

sin:

```text
voz_predeterminada.mp3
```

En ese caso el lanzador te pedirá seleccionar manualmente una referencia cada vez.

---

# Si todavía no has descargado el repositorio

No pasa nada.

Guarda por ahora tu archivo de referencia en un lugar seguro.

En:

```text
06_INSTALAR_LANZADOR.md
```

descargaremos o clonaremos el repositorio en Windows y podrás copiar la referencia dentro de:

```text
voces/
```

---

# No guardes la voz dentro de WSL

Para el uso final no es necesario guardar la referencia dentro de:

```text
~/ChatterboxES
```

ni crear carpetas personales de voces dentro de Ubuntu.

La estructura final separará:

```text
WSL
└── motor y modelos de Chatterbox
```

de:

```text
Windows
└── lanzador, voces y salidas
```

Esto hace más sencillo:

- cambiar voces;
- hacer copias de seguridad;
- mover el proyecto;
- reinstalarlo en otro PC;
- mantener limpio Chatterbox;
- publicar el repositorio sin modelos ni archivos personales.

---

# No utilices rutas fijas personales

Los archivos del repositorio no deben contener rutas como:

```text
C:\Users\Nombre\
/home/nombre/
OneDrive\
Escritorio\
```

El lanzador utilizará rutas relativas al lugar donde esté guardado el propio repositorio.

Así podrá funcionar en otros ordenadores sin editar nombres de usuario.

---

# Privacidad

Una voz de referencia puede ser información personal.

No la subas a GitHub.

El repositorio incluirá reglas de `.gitignore` para evitar que los archivos de audio de:

```text
voces/
```

se añadan accidentalmente al repositorio.

La carpeta podrá existir en GitHub, pero las voces reales permanecerán únicamente en el ordenador del usuario.

---

# Importante al publicar el repositorio

No hagas:

```bash
git add voces/voz_predeterminada.mp3
```

ni subas otras grabaciones personales.

En GitHub solo conservaremos un archivo de documentación dentro de:

```text
voces/
```

para explicar dónde debe colocar cada usuario su propia referencia.

---

# Uso responsable

Utiliza:

- tu propia voz;
- voces para las que tengas permiso;
- grabaciones que tengas derecho a utilizar.

No utilices una referencia para suplantar a otra persona o generar contenido engañoso atribuido a ella.

---

# Qué ocurre cuando Chatterbox utiliza la referencia

El generador cargará la voz una vez al comenzar el proceso.

Después utilizará esa referencia para generar los diferentes bloques del guion.

No será necesario volver a seleccionar la voz entre cada bloque.

El resultado final se unirá automáticamente en un solo archivo `.wav`.

---

# La referencia no garantiza una copia exacta

La voz generada puede parecerse a la referencia, pero no debe esperarse una reproducción idéntica.

El resultado también depende de:

- calidad de la referencia;
- texto;
- puntuación;
- duración del bloque;
- parámetros de generación;
- aleatoriedad del modelo.

Es posible que una voz generada resulte agradable aunque no sea una copia exacta de la referencia.

---

# Si la voz cambia demasiado

Antes de modificar toda la instalación, comprueba primero:

1. que estás utilizando el archivo original de referencia;
2. que no utilizaste una copia reducida o muy comprimida;
3. que no contiene ruido o música;
4. que solo habla una persona;
5. que el archivo no está distorsionado;
6. que la muestra contiene voz natural.

Después puedes probar parámetros diferentes de generación.

Los parámetros se configurarán posteriormente dentro de:

```text
generar_guion.py
```

---

# Si una referencia funciona peor que otra

Es normal que diferentes grabaciones de la misma persona produzcan resultados distintos.

Si tienes varias muestras, prueba cada una por separado.

Una grabación más larga no tiene por qué ser mejor.

Conserva la referencia que produzca el resultado más natural.

---

# No modifiques todavía los parámetros

En este paso solo estamos preparando la referencia.

La configuración inicial del generador será:

```text
Exaggeration: 0.70
CFG:          0.20
Temperature:  0.80
```

Estos valores podrán cambiarse más adelante sin volver a preparar ni descargar la voz.

---

# Comprobación antes de continuar

Debes tener preparado al menos un archivo:

```text
.mp3
```

o:

```text
.wav
```

con:

```text
una sola voz
audio limpio
sin música
sin efectos
sin saturación
```

Si quieres utilizarlo como voz predeterminada, cuando tengamos el repositorio en Windows lo guardaremos como:

```text
voces/voz_predeterminada.mp3
```

Si prefieres seleccionar siempre la voz manualmente, puedes conservar cualquier nombre.

---

# Siguiente paso

Continúa con:

```text
06_INSTALAR_LANZADOR.md
```

En ese paso configuraremos la parte que permite utilizar todo el sistema desde Windows mediante doble clic.
