# FlightAgent.ai

<div align="center">
  <img src="https://ollama.com/public/ollama.png" alt="Ollama" height="100" style="margin: 0 20px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Meta-Logo.png/2560px-Meta-Logo.png" alt="Meta" height="100" style="margin: 0 20px;">
</div>

<br>

A fully local, stateful flight-booking assistant built around Meta's Llama 3.2 model. FlightAgent.ai combines natural language understanding with tool-calling and an embedded SQLite database to deliver a conversational travel agent that runs entirely on your machine.

This project demonstrates end-to-end AI engineering skills including prompt design, LLM integration, tool schema design, data validation, state management, and UI development.

> **⚠️ Note:** This project uses the 3B parameter model to avoid overwhelming MacBook RAM. While the 3B model excels at tool calling, it is **recommended to use 70B or 405B parameter models** for better conversational flow if you have sufficient hardware resources. With 3B parameters, the model primarily focuses on tool execution and struggles to maintain continuous natural conversation.

This project demonstrates end-to-end AI engineering skills including prompt design, LLM integration, tool schema design, data validation, state management, and UI development.

## Key Features

- **Local LLM Integration** – Uses the instruction-tuned Llama 3.2 3B model to interpret user requests. The model runs locally via Ollama, ensuring privacy and low latency. Conversations are seeded with a system prompt that guides the agent to behave like a flight booking assistant.

- **Tool Calling** – Implements a suite of JSON function schemas for adding flights, searching flights with multi-criteria filters (source, destination, airline, and maximum price), creating bookings, and retrieving user bookings. The agent automatically decides when to call a tool based on the conversation and continues calling tools until all required information is gathered.

- **SQLite Database** – Stores flight schedules, bookings, and user preferences in a local SQLite database. The schema is initialized via a Python script, and example flight data for Canadian routes is provided.

- **Natural Language Date Parsing** – A lightweight utility leverages the dateutil library to interpret fuzzy date expressions (e.g., "today after 6 pm").

- **Input Validation & Normalization** – Helper functions ensure that city names, prices, and other fields are cleaned and converted to the correct types before being persisted or queried.

- **Stateful Conversational Agent** – The chat function maintains conversation history and loops over the Llama 3.2 API until the model's responses no longer include tool calls, enabling multi-step interactions (e.g., ask for missing parameters, perform a search, and then book a flight).

- **Gradio UI** – A simple Gradio interface exposes the agent through a web chat, allowing non-technical users to interact with the assistant.

## Architecture Overview

The project is structured into four main components:

| Component | Description |
|-----------|-------------|
| **agent/** | Contains the core agent logic. `agent.py` defines the `SYSTEM_PROMPT` and the chat loop that orchestrates message history, Llama 3.2 completions, and tool calls. `tools.py` defines database functions, their JSON schemas, and a dispatcher (`handle_tool_calls`) that executes the appropriate function and formats the response. Small modules for LLM initialization (`llm.py`) and conversation memory (`memory.py`) encapsulate dependencies. |
| **database/** | Holds the SQLite database (`flights.db`), the schema definition, and a seed script. `init_db.py` creates tables for flights, bookings, and user preferences and populates them with sample data. |
| **utils/** | Utility functions for parsing dates and validating user input. These modules normalize city names, convert prices, and parse fuzzy date strings into ISO-8601 format. |
| **ui/** | A minimal Gradio app that launches a chat interface. The UI imports the chat function from `agent/agent.py` and exposes it to the browser. |

The Llama 3.2 model is accessed via the OpenAI Python client configured to point at an Ollama server. When the model responds with a `tool_calls` finish reason, the agent extracts the tool name and arguments, executes the corresponding Python function, and feeds the result back into the model, repeating until a final answer is returned.

## Setup & Installation

### 1. Install a Local Llama 3.2 Model

Follow the [Ollama installation guide](https://ollama.ai) and download the `llama3.2:3b` model (about 2 GB). Once installed, run the model server:

```bash
ollama run llama3.2:3b
```

Meta's 3B-parameter model excels at instruction following, summarization, prompt rewriting, and tool use, outperforming other open-source models in its size class.

### 2. Clone This Repository and Install Dependencies

```bash
git clone https://github.com/DhRuva-1509/FlightAgent.ai.git
cd FlightAgent.ai

# Create a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

**Required packages include:**
- `openai` for accessing the LLM
- `gradio` for the UI
- `python-dateutil` for natural language date parsing
- `sqlite3` (built into Python)

### 3. Initialize the Database

Populate the SQLite database with tables and sample flight data:

```bash
python database/init_db.py
```

### 4. Launch the UI

Start the Gradio application:

```bash
python ui/app.py
```

The chat interface will open in your browser. You can now ask the assistant to search for flights, filter by price or airline, and book seats.

## Usage Examples

### Searching for Flights

```
"Find me flights from Toronto to Vancouver with Air Canada under $500."
```

The assistant normalizes the city names and price, queries the database with your filters, and returns a list of matching flights with their IDs, departure times, durations, and number of stops.

### Booking a Flight

```
"Book seat 12A with a vegetarian meal on flight 3 under the name Alex."
```

The agent calls the booking tool, inserts a new record into the bookings table, and confirms the booking. You can then ask, "Show my bookings" to retrieve your reservations.

## Project Goals & Learning Outcomes

This project was built to solidify and showcase AI engineering skills:

- **Tool-Driven Agents** – Designing JSON schemas, implementing a dispatcher, and wiring them to the Llama 3.2 API demonstrates an understanding of function calling, a critical capability for modern multimodal agents.

- **Prompt and Conversation Management** – Crafting a system prompt that constrains model behavior and iterating over messages and tool calls highlight the importance of state management and safety when integrating LLMs into applications.

- **Database Integration** – Using SQLite shows how to persist structured data locally and query it efficiently. The schema was designed to allow multi-criteria searches and relational lookups.

- **User Experience** – Building a web interface with Gradio underscores the ability to translate AI prototypes into accessible products that non-technical users can try.

## Future Work

- Integrate real-time flight search APIs (e.g., Amadeus, Skyscanner) instead of the static seed data
- Add user authentication and persistent conversation sessions for personalized recommendations
- Deploy the model and UI using containerization (Docker) for easy sharing and scalability
- Experiment with larger models (e.g., Llama 3.2 1B or 70B) and evaluate performance vs. hardware constraints

## Contributing

Contributions are welcome! Feel free to open issues for feature requests or submit pull requests. Please ensure code adheres to PEP 8 standards and includes docstrings and type hints.

## Author

**Dhruva** – Aspiring AI Engineer with a passion for building practical applications powered by open-source models.

- GitHub: [@DhRuva-1509](https://github.com/DhRuva-1509)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/dhruva-patil-692baa214/)

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!