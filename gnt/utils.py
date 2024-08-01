import re

def correct(output: str, reference: str) -> bool:
    """Check if the output is correct. """
    pattern = re.compile(r'\[(.*?)\]')
    output = pattern.findall(output)
    return reference in output
    