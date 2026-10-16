# Cyber Rakshak

A small cyber-safety project with two independent interfaces: a Streamlit Q&A demo and a standalone HTML link checker. The interface text is primarily Telugu-English (Tenglish).

## Features

- **Streamlit app (`app.py`)**: asks for a cyber-safety question and displays a short sample response with basic safety reminders. This version currently uses a fixed demo response; it does not call Gemma or another AI service.
- **HTML app (`index.html`)**: checks a pasted link using simple text matching and displays a warning, danger, or safe message.
- **Shared styling (`style.css`)**: styles both interfaces and uses a background image hosted on Unsplash. Internet access is required to load that image.

## Run the Streamlit app

Python 3 and Streamlit are required. From this project folder, install Streamlit if it is not already installed:

```powershell
py -m pip install streamlit
```

Start the app:

```powershell
py -m streamlit run app.py
```

Streamlit prints a local URL in the terminal, usually `http://localhost:8501`.

## Run the HTML app

Open `index.html` in a web browser. It loads `style.css` from the same folder and does not require Python or a web server.

## Project files

- `app.py` - Streamlit cyber-safety Q&A demo
- `index.html` - standalone link-checking page
- `style.css` - shared page styling and background image

## Important safety note

The HTML link checker relies on simple keyword and domain matching. A result marked "safe" is not a security verification; malicious links can evade these checks, and legitimate links may be flagged. Do not enter credentials or OTPs based on this result. Verify links through trusted sources and report cybercrime in India through the official helpline at **1930**.
