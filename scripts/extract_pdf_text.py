import sys
from pathlib import Path
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path, output_path=None):
    pdf_path = Path(pdf_path)
    if output_path is None:
        output_path = pdf_path.with_suffix(".txt")

    reader = PdfReader(str(pdf_path))
    extracted_text = ""

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        extracted_text += f"\n\n--- Page {page_num} ---\n{text}\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"[INFO] Extracted text saved to {output_path}")
    return extracted_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <path_to_pdf> [output_txt_path]")
        sys.exit(1)

    pdf_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_text_from_pdf(pdf_file, out_file)
