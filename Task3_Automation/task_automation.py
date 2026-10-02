import os
import shutil
import re
import urllib.request

def move_jpg_files(source_dir="sample_source", dest_dir="jpg_archive"):
    """
    Automates moving all .jpg / .jpeg files from a source directory to a destination directory.
    Uses 'os' and 'shutil'.
    """
    print(f"\n--- [1] Moving JPG Files ---")
    if not os.path.exists(source_dir):
        os.makedirs(source_dir, exist_ok=True)
        # Create a few dummy sample files if empty
        with open(os.path.join(source_dir, "photo1.jpg"), "w") as f: f.write("sample image")
        with open(os.path.join(source_dir, "photo2.jpg"), "w") as f: f.write("sample image")
        with open(os.path.join(source_dir, "notes.txt"), "w") as f: f.write("sample notes")
        print(f"Created sample files in '{source_dir}'.")

    os.makedirs(dest_dir, exist_ok=True)
    moved_count = 0

    for file_name in os.listdir(source_dir):
        if file_name.lower().endswith((".jpg", ".jpeg")):
            source_file = os.path.join(source_dir, file_name)
            dest_file = os.path.join(dest_dir, file_name)
            shutil.move(source_file, dest_file)
            print(f"Moved: {file_name} -> {dest_dir}/")
            moved_count += 1

    print(f"Done! Total {moved_count} image(s) moved to '{dest_dir}'.\n")

def extract_emails(input_file="sample_contacts.txt", output_file="extracted_emails.txt"):
    """
    Automates extracting all email addresses from a text file and saves them to a new file.
    Uses 're' (regular expressions) and file handling.
    """
    print(f"\n--- [2] Extracting Email Addresses ---")
    if not os.path.exists(input_file):
        sample_text = (
            "Reach out to CodeAlpha at services@codealpha.tech or services.codealpha@gmail.com.\n"
            "For HR inquiries, email hr.department@company.org or careers_2026@startup.co.uk.\n"
            "Invalid samples: notanemail, @nodomain.com, test@.com\n"
        )
        with open(input_file, "w", encoding="utf-8") as f:
            f.write(sample_text)
        print(f"Created '{input_file}' with demo contact entries.")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Robust email regex pattern that avoids trailing punctuation
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z0-9]'
    emails = sorted(list(set(re.findall(email_pattern, content))))

    print(f"Found {len(emails)} unique email addresses:")
    for email in emails:
        print(f"  • {email}")

    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Saved extracted emails to '{output_file}'.\n")

def scrape_webpage_title(url="https://www.python.org", output_file="page_title.txt"):
    """
    Scrapes the title tag of a webpage and saves it to a file.
    Uses Python's standard library (urllib.request + re) for zero external dependencies.
    """
    print(f"\n--- [3] Scraping Webpage Title ---")
    print(f"Fetching title from: {url}")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')

        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            print(f"Found Title: \"{title}\"")

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"URL: {url}\nTitle: {title}\n")

            print(f"Saved title to '{output_file}'.\n")
        else:
            print("No <title> tag found on the webpage.\n")
    except Exception as e:
        print(f"Error fetching URL: {e}\n")

def main():
    while True:
        print("=" * 45)
        print("     TASK AUTOMATION SUITE (Python)")
        print("=" * 45)
        print("1. Move .jpg files to a new folder (os, shutil)")
        print("2. Extract email addresses from file (re, file I/O)")
        print("3. Scrape title of a webpage (urllib, re)")
        print("4. Run all automation tasks")
        print("5. Exit")
        choice = input("\nSelect an automation task (1-5): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            url = input("Enter URL (press Enter for 'https://www.python.org'): ").strip()
            if not url:
                url = "https://www.python.org"
            scrape_webpage_title(url)
        elif choice == "4":
            move_jpg_files()
            extract_emails()
            scrape_webpage_title()
        elif choice == "5":
            print("Exiting Task Automation Suite. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, 4, or 5.\n")

if __name__ == "__main__":
    main()
