
from pathlib import Path
import torch
from PIL import Image
from diffusers import StableDiffusionXLImg2ImgPipeline

def main():
    # Ruta de la imagen de referencia
    img_path = input("Ruta de la imagen de referencia (ej: data/astro.png): ").strip()
    ref_img = Image.open(img_path).convert("RGB")

    # Prompt
    prompt = input(" Escribe tu prompt (ej: astronauta anime en estilo retro): ")
    if not prompt.strip():
        prompt = "anime illustration, cel-shading, vibrant colors, clean lineart"

    # Negative prompt
    negative = input("Negative prompt (Enter = por defecto): ")
    if not negative.strip():
        negative = "blurry, bad anatomy, deformed, extra limbs, bad hands, text, watermark, logo, low quality"

    # Opciones básicas
    width = 768
    height = 768
    steps = 30
    cfg = 7.5
    strength = 0.6  # qué tanto se aleja del original
    seed = 42

    print("\n🔧 Generando con:")
    print(f" Ref: {img_path}")
    print(f" Prompt: {prompt}")
    print(f" Negative: {negative}")
    print(f" Size: {width}x{height}, steps={steps}, cfg={cfg}, strength={strength}, seed={seed}")

    # Cargar modelo
    model_id = "cagliostrolab/animagine-xl-3.0"
    pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32
    ).to("cpu")


    pipe.enable_attention_slicing()
    pipe.enable_vae_slicing()

    generator = torch.manual_seed(seed)

    # Redimensionar imagen base al tamaño deseado
    ref_img = ref_img.resize((width, height))

    # Generar
    result = pipe(
        prompt=prompt,
        negative_prompt=negative,
        image=ref_img,
        strength=strength,
        num_inference_steps=steps,
        guidance_scale=cfg,
        generator=generator
    )

    # Guardar salida
    Path("outputs").mkdir(exist_ok=True)
    out = Path("outputs/animagine_img2img.png")
    result.images[0].save(out)
    print(f"\n Imagen generada en: {out.resolve()}")

if __name__ == "__main__":
    main()
