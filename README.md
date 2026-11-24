# Experiment No. 7: Email Pattern Extraction Using Regular Expressions

**Course Outcome:** CO-3  
**Student:** Vastav Nandedkar  
**Institution:** School of Computing, MIT Art, Design and Technology University, Pune  

## Aim
Develop a Python script using regular expressions (`regex`) to identify and extract valid email addresses from a text file.

## Problem Statement
Write a Python program that reads unstructured text from an input file (`sample_input.txt`), applies a regular expression pattern using Python's built-in `re` module to detect valid email addresses while ignoring malformed strings, prints the results, and saves the extracted emails to an output file (`extracted_emails.txt`).

## Regex Pattern Breakdown
```regex
\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b
```
- `\b` — Word boundary to avoid partial matches.
- `[a-zA-Z0-9._%+-]+` — Username/local part (letters, digits, and allowed special characters).
- `@` — Mandatory `@` separator.
- `[a-zA-Z0-9.-]+` — Domain name.
- `\.[a-zA-Z]{2,}` — Dot followed by a top-level domain (TLD) of at least 2 characters.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Experiment-07-Email-Extractor.git
   cd Experiment-07-Email-Extractor
   ```
2. Run the script:
   ```bash
   python email_extractor.py
   ```
3. View the extracted addresses in the terminal or open `extracted_emails.txt`.
