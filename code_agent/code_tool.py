import logging
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_openai import AzureChatOpenAI

from .prompt import codegen_prompt
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@tool(return_direct=True)
def generate_code_tool(query: str, config: RunnableConfig) -> str:
    """
    Generates high-quality, production-ready code using Azure OpenAI GPT-4o.

    Trigger:
        When the user requests code generation (e.g., "create FastAPI route", "build Python class").
    """
    try:

        project_name = config.get("configurable", {}).get("project_name", "Untitled Project")
        language = config.get("configurable", {}).get("language", "Python")



        # Replace these environment variables with your Azure OpenAI details
        llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            temperature=0.4,
        )

        runnable = codegen_prompt | llm | StrOutputParser()

        generated_code = runnable.invoke(
            {
                "query": query,
                "project_name": project_name,
                "language": language,
            }
        )

        return generated_code

    except Exception as e:
        logger.error(f"Error in generate_code_tool: {str(e)}")
        return f"Error: {str(e)}"



# if __name__ == "__main__":
#     config = RunnableConfig(
#         configurable={
#             "project_name": "WISPR Code Agent",
#             "container_name": "wispr-code-namespace",
#             "language": "Python",
#         }
#     )
#
#     query = "Create a FastAPI endpoint for uploading files to Azure Blob Storage."
#
#     # Correct modern invocation for LangChain Tools
#     response = generate_code_tool.invoke({"query": query, "config": config})
#
#     print("\nGenerated Code:\n")
#     print(response)


