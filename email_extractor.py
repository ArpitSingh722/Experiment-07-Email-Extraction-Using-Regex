"""
Experiment No. 7 (CO-3)
Develop a Python script using regular expressions (regex) to identify and
extract valid email addresses from a text file.
"""

import os
import re

# Regular expression pattern for standard valid email addresses
EMAIL_PATTERN = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"


def extract_emails_from_file(input_filepath: str, output_filepath: str) -> list[str]:
    """Reads text from input_filepath, extracts valid emails, and writes them to output_filepath."""
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file not found: '{input_filepath}'")

    with open(input_filepath, "r", encoding="utf-8") as infile:
        content = infile.read()

    # Find all matching email patterns
    matches = re.findall(EMAIL_PATTERN, content)

    # Remove duplicates while preserving original order
    unique_emails = list(dict.fromkeys(matches))

    with open(output_filepath, "w", encoding="utf-8") as outfile:
        for email in unique_emails:
            outfile.write(email + "\n")

    return unique_emails


def main() -> None:
    input_file = "sample_input.txt"
    output_file = "extracted_emails.txt"

    try:
        extracted_emails = extract_emails_from_file(input_file, output_file)

        print(f"Total unique valid emails found: {len(extracted_emails)}")
        print("-" * 45)
        for idx, email in enumerate(extracted_emails, start=1):
            print(f"{idx}. {email}")
        print("-" * 45)
        print(f"Results saved to '{output_file}'.")

    except FileNotFoundError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
