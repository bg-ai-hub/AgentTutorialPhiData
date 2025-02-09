
# AgentTutorialPhiData

A brief description of what this project does and who it's for


## Overview

AgentTutorialPhiData is a comprehensive tutorial repository designed to guide developers and AI enthusiasts through the process of building, deploying, and optimizing AI-powered agents using PhiData. The repository provides hands-on examples, best practices, and code implementations to help users effectively integrate AI agents into their projects.
## Features

- Step-by-step tutorials: Covers various stages of AI agent development.
- Pre-built examples: Ready-to-use Python scripts and configurations.
- Optimized AI agent workflows: Demonstrates best practices for performance and efficiency.
- Integration with PhiData: Illustrates how to connect AI agents with PhiData services.
- Modular design: Components can be easily adapted for custom AI agent applications.

## Prerequisites
- Before using this repository, ensure you have the following installed:
- Python 3.8+
- Git
- Required Python packages (specified in requirements.txt)
- An active PhiData account (if required for integration)
## Installation

Install my-project with npm

```bash
# Clone the repository
git clone https://github.com/bg-ai-hub/AgentTutorialPhiData.git
cd AgentTutorialPhiData

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```
    
## Documentation

```
1_simple_groq_agent.py : Python program that demonstrates the implementation of a simple agent using the Groq API. 
It showcases how to set up an agent, define its behavior, and interact with the Groq platform for processing tasks.

2_finance_agent.py : Python program that demonstrates the creation of a financial analysis agent using the Agno framework. 
It sets up a team of agents, including a Web Agent for searching and analyzing the latest news, a Finance Agent for analyzing financial data and market trends, and a Lead Editor to coordinate and combine insights from both agents. 
The script provides example prompts to interact with the agent team, such as analyzing the impact of AI developments on NVIDIA's stock (NVDA) or summarizing recent developments and stock performance of Microsoft (MSFT). 

3_agent_teams.py : Python script demonstrates how to create a team of agents using the Phi framework. 
It sets up a Web Agent and a Finance Agent, both utilizing the OpenAIChat model (gpt-4o-mini). 
The Web Agent is equipped with the DuckDuckGo tool for web searches, while the Finance Agent uses YFinanceTools to access financial data. 
These agents are then combined into an agent team that can collaboratively handle tasks requiring both web search and financial analysis.
```


## Contributing

Contributions are always welcome!

```
# Fork the repository
# Create a new branch
git checkout -b feature-branch

# Commit your changes
git commit -m 'Add new feature'

# Push to your branch
git push origin feature-branch

# Open a pull request on GitHub
```


## Support

If you encounter any issues, feel free to open an issue on GitHub.

