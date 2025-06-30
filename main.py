from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

from get_images import process_slide_images
from data import create_presentation
from gem import generate_presentation_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific origin in production
    allow_methods=["POST"],
    allow_headers=["*"],
)

class PPTRequest(BaseModel):
    topic: str
    number_of_slides: int

@app.post("/generate-ppt")
async def generate_ppt(data: PPTRequest):
    try:
        presentation_json = generate_presentation_data(data.topic, data.number_of_slides)
        processed_data = process_slide_images(json.loads(presentation_json))
        ppt_stream = create_presentation(processed_data)

        filename = f"{data.topic.replace(' ', '_').replace('/', '-').replace(':', '-')}_presentation.pptx"

        return Response(
            content=ppt_stream.getvalue(),
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)