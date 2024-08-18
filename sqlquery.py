def insert_vault_entry(url, username, password):
    """Inserts a new entry into the Vault table.

    Args:
        url (str): The URL of the website.
        username (str): The username for the website.
        password (str): The encrypted password for the website.
    """
    insert_query = """
        INSERT INTO Vault (URL, USRNAME, PASSWD) 
        VALUES (%s, %s, %s)
        """
    return insert_query

def delete_vault_entry(url):
    """Deletes an entry from the Vault table based on the URL.

    Args:
        url (str): The URL of the entry to delete.
    """
    delete_query = """
        DELETE FROM Vault 
        WHERE URL = %s
        """
    return delete_query

def update_vault_url(new_url, old_url):
    """Updates the URL of an existing entry in the Vault table.

    Args:
        new_url (str): The new URL.
        old_url (str): The old URL to be updated.
    """
    update_query = """
        UPDATE Vault 
        SET URL = %s 
        WHERE URL = %s
        """
    return update_query

def update_vault_username(username, url):
    """Updates the username of an existing entry in the Vault table.

    Args:
        username (str): The new username.
        url (str): The URL of the entry to update.
    """
    update_query = """
        UPDATE Vault 
        SET USRNAME = %s 
        WHERE URL = %s
        """
    return update_query

def update_vault_password(password, url):
    """Updates the password of an existing entry in the Vault table.

    Args:
        password (str): The new encrypted password.
        url (str): The URL of the entry to update.
    """
    update_query = """
        UPDATE Vault 
        SET PASSWD = %s 
        WHERE URL = %s
        """
    return update_query

def select_vault_entry(url):
    """Selects an entry from the Vault table based on the URL.

    Args:
        url (str): The URL of the entry to select.
    """
    select_query = """
        SELECT * 
        FROM Vault 
        WHERE URL = %s
        """
    return select_query