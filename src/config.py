import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_FILES_DIR = DATA_DIR / "raw_files"
PROCESSED_FILES_DIR = DATA_DIR / "processed_files"
OUTPUT_DIR = BASE_DIR / "output"
EVALUATIONS_DIR = OUTPUT_DIR / "evaluations"
REPORTS_DIR = OUTPUT_DIR / "reports"
PROMPTS_DIR = BASE_DIR / "prompts"

# API Keys
LLAMAPARSE_API_KEY = os.getenv("LLAMAPARSE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LlamaParse settings
LLAMAPARSE_CONFIG = {
    "result_type": "markdown",
    "verbose": True,
}

# Gemini settings
GEMINI_MODEL = "gemini-3-pro-preview"
GEMINI_CONFIG = {
    "temperature": 0.1,  # Low temperature for consistent evaluations
    "max_output_tokens": 8192,
}
