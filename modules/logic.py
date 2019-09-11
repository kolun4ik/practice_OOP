# Реализуем логические элементы


class LogicGate:
    """Простой логический эелемент: здесь важно знать
    наименование и то, что получаем на выходе (output)"""

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

# разделим логические элементы, основываясь на кол-ве их входных линий


class BinaryGate(LogicGate):
    """Элемент с двумя входами (AND, OR)"""
    def __init__(self, label):
        super(BinaryGate, self).__init__(label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(
                input('Enter pin A input for gate ' + self.getLabel() + '-->')
            )
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(
                input('Enter pin B input for gate ' + self.getLabel() + '-->')
            )
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError('Error: no empty pins')


class UnaryGate(LogicGate):
    """Элемент с одним входом (NOT)"""
    def __init__(self, label):
        super(UnaryGate, self).__init__(label)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(
                input('Enter Pin  input for gate ' + self.getLabel() + ' -->')
            )
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print('Cannot connect: NO EMPTY PIN on this gate')


class AndGate(BinaryGate):
    """Элемент AND"""
    def __init__(self, label):
        super(AndGate, self).__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """Элемент OR"""
    def __init__(self, label):
        super(OrGate, self).__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(OrGate):
    """Элемент NOT"""

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NorGate(BinaryGate):
    """Элемент Nor"""
    def __init__(self, label):
        super(NorGate, self).__init__(label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 0
        else:
            return 1


class NandGate(AndGate):
    """Исключающее И"""
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 0
        else:
            return 1


# Реализуем Конектор соединяет выход одного элемента со входом другого

class Connector:
    """Абстрактный проводок"""
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
