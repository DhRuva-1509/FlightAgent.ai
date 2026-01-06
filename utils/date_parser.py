from dateutil import parser

def parse_date(text):
    try:
        return parser.parse(text, fuzzy=True).date().isoformat()
    except Exception:
        return None
