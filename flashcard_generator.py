import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyBdeyKJqlXOKmNA8-kP-ES_A5s4_BxGGAA"))  

def generate_flashcards(text, subject="General", language="English"):
    prompt = f"""
You are an expert educational flashcard generator.
Generate 10–15 well-structured question-answer flashcards from the content below.

- Subject: {subject}
- Language: {language}

Format each flashcard as:
Q: <question>
A: <answer>
Difficulty: <Easy/Medium/Hard>

Only output the flashcards in the exact format. Do not include any notes or instructions.

Content:
{text[:3000]}
"""

    try:
        print("Generating flashcards with prompt length:", len(prompt))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        raw_output = response.text.strip()

        print("\n🔍 RAW GEMINI OUTPUT:\n", raw_output)

        if not raw_output or "Q:" not in raw_output:
            raise ValueError("No valid flashcard format detected in output.")

        cards = []
        blocks = raw_output.split("Q:")
        for block in blocks[1:]:
            qa = block.strip().split("A:", 1)
            if len(qa) != 2:
                continue
            question, rest = qa
            if "Difficulty:" in rest:
                answer, difficulty = rest.split("Difficulty:", 1)
            else:
                answer, difficulty = rest, "Medium"
            cards.append({
                "question": question.strip(),
                "answer": answer.strip(),
                "difficulty": difficulty.strip().splitlines()[0]
            })
        return cards if cards else []

    except Exception as e:
        print("❌ Error generating flashcards with Gemini:", e)
        return []
