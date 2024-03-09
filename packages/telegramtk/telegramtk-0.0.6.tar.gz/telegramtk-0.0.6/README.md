# telegramtk

**Telegram toolkit**

This package provides easy (and sync) access for the Telegram Bot API.

## Installation

```console
pip install telegramtk
```

## Setup

```python
import telegramtk

telegramtk.init('<your-telegram-bot-token-here>')
```

## Send message

```python
import telegramtk

telegramtk.send_message(to, msg)
```

→ `msg` can be "Markdown" formatted.

## Escape markdown

It's common to send Markdown content through Telegram, but sometimes we want to escape Markdown symbols in order to avoid syntax errors when parsing.

For that end, you might use the following function:

```python
from telegramtk.utils import escape_markdown

>>> escape_markdown('Just some *Markdown* _stuff_ [here](https://example.com/)')
'Just some \\*Markdown\\* \\_stuff\\_ \\[here\\]\\(https://example\\.com/\\)'
```

> 💡 Source: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/telegram/helpers.py#L45
