# aye-saac-nlu

## Rasa

### Initialised with:
```rasa init --no-prompt```

### Train for conversation:
```rasa train```

### Train for nlu:
```rasa train nlu```

### Run:
```rasa shell```

#
## Scripting
#### For any info on the usage of one command, just run it without any parameter
##### (Run everything from within 'scripting' directory)

### parseData.py
#### To see the output:
```python parseData.py dataset/*.json```
#### To save the output:
```python parseData.py dataset/*.json > questions.txt```

### stats.py
#### Run:
```python stats.py dataset/*.json```

### createmd.py
#### To create the nlu.md file:
```python createmd.py intents/ nlu.md```

#### Then you have to move the nlu.md file to the 'data' directory which is in the root folder or you can also run one of the following:
```python createmd.py intents/ ../data/nlu.md```

```python createmd.py intents/ nlu.md ; cp nlu.md ../data/nlu.md```
