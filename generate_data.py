from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import re

def generate_presentation_data(topic: str, number_of_slides: int = 4):
    prompt = ChatPromptTemplate.from_template(
        """Generate a PowerPoint presentation about '{topic}' with {number_of_slides} slides.
        Structure Requirements:
        1. FIRST SLIDE (Title Slide):
           - Title only (no content)
           - background_image: "topic_keyword.jpg"
        
        2. SUBSEQUENT SLIDES:
           - Title
           - 3-5 bullet points
           - side_image: "related_keyword.jpg"
        
        Example for "cricket":
        {{
          "slides": [
            {{
              "title": "Introduction to Cricket",
              "background_image": "cricket_stadium.jpg"
            }},
            {{
              "title": "History",
              "content": ["Originated in England", "First match in 1844"],
              "side_image": "vintage_cricket.jpg"
            }}
          ]
        }}"""
    )

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.7)
    chain = prompt | llm
    
    response = chain.invoke({
        "topic": topic,
        "number_of_slides": number_of_slides
    })
    
    # Clean and validate JSON
    cleaned = re.sub(r'^```(json)?|```$', '', response.content, flags=re.MULTILINE).strip()
    return cleaned

cleaned=generate_presentation_data('artificial intelligence',4)