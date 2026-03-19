
Process to instal & use the **Git hub**


## Step 1: Install Git (Do once)
1. Download Git from git-scm.com  
2. Install like any app  
3. Open terminal (Windows: Git Bash, Mac: Terminal)  
4. Type: `git --version` (should show version number)

## Step 2: Get Your Project (Clone)
1. Go to your GitHub repo page  
2. Click green "Code" button → copy HTTPS link  
3. In terminal: `git clone [paste-link-here]`  
4. `cd [folder-name]` (enter project folder)

## Step 3: Daily Work Pattern (Always follow this order)

```
START → Update main → Create your branch → Work → Push → Pull Request → END
```

## Step 4: Start Working (Your daily routine)

**Morning/Before starting work:**
```
1. git checkout main
2. git pull origin main  
3. git checkout -b my-feature-name
```
*Example: `git checkout -b fix-login-button`*

**While working:**
```
4. Edit files in VS Code
5. git status (see what changed)
6. git add . (stage all changes)
7. git commit -m "Fixed login button"
8. git push
```

## Step 5: Share Your Work (Pull Request)
1. Go to GitHub repo  
2. See yellow "Compare & pull request" banner → click it  
3. Write title: "Fix login button"  
4. Click "Create pull request"  
5. Wait for admin approval → Merge happens automatically

## Step 6: If Merge Conflict Happens (Don't panic!)

**What it looks like:** Git says "CONFLICT" in red

**Fix it:**
```
1. Open the conflicted file
2. Look for: <<<<<<< ======= >>>>>>> markers
3. Delete the markers, keep only YOUR final code
4. git add [filename]
5. git commit -m "Fixed conflicts"
6. git push
```

## Step 7: Team Rules (Print this!)
```
✅ ALWAYS start from fresh main
✅ One task = one branch  
✅ Branch names: feature/fix-login, bug/user-profile
✅ Small commits with clear messages
✅ Push daily, don't wait till end
✅ Never work directly on main branch
```

## Quick Commands Cheat Sheet
```
Check where I am: git branch
See changes: git status  
Save work: git add . && git commit -m "message"
Send to GitHub: git push
Get latest main: git checkout main && git pull
New branch: git checkout -b my-branch-name
```

## For Admin (You): Protect Your Main Branch
1. GitHub → Settings → Branches  
2. Add rule for `main`: "Require pull request reviews before merging"  
3. Done! No one can break main accidentally

**Copy this entire guide into your README.md file.** Team members can follow it like a recipe without thinking.