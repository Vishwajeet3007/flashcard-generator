# 📘 LLM-Powered Flashcard Generator

This is a lightweight Streamlit app that uses OpenAI GPT to generate flashcards from educational content.

## 📁 Project Structure
```
flashcard-generator/
├── app.py                  # Main Streamlit app
├── flashcard_generator.py # Core logic: LLM prompt + processing
├── utils.py               # File handling & export
├── requirements.txt       # Dependencies
├── templates/             # (Optional - Flask)
├── static/                # (Optional - Flask)
├── samples/               # Sample input files
├── outputs/               # Exported flashcards
├── README.md
└── .env                   # Contains OPENAI_API_KEY
```

## 🚀 Features
- Upload `.pdf` or `.txt` files or paste raw content
- Generate 10–15 question-answer flashcards
- Each card includes difficulty level (Easy/Medium/Hard)
- Multi-language support (English, Hindi, Spanish, French)
- Download in CSV, JSON, or Anki (TXT) format
- Optional subject guidance for better prompts

## 🛠️ Setup Instructions
```bash
git clone https://github.com/your-username/flashcard-generator
cd flashcard-generator
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_openai_key_here
```

Run the app:
```bash
streamlit run app.py
```

## 🧪 Sample Input
A chapter on cell biology (PDF) under `samples/`

## 📦 Outputs
Flashcards are saved/exportable in `outputs/` folder.

## 📹 Demo
(Optional) Include a Loom/OBS video link

---