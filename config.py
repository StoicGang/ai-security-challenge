from pathlib import Path
 
# Project Root
ROOT_DIR = Path(__file__).resolve().parent

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
MODEL_NAME = "all-MiniLM-L6-v2"

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