# AI-Powered PowerPoint Generator

A web application that automatically generates PowerPoint presentations on any topic using AI (Google Gemini) and includes relevant images.

## ✨ Features

- **AI-Generated Content**: Uses Google Gemini to create structured presentation content
- **Automatic Image Integration**: Fetches relevant images for each slide
- **Customizable**: Choose your topic and number of slides
- **Fast API Backend**: Built with FastAPI for efficient processing
- **Clean Frontend**: Simple, user-friendly interface

## 📂 File Structure
project/
│
├── create_presentation.py # Creates PPTX from structured data
├── generate_data.py # Generates presentation content using AI
├── get_images.py # Handles image search and processing
├── main.py # FastAPI server implementation
├── index.html # Frontend interface
└── example_ppt/ # Example presentations


## Dependencies
Backend:

* FastAPI

* Google Generative AI

* python-pptx

* requests

* SerpAPI (for image search)

Frontend:

* Plain HTML/CSS/JavaScript

## What It Does

1. Takes two inputs:
   - Presentation topic (e.g., "Renewable Energy")
   - Number of slides needed

2. Uses AI (Google Gemini) to:
   - Generate relevant content for each slide
   - Structure the presentation with titles and bullet points

3. Adds images (via SerpAPI) where available

4. Outputs a downloadable .pptx file

## Technical Details

- **Backend**: FastAPI server
- **AI Processing**: Google Gemini via LangChain prompts
- **Image Search**: SerpAPI integration
- **Frontend**: Basic HTML/JS interface

## Limitations

- Content quality depends on Gemini's output
- Basic slide formatting (no complex designs)
- Processing time typically 10-20 seconds

## When To Use This

- Last-minute presentation needs
- Basic topic overviews
- When starting from scratch is overwhelming

## Final Notes

This project serves as a basic prototype demonstrating how AI can automate simple presentation creation. It's not a production-ready tool, but rather:

- A proof-of-concept for AI-powered content generation  
- A starting point for more sophisticated presentation tools  
- An educational example of API integration (Gemini + SerpAPI + FastAPI)  

The code is intentionally kept simple to show the core functionality. For real-world use, you'd want to add more robust error handling, design templates, and content validation.
