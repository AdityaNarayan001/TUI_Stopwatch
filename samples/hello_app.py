from textual.app import App, ComposeResult
from textual.widgets import Static

class HelloApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Hello, Aditya!", id="greeting")

    CSS = """
    #greeting {
        align: center middle;
        color: green;
        text-style: bold;
    }
    """

if __name__ == "__main__":
    app = HelloApp()
    app.run()
