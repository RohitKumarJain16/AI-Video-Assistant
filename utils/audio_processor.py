import os
import tempfile
from pathlib import Path

import yt_dlp
from pydub import AudioSegment


CHUNK_LENGTH_MINUTES = 10
CHUNK_LENGTH_MS = CHUNK_LENGTH_MINUTES * 60 * 1000

TEMP_DIR = Path(tempfile.gettempdir()) / "ai_video_assistant"
TEMP_DIR.mkdir(parents=True, exist_ok=True)


def is_youtube_url(source: str) -> bool:
    """Check whether source looks like a YouTube URL."""

    source = source.lower().strip()

    return (
        "youtube.com/watch" in source
        or "youtu.be/" in source
        or "youtube.com/shorts/" in source
    )


def download_youtube_audio(url: str) -> str:
    """
    Download audio from YouTube and convert it to WAV.
    Returns the WAV file path.
    """

    output_template = str(TEMP_DIR / "youtube_audio.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],

        "quiet": False,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    wav_path = TEMP_DIR / "youtube_audio.wav"

    if not wav_path.exists():
        raise RuntimeError("YouTube audio download/conversion failed.")

    return str(wav_path)


def convert_to_wav(source_path: str) -> str:
    """
    Convert local audio/video file to WAV.
    """

    source_path = Path(source_path)

    if not source_path.exists():
        raise FileNotFoundError(
            f"Input file does not exist: {source_path}"
        )

    output_path = TEMP_DIR / "input_audio.wav"

    audio = AudioSegment.from_file(str(source_path))

    audio = (
        audio
        .set_channels(1)
        .set_frame_rate(16000)
        .set_sample_width(2)
    )

    audio.export(
        str(output_path),
        format="wav"
    )

    return str(output_path)


def split_audio(audio_path: str) -> list[str]:
    """
    Split WAV audio into smaller WAV chunks.
    """

    audio = AudioSegment.from_wav(audio_path)

    chunks = []

    for index, start in enumerate(
        range(0, len(audio), CHUNK_LENGTH_MS)
    ):

        end = start + CHUNK_LENGTH_MS

        chunk = audio[start:end]

        chunk_path = TEMP_DIR / f"chunk_{index}.wav"

        chunk.export(
            str(chunk_path),
            format="wav"
        )

        chunks.append(str(chunk_path))

    return chunks


def process_input(source: str) -> list[str]:
    """
    Main audio-processing entry point.

    Accepts:
    - YouTube URL
    - Local audio file
    - Local video file

    Returns:
        List of WAV chunk file paths.
    """

    source = source.strip()

    if not source:
        raise ValueError("Input source cannot be empty.")

    print("Processing input...")

    if is_youtube_url(source):

        print("YouTube URL detected.")

        audio_path = download_youtube_audio(source)

    else:

        print("Local file detected.")

        audio_path = convert_to_wav(source)

    print("Splitting audio into chunks...")

    chunks = split_audio(audio_path)

    if not chunks:
        raise RuntimeError("No audio chunks were created.")

    print(f"Created {len(chunks)} audio chunk(s).")

    return chunks
