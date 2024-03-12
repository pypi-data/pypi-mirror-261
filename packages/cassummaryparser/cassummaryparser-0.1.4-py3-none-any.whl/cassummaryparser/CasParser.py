import tabula
from cassummaryparser import CasRecord

class CasParser:
    """Class that parses a cas summary file using tabula-py"""
    def __init__(self, file, password: str=''):
        if file is None:
            raise ValueError("The file argument cannot be None")

        if password is None:
            password = ''

        self.file = file
        self.password = password

    def parse(self) -> list[CasRecord]:
        try:
            # TODO: Enhance this to handle multiple pages
            pdfData = tabula.read_pdf(self.file, pages='1', password=self.password, silent=True)
            table = pdfData[0]
            return self.__parse(table)
        except Exception as parse_exception:
            raise RuntimeError("An Error while parsing the pdf file. Please check if the file provided and the password are correct") from parse_exception

    def __parse(self, table) -> list[CasRecord]:
        data = []

        for row in range(1, len(table)):
            record = self.__get_record(table, row)

            # Sometimes the scheme name overflows to the next line. 
            # The overflow is identified when the first field is NaN - 
            #   Or we can say the type of the attribute is float
            # This code appends the next line to the above record
            if type(record.folio_no) == float:
                last_record = data[-1]
                last_record.scheme_name += ' ' + record.scheme_name
            else:
                data.append(record)    

        return data

    def __get_record(self, table, row: int) -> CasRecord:
        cas_record = CasRecord()
        if not self.__within_index(table, row):
            return cas_record

        record = table.iloc[row]

        folio_no = record.iloc[0]

        cas_record.folio_no = folio_no

        # Folio and ISIN comes in the same row when tabula parses
        if type(folio_no) == str:
            parts = folio_no.split('IN')
            cas_record.folio_no = parts[0]
            cas_record.isin = 'IN' + parts[1]
        
        cas_record.scheme_name = record.iloc[2]
        cas_record.cost_value = record.iloc[3]
        cas_record.unit_balance = record.iloc[4]
        cas_record.nav_date = record.iloc[5]
        cas_record.nav = record.iloc[6]
        cas_record.market_value = record.iloc[7]
        cas_record.registrar = record.iloc[8]
        
        return cas_record

    def __within_index(self, table, row):
        N_ROWS = len(table)
        if row >= N_ROWS:
            return False
        return True

