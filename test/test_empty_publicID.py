import tempfile
import rdflib
from pathlib import Path
from rdflib.term import URIRef


def test_empty_string_for_publicID_when_loading_an_rdfxml_file():
    ''' Tests that we can pass in an empty string to publicID when
        parsing from an RDF/XML file name. since '' is falsy, it could be
        treated as None (e.g. if not publicID). '''

    xml_sample = """\
<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim16#"
         xmlns:cyme="http://www.cyme.com/CIM/1.0.2#"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
    <cim:SwitchInfo rdf:ID="_AB16765A-B19E-4454-A58F-868D23C6CD26" />
</rdf:RDF>"""

    g = rdflib.Graph()
    with tempfile.TemporaryDirectory() as td:
        sample_file = str(Path(td) / "sample.xml")
        open(sample_file, 'w').write(xml_sample)

        g.parse(sample_file, publicID="")

    subject, predicate, object = next(iter(g))

    assert subject == URIRef("#_AB16765A-B19E-4454-A58F-868D23C6CD26")
    assert predicate == URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
    assert object == URIRef("http://iec.ch/TC57/2013/CIM-schema-cim16#SwitchInfo")


def test_empty_string_for_publicID_when_loading_a_ttl_file():
    ''' Tests that we can pass in an empty string to publicID when
        parsing from a turtle file name. since '' is falsy, it could be
        treated as None (e.g. if not publicID). '''

    ttl_sample = """\
    <#_AB16765A-B19E-4454-A58F-868D23C6CD26> a
    <http://iec.ch/TC57/2013/CIM-schema-cim16#SwitchInfo> .
    """

    g = rdflib.Graph()
    with tempfile.TemporaryDirectory() as td:
        sample_file = str(Path(td) / "sample.ttl")
        open(sample_file, 'w').write(ttl_sample)

        g.parse(sample_file, publicID="")

    subject, predicate, object = next(iter(g))

    assert subject == URIRef("#_AB16765A-B19E-4454-A58F-868D23C6CD26")
    assert predicate == URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
    assert object == URIRef("http://iec.ch/TC57/2013/CIM-schema-cim16#SwitchInfo")
