from pptx import Presentation
from PIL import Image, ImageDraw, ImageFont
import io
import base64

def process_slide_images(presentation_json):
    images = []

    for i, slide in enumerate(presentation_json['slides']):
        # Mock image from text (title + content)
        width, height = 1280, 720
        image = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(image)

        title = slide.get("title", f"Slide {i+1}")
        content = slide.get("content", "")

        draw.text((50, 100), title, fill="black")
        draw.text((50, 200), content, fill="black")

        # Save to base64
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
        images.append(f"data:image/png;base64,{base64_img}")

    return images
