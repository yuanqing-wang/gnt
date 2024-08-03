import re

def correct(output: str, reference: str) -> bool:
    """Check if the output is correct. """
    output = re.findall(r'\[(.*?)\]', output)
    return str(reference) in output
    