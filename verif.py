import re
def isGoodIp(ip):
    """
    Vérifie si une chaîne de caractères contient uniquement des chiffres, des points et des slashes.
    """
    regex = r'^[0-9./]+$'
    if re.match(regex, ip):
        return True
    else:
        return False
    

