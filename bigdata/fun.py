import datetime
import xml.etree.ElementTree as ET
def parse_xml(rdd):
    """
    Read the xml string from rdd, parse and extract the elements,
    then return a list of list.
    """
    results = []
    root = ET.fromstring(rdd[0])
    ELEMENTS_TO_EXTRAT = ['CountryRegionCode', 'IsOnlyStateProvinceFlag']
    for b in root.findall('Person_StateProvince'):
        rec = []
        rec.append(b.attrib['StateProvinceID'])
        for e in ELEMENTS_TO_EXTRAT:
            value = b.find(e).text
            rec.append(value)
        results.append(rec)

    return results