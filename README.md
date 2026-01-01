# 🐦 Floppy Bird — Flappy Bird Clone (Python + Pygame)

A lightweight **Flappy Bird** clone built with **Python** and **Pygame**.  
Simple, fast, and easy to extend — perfect as a mini game-dev project or for showcasing clean Python structure.

---

## 📌 Features
- Classic Flappy Bird gameplay loop (gravity + flap + pipes + scoring)
- Sprite-based rendering via **Pygame**
- Centralized configuration in `variables.py` for quick tuning
- Bundled game assets in `assets/` citeturn7view0

---

## 🎮 Controls
Typical controls (most clones use these):
- **Space / Left Click**: flap
- **Esc**: quit


---

## 🧱 Project Structure
```text
.
├── assets/            # Images / sounds used by the game
├── flappyBird.py      # Game loop + rendering + collision + scoring citeturn7view0
├── variables.py       # Constants/config (window, speed, gravity, etc.) citeturn7view0
├── requirements.txt   # Python dependencies citeturn7view0
└── .gitignore
```

---

## ✅ Requirements
- **Python 3.9+** (recommended)
- OS: Windows / macOS / Linux
- Dependencies installed from `requirements.txt` citeturn7view0

---

## 🚀 Quick Start

### 1) Clone
```bash
git clone https://github.com/pouriashiralipour/floppy-bird_python.git
cd floppy-bird_python
```

### 2) Create a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -U pip
pip install -r requirements.txt
```

### 4) Run the game
```bash
python flappyBird.py
```

---

## ⚙️ Customization

Tune gameplay in `variables.py` (recommended place for):
- Screen width/height
- FPS
- Gravity / jump impulse
- Pipe gap / speed
- Sprite sizes / offsets

> Keep all “game feel” knobs in `variables.py` so `flappyBird.py` stays clean and readable.

---

## 🖼️ Screenshots / Gameplay GIF

Add a `screenshots/` folder and include images/GIFs:

```text
screenshots/
  gameplay.gif
  home.png
```

Then embed here:

| Gameplay |
|---------|
| ![](screenshots/gameplay.gif) |

---

## 🧪 Development Tips

- Add a `src/` package for clean imports if the code grows:
  ```text
  src/
    game/
      __init__.py
      entities.py
      physics.py
      ui.py
  main.py
  ```
- Add formatting + linting:
  - `ruff` (lint + format) or `black` + `flake8`
- Add tests for non-graphical logic (collision math, scoring, pipe generation).

---

## 🗺️ Roadmap (Optional)
- [ ] Start menu + game over screen
- [ ] Sound effects + mute toggle
- [ ] Difficulty scaling
- [ ] High score persistence (JSON file)
- [ ] Packaging (Windows `.exe`) using PyInstaller

---

## 📦 Build an Executable (Optional)

Install PyInstaller:
```bash
pip install pyinstaller
```

Build:
```bash
pyinstaller --onefile --noconsole flappyBird.py
```

> If assets are loaded by relative paths, ensure you bundle them properly (PyInstaller `--add-data`).

---

## 📄 License
A license file is not visible from the root listing captured here; if you have one, link it.  
If you don’t, consider adding **MIT** for simple projects.

---

## 👤 Author
**Pouria Shirali**  
- GitHub: https://github.com/pouriashiralipour  
- LinkedIn: https://linkedin.com/in/pouriashiralipour  
- Instagram: https://instagram.com/pouria.shirali

---

## ⭐ Repo rename suggestions
If you want a more “GitHub-friendly” name:

- `flappy-bird-pygame`
- `flappy-bird-python`
- `floppy-bird-clone`
- `pygame-flappy-bird`
