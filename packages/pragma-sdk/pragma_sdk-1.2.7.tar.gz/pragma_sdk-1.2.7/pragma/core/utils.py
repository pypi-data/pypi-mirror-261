import logging

logger = logging.getLogger(__name__)


def str_to_felt(text):
    if text.upper() != text:
        logger.warning("Converting lower to uppercase for str_to_felt: %s", text)
        text = text.upper()
    b_text = bytes(text, "utf-8")
    return int.from_bytes(b_text, "big")


def felt_to_str(felt):
    num_bytes = (felt.bit_length() + 7) // 8
    bytes_ = felt.to_bytes(num_bytes, "big")
    return bytes_.decode("utf-8")


def log_entry(entry):
    logger.info("Entry: %s", entry.serialize())


def currency_pair_to_pair_id(quote, base):
    return f"{quote}/{base}".upper()


def key_for_asset(asset):
    return asset["key"] if "key" in asset else currency_pair_to_pair_id(*asset["pair"])


def pair_id_for_asset(asset):
    pair_id = (
        asset["key"] if "key" in asset else currency_pair_to_pair_id(*asset["pair"])
    )
    return pair_id
