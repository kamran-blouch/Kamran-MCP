# GitHub Repository Setup Guide

This guide will help you upload your project to GitHub and include your screen recording.

---

## Step 1: Create a GitHub Account

If you don't have one already, create an account at [github.com](https://github.com)

---

## Step 2: Install Git

### Windows:
Download Git from [git-scm.com](https://git-scm.com/download/win)

### Verify Installation:
```bash
git --version
```

---

## Step 3: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 4: Create a New Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Repository name: `task-manager-mcp-server` (or any name you prefer)
5. Description: `FastAPI Task Manager with MCP Server integration for Gemini CLI`
6. Choose **Public** (so it's accessible)
7. **DO NOT** initialize with README (we already have one)
8. Click **"Create repository"**

---

## Step 5: Initialize Git in Your Project

Open a terminal in your project directory:

```bash
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"
```

Initialize git:
```bash
git init
```

---

## Step 6: Record Your Demo Video

Before committing, record your screen demonstration showing:

1. **FastAPI Server Running**
   - Start the server: `python app.py`
   - Show it running in terminal
   - Open browser to http://localhost:8000

2. **Gemini CLI MCP List**
   - Open new terminal
   - Run: `gemini mcp list`
   - Show task-manager in the list

3. **Using MCP Tools**
   - Create tasks: `gemini "Create a task: title 'Demo Task', description 'This is a demo'"`
   - List tasks: `gemini "Show me all tasks"`
   - Update task: `gemini "Mark task 1 as completed"`
   - Delete task: `gemini "Delete task 1"`

### Recommended Screen Recording Tools:

**Windows:**
- **OBS Studio** (Free, Open Source): https://obsproject.com/
- **ShareX** (Free): https://getsharex.com/
- **Windows Game Bar** (Built-in): Press `Win + G`
- **Loom** (Free tier available): https://www.loom.com/

**Tips for Recording:**
- Record in 1080p (1920x1080) if possible
- Make sure text in terminal is readable
- Speak while recording to explain what you're doing
- Keep it under 5 minutes
- Show both terminals side by side if possible

### Save Your Video:

Save your recording as: `demo-video.mp4` or upload to YouTube/Loom

---

## Step 7: Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed
git status
```

---

## Step 8: Commit Your Changes

```bash
git commit -m "Initial commit: FastAPI Task Manager with MCP Server"
```

---

## Step 9: Link to GitHub Repository

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual GitHub username and repository name:

```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

Example:
```bash
git remote add origin https://github.com/johndoe/task-manager-mcp-server.git
```

---

## Step 10: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

If prompted for credentials:
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your account password)

### Creating a Personal Access Token:
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "Git Operations"
4. Select scopes: `repo` (all)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when pushing

---

## Step 11: Upload Your Demo Video

You have two options:

### Option A: Upload to GitHub (Recommended for small videos < 100MB)

1. Go to your GitHub repository
2. Click "Add file" → "Upload files"
3. Upload your `demo-video.mp4`
4. Commit the changes

Then update README to link to it:
```markdown
## 🎥 Demo Video

[Watch the demo video](./demo-video.mp4)
```

### Option B: Upload to YouTube/Loom (Recommended for large videos)

1. Upload your video to YouTube or Loom
2. Get the shareable link
3. Update README with the link:

```markdown
## 🎥 Demo Video

[Watch the demo on YouTube](https://youtube.com/watch?v=YOUR_VIDEO_ID)
```

Or for Loom:
```markdown
## 🎥 Demo Video

[Watch the demo on Loom](https://www.loom.com/share/YOUR_VIDEO_ID)
```

---

## Step 12: Update README with Video Link

1. Edit `README.md` in your GitHub repository
2. Add the video link in the "🎥 Video Demonstration" section
3. Commit the changes

---

## Step 13: Get Your Repository Link

Your repository URL will be:
```
https://github.com/YOUR-USERNAME/YOUR-REPO-NAME
```

This is the link you'll submit!

---

## Complete Git Command Summary

```bash
# Navigate to project
cd "C:\Users\PMLS\OneDrive\Desktop\Kamran MCP"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: FastAPI Task Manager with MCP Server"

# Add remote (replace with your info)
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### Issue: Git is not recognized
**Solution:** Install Git from [git-scm.com](https://git-scm.com/) and restart terminal

### Issue: Authentication failed
**Solution:** Use a Personal Access Token instead of password

### Issue: Large file warning
**Solution:** 
- For videos > 100MB, use YouTube/Loom instead
- Or use Git LFS: https://git-lfs.github.com/

### Issue: Push rejected
**Solution:**
```bash
git pull origin main --rebase
git push origin main
```

---

## Verification Checklist

Before submitting, verify:

- [ ] Repository is public on GitHub
- [ ] All project files are uploaded
- [ ] README.md displays correctly
- [ ] Demo video is accessible (either in repo or via link)
- [ ] Repository has a clear description
- [ ] All code is properly formatted
- [ ] .gitignore is working (no __pycache__, etc.)

---

## Example Repository Structure on GitHub

```
task-manager-mcp-server/
├── app.py
├── mcp_server.py
├── requirements.txt
├── setup.py
├── gemini_config.json
├── start_fastapi.bat
├── start_fastapi.sh
├── test_api.py
├── README.md
├── SETUP_INSTRUCTIONS.md
├── GITHUB_SETUP.md
├── .gitignore
└── demo-video.mp4 (or link in README)
```

---

## Final Step: Submit Your Link

Your submission should be:
```
https://github.com/YOUR-USERNAME/task-manager-mcp-server
```

Make sure the repository is **public** so it can be accessed!

---

**Congratulations! Your project is now on GitHub! 🎉**

