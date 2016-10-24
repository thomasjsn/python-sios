import statistics


class Measurement:
    def __init__(self, decimals=2, length=300):
        self.__decimals = decimals
        self.__values = list()
        self.__length = length

    @property
    def length(self):
        return len(self.__values)

    @property
    def mean(self):
        return round(statistics.mean(self.__values), self.__decimals)

    @property
    def stdev(self):
        return round(statistics.stdev(self.__values), self.__decimals) if len(self.__values) > 1 else -1

    @property
    def rising(self):
        return (self.get(3) - self.mean) > (self.stdev * 3)

    def add(self, value):
        self.__values.append(float(value))

        if len(self.__values) > self.__length:
            del self.__values[0]

    def get(self, length):
        return round(statistics.mean(self.__values[length * -1:]), self.__decimals)
