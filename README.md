# GitHub Basic Collaboration Guide

This repository explains a simple GitHub team workflow for small projects.[cite:23] It focuses on the basic process: fork the repository, clone it to a local computer, create a branch, make changes, commit, push, and create a pull request.[cite:32]

## Why use GitHub?
GitHub helps teams store code, track changes, and work together using repositories and Markdown documentation such as README files.[cite:23][cite:24] A README file is usually placed in the root of the repository and GitHub automatically shows it on the main repository page.[cite:23]

## Basic Workflow
1. Fork the repository on GitHub.
2. Clone your fork to your local computer.[cite:32]
3. Open the project folder.
4. Create a new branch.
5. Make changes.
6. Commit the changes.
7. Push the branch.
8. Create a pull request.

## Commands
```bash
git clone https://github.com/your-username/project-name.git
cd project-name
git checkout -b feature/login-page
git add .
git commit -m "feat: added login page"
git push origin feature/login-page
```

## Branch Example
```bash
git checkout -b feature/home-page
```

## Commit Example
```bash
git commit -m "fix: corrected navbar issue"
```

## Pull Request
After pushing your branch, open GitHub and create a pull request so the team leader can review and merge your changes.

## README Notes
GitHub supports Markdown formatting in README files, including headings, lists, code blocks, and links.[cite:24][cite:25] This makes README.md useful for showing project purpose, steps, and commands in a clean format.[cite:23][cite:24]
EOF && cp output/README.md output/github_readme_basic_template.md
