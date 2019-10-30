from collections import namedtuple

class ConverterManager(object):
    def convertDictToObject(d):
        top = type('new', (object,), d)
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                setattr(top, i, ConverterManager.convertDictToObject(j))
            elif isinstance(j, seqs):
                setattr(top, i, type(j)(ConverterManager.convertDictToObject(sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                setattr(top, i, j)
        return top