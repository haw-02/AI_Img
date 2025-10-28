# 🧠 Generative AI Image Creator — *Animagine XL 3.0*

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Diffusers](https://img.shields.io/badge/Diffusers-HuggingFace-orange)
![Torch](https://img.shields.io/badge/PyTorch-Framework-red)
![Model](https://img.shields.io/badge/Model-AnimagineXL3.0-violet)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎨 Descripción del Proyecto

**Generative AI Image Creator** es un proyecto en **Python** que utiliza el modelo `Animagine XL 3.0` (basado en Stable Diffusion) para generar **nuevas imágenes a partir de una imagen de referencia y un prompt textual**.

El sistema permite al usuario experimentar con parámetros como prompts positivos/negativos, resolución, pasos de inferencia y fuerza de transformación, para producir resultados visuales únicos.

> 🧩 Inspirado en la técnica *img2img* (image-to-image) de los modelos de difusión.

---

## 🧰 Tecnologías Utilizadas

| Herramienta | Uso Principal |
|--------------|---------------|
| 🐍 **Python 3.9+** | Lenguaje principal |
| 🔥 **PyTorch** | Framework de inferencia |
| 🧠 **Diffusers (HuggingFace)** | Pipeline para generación de imágenes |
| 🖼️ **Pillow (PIL)** | Manipulación y carga de imágenes |
| 📂 **Pathlib** | Gestión de rutas y archivos |

---

## ⚙️ Estructura del Proyecto

📁 IA-Image-Generator/
├── app/
│ └── script.py ← Script principal de generación
├── data/ ← Imágenes de entrada (referencia)
├── outputs/ ← Resultados generados
├── requirements.txt ← Dependencias del proyecto
└── README.md ← Documentación del proyecto

---

## 🚀 Cómo Iniciar

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd IA-Image-Generator

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate   # En Windows
# o source .venv/bin/activate en Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script
python app/script.py

🧩 Funcionamiento del Script

Solicita una imagen de referencia (por ejemplo: data/astro.png).

Permite ingresar un prompt positivo y un prompt negativo.

Ajusta automáticamente parámetros base:

Tamaño: 768×768

Pasos de inferencia: 30

CFG Scale: 7.5

Strength: 0.6

Usa el modelo cagliostrolab/animagine-xl-3.0 para generar la imagen.

Guarda el resultado final en la carpeta outputs/.

Ruta de la imagen de referencia (ej: data/astro.png): data/astro.png
Escribe tu prompt (ej: astronauta anime en estilo retro): astronauta en estilo anime, luces de neón
Negative prompt (Enter = por defecto): texto, marcas de agua

🔧 Generando con:
 Ref: data/astro.png
 Prompt: astronauta en estilo anime, luces de neón
 Negative: texto, marcas de agua
 Size: 768x768, steps=30, cfg=7.5, strength=0.6, seed=42

 Imagen generada en: outputs/animagine_img2img.png
📊 Resultados Esperados
| Tipo               | Descripción                               |
| ------------------ | ----------------------------------------- |
| 🎨 Imagen base     | Imagen original cargada desde `/data`     |
| 🧠 Imagen generada | Nueva imagen basada en el prompt          |
| 🔍 Comparativa     | Permite evaluar fidelidad y estilo visual |

🪄 Posibles Mejoras

Interfaz gráfica (GUI) con Streamlit o Gradio

Control del semillado aleatorio (seed)

Implementar parámetros dinámicos desde archivo JSON

Soporte para aceleración GPU (CUDA)

Este proyecto se distribuye bajo licencia MIT, por lo que puede ser reutilizado, modificado y distribuido libremente con atribución al autor original.
