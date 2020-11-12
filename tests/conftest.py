import pytest
from pathlib import Path

@pytest.fixture
def data_dir():
    return Path(__file__).parent.absolute() / 'data' / 'xml'

@pytest.fixture
def output_file():
    return Path(__file__).parent.absolute() / 'output' / 'doccano_ents.jsonl'

@pytest.fixture
def transcription_texts_fix():
    texts = (
        """We start with a letter Charles Lyell sent to Darwin in 1865 where he discusses the latest revision of his book Elements of Geology and relates to Darwin his discussions with various aquaintances about Darwin's own book On the Origin of Species.
This letter has been transcribed and annotated in TEI-XML by editors from the DCP team in Cambridge.""",
"""Their correspondence began in 1843 when Hooker, just returned from James Clark Ross's Antarctic expedition, and already an admirer of the older man, was approached about working on Darwin's collection of plants from the Beagle voyage.
Hooker was a frequent visitor to Darwin at his home in Downe, Kent, and became a great favourite of Darwin's children."""
    )
    return texts

@pytest.fixture
def spacy_ents_fix():
    return (
        {
        "text": "We start with a letter Charles Lyell sent to Darwin in 1865 where he discusses the latest revision of his book Elements of Geology and relates to Darwin his discussions with various aquaintances about Darwin's own book On the Origin of Species. This letter has been transcribed and annotated in TEI-XML by editors from the DCP team in Cambridge.",
        "ents": [{'start': 23, 'end': 36, 'label': 'PERSON'},
                 {'start': 45, 'end': 51, 'label': 'PERSON'},
                 {'start': 55, 'end': 59, 'label': 'DATE'},
                 {'start': 111, 'end': 130, 'label': 'WORK_OF_ART'},
                 {'start': 146, 'end': 152, 'label': 'PERSON'},
                 {'start': 201, 'end': 207, 'label': 'PERSON'},
                 {'start': 219, 'end': 243, 'label': 'WORK_OF_ART'},
                 {'start': 323, 'end': 326, 'label': 'ORG'},
                 {'start': 335, 'end': 344, 'label': 'GPE'}, ]},
        {
        "text": "Their correspondence began in 1843 when Hooker, just returned from James Clark Ross's Antarctic expedition, and already an admirer of the older man, was approached about working on Darwin's collection of plants from the Beagle voyage. Hooker was a frequent visitor to Darwin at his home in Downe, Kent, and became a great favourite of Darwin's children.",
        "ents": [{'start': 30, 'end': 34, 'label': 'DATE'},
                 {'start': 40, 'end': 46, 'label': 'ORG'},
                 {'start': 67, 'end': 85, 'label': 'PERSON'},
                 {'start': 181, 'end': 187, 'label': 'PERSON', },
                 {'start': 220, 'end': 226, 'label': 'PERSON', },
                 {'start': 235, 'end': 241, 'label': 'ORG', },
                 {'start': 268, 'end': 274, 'label': 'PERSON', },
                 {'start': 290, 'end': 295, 'label': 'GPE', },
                 {'start': 297, 'end': 301, 'label': 'PERSON', },
                 {'start': 335, 'end': 341, 'label': 'PERSON', }]}
    )

@pytest.fixture
def doccano_ents_fix():
    return (
        {
        "text": "We start with a letter Charles Lyell sent to Darwin in 1865 where he discusses the latest revision of his book Elements of Geology and relates to Darwin his discussions with various aquaintances about Darwin's own book On the Origin of Species. This letter has been transcribed and annotated in TEI-XML by editors from the DCP team in Cambridge.",
        "labels": [[23, 36, "PERSON"], [45, 51, "PERSON"], [55, 59, "DATE"], [111, 130, "WORK_OF_ART"],
                   [146, 152, "PERSON"], [201, 207, "PERSON"], [219, 243, "WORK_OF_ART"], [323, 326, "ORG"],
                   [335, 344, "GPE"]]},
        {
        "text": "Their correspondence began in 1843 when Hooker, just returned from James Clark Ross's Antarctic expedition, and already an admirer of the older man, was approached about working on Darwin's collection of plants from the Beagle voyage. Hooker was a frequent visitor to Darwin at his home in Downe, Kent, and became a great favourite of Darwin\'s children.",
        "labels": [[30, 34, "DATE"], [40, 46, "ORG"], [67, 85, "PERSON"], [181, 187, "PERSON"], [220, 226, "PERSON"],
                   [235, 241, "ORG"], [268, 274, "PERSON"], [290, 295, "GPE"], [297, 301, "PERSON"],
                   [335, 341, "PERSON"]]}
    )

@pytest.fixture
def printed_ents_fix():
    prints = (
        """{"text": "We start with a letter Charles Lyell sent to Darwin in 1865 where he discusses the latest revision of his book Elements of Geology and relates to Darwin his discussions with various aquaintances about Darwin's own book On the Origin of Species. This letter has been transcribed and annotated in TEI-XML by editors from the DCP team in Cambridge.", "labels": [[23, 36, "PERSON"], [45, 51, "PERSON"], [55, 59, "DATE"], [111, 130, "WORK_OF_ART"], [146, 152, "PERSON"], [201, 207, "PERSON"], [219, 243, "WORK_OF_ART"], [323, 326, "ORG"], [335, 344, "GPE"]]}
{"text": "Their correspondence began in 1843 when Hooker, just returned from James Clark Ross's Antarctic expedition, and already an admirer of the older man, was approached about working on Darwin's collection of plants from the Beagle voyage. Hooker was a frequent visitor to Darwin at his home in Downe, Kent, and became a great favourite of Darwin's children.", "labels": [[30, 34, "DATE"], [40, 46, "ORG"], [67, 85, "PERSON"], [181, 187, "PERSON"], [220, 226, "PERSON"], [235, 241, "ORG"], [268, 274, "PERSON"], [290, 295, "GPE"], [297, 301, "PERSON"], [335, 341, "PERSON"]]}
""",
"""{"text": "Their correspondence began in 1843 when Hooker, just returned from James Clark Ross's Antarctic expedition, and already an admirer of the older man, was approached about working on Darwin's collection of plants from the Beagle voyage. Hooker was a frequent visitor to Darwin at his home in Downe, Kent, and became a great favourite of Darwin's children.", "labels": [[30, 34, "DATE"], [40, 46, "ORG"], [67, 85, "PERSON"], [181, 187, "PERSON"], [220, 226, "PERSON"], [235, 241, "ORG"], [268, 274, "PERSON"], [290, 295, "GPE"], [297, 301, "PERSON"], [335, 341, "PERSON"]]}
{"text": "We start with a letter Charles Lyell sent to Darwin in 1865 where he discusses the latest revision of his book Elements of Geology and relates to Darwin his discussions with various aquaintances about Darwin's own book On the Origin of Species. This letter has been transcribed and annotated in TEI-XML by editors from the DCP team in Cambridge.", "labels": [[23, 36, "PERSON"], [45, 51, "PERSON"], [55, 59, "DATE"], [111, 130, "WORK_OF_ART"], [146, 152, "PERSON"], [201, 207, "PERSON"], [219, 243, "WORK_OF_ART"], [323, 326, "ORG"], [335, 344, "GPE"]]}
"""
    )
    return prints


