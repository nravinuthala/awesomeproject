import pypandoc
import sys
import os

def convert_docx_to_md(input_file, output_file):
    """Convert DOCX to Markdown using pypandoc."""
    try:
        # Convert DOCX to Markdown and save to output file
        pypandoc.convert_file(input_file, 'gfm', outputfile=output_file, extra_args=['--extract-media=.'])
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.docx output.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Input file does not exist: {input_file}")
        sys.exit(1)

    convert_docx_to_md(input_file, output_file)
