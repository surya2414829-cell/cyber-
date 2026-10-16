# Cyber Rakshak

A small cyber-safety project with two independent interfaces: a Streamlit-powered Gemma Q&A app and a standalone HTML link checker. The interface text is primarily Telugu-English (Tenglish).

## Features

- **Streamlit app (`app.py`)**: sends cyber-safety questions to the Gemma model `gemma-3-12b-it` and displays its response. A Gemini API key is required.
- **HTML app (`index.html`)**: checks a pasted link using simple text matching and displays a warning, danger, or safe message.
- **Shared styling (`style.css`)**: styles both interfaces and uses a background image hosted on Unsplash. Internet access is required to load that image.

## Run the Streamlit app

Python 3 is required. From this project folder, install the project dependencies:

```powershell
py -m pip install -r requirements.txt
```

Start the app and enter your Gemini API key in the sidebar:

```powershell
py -m streamlit run app.py
```

Streamlit prints a local URL in the terminal, usually `http://localhost:8501`.
Create or manage a Gemini API key through Google AI Studio. The key is entered into a password field and is not written into the source files.

## Run the HTML app

Open `index.html` in a web browser. It loads `style.css` from the same folder and does not require Python or a web server.

## Project files

- `app.py` - Streamlit Gemma cyber-safety Q&A app
- `index.html` - standalone link-checking page
- `style.css` - shared page styling and background image
- `requirements.txt` - Python dependencies

## Important safety note

The HTML link checker relies on simple keyword and domain matching. A result marked "safe" is not a security verification; malicious links can evade these checks, and legitimate links may be flagged. Do not enter credentials or OTPs based on this result. Verify links through trusted sources and report cybercrime in India through the official helpline at **1930**.
