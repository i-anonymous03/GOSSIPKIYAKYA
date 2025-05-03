This folder will contain detailed explanations for each code section as we go step-by-step.

Structure 
GossipKiyaKya/
├── app.py                 ← Flask main app
├── models.py              ← DB model
├── static/
│   ├── css/style.css      ← CSS styling
│   ├── js/script.js       ← JS if needed
│   └── uploads/           ← Profile pictures
├── templates/
│   ├── step1.html         ← Signup Step 1
│   ├── step2.html         ← Step 2 ...
│   ├── step3.html
│   ├── step4.html
│   ├── success.html       ← After signup
│   └── explanation.html   ← Code explanations
├── database/users.db      ← SQLite DB
├── README.md              ← Project guide
└── explanation/           ← Code explanation files

# Make changes in VS Code...
git add .
git commit -m "your message"
git push  # No need for -u origin main anymore!

# If You Need to Pull Changes
powershell
git pull