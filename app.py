import streamlit as st
from flashcard_generator import generate_flashcards
from utils import read_file, export_flashcards, export_anki

st.set_page_config(page_title="LLM Flashcard Generator", layout="centered")
st.title("🧠 LLM-Powered Flashcard Generator")

uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])
raw_text = st.text_area("Or paste content directly here", height=250)
subject = st.selectbox("Select Subject (optional)", ["General", "Biology", "CS", "History"])
language = st.selectbox("Generate flashcards in", ["English", "Hindi", "Spanish", "French"])

if st.button("Generate Flashcards"):
    if uploaded_file:
        text = read_file(uploaded_file)
    elif raw_text.strip():
        text = raw_text
    else:
        st.warning("Please upload a file or paste some text.")
        st.stop()

    flashcards = generate_flashcards(text, subject, language)

    if not flashcards:
        st.error("No flashcards generated. Try with more content.")
    else:
        st.success(f"Generated {len(flashcards)} flashcards.")
        for i, card in enumerate(flashcards, 1):
            st.markdown(f"**Q{i}:** {card['question']}")
            st.markdown(f"**A{i}:** {card['answer']}")
            st.markdown(f"_Difficulty:_ {card.get('difficulty', 'Medium')}")
            st.markdown("---")

        with st.expander("Download Flashcards"):
            export_format = st.radio("Choose format", ["CSV", "JSON", "Anki"])
            if export_format == "CSV":
                st.download_button("Download CSV", export_flashcards(flashcards, 'csv'), "flashcards.csv")
            elif export_format == "JSON":
                st.download_button("Download JSON", export_flashcards(flashcards, 'json'), "flashcards.json")
            else:
                st.download_button("Download Anki (TXT)", export_anki(flashcards), "flashcards_anki.txt")
