"""
Main entry point for the Console Todo App.

This application provides a command-line interface for managing tasks.
Users can add, view, update, delete, and mark tasks as complete/incomplete.
"""

from cli.menu import TodoMenu

def main():
    """Main function to start the Todo application."""
    print("Welcome to the Todo App!")
    menu = TodoMenu()
    menu.run()

if __name__ == "__main__":
    main()