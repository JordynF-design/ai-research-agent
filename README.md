# AI Research Agent

A Python-powered AI research tool that searches for information, uses OpenAI to generate research summaries, and creates downloadable PDF reports with clickable source links.

## Features

- **Automated Research:** Search Wikipedia for information about a topic.
- **AI-Powered Summaries:** Use OpenAI to organize research into readable summaries.
- **PDF Report Generation:** Create formatted PDF research reports.
- **Clickable Sources:** Open original research sources directly from the PDF.
- **Page Numbering:** Automatically number report pages.
- **Interactive Menu:** Research multiple topics or exit the application.

## Technologies Used

- Python
- OpenAI API
- Wikipedia API
- Requests
- ReportLab
- python-dotenv
- Git and GitHub

## Project Structure

```text
ai-research-agent/
├── main.py
├── research.py
├── summarize.py
├── pdf_report.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JordynF-design/ai-research-agent.git
cd ai-research-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `.env` in the project directory.

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload your `.env` file or share your API key publicly.

## Running the Application

Start the application with:

```bash
python main.py
```

Choose the research option, enter a topic, and allow the application to search for information, generate an AI summary, and create a PDF report.

## Example Research Topics

- Cybersecurity
- Artificial Intelligence
- Software Engineering
- Machine Learning
- Cloud Computing

## Future Improvements

- Add more research sources.
- Improve research accuracy and source validation.
- Add PDF customization options.
- Develop a web-based user interface.
- Add advanced AI research capabilities.

## Author

**Jordyn Flynn**

Computer Science Student | Aspiring Software Engineer

[GitHub Profile](https://github.com/JordynF-design)
