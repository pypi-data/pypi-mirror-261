import re


def check_token(token: str) -> bool:
    if not token:
        raise ValueError('Bot token is undefined! Use init()')
    return True


def escape_markdown(text: str) -> str:
    ESCAPE_CHARS = r'\_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(ESCAPE_CHARS)}])', r'\\\1', text)
