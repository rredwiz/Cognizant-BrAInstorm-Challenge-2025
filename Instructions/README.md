# Instructions & Demo Guide

Document exactly how judges or mentors can experience your solution. Update this file as the project evolves so it remains the single source of truth.

## Quick Start

1. Clone the repo and check out the main branch.

2. Install dependencies:

    - Ensure Python 3.9+ is installed on your machine.
    - Create a virtual environment and run the script for your shell: `python -m venv .venv`.
    - Navigate to the backend folder in from root/Codebase/backend/ and install python dependencies: `pip install -r requirements.txt`.
    - Ensure Node.js is updated to at least Node.js 18.18.0 or higher, with recommended Node.js 20.x for LTS.
    - Next, ensure the frontend node modules are installed by navigating to /Codebase/frontend/ and running `npm install`.

3. Set required environment variables or secrets:

    - Create a .env file inside of backend/
    - Create a field "GEMINI_API_KEY" and use Google AI Studio to set this to an api key value.

4. Run the project locally using the commands in the next section.

## Local Run Commands

| Step             | Command                           | Notes                                                             |
| ---------------- | --------------------------------- | ----------------------------------------------------------------- |
| Install Backend  | `pip install -r requirements.txt` | Navigate to Codebase/backend/ first                               |
| Install Frontend | `npm install`                     | Navigate to Codebase/frontend/ first                              |
| Train            | N/A                               | Pre-trained YOLO model (yoloe-11l-seg-pf.pt) included in backend/ |
| Evaluate         | N/A                               | No evaluation step required                                       |
| Serve Backend    | `python api.py`                   | Run from Codebase/backend/ with activated venv                    |
| Serve Frontend   | `npm run dev`                     | Run from Codebase/frontend/ in separate terminal                  |

## Environment Variables

| Name             | Purpose                                 | Example                    |
| ---------------- | --------------------------------------- | -------------------------- |
| `GEMINI_API_KEY` | Google Gemini API for recipe generation | `AIzaSyDxxxxxxxxxxxxxxxxx` |

## Hosted Demo / Video

-   Video walkthrough: [Add URL](https://example.com/video)

## Troubleshooting

-   Common issue 1 → GEMINI_API_KEY not set. Check .env file exists in backend/ and contains GEMINI_API_KEY=your_key with no quotes.
-   Common issue 2 → Module not found errors. Ensure virtual environment is activated before running pip install.

Keep this guide concise and up to date—reviewers will follow it verbatim.
