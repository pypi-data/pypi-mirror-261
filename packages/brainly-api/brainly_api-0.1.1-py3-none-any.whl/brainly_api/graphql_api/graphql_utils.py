import base64


def str_to_graphql_id(str_: str) -> str:
    """Encode string to a GraphQL Base64 id"""
    encoded = base64.b64encode(bytes(str_, "utf-8"))

    return encoded.decode("utf-8")


def decode_graphql_id(id_: str) -> str:
    return base64.b64decode(id_).decode("utf-8")
