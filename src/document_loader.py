from pathlib import Path
from llama_parse import LlamaParse
from src.config import LLAMAPARSE_API_KEY, LLAMAPARSE_CONFIG, PROCESSED_FILES_DIR


def load_document(file_path: str | Path) -> str:
    """
    Load a PDF or DOCX file and return its content as markdown.

    Args:
        file_path: Path to the document (PDF or DOCX)

    Returns:
        Document content as markdown string
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    parser = LlamaParse(
        api_key=LLAMAPARSE_API_KEY,
        **LLAMAPARSE_CONFIG
    )

    documents = parser.load_data(str(file_path))

    # Combine all pages into single markdown string
    content = "\n\n".join(doc.text for doc in documents)

    return content


def load_and_save(file_path: str | Path, output_name: str = None) -> str:
    """
    Load a document and save the parsed markdown to processed_files.

    Args:
        file_path: Path to the document
        output_name: Optional name for output file (without extension)

    Returns:
        Document content as markdown string
    """
    file_path = Path(file_path)
    content = load_document(file_path)

    # Determine output filename
    if output_name is None:
        output_name = file_path.stem

    output_path = PROCESSED_FILES_DIR / f"{output_name}.md"
    output_path.write_text(content)

    return content


def load_triplet(trial_id: str, raw_dir: Path = None) -> dict:
    """
    Load a complete SAP triplet (protocol, original SAP, generated SAP).

    Args:
        trial_id: The trial identifier (e.g., "NCT03676192")
        raw_dir: Directory containing raw files (defaults to RAW_FILES_DIR)

    Returns:
        Dictionary with keys: protocol, original_sap, generated_sap
    """
    from src.config import RAW_FILES_DIR

    if raw_dir is None:
        raw_dir = RAW_FILES_DIR

    raw_dir = Path(raw_dir)

    # Expected file patterns
    files = {
        "protocol": raw_dir / f"{trial_id}_protocol.pdf",
        "original_sap": raw_dir / f"{trial_id}_original_sap.pdf",
        "generated_sap": raw_dir / f"{trial_id}_generated_sap.pdf",
    }

    # Check for DOCX alternatives
    for key, path in files.items():
        if not path.exists():
            docx_path = path.with_suffix(".docx")
            if docx_path.exists():
                files[key] = docx_path

    # Load all documents
    triplet = {}
    for key, path in files.items():
        if not path.exists():
            raise FileNotFoundError(f"Missing {key} file: {path}")
        triplet[key] = load_document(path)

    return triplet
