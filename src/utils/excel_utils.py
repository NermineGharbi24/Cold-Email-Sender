import pandas as pd

def read_contacts(file_path):
    """
    Read email addresses from an Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        list: A list of email addresses.
              Returns None if an error occurs.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Ensure the required column exists
        if "Email" not in df.columns:
            print("Error: The Excel file must contain an 'Email' column.")
            return None
        
        # Extract email addresses as a list
        emails = df["Email"].tolist()
        return emails
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None