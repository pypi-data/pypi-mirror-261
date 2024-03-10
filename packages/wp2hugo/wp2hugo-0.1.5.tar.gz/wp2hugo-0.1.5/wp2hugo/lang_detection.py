"""
Module that accepts a Markdown object, parses it and extracts all
code fences, and attempts to guess which coding language it is,
and applies this to the code fence for syntax highlighting.
"""

import re

from magika import Magika
from markdown_it import MarkdownIt


def remove_blank_lines_at_end(content: str) -> str:
    """ "Takes the input, and strips away any blank lines at the end.

    Parameters
    -----------
    content: str
        A string object.
    Returns
    -------
        The string object with any blank lines removed.
    """
    lines = content.split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def ensure_carriage_return_at_end(content: str) -> str:
    """Takes the input, and ensure we have a carriage return at the end.

    Parameters
    ----------
    content: str
        A string object.
    Returns
    -------
        The string object with a carriage return at the end.
    """
    lines = content.split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    lines.append("")
    return "\n".join(lines)


def extract_code_blocks(markdown_content: str) -> list:
    """Parses the Markdown object, and returns a list of MD objects.

    Paramenters
    -----------
    markdown_content : str
      A string object with the Markdown content we want to find code blocks from.

    Returns
    -------
        A list of code blocks found within the markdown object.
    """
    md = MarkdownIt()
    tokens = md.parse(markdown_content)

    code_blocks = []

    for token in tokens:
        if token.type == "fence":
            code_blocks.append(token.content)

    return code_blocks


def detect_and_replace_languages(markdown_content: str) -> str:
    """
    Parses the Markdown object, and attempts to detect and replace
    code blocks with its correct language applied to the code fence.

    Paramenters
    -----------
    markdown_content : str
      A string object with the Markdown content we want code language applied to.
    """

    code_blocks = extract_code_blocks(markdown_content)
    m = Magika()

    for code_block in code_blocks:
        byte_representation = code_block.encode("utf-8")
        guess_language = m.identify_bytes(byte_representation)
        detected_language = guess_language.output.ct_label

        # First we need to escape all backwards slashes seperatly
        # This as the re parser chokes on \ if we don't.
        code_block = re.sub(r"\\", r"\\\\", code_block)
        escaped_block = re.escape(code_block)
        markdown_content = re.sub(
            escaped_block, f"```{detected_language}\n{code_block}", markdown_content
        )

    markdown_content = re.sub(r"```\n```", "```", markdown_content)
    markdown_content = remove_blank_lines_at_end(markdown_content)
    markdown_content = ensure_carriage_return_at_end(markdown_content)
    return markdown_content
