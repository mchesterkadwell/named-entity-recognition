import pytest
from doccano.doccano_named_ents import DoccanoNamedEnts

@pytest.fixture
def dne(data_dir):
    return DoccanoNamedEnts(data_dir)


def test_instance_init(dne, data_dir):
    assert dne.xml_dir == data_dir


def test_print_two_ner_results_in_doccano_format(dne, printed_ents_fix, capfd):
    dne.print()
    printed = capfd.readouterr().out
    assert printed in printed_ents_fix


def test_write_to_file_two_ner_results_in_doccano_format(dne, output_file, capfd):
    dne.to_file(output_file)
    printed = capfd.readouterr().out
    assert printed == f'{len(dne.doccano_ents)} items saved to ' \
                      f'{output_file}\n'


def test_initialise_spacy_named_entities_for_two_texts(dne, spacy_ents_fix):
    spacy_ents = dne._init_spacy_ents()
    assert isinstance(spacy_ents, tuple)
    assert len(spacy_ents) == 2
    assert spacy_ents[0] in spacy_ents_fix
    assert spacy_ents[1] in spacy_ents_fix


def test_initialise_doccano_named_entities_for_two_texts(dne, doccano_ents_fix):
    doccano_ents = dne._init_doccano_ents()
    assert isinstance(doccano_ents, tuple)
    assert len(doccano_ents) == 2
    assert doccano_ents[0] in doccano_ents_fix
    assert doccano_ents[1] in doccano_ents_fix


def test_get_single_text_from_xml(dne, transcription_texts_fix):
    for text in dne._next_text():
        assert text in transcription_texts_fix


def test_count_of_text_from_xml(dne):
    count = sum(1 for _ in dne._next_text())
    assert count == 2


def test_convert_named_entities_from_spacy_to_doccano_format(dne, spacy_ents_fix, doccano_ents_fix):
    spacy_fix, doccano_fix = spacy_ents_fix[0], doccano_ents_fix[0]
    doccano_ents = dne.convert_ents(spacy_fix)
    assert isinstance(doccano_ents, dict)
    assert doccano_ents == doccano_fix


def test_generate_spacy_named_entities_for_single_text(dne, transcription_texts_fix, spacy_ents_fix):
    trans_fix, spacy_fix = transcription_texts_fix[0], spacy_ents_fix[0]
    spacy_ents = dne.label_spacy_ents(trans_fix)
    assert isinstance(spacy_ents, dict)
    assert spacy_ents == spacy_fix
