# app/txt2img_animagine.py
from pathlib import Path
import torch
from diffusers import StableDiffusionXLPipeline

def main():
    model_id = "cagliostrolab/animagine-xl-3.0"   # Animagine XL v3.0 (SDXL)
    prompt = (
        "anime illustration of a cute cat astronaut, clean lineart, cel-shading,"
        " vibrant colors, detailed eyes, soft lighting, high quality"
    )
    negative = (
        "blurry, low quality, bad anatomy, deformed, extra limbs, mutated hands,"
        " watermark, text, logo"
    )

    device = "cpu"  
    width, height = 704, 704   
    steps, cfg = 30, 7.5         #para más detalle (más lento)
    seed = 42

    # Carga del pipeline SDXL
    pipe = StableDiffusionXLPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,    # CPU = float32
        use_safetensors=True
    )
    pipe = pipe.to(device)

    # Optimizaciones para CPU (menos RAM)
    pipe.enable_attention_slicing()
    pipe.enable_vae_slicing()

    generator = torch.manual_seed(seed)

    image = pipe(
        prompt=prompt,
        negative_prompt=negative,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=cfg,
        generator=generator,
    ).images[0]

    Path("outputs").mkdir(exist_ok=True)
    out = Path("outputs/animagine_txt2img.png")
    image.save(out)
    print(f"Imagen guardada en: {out.resolve()}")

if __name__ == "__main__":
    main()
