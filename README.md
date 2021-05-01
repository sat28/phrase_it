# phrase_it

#### Summary
This dash application used word2vec library and phrases.csv provided inside data to find similiar phrases and to calculate cosine similarity

#### Important Links

Hosted version - http://3.138.61.60:8050/

S3 location for vectors data -
- https://phrase-it.s3.amazonaws.com/vectors.pickle
- https://phrase-it.s3.amazonaws.com/vectors.pickle.vectors.npy

#### Artifacts
Contains the notebook initially used

#### Data
All data being used by the app resides here

#### phrase_interface
This python package holds the class Phrase and other functions 

#### main.py
This is the entry point of the dash application

#### Dockerfile
Docker image built using this file on the hosted VM
