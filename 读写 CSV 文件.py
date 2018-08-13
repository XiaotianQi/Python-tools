# _*_coding:utf-8_*_
import csv

def writeCsvFile(path, data, header=None, mode='w'):
    try:
        with open(path, mode, newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')

            if header is not None:
                writer.writerow(header)

            writer.writerows(data)

            print("Successful! Path: %s." % path)
    except Exception as e:
        print("Error! Path: %s, Case: %s" % (path, e))

def openCsvFile(path):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


TEMPLATE = '''
Dialect: "{name}"

    delimiter   = {dl!r:<6}    skipinitialspace = {si!r}
    doublequote = {dq!r:<6}    quoting          = {qu}
    quotechar   = {qc!r:<6}    lineterminator   = {lt!r}
    escapechar  = {ec!r:<6}
'''
quoting_modes = {
    getattr(csv, n): n
    for n in dir(csv)
    if n.startswith('QUOTE_')
}

def showDialectList():
    for name in sorted(csv.list_dialects()):
        dialect = csv.get_dialect(name)

        print(TEMPLATE.format(
            name=name,
            dl=dialect.delimiter,
            si=dialect.skipinitialspace,
            dq=dialect.doublequote,
            qu=quoting_modes[dialect.quoting],
            qc=dialect.quotechar,
            lt=dialect.lineterminator,
            ec=dialect.escapechar,
        ))

if __name__ == '__main__':
    header = ['Symbol','Price','Date','Time','Change','Volume']
    data = [
        ["AA", 39.48, "6/11/2007", "9:36am", -0.18,181800],
        ["AIG", 71.38, "6/11/2007", "9:36am", -0.15,195500],
        ["AXP", 62.58, "6/11/2007", "9:36am", -0.46,935000],
        ["BA", 98.31, "6/11/2007", "9:36am", +0.12,104800],
        ["C", 53.08, "6/11/2007", "9:36am", -0.25,360900],
        ["CAT", 78.29, "6/11/2007", "9:36am", -0.23,225400]
    ]
    writeCsvFile('testCSV.csv', data, header)
    openCsvFile('testCSV.csv')
    showDialectList()
