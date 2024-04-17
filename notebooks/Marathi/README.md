# Training a spaCy Marathi NLP pipeline

(C) 2024 by [Damir Cavar]


Steps:

- generate a base_config.cfg file using the [spaCy Widget](https://spacy.io/usage/training)
- run `python -m spacy init fill-config ./base_config.cfg ./config.cfg` to create a full config
- run `python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy`

This requires that you place the training data into the respective folders (`train.spacy` and `dev.space`).

Download the CoNLL file for Marathi here:

- [UD_Marathi-UFAL](https://github.com/UniversalDependencies/UD_Marathi-UFAL)

Convert the CoNLL files to spaCy binary files, as documented [here](https://spacy.io/api/cli#convert):

- Run `python -m spacy convert ./mr_ufal-ud-dev.conllu ./dev.spacy --converter conllu --file-type spacy --seg-sents --morphology --merge-subtokens --ner-map --lang mr`
- Run `python -m spacy convert ./mr_ufal-ud-train.conllu ./train.spacy --converter conllu --file-type spacy --seg-sents --morphology --merge-subtokens --ner-map --lang mr`


[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar"
