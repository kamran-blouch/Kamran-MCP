from setuptools import setup, find_packages

setup(
    name="task-manager-mcp",
    version="1.0.0",
    description="MCP Server for Task Manager FastAPI Application",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn[standard]>=0.24.0",
        "pydantic>=2.5.0",
        "httpx>=0.25.1",
        "mcp>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "task-manager-mcp=mcp_server:main",
        ],
    },
    python_requires=">=3.10",
)

