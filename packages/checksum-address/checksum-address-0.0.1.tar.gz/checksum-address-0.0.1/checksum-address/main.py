import eth_utils

def checksum_address(address):
    address_bytes = eth_utils.to_bytes(hexstr=address)
    address_hex = address_bytes.hex()
    address_hash = eth_utils.keccak(text=address_hex).hex()

    checksummed_buffer = ""

    for nibble_index, character in enumerate(address_hex):
        if character in "0123456789":
            checksummed_buffer += character
        elif character in "abcdef":
            nibble_address = int(address_hash[nibble_index], 16)
            if nibble_address > 7:
                checksummed_buffer += character.upper()
            else:
                checksummed_buffer += character
        else:
            raise eth_utils.ValidationError(
                f"Unrecognized hex character {character!r} at position {nibble_index}"
            )

    print("0x" + checksummed_buffer)
    return "0x" + checksummed_buffer