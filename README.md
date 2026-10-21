---
title: Digital Twin Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.29.0
app_file: app.py
pinned: false
---

# Digital Twin Assistant 🤖

An advanced, AI-powered personal assistant designed to replicate and interact with domain-specific knowledge using a robust Retrieval-Augmented Generation (RAG) architecture.

## Features

- **Natural Conversation:** Engaging, human-like dialogue powered by advanced language models.
- **Context-Aware Responses:** Retrieves precise knowledge dynamically to ground assistant answers.
- **Persistent Memory:** Maintains conversation continuity and context across multiple sessions.
- **Tool Integration:** Capable of invoking specialized tools to execute real-time actions.
- **Interactive UI:** Built with Streamlit for a clean, responsive user experience.

## Tech Stack

- **LLM:** Claude Sonnet
- **Knowledge Retrieval:** RAG (Retrieval-Augmented Generation)
- **Framework:** Streamlit

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/blackbox24/DigitalTwin.git](https://github.com/blackbox24/DigitalTwin.git)
   cd DigitalTwin

```

2. Install the required dependencies:
```bash
pip install -r requirements.txt

```


3. Configure your environment variables:
* Add your API keys and configuration settings in the app settings or via a `.env` file.


4. Run the Streamlit application:
```bash
streamlit run app.py

```



## Built With

Part of the **LLM Foundations** course.

---

### What was improved:
* **Enhanced Visual Hierarchy:** Added relevant emojis and clearer headers (`##`) for better readability.
* **Expanded Tech Stack & Features:** Grouped features cleanly with bullet points and explicitly highlighted the core components.
* **Actionable Setup Guide:** Replaced the brief setup note with standard developer steps (cloning, installing dependencies, running the app) so anyone viewing your repo can easily test it.
