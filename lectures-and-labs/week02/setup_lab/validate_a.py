def validate_email(email: str) -> bool:
    """Return whether an email has a basic address shape."""
    if len(email) > 254 or any(character.isspace() for character in email):
        return False

    local_part, separator, domain = email.partition("@")
    return bool(local_part and separator and "." in domain)
