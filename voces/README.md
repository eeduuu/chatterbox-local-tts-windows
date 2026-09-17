# Voces de referencia

Esta carpeta está destinada a guardar las voces de referencia que utilizará Chatterbox.

Los archivos de voz reales no deben subirse al repositorio.

El archivo `.gitignore` está configurado para ignorar los audios guardados dentro de esta carpeta.

---

## Voz predeterminada

El lanzador puede utilizar automáticamente una voz predeterminada.

Para ello, coloca un archivo con este nombre:

```text
voz_predeterminada.mp3
```

La estructura quedaría:

```text
voces/
├── README.md
└── voz_predeterminada.mp3
```

El archivo `voz_predeterminada.mp3` solo debe existir localmente en el ordenador y no debe aparecer en GitHub.

---

## Otras voces

También puedes guardar más referencias dentro de esta carpeta:

```text
voces/
├── README.md
├── voz_predeterminada.mp3
├── voz_secundaria.mp3
└── otra_voz.wav
```

El lanzador permite seleccionar manualmente otra voz cuando no quieras utilizar la predeterminada.

---

## Formatos admitidos

La configuración incluida está preparada para seleccionar archivos:

```text
.mp3
.wav
```

---

## Recomendaciones

Utiliza preferentemente una grabación:

- con una sola persona;
- clara;
- sin música;
- sin efectos;
- sin ruido fuerte de fondo;
- sin saturación;
- con poco eco;
- con una voz natural.

Una referencia limpia suele ser más importante que una referencia muy larga.

---

## Privacidad

No subas al repositorio:

- voces personales;
- grabaciones privadas;
- audios de otras personas sin permiso.

Utiliza únicamente voces propias o voces para las que tengas autorización.

---

## Ubicación de las voces

No es obligatorio guardar todas las referencias dentro de esta carpeta.

El lanzador también permite seleccionar un archivo `.mp3` o `.wav` situado en otra carpeta de Windows.

La carpeta `voces/` sirve principalmente para mantener una voz predeterminada y organizar referencias de uso frecuente.
