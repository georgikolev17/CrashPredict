import keras
from keras.layers import Dense, ConvLSTM1D, Flatten
from keras.models import Model
from keras.losses import BinaryCrossentropy
from keras.optimizers import Adam


def GenModel(TimeSteps, Features):
    inputs = keras.Input(shape=(TimeSteps, Features, 1))
    layers = Dense(128, activation="relu")(inputs)
    layers = ConvLSTM1D(7, 5, data_format='channels_last', activation="relu", return_sequences=True)(layers)
    layers = ConvLSTM1D(5, 3, data_format='channels_last', activation="relu", return_sequences=True)(layers)
    layers = ConvLSTM1D(3, 2, data_format='channels_last', activation="relu", return_sequences=True)(layers)
    layers = Flatten()(layers)
    layers = Dense(64, activation="relu")(layers)
    output = Dense(1, activation="sigmoid")(layers)
    model = Model(inputs=inputs, outputs=output)
    model.compile(loss=BinaryCrossentropy(),
                  optimizer=Adam(learning_rate=0.01))
    return model

