# AI-Based Tic-Tac-Toe Game 🧠❌⭕

## 📌 Description
An AI-powered Tic-Tac-Toe game developed using Python.  
The game allows a human player to compete against an intelligent AI opponent that uses the **Minimax algorithm** to make optimal decisions.

The AI evaluates all possible game states recursively and always selects the best possible move, ensuring it never loses.

---

## 🎯 Features
- Human vs AI gameplay  
- Optimal AI decision-making using the Minimax algorithm  
- Clean and modular code structure  
- Command-line interface (CLI)  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Algorithm:** Minimax  
- **Interface:** Command Line Interface (CLI)  

---

## 📂 Project Structure
```
AI_TicTacToe/
│
├── main.py              # Entry point of the application
├── board.py             # Board creation and display logic
├── game.py              # Game flow and user interaction
├── minimax.py           # AI logic using Minimax algorithm
├── utils.py             # Helper functions (win/draw checks)
├── README.md            # Project documentation
```

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/KedarPoul/AI-Based-Tic-Tac-Toe-Game.git
```

### 2. Navigate to the Project Directory
```bash
cd AI-Based-Tic-Tac-Toe-Game
```



> No external libraries are required.

### 3. Run the Game
```bash
python main.py
```

---

## 🎮 How to Play
- You play as **X**
- AI plays as **O**
- Enter numbers from **1 to 9** to make a move:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## 🚀 Future Enhancements
- Add Alpha-Beta Pruning for optimization  
- Create a GUI using Tkinter or Pygame  
- Add score tracking (wins/losses/draws)  

---

## 📄 License
This project is open-source and available for learning and educational purposes.

