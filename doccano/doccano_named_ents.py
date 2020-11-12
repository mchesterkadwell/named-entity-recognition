"""Utility class to generate and output spaCy NER labels in Doccano format from XML input.

:param xml_folder_path: Absolute path as str or Path to the directory containing XML files to parse for texts.

Usage:
    >>> from doccano.doccano_named_ents import DoccanoNamedEnts
    >>> labels = DoccanoNamedEnts('tests/data/xml') # doctest: +SKIP
    >>> labels.print() # doctest: +SKIP
    # Prints out all the labels in Doccano format
    >>> labels.to_file('tests/output/doccano_ner.jsonl') # doctest: +SKIP
    # Writes all the labels in Doccano format to file

"""
from pathlib import Path
import json
from bs4 import BeautifulSoup
import en_core_web_sm

nlp = en_core_web_sm.load(disable=['tagger', 'parser'])

class DoccanoNamedEnts:
    def __init__(self, xml_folder_path: str, verbose: bool = False):
        self.xml_dir = xml_folder_path
        self.verbose = verbose
        self.spacy_ents = self._init_spacy_ents()
        self.doccano_ents = self._init_doccano_ents()

    def print(self, text_only=False) -> None:
        """Prints all texts and their named entities in Doccano format.
        When text_only=True returns only the texts without the labels."""
        for item in self.doccano_ents:
            text_first = dict(sorted(item.items(), reverse=True))
            if text_only:
                text_first['labels'] = []
            print(json.dumps(text_first))

    def to_file(self, output_file_path, text_only=False) -> None:
        """Writes all texts and their named entities in Doccano format to specified file.
        When text_only=True returns only the texts without the labels."""
        file = Path(output_file_path).absolute()
        with file.open('w+', encoding='utf-8', newline='\n') as f:
            for item in self.doccano_ents:
                item_ = item.copy()
                if text_only:
                    item_['labels'] = []
                f.write(json.dumps(item_) + '\n')
            print(f'{len(self.doccano_ents)} items saved to {output_file_path}')

    def _init_spacy_ents(self) -> tuple:
        """Returns NER results in spaCy format from the initialised texts."""
        spacy_t = tuple(self.label_spacy_ents(text) for text in self._next_text())
        return spacy_t

    def _init_doccano_ents(self) -> tuple:
        """Returns NER results in Doccano format from the initialised texts."""
        doccano_t = tuple(self.convert_ents(ents) for ents in self.spacy_ents)
        return doccano_t

    def _next_text(self) -> str:
        """Returns a generator that yields the next text from a folder of XML files."""
        dir_path = Path(self.xml_dir).absolute()
        xml_files = (file for file in dir_path.iterdir() if file.is_file() and file.name.lower().endswith('.xml'))
        for file in xml_files:
            if self.verbose:
                print(f'Getting text from {file}...')
            with file.open('r', encoding='utf-8') as xml:
                letter = BeautifulSoup(xml, "lxml-xml")
                text = letter.find(type='transcription')
                if text:
                    yield text.text.strip()

    @classmethod
    def convert_ents(cls, spacy_ne: dict) -> dict:
        """Converts NER results in spaCy format to Doccano format."""
        doccano_d = spacy_ne.copy()
        doccano_d['labels'] = doccano_d.pop('ents')
        new_labels = []
        for item in list(doccano_d['labels']):
            values = list(item.values())
            new_labels.append(values)
        doccano_d['labels'] = new_labels
        return doccano_d

    @classmethod
    def label_spacy_ents(cls, text: str) -> dict:
        """Returns NER results predicted by spaCy for a single text."""
        text_no_linebreaks = text.replace('\n', ' ')
        doc = nlp(text_no_linebreaks)
        doc_dict = doc.to_json()
        return {key: value for (key, value) in doc_dict.items() if key in ['text', 'ents']}
