from datetime import timedelta, datetime
import string

COUNTRIES = ['Arstotzka', 'Antegria', 'Impor', 'Kolechia', 'Obristan', 'Republia', 'United Federation']
TODAY = datetime.strptime('November 22, 1982', '%B %d, %Y')
VACCINES = []


class Inspector:
    def __init__(self):
        self.allowed_countries = []
        self.denied_countries = []
        self.vaccines = {}
        self.documents = {'Citizens': [], 'Foreigners': [], 'Workers': []}
        self.wanted = []

    def _parse_docs(self, documents):
        self.current = {}

        if 'passport' in documents:
            pass

    def _read_country(self, parsed):
        if 'Allow' in parsed:
            self.allowed_countries = [i for i in parsed if i in COUNTRIES]
        if 'Deny' in parsed:
            self.denied_countries = [i for i in parsed if i in COUNTRIES]

    def _read_documents(self, parsed, sentence):
        documents = [
            'passport',
            'certificate of vaccination',
            'ID_card',
            'access permit',
            'work pass',
            'grant of asylum',
            'diplomatic authorization',
        ]
        docs = [i for i in documents if i in sentence]
        if 'Entrants' in parsed:
            self.documents.update(Citizens=docs)
            self.documents.update(Foreigners=docs)
            self.documents.update(Workers=docs)
        if 'Citizens' in parsed:
            self.documents.update(Citizens=docs)
        elif 'Foreigners' in parsed:
            self.documents.update(Foreigners=docs)
        elif 'Worker' in parsed:
            self.documents.update(Workers=docs)

    def _read_vaccines(self, parsed):
        vac = parsed[-2]
        if all(['require', 'vaccination']) in parsed:
            self.vaccines.update({vac: [i for i in parsed if i in COUNTRIES]})
        if all(['no', 'longer', 'vaccination']) in parsed:
            self.vaccines.pop(vac)

    def _read_wanted(self, parsed, sentence):
        if 'Wanted' in parsed:
            self.wanted = sentence.split(': ')[-1]

    def receive_bulletin(self, bulletin):
        print(bulletin)
        if bulletin:
            lines = [i.strip() for i in bulletin.split('\n')]
            for line in lines:
                parsed = line.split(' ')
                parsed = [i.translate(str.maketrans('', '', string.punctuation)) for i in parsed]
                self._read_country(parsed)
                self._read_documents(parsed, line)
                self._read_vaccines(parsed)
                self._read_wanted(parsed, line)

        print(bulletin)

    def inspect(self, documents):
        self.wanted = []
        for doc in documents:
            pass
        return True


inspector = Inspector()
bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector.receive_bulletin(bulletin)

josef = {
    "passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
}
guyovich = {
    "access_permit": 'NAME: Guyovich, Russian\nNATION: Obristan\nID#: TE8M1-V3N7R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 159cm\nWEIGHT: 60kg\nEXP: 1983.07.13'
}
roman = {
    "passport": 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
    "grant_of_asylum": 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'
}

inspector.inspect(josef),  # 'Glory to Arstotzka.'
inspector.inspect(guyovich),  # 'Entry denied: missing required passport.'
inspector.inspect(roman),  # 'Detainment: ID number mismatch.'

# a = {}
# a.update(b = [i for i in range(5)])
# a.update(b = [i for i in range(2)])
# print(a)
