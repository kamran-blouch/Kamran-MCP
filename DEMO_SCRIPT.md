# Demo Recording Script

Use this script as a guide when recording your screen demonstration.

---

## Before Recording

### Preparation Checklist:
- [ ] Clear your desktop/close unnecessary applications
- [ ] Set terminal font size to be readable (16-18pt recommended)
- [ ] Test your microphone (if recording audio)
- [ ] Have this script open for reference
- [ ] Open screen recording software
- [ ] Prepare 2 terminal windows

---

## Demo Script (5 minutes)

### Part 1: Introduction (30 seconds)

**Say:**
> "Hello! In this demo, I'll show you a FastAPI Task Manager application integrated with an MCP Server that works with Gemini CLI. Let me walk you through the setup and usage."

**Show:**
- Your desktop with the project folder open
- Briefly show the project structure in VS Code or File Explorer

---

### Part 2: Start FastAPI Server (1 minute)

**Say:**
> "First, I'll start the FastAPI server."

**Do:**
1. Open Terminal 1
2. Navigate to project:
   ```bash
   cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
   ```
3. Start the server:
   ```bash
   python app.py
   ```

**Show:**
- Server starting messages
- "Uvicorn running on http://0.0.0.0:8000"

**Say:**
> "The FastAPI server is now running. Let me verify it's working by opening the API documentation."

**Do:**
4. Open browser
5. Navigate to: `http://localhost:8000`
6. Show the welcome message
7. Navigate to: `http://localhost:8000/docs`
8. Show the interactive API documentation

**Say:**
> "Great! The API is working. Now let's move to the MCP server integration."

---

### Part 3: Gemini CLI MCP List (30 seconds)

**Say:**
> "Now I'll open a second terminal to interact with the MCP server through Gemini CLI."

**Do:**
1. Open Terminal 2 (keep Terminal 1 visible if possible)
2. Run:
   ```bash
   gemini mcp list
   ```

**Show:**
- The output showing available MCP servers
- Highlight where "task-manager" appears in the list

**Say:**
> "As you can see, our task-manager MCP server is registered and available. Now let's use it to manage tasks."

---

### Part 4: Using MCP Tools (2.5 minutes)

#### 4.1 Create Tasks

**Say:**
> "Let me create a few tasks using natural language through Gemini CLI."

**Do:**
```bash
gemini "Create a task with title 'Complete Project Documentation' and description 'Write comprehensive README and setup guides'"
```

**Show:**
- The command being typed
- The response showing task created

**Do:**
```bash
gemini "Create another task: title 'Record Demo Video', description 'Screen record the MCP server in action'"
```

**Show:**
- Task creation confirmation

**Do:**
```bash
gemini "Create one more task: title 'Push to GitHub', description 'Upload project to GitHub repository'"
```

#### 4.2 List All Tasks

**Say:**
> "Now let's see all the tasks we've created."

**Do:**
```bash
gemini "Show me all my tasks"
```

**Show:**
- All three tasks displayed in JSON format
- Point out the task IDs, titles, and completed status

#### 4.3 Update a Task

**Say:**
> "Let's mark the first task as completed."

**Do:**
```bash
gemini "Update task 1 and mark it as completed"
```

**Show:**
- The updated task with completed: true

**Say:**
> "We can also update the title or description."

**Do:**
```bash
gemini "Update task 2 title to 'Demo Video Completed'"
```

**Show:**
- The task with updated title

#### 4.4 Get Specific Task

**Say:**
> "I can retrieve details of a specific task."

**Do:**
```bash
gemini "Get details of task 2"
```

**Show:**
- Task 2 details displayed

#### 4.5 Delete a Task

**Say:**
> "Now let me delete one of the tasks."

**Do:**
```bash
gemini "Delete task 3"
```

**Show:**
- Deletion confirmation message

#### 4.6 Verify Changes

**Say:**
> "Let's verify the changes by listing all remaining tasks."

**Do:**
```bash
gemini "List all tasks"
```

**Show:**
- Only tasks 1 and 2 remaining
- Task 1 marked as completed
- Task 2 with updated title

---

### Part 5: FastAPI Verification (30 seconds)

**Say:**
> "Let me verify these changes are actually reflected in the FastAPI server."

**Do:**
1. Switch back to browser
2. Refresh or navigate to: `http://localhost:8000/docs`
3. Try the GET /tasks endpoint
4. Click "Try it out" → "Execute"

**Show:**
- The same tasks in the API response
- Matching the data from Gemini CLI

---

### Part 6: Conclusion (30 seconds)

**Say:**
> "To summarize, we have:"
> 
> "1. A FastAPI Task Manager running on port 8000"
> "2. An MCP Server that exposes tools to interact with the API"
> "3. Integration with Gemini CLI allowing natural language task management"
> "4. Full CRUD operations: Create, Read, Update, and Delete"
>
> "The MCP server acts as a bridge between Gemini CLI and the FastAPI backend, making it easy to manage tasks using conversational commands."
>
> "Thank you for watching!"

**Show:**
- Both terminals side by side
- The browser with API docs
- Maybe show the project structure one more time

---

## After Recording

### Post-Production Checklist:
- [ ] Review the recording
- [ ] Trim any unnecessary parts
- [ ] Add title slide if desired (optional)
- [ ] Export in 1080p MP4 format
- [ ] Name file: `demo-video.mp4`
- [ ] Upload to GitHub or YouTube/Loom

---

## Quick Command Reference

```bash
# Terminal 1 - FastAPI
python app.py

# Terminal 2 - Gemini CLI
gemini mcp list
gemini "Create a task: title 'Task Title', description 'Task Description'"
gemini "Show me all tasks"
gemini "Update task 1 and mark it as completed"
gemini "Get details of task 2"
gemini "Delete task 3"
gemini "List all tasks"
```

---

## Tips for a Great Recording

1. **Clear Audio**: Speak clearly and at a moderate pace
2. **Visible Text**: Ensure terminal text is large enough to read
3. **Smooth Navigation**: Practice the demo once before recording
4. **Highlight Important Parts**: Use your cursor to point at key information
5. **Keep It Concise**: Aim for 3-5 minutes total
6. **Show Confidence**: Don't worry about small mistakes, they show it's real!
7. **Good Lighting**: If using webcam, ensure you're well lit

---

## Alternative: No Audio Script

If not recording audio, add text overlays explaining:
- "Starting FastAPI Server"
- "Checking Available MCP Servers"
- "Creating Tasks via Gemini CLI"
- "Updating and Deleting Tasks"
- "Verifying Changes in API"

---

**Good luck with your recording! 🎬**

