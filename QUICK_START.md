# Quick Start Guide

Get up and running in 5 minutes!

---

## Prerequisites

- Python 3.10+
- Node.js 18+ (for Gemini CLI)
- Git (for GitHub upload)

---

## Installation (One-Time Setup)

```bash
# 1. Navigate to project
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install Gemini CLI
npm install -g @google/generative-ai-cli
```

---

## Configuration (One-Time Setup)

### Windows (PowerShell):
```powershell
# Create config directory
mkdir "$env:APPDATA\Gemini" -Force

# Create config file at: %APPDATA%\Gemini\config.json
# Add this content:
```

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

**Note:** Update paths to match your actual project location!

---

## Running the Application

### Terminal 1 - Start FastAPI Server:
```bash
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
python app.py
```

✅ Server should start on http://localhost:8000

### Terminal 2 - Use Gemini CLI:
```bash
# Verify MCP server is available
gemini mcp list

# Create a task
gemini "Create a task: title 'Buy groceries', description 'Milk, eggs, bread'"

# List all tasks
gemini "Show me all tasks"

# Update a task
gemini "Mark task 1 as completed"

# Get specific task
gemini "Get details of task 1"

# Delete a task
gemini "Delete task 1"
```

---

## Testing

### Test FastAPI directly:
```bash
# In a browser, visit:
http://localhost:8000
http://localhost:8000/docs

# Or use curl:
curl http://localhost:8000/tasks
```

### Test with Python script:
```bash
python test_api.py
```

---

## Common Issues

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Port 8000 in use"
```powershell
# Find process
netstat -ano | findstr :8000
# Kill it
taskkill /PID <PID> /F
```

### "MCP server not found"
- Check config file path and format
- Restart terminal after config changes
- Use absolute paths in config

---

## Next Steps

1. ✅ Test the application
2. 📹 Record your demo video
3. 📦 Upload to GitHub
4. 🎉 Submit your repository link

---

## File Structure

```
Kamran MCP/
├── app.py                 # FastAPI application
├── mcp_server.py         # MCP server
├── requirements.txt      # Dependencies
├── gemini_config.json   # Gemini config
├── README.md            # Full documentation
├── SETUP_INSTRUCTIONS.md # Detailed setup
├── GITHUB_SETUP.md      # GitHub guide
├── DEMO_SCRIPT.md       # Recording guide
└── QUICK_START.md       # This file
```

---

## Important URLs

- **FastAPI Server:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Interactive API:** http://localhost:8000/redoc

---

## Help & Documentation

- Full setup: See `SETUP_INSTRUCTIONS.md`
- GitHub upload: See `GITHUB_SETUP.md`
- Recording guide: See `DEMO_SCRIPT.md`
- Detailed info: See `README.md`

---

**Ready to go! 🚀**

