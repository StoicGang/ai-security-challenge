from pathlib import Path
import os
from dotenv import load_dotenv

# Project Root
ROOT_DIR = Path(__file__).resolve().parent

# Load environment variables from the project's .env file
load_dotenv(
    dotenv_path=ROOT_DIR / ".env",
    override=True,
)

# Environment Variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GENAI_MODEL_NAME = os.getenv(
    "GENAI_MODEL_NAME",
    "models/gemini-3.5-flash",
)

if not GENAI_MODEL_NAME.startswith("models/"):
    GENAI_MODEL_NAME = f"models/{GENAI_MODEL_NAME}"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Embedding model (for sentence-transformers)
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Week Directories
WEEK_01 = ROOT_DIR / "Week-01"
WEEK_02 = ROOT_DIR / "Week-02"
WEEK_03 = ROOT_DIR / "Week-03"
WEEK_04 = ROOT_DIR / "Week-04"
WEEK_05 = ROOT_DIR / "Week-05"
WEEK_06 = ROOT_DIR / "Week-06"
WEEK_07 = ROOT_DIR / "Week-07"
WEEK_08 = ROOT_DIR / "Week-08"

# Shared Code
COMMON_DIR = ROOT_DIR / "common"
 
# Global Defaults
# NOTE: Do not override model names below; use the env vars instead.

# ChromaDB collection name
COLLECTION_NAME = "cybersecurity"

# Chunking defaults
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_OVERLAP = 200
 
# Helper Functions
def week_path(week: int) -> Path:
    return ROOT_DIR / f"Week-{week:02d}"


def day_path(week: int, day: int) -> Path:
    return week_path(week) / f"Day-{day:03d}"


def file_path(week: int, day: int, filename: str) -> Path:
    return day_path(week, day) / filename