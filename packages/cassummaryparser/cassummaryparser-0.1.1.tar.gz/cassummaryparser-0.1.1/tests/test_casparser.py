from cassummaryparser import CasParser

def test_the_parser():
    file = './tests/nopass.pdf'
    parser = CasParser(file=file, password='')

    data = parser.parse()
    assert 8 == len(data)

    first_record = data[0]
    assert first_record.folio_no == '910132174992/0'
    assert first_record.isin == 'INF846K01EW2'
    assert first_record.scheme_name == '128TSDGG - Axis ELSS Tax Saver Fund - Direct Growth'
    assert first_record.cost_value == '12,000.000'
    assert first_record.unit_balance == 141.247
    assert first_record.nav_date == '17-Jan-2024'
