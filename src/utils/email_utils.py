def extract_name_from_email(email):
    """
    Extract the recipient's name from their email address.

    Args:
        email (str): The recipient's email address.

    Returns:
        str: The recipient's name (e.g., "John Doe").
    """
    try:
        # Extract the part before the '@' symbol
        name_part = email.split("@")[0]

        # Split by '.' and capitalize each part
        name = " ".join([part.capitalize() for part in name_part.split(".")])

        return name
    except Exception as e:
        print(f"Error extracting name from email {email}: {e}")
        return "Recipient"  # Fallback value if extraction fails