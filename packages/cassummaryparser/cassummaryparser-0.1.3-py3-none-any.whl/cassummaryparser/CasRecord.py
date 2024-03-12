from dataclasses import dataclass

@dataclass
class CasRecord:
    """Model that stores attributes of each record."""
    folio_no: str = ''
    isin: str = ''
    scheme_name: str = ''
    cost_value: str = ''
    unit_balance: str = ''
    nav_date: str = ''
    nav: str = ''
    market_value: str = ''
    registrar: str = ''

