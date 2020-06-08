import tensorflow as tf
import NeuralNetwork.library as library


class RNN:
    def __init__(self, prev, type="KOSPI"):
        self.input_data, self.output_data = library.get_data(prev, type)
        self.model = tf.keras.Sequential([
            tf.keras.layers.LSTM(units=40, return_sequences=True, input_shape=[prev, 1]),
            tf.keras.layers.LSTM(units=40),
            tf.keras.layers.Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        self.type = type

    def training(self, epochs=200, validation_split=0.2):
        self.history = self.model.fit(self.input_data, self.output_data, epochs=epochs, validation_split=validation_split)
        self.model.save_weights("Data/" + self.type)

    def predict(self, input_data):
        self.model.load_weights("Data/" + self.type)
        result = self.model.predict(input_data)
        for i in range(len(result)):
            result[i] = library.de_normalization_data(result[i], self.type)
        return result

    def test(self, test_num):
        result = self.predict(self.input_data[:test_num])
        result_loss = 0
        for i in range(test_num):
            print(result[i])
            result_loss += abs(round(library.de_normalization_data(self.output_data[i], self.type), 4) - result[i])


if __name__ == "__main__":

    # kospi = RNN(25)
    # kospi.training(300, 0.2)

    usd = RNN(25, "USD")
    usd.training(300, 0.2)

    chn = RNN(25, "CHN")
    chn.training(300, 0.2)


    """
    for i in range(100):
        print("오늘의 값: ", library.de_normalization_data(input_test[i][-1]), " 인공지능 : ",
              library.de_normalization_data(answer[i]), " 실제값 : ", library.de_normalization_data(result[i]))
    """
