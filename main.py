from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.runnables import RunnableConfig
from code_agent import generate_code_tool
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="WISPR Code Agent API",
    description="Generate production-ready code using Azure GPT-4o + LangChain",
    version="1.0.0",
)

class CodeGenRequest(BaseModel):
    query: str
    project_name: str = "WISPR Code Agent"
    language: str = "Python"



class CodeGenResponse(BaseModel):
    generated_code: str



@app.post("/generate", response_model=CodeGenResponse)
async def generate_code(req: CodeGenRequest):
    """
    Generate production-grade code using Azure OpenAI GPT-4o model.
    """
    try:
        # Build LangChain runnable configuration
        config = RunnableConfig(
            configurable={
                "project_name": req.project_name,
                "language": req.language,
            }
        )

        # Use .invoke() for LangChain tool
        logger.info(f"Generating code for query: {req.query}")
        generated_code = generate_code_tool.invoke({"query": req.query, "config": config})

        return CodeGenResponse(generated_code=generated_code)

    except Exception as e:
        logger.exception("Error generating code")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", tags=["Health Check"])
async def root():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "WISPR Code Agent API running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



