from rasa.nlu.training_data import load_data
from rasa.nlu.model import Trainer
from rasa.nlu import config

training_data = load_data('data/nlu.md')
trainer = Trainer(config.load())
trainer.train(training_data)
model_directory = trainer.persist('./models/default/')  # Returns the directory the model is stored in
print(model_directory)

from rasa.nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load(model_directory)
print(interpreter.parse(u"Where am I"))