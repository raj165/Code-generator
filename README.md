# ⚙ Code Generator API  
AI-powered code generation API using **Azure OpenAI GPT-4o**, **FastAPI**, **LangChain**, and **Poetry**.

This service provides a REST API endpoint that generates high-quality, production-ready code based on natural-language prompts using Azure OpenAI GPT-4o.

---

##  Features

- Generate Python, FastAPI, Node.js, React, TypeScript, Go, and more  
-  Powered by **Azure OpenAI GPT-4o**  
-  LangChain `@tool` integration for agent workflows  
-  FastAPI backend with automatic docs   
-  Dependency-managed with Poetry  
 

---


---

## 🔧 Requirements

- Python **3.12+**
- Poetry **1.8.4**
- Azure OpenAI Service access


---

## ⚙️ Environment Variables

Create a `.env` file at the project root:

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_VERSION=2024-05-01-preview
AZURE_OPENAI_API_KEY=<your-key>
```






