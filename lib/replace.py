import re

def replace_cve_text_with_link(text: str) -> str:
    # Regex should match strings like "${whitespace}CVE${any_number_of_digits_and_dashes}"
    return re.sub('(\s)(cve)([\d-]+)', r'\1[\2\3](https://nvd.nist.gov/vuln/detail/CVE\3)', text, flags=re.IGNORECASE)
