# Disco DSA Tutor - Premium DSA Chat Simulator 💬

NexusChat is a high-performance, aesthetically pleasing chat application built with **Streamlit**. It serves as a demonstration of fundamental Data Structures and Algorithms (DSA) applied to a real-world use case.

## ✨ Features
- **Modern UI**: Dark mode with Glassmorphism and smooth animations.
- **Linked List History**: All messages are stored in a custom-built Linked List for efficient sequential access.
- **Undo/Redo Stack**: Deleted messages are stored in a Stack, allowing for seamless recovery.
- **Message Queue**: Demonstrates asynchronous processing simulation using a Deque.
- **Real-time Analytics**: Monitor your data structures in real-time via the sidebar.

## 🛠 Tech Stack
- **Frontend/Backend**: Streamlit
- **Styling**: Custom CSS (Vanilla)
- **Data Structures**: Linked List, Stack, Queue

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:
   ```bash
   streamlit run chat_app.py
   ```

## 🧠 DSA Integration
- **Linked List**: Used as the primary data store for chat history to showcase node management.
- **Stack**: Implements the `Undo` functionality (Last-In-First-Out).
- **Queue**: Implements message processing simulation (First-In-First-Out).

