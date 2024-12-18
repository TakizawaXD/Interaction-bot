# MAGBOT

MAGBOT es un bot de Discord diseñado para interacciones entretenidas entre usuarios. Ofrece comandos para realizar acciones como abrazos, besos, bofetadas, caricias y más, además de un sistema de economía básica que permite realizar trabajos y ganar monedas.

---

## Características principales

1. **Interacciones entre usuarios:**
   - Los usuarios pueden realizar acciones como abrazar, besar, abofetear, acariciar, y más.
   - Cada interacción se contabiliza y se almacena en una base de datos SQLite.

2. **Sistema de economía:**
   - Los usuarios pueden realizar trabajos para ganar monedas virtuales.
   - La tienda muestra los trabajos disponibles y sus recompensas.
   - Los usuarios pueden consultar su saldo y las estadísticas de sus actividades.

3. **Base de datos persistente:**
   - Utiliza SQLAlchemy para manejar una base de datos SQLite que guarda los perfiles de los usuarios.

4. **GIFs animados:**
   - Cada acción muestra un GIF animado correspondiente, seleccionado al azar de una lista.

---

## Requisitos

| **Requisito**        | **Descripción**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| Python 3.8 o superior | Asegúrate de tener instalada una versión compatible de Python.                 |
| Librerías necesarias  | `discord.py`, `SQLAlchemy` (ambas se instalan automáticamente con `pip`).       |
| Base de datos SQLite  | Manejo integrado con `SQLAlchemy` para el almacenamiento de datos persistente. |

---

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/TakizawaXD/MAGBOT.git
   cd MAGBOT
   ### Requisitos

| **Requisito**        | **Descripción**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| Python 3.8 o superior | Asegúrate de tener instalada una versión compatible de Python.                 |
| Librerías necesarias  | `discord.py`, `SQLAlchemy` (ambas se instalan automáticamente con `pip`).       |
| Base de datos SQLite  | Manejo integrado con `SQLAlchemy` para el almacenamiento de datos persistente. |

---

### Comandos de Interacción

| **Comando**       | **Descripción**                                                 | **Ejemplo de uso**        |
|--------------------|-----------------------------------------------------------------|---------------------------|
| `T hug @user`      | Abrazas a un usuario.                                           | `T hug @Takizawa`         |
| `T kiss @user`     | Besas a un usuario.                                             | `T kiss @Takizawa`        |
| `T slap @user`     | Abofeteas a un usuario.                                         | `T slap @Takizawa`        |
| `T pat @user`      | Acaricias a un usuario.                                         | `T pat @Takizawa`         |
| `T highfive @user` | Chocas esos cinco con un usuario.                               | `T highfive @Takizawa`    |
| `T dom @user`      | Muestras tu dominio sobre un usuario (acción humorística).      | `T dom @Takizawa`         |

---

### Comandos de Economía

| **Comando**        | **Descripción**                                                 | **Ejemplo de uso**        |
|---------------------|-----------------------------------------------------------------|---------------------------|
| `T shop`           | Muestra los trabajos disponibles en la tienda.                 | `T shop`                  |
| `T work X`         | Realiza un trabajo específico (1, 2 o 3).                      | `T work 1`                |
| `T balance`        | Consulta tus monedas y trabajos realizados.                    | `T balance`               |
| `T stats`          | Muestra tus estadísticas generales.                            | `T stats`                 |

---

### Campos de la Base de Datos

| **Campo**     | **Descripción**                                |
|---------------|-----------------------------------------------|
| `user_id`     | ID único del usuario en Discord.              |
| `hugs`        | Total de abrazos recibidos.                   |
| `kisses`      | Total de besos recibidos.                     |
| `slaps`       | Total de bofetadas recibidas.                 |
| `pats`        | Total de caricias recibidas.                  |
| `highfives`   | Total de choca esos cinco recibidos.          |
| `dominance`   | Total de veces que alguien mostró dominio.    |
| `money`       | Monedas acumuladas por trabajos realizados.   |
| `work_done`   | Total de trabajos completados.                |

