# CodeAlpha Python Programming Tasks

This repository contains solutions for the Python Programming Internship tasks assigned by **CodeAlpha**.

---

## 📌 Project Overview

This repository includes implementations for the following 4 tasks:

| Task # | Task Name | Description | Key Modules / Concepts |
| :--- | :--- | :--- | :--- |
| **Task 1** | **Hangman Game** | Interactive text-based word guessing game with 6 allowed incorrect attempts and ASCII visual stages. | `random`, `while` loops, strings, lists |
| **Task 2** | **Stock Portfolio Tracker** | Calculates total portfolio value from stock quantities and hardcoded dictionary prices, with CSV/TXT export. | `dict`, arithmetic, file I/O (`csv`) |
| **Task 3** | **Task Automation Scripts** | Automates repetitive file management (moving JPGs), regex email extraction, and web title scraping. | `os`, `shutil`, `re`, `urllib` |
| **Task 4** | **Basic Chatbot** | Rule-based conversational chatbot answering inquiries, date/time, jokes, and farewells. | `if-elif`, functions, loops |

---

## 📂 Repository Structure

```text
CodeAlpha_Python_Tasks/
│
├── Task1_Hangman/
│   └── hangman.py               # Hangman text game
│
├── Task2_Stock_Tracker/
│   └── stock_tracker.py         # Portfolio value calculator & exporter
│
├── Task3_Automation/
│   └── task_automation.py       # File mover, email extractor, webpage title scraper
│
├── Task4_Chatbot/
│   └── chatbot.py               # Rule-based conversational chatbot
│
└── README.md                    # Project documentation
```

---

## 🚀 How to Run the Tasks

Ensure you have **Python 3.x** installed. You can execute any task directly using your terminal or command prompt:

### Task 1: Hangman Game
```bash
python Task1_Hangman/hangman.py
```
- A secret word is picked at random.
- Enter one letter at a time to uncover the word.
- You have 6 incorrect attempts before the game ends.

---

### Task 2: Stock Portfolio Tracker
```bash
python Task2_Stock_Tracker/stock_tracker.py
```
- Available stocks: `AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`, `NVDA`, `META`.
- Enter the stock symbol and share quantity.
- Type `done` to calculate the total portfolio value.
- Choose whether to save the report to `portfolio_summary.txt` or `portfolio_summary.csv`.

---

### Task 3: Task Automation Scripts
```bash
python Task3_Automation/task_automation.py
```
Provides an interactive menu for:
1. **Move .jpg files**: Automatically moves all `.jpg` images from a source folder into an archive directory.
2. **Extract email addresses**: Parses text files using regular expressions (`re`) and outputs extracted emails to `extracted_emails.txt`.
3. **Scrape webpage title**: Retrieves and saves the title tag of any given URL.

---

### Task 4: Basic Chatbot
```bash
python Task4_Chatbot/chatbot.py
```
- Chat interactively in the console.
- Try greetings (`"hello"`), asking how it is (`"how are you"`), requesting time/date, asking for a joke (`"joke"`), or saying goodbye (`"bye"`).

---

## 🛠️ Submission Checklist for CodeAlpha

1. **Repository Naming**: Ensure the GitHub repository name follows: `CodeAlpha_PythonProgramming` (or `CodeAlpha_<TaskName>`).
2. **LinkedIn Post**: Share a brief video explanation/demo of the projects and tag **@CodeAlpha**.
3. **Submission Form**: Submit the GitHub repository link and LinkedIn post link through the official CodeAlpha submission form.
