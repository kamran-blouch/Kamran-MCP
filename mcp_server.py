#!/usr/bin/env python3
"""
MCP Server for Task Manager API
This server provides tools to interact with the FastAPI Task Manager
"""

import asyncio
import json
import httpx
from typing import Any, Optional
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

# FastAPI server URL
API_BASE_URL = "http://localhost:8000"

# Create MCP server instance
server = Server("task-manager-mcp")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools for interacting with the Task Manager API"""
    return [
        Tool(
            name="get_all_tasks",
            description="Get all tasks from the Task Manager",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_task",
            description="Get a specific task by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "number",
                        "description": "The ID of the task to retrieve"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task",
            description="Create a new task in the Task Manager",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the task"
                    },
                    "description": {
                        "type": "string",
                        "description": "The description of the task"
                    },
                    "completed": {
                        "type": "boolean",
                        "description": "Whether the task is completed (default: false)"
                    }
                },
                "required": ["title", "description"]
            }
        ),
        Tool(
            name="update_task",
            description="Update an existing task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "number",
                        "description": "The ID of the task to update"
                    },
                    "title": {
                        "type": "string",
                        "description": "The new title of the task (optional)"
                    },
                    "description": {
                        "type": "string",
                        "description": "The new description of the task (optional)"
                    },
                    "completed": {
                        "type": "boolean",
                        "description": "Whether the task is completed (optional)"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="delete_task",
            description="Delete a task by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "number",
                        "description": "The ID of the task to delete"
                    }
                },
                "required": ["task_id"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool execution requests"""
    
    async with httpx.AsyncClient() as client:
        try:
            if name == "get_all_tasks":
                response = await client.get(f"{API_BASE_URL}/tasks")
                response.raise_for_status()
                tasks = response.json()
                return [
                    TextContent(
                        type="text",
                        text=json.dumps(tasks, indent=2)
                    )
                ]
            
            elif name == "get_task":
                task_id = arguments.get("task_id")
                response = await client.get(f"{API_BASE_URL}/tasks/{task_id}")
                response.raise_for_status()
                task = response.json()
                return [
                    TextContent(
                        type="text",
                        text=json.dumps(task, indent=2)
                    )
                ]
            
            elif name == "create_task":
                task_data = {
                    "title": arguments.get("title"),
                    "description": arguments.get("description"),
                    "completed": arguments.get("completed", False)
                }
                response = await client.post(f"{API_BASE_URL}/tasks", json=task_data)
                response.raise_for_status()
                task = response.json()
                return [
                    TextContent(
                        type="text",
                        text=f"Task created successfully:\n{json.dumps(task, indent=2)}"
                    )
                ]
            
            elif name == "update_task":
                task_id = arguments.get("task_id")
                update_data = {}
                if "title" in arguments:
                    update_data["title"] = arguments["title"]
                if "description" in arguments:
                    update_data["description"] = arguments["description"]
                if "completed" in arguments:
                    update_data["completed"] = arguments["completed"]
                
                response = await client.put(f"{API_BASE_URL}/tasks/{task_id}", json=update_data)
                response.raise_for_status()
                task = response.json()
                return [
                    TextContent(
                        type="text",
                        text=f"Task updated successfully:\n{json.dumps(task, indent=2)}"
                    )
                ]
            
            elif name == "delete_task":
                task_id = arguments.get("task_id")
                response = await client.delete(f"{API_BASE_URL}/tasks/{task_id}")
                response.raise_for_status()
                result = response.json()
                return [
                    TextContent(
                        type="text",
                        text=json.dumps(result, indent=2)
                    )
                ]
            
            else:
                raise ValueError(f"Unknown tool: {name}")
        
        except httpx.HTTPStatusError as e:
            return [
                TextContent(
                    type="text",
                    text=f"Error: {e.response.status_code} - {e.response.text}"
                )
            ]
        except Exception as e:
            return [
                TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )
            ]


async def main():
    """Main entry point for the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="task-manager-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )


if __name__ == "__main__":
    asyncio.run(main())

