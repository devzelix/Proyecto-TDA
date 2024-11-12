class Cola:

    def __init__(self):

        self.__elementos = []

    def esta_vacia(self):

        return len(self.__elementos) == 0

    def encolar(self, valor):

        self.__elementos.append(valor)

    def desencolar(self):

        if not self.esta_vacia():
        
            return self.__elementos.pop(0)

        else:

            return None