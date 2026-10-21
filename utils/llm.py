
import anthropic

def get_llm_response(prompt: str, api_key: str) -> str:
    """Send a prompt to the Anthropic API and return the response."""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"An error occurred: {e}"