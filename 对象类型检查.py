# _*_coding:utf-8_*_

def interrogate(item):
    if hasattr(item, '__name__'):
        print('NAME:     ', item.__name__)
    if hasattr(item, '__class__'):
        print('CLASS:    ', item.__class__.__name__)
    print('TYPE:     ', type(item))
    print('VALUE:    ', repr(item))
    if callable(item):
        print('CALLABLE:  YES')
    else:
        print('CALLABLE:  NO')
    if hasattr(item, '__doc__'):
        doc = getattr(item, '__doc__')
    doc = doc.strip()
    firstline = doc.split('\n')[0]
    print('DOC:      ', firstline)

if __name__ == '__main__':
    interrogate('a string')
    interrogate(123)
    interrogate(iter)