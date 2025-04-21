from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Static

class GreetApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="What's your name?", id="name_input")
        yield Button("Greet me!", id="greet_button")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        name = self.query_one("#name_input", Input).value
        output = self.query_one("#output", Static)
        output.update(f"Hello, {name or 'stranger'}! 👋")

    CSS = """
    #name_input, #greet_button, #output {
        align: center middle;
        width: 50%;
        margin: 1 0;
    }

    #output {
        color: magenta;
    }
    """

if __name__ == "__main__":
    GreetApp().run()
