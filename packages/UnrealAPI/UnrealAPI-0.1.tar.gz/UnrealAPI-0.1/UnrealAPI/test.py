import base64

def encode(input_string):
    """Encode a string using base64."""
    # Convert the input string to bytes, encode it with base64, and then convert the bytes back to string
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode(encoded_string):
    """Decode a base64 encoded string."""
    # Convert the encoded string to bytes, decode it with base64, and then convert the bytes back to string
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string
