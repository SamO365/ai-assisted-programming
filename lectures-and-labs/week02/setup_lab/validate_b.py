def validate_email(email: str) -> bool:
    """Return whether an email contains an @ followed by a dot."""
    if len(email) > 254:
        return False

    at_index = email.find("@")
    return at_index != -1 and email.find(".", at_index + 1) != -1
