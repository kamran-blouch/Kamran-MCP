# Step-by-Step Setup Instructions

## Complete Setup Guide for Task Manager MCP Server

Follow these steps carefully to set up and run the project.

---

## Part 1: Environment Setup

### 1.1 Install Python (if not already installed)

Download Python 3.10+ from [python.org](https://www.python.org/downloads/)

Verify installation:
```bash
python --version
```

### 1.2 Install Node.js (for Gemini CLI)

Download Node.js 18+ from [nodejs.org](https://nodejs.org/)

Verify installation:
```bash
node --version
npm --version
```

---

## Part 2: Project Setup

### 2.1 Navigate to Project Directory

```bash
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
```

### 2.2 Install Python Dependencies

```bash
pip install -r requirements.txt
```

Expected output: Successfully installed fastapi, uvicorn, pydantic, httpx, mcp

### 2.3 Install Gemini CLI

```bash
npm install -g @google/generative-ai-cli
```

Or use npx (no installation):
```bash
npx @google/generative-ai-cli --version
```

---

## Part 3: Configure Gemini CLI for MCP

### Option A: Using Config File (Recommended for Windows)

1. Create the Gemini config directory:
```powershell
mkdir "$env:APPDATA\Gemini" -Force
```

2. Create/edit the config file at `%APPDATA%\Gemini\config.json`:
```json
{
  "mcpServers": {
    "task-manager": {
      "command": "python",
      "args": ["C:\\Users\\PMLS\\OneDrive\\Desktop\\Kamran MCP\\mcp_server.py"],
      "cwd": "C:\\Users\\PMLS\\OneDrive\\Desktop\\Kamran MCP"
    }
  }
}
```

3. Save the file and restart your terminal

### Option B: Using Environment Variable

In PowerShell:
```powershell
$env:MCP_CONFIG = "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP\gemini_config.json"
```

In Command Prompt:
```cmd
set MCP_CONFIG=C:\Users\PMLS\OneDrive\Desktop\Kamran MCP\gemini_config.json
```

---

## Part 4: Running the Application

### 4.1 Start FastAPI Server (Terminal 1)

Open a new terminal window:

```bash
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
python app.py
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal running!**

### 4.2 Verify FastAPI is Running

Open a browser and visit: `http://localhost:8000`

You should see a welcome message with API endpoints.

Interactive docs: `http://localhost:8000/docs`

---

## Part 5: Testing with Gemini CLI

### 5.1 Open a New Terminal (Terminal 2)

Keep the FastAPI terminal running, open a NEW terminal window.

### 5.2 List Available MCP Servers

```bash
gemini mcp list
```

Expected output should include:
```
Available MCP Servers:
- task-manager
```

### 5.3 Test MCP Tools

#### Create a task:
```bash
gemini "Use the task manager to create a task with title 'Test Task' and description 'This is my first test task'"
```

#### Get all tasks:
```bash
gemini "Show me all tasks in the task manager"
```

#### Update a task:
```bash
gemini "Update task 1 to mark it as completed"
```

#### Get specific task:
```bash
gemini "Get details of task 1"
```

#### Delete a task:
```bash
gemini "Delete task number 1"
```

---

## Part 6: Verification Checklist

Before recording your demo, verify:

- [ ] Python 3.10+ installed and working
- [ ] All Python dependencies installed (`pip list` shows fastapi, uvicorn, etc.)
- [ ] Node.js and npm installed
- [ ] Gemini CLI installed or accessible via npx
- [ ] FastAPI server starts without errors on port 8000
- [ ] Can access http://localhost:8000 in browser
- [ ] Gemini CLI config file created and properly formatted
- [ ] `gemini mcp list` shows task-manager server
- [ ] Can create, read, update, and delete tasks via Gemini CLI

---

## Part 7: Recording Your Demo

### What to Show in Your Screen Recording:

1. **Start FastAPI Server:**
   - Open terminal
   - Navigate to project directory
   - Run `python app.py`
   - Show the server starting successfully

2. **Open Browser:**
   - Visit http://localhost:8000
   - Show the API welcome page
   - Optional: Show http://localhost:8000/docs

3. **Open Second Terminal:**
   - Show you're in the project directory
   - Run `gemini mcp list`
   - Show task-manager in the list

4. **Demonstrate MCP Tools:**
   - Create 2-3 tasks using Gemini CLI
   - Show all tasks
   - Update one task
   - Delete one task
   - Show remaining tasks

5. **Summary:**
   - Show both terminals running
   - Explain what was demonstrated

---

## Troubleshooting Common Issues

### Issue: "python not recognized"
**Solution:** Add Python to PATH or use `py` command instead

### Issue: Port 8000 already in use
**Solution:** Find and kill the process using port 8000:
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Issue: Gemini CLI can't find MCP server
**Solution:**
1. Check config file path and format
2. Use absolute paths in config
3. Restart terminal after config changes
4. Try environment variable method instead

### Issue: MCP tools return errors
**Solution:**
1. Verify FastAPI server is running
2. Test API directly: `curl http://localhost:8000/tasks`
3. Check mcp_server.py for correct API_BASE_URL

### Issue: Module not found errors
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

---

## Additional Resources

- FastAPI Documentation: https://fastapi.tiangolo.com/
- MCP Documentation: https://modelcontextprotocol.io/
- Gemini CLI: https://github.com/google/generative-ai-cli

---

## Quick Start Commands (Summary)

```bash
# Terminal 1 - Start FastAPI
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
python app.py

# Terminal 2 - Use Gemini CLI
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
gemini mcp list
gemini "Create a task: title 'My Task', description 'Task description'"
gemini "Show me all tasks"
```

---

**Remember:** Always keep the FastAPI server running in Terminal 1 while using Gemini CLI in Terminal 2!

