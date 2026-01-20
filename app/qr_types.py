"""QR Code type generators"""

def format_url(data):
    """Format URL data - adds https:// if missing"""
    url = data.get('url', '')
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def format_vcard(data):
    """Format vCard contact data - creates a contact card"""
    name = data.get('name', '')
    phone = data.get('phone', '')
    email = data.get('email', '')
    organization = data.get('organization', '')
    
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ORG:{organization}
END:VCARD"""
    return vcard

def format_wifi(data):
    """Format WiFi credentials - auto-connect format"""
    ssid = data.get('ssid', '')
    password = data.get('password', '')
    security = data.get('security', 'WPA')  # WPA, WEP, or nopass
    
    # WiFi QR format: WIFI:T:WPA;S:network_name;P:password;;
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"
    return wifi_string

def format_text(data):
    """Format plain text - returns as-is"""
    return data.get('text', '')

# Map QR types to their formatter functions
QR_FORMATTERS = {
    'url': format_url,
    'vcard': format_vcard,
    'wifi': format_wifi,
    'text': format_text
}