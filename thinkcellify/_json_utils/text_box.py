__all__ = ["create_text_box"]

def create_text_box(name, text):
    """
    Create a simple text box represented as a dictionary with a name and table.

    Args:
        name (str): The name of the text box.
        text (str): The text content to display inside the box.

    Returns:
        dict: A dictionary containing the name and a table with a single cell containing the text.

    Example:
        >>> create_text_box(name="Greeting", text="Hello, world!")
        {
        'name': 'Greeting',
        'table': [[{'string': 'Hello, world!'}]]
    }
    """
    return {
        "name": f"{name}",
        "table": [[{"string": f"{text}"}]]
    }












