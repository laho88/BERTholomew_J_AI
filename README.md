#**B**idirectional **E**ncoder **R**epresentations from **T**ransformers

[BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html)



Dependencies:

python 3.8.10
pip
bert-api
wikipedia-api
django 2.2.23
tensorflow
pandas
matplotlib
numpy
transformers
ipython

##Documentation

[bert-api](https://pypi.org/project/bert-api/)

[Huggingface Transformers - Pipeline](https://huggingface.co/transformers/model_doc/bert.html)

[Tensorflow](https://www.tensorflow.org/official_models/fine_tuning_bert)

[Transformers](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)


##Security:

[Security concerns for transparency](https://openreview.net/forum?id=7nfCtKep-v)



##BERT Data Input:

IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import wikipediaapi

In [2]: wiki=wikipediaapi.Wikipedia('en')

In [3]: wiki.page('quantum computing')
Out[3]: quantum computing (id: ??, ns: 0)

In [4]: wiki.page('quantum computing').summary
Out[4]: 'Quantum computing is the exploitation of collective 


Pipeline Setup:

ipython

In [1]: from transformers import pipeline
In [2]: b = pipeline('question-answering')
In [3]: text = 'Quantum computing began in the early 1980s.'
In [4]: q = 'When did Quantum Computing begin?'
In [5]: b(question=q,context=text)
Out[6]: {'score': 0.5067328214645386, 'start': 31, 'end': 42, 'answer': 'early 19
80s'}


