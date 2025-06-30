import json
from serpapi.google_search import GoogleSearch

def search_image(image_name):
    """Search for an image using SerpApi and return the first result URL"""
    search_params = {
        "q": image_name,
        "tbm": "isch", 
        "api_key": "1bec62d88e543f77eb7bb2917d043d933261cbfe5fa8f4bb8cc847cd993baeb5" 
    }
    
    try:
        search = GoogleSearch(search_params)
        results = search.get_dict()
        return results.get("images_results", [{}])[0].get("original")
    except Exception as e:
        print(f"Error searching for {image_name}: {e}")
        return None

def process_slide_images(data):
    for i, slide in enumerate(data["slides"]):
        # First slide uses background_image
        if i == 0 and "background_image" in slide:
            image_url = search_image(slide["background_image"] + " widescreen background")
            if image_url:
                slide["background_image"] = image_url
            else:
                print(f"Background image not found: {slide['background_image']}")
                slide.pop("background_image", None)  # Remove if not found
        
        # Subsequent slides use side_image
        elif i > 0 and "side_image" in slide:
            image_url = search_image(slide["side_image"] + " tall vertical image")
            if image_url:
                slide["side_image"] = image_url
            else:
                print(f"Side image not found: {slide['side_image']}")
                slide.pop("side_image", None)  # Remove if not found
    return data