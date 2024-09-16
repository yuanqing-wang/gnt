import re

def parse(text: str) -> str:
    """Parse the output. """
    matches = re.findall(r"<ANSWER>(.*?)</ANSWER>", text)
    if len(matches) == 0:
        return None
    matches = [match.strip() for match in matches if match != ""]
    if len(matches) == 0:
        return None
    return matches[0]

def correct(output: str, reference: str) -> bool:
    """Check if the output is correct. """
    output = parse(output)
    return output == reference
    