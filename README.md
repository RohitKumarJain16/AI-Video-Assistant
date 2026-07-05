# 🎬 AI Video Assistant

AI Video Assistant is a Python-based Generative AI application that converts video or audio content into useful meeting insights.

The application accepts a YouTube URL or a local audio/video file, processes the audio, generates a transcript, summarizes the content, extracts important meeting information, and allows users to ask questions about the transcript using a RAG-based chat system.

## 🚀 Features

- Accepts YouTube URLs and local audio/video files.
- Downloads and converts audio into WAV format.
- Splits long audio into smaller chunks for transcription.
- Transcribes English audio using Whisper.
- Supports Hinglish speech transcription and translation using Sarvam AI.
- Generates a title from the transcript.
- Generates a summary of long transcripts.
- Extracts action items from meeting conversations.
- Extracts key decisions.
- Identifies unresolved questions and topics that need follow-up.
- Builds a vector database from the transcript.
- Uses Retrieval-Augmented Generation (RAG) to answer questions about the processed content.
- Provides a Streamlit-based user interface.

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- OpenAI Whisper
- Sarvam AI
- Hugging Face Embeddings
- FAISS
- yt-dlp
- pydub
- FFmpeg

## 📂 Project Structure

```text
AI-Video-Assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── extractor.py
│   ├── rag_engine.py
│   ├── summarizer.py
│   ├── transcriber.py
│   └── vector_store.py
│
└── utils/
    └── audio_processor.py
```

## ⚙️ How It Works

```text
YouTube URL / Local Audio or Video File
                    ↓
              Audio Processing
                    ↓
              Audio Chunking
                    ↓
          Whisper / Sarvam AI
                    ↓
                 Transcript
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    Summary    Action Items   Decisions &
                              Open Questions
                    ↓
             Vector Database
                    ↓
          RAG-Based Question Answering
```

## 🔐 Environment Variables

Create a `.env` file in the root directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
WHISPER_MODEL=small
```

Do not upload the `.env` file to GitHub.

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/RohitKumarJain16/AI-Video-Assistant.git

cd AI-Video-Assistant
```

Create and activate a virtual environment.

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Make sure FFmpeg is installed and available in your system PATH.

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

Open the local Streamlit URL shown in the terminal.

Enter a YouTube URL or local audio/video file path, select the language, and run the processing pipeline.

After processing is complete, the application displays the generated title, transcript, summary, action items, key decisions, and open questions.

You can also ask questions about the processed content using the RAG-based chat feature.

## 🎯 What I Learned

While building this project, I worked with:

- Audio and video preprocessing.
- Speech-to-text transcription using Whisper.
- Speech translation and transcription APIs.
- Prompt engineering and LLM chains using LangChain.
- Processing long transcripts using text splitting.
- Extracting structured information from unstructured conversations.
- Creating embeddings and storing them in a FAISS vector database.
- Building a Retrieval-Augmented Generation pipeline.
- Managing environment variables and external API keys.
- Integrating multiple AI components into a complete application.
- Building an interactive application using Streamlit.

## 🔮 Future Improvements

- Support direct file uploads from the Streamlit interface.
- Add speaker diarization.
- Add timestamps to transcripts.
- Improve temporary file cleanup.
- Add support for more languages.
- Export summaries and meeting insights as PDF or text files.
- Add persistent vector database storage.
- Deploy the application online.

## 👨‍💻 Author

**Rohit Kumar Jain**

GitHub: https://github.com/RohitKumarJain16

## 📄 License

This project is created for learning and educational purposes.
