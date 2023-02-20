# Importing the unittest module.
import unittest

def es_movimiento_posible_caballo(pos1, pos2):
    """
    It returns True if the two positions are two units apart in one direction and one unit apart in the
    other direction, and False otherwise
    
    :param pos1: The current position of the knight
    :param pos2: (0, 0)
    :return: True or False
    """
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def es_movimiento_posible_alfil(pos1, pos2):
    """
    It returns True if the absolute value of the difference between the first elements of the two tuples
    is equal to the absolute value of the difference between the second elements of the two tuples.
    
    :param pos1: The position of the piece you want to move
    :param pos2: The position of the piece you want to move to
    :return: True or False
    """
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx == dy

def es_movimiento_posible_torre(pos1, pos2):
    """
    If the difference between the x coordinates is zero or the difference between the y coordinates is
    zero, then the move is possible.
    
    :param pos1: the position of the piece you want to move
    :param pos2: The position of the piece you want to move to
    :return: True or False
    """
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx == 0 or dy == 0

def es_movimiento_posible_reina(pos1, pos2):
    """
    It checks if a queen can move from one position to another.
    
    :param pos1: The position of the queen
    :param pos2: The position of the piece you want to move to
    :return: A boolean value.
    """
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx == dy or dx == 0 or dy == 0

def es_movimiento_posible_rey(pos1, pos2):
    """
    If the difference between the x-coordinates is less than or equal to 1 and the difference between
    the y-coordinates is less than or equal to 1, then the move is possible
    
    :param pos1: The position of the piece you want to move
    :param pos2: The position of the piece you want to move to
    :return: True or False
    """
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx <= 1 and dy <= 1

def main():
    """
    It takes two tuples as input and returns True if the move is possible and False otherwise.
    """
    print("Introduce las posiciones de las casillas (fila, columna) y la figura de ajedrez que quieres utilizar:")
    pos1 = tuple(map(int, input("Posición 1: ").split(",")))
    pos2 = tuple(map(int, input("Posición 2: ").split(",")))
    figura = input("Figura (C: caballo, A: alfil, T: torre, R: reina, Y: rey): ")

    # Checking if the input is equal to the letter of the chess piece.
    if figura == "C":
        posible = es_movimiento_posible_caballo(pos1, pos2)
    elif figura == "A":
        posible = es_movimiento_posible_alfil(pos1, pos2)
    elif figura == "T":
        posible = es_movimiento_posible_torre(pos1, pos2)
    elif figura == "R":
        posible = es_movimiento_posible_reina(pos1, pos2)
    elif figura == "Y":
        posible = es_movimiento_posible_rey(pos1, pos2)

    # Printing the result of the function.
    if posible:
        print("Es posible realizar el movimiento")
    else:
        print("No es posible realizar el movimiento")

# A way to make sure that the code in the main() function is only executed when the file is run as a
# script.
if __name__ == '__main__':
    main()

# TestEsMovimientoPosibleCaballo is a class that tests the function es_movimiento_posible_caballo.
class TestEsMovimientoPosibleCaballo(unittest.TestCase):

    def test_movimiento_posible(self):
        self.assertTrue(es_movimiento_posible_caballo((1,2), (3,3)))

    def test_movimiento_no_posible(self):
        self.assertFalse(es_movimiento_posible_caballo((1,2), (2,3)))

# The class TestEsMovimientoPosibleAlfil has two methods: test_movimiento_posible_alfil and
# test_movimiento_no_posible_alfil
class TestEsMovimientoPosibleAlfil(unittest.TestCase):

    def test_movimiento_posible_alfil(self):
        self.assertTrue(es_movimiento_posible_alfil((1,2), (4,5)))

    def test_movimiento_no_posible_alfil(self):
        self.assertFalse(es_movimiento_posible_alfil((1,2), (3,4)))

# This class tests the function es_movimiento_posible_torre
class TestEsMovimientoPosibleTorre(unittest.TestCase):

    def test_es_movimiento_posible_torre(self):
        self.assertTrue(es_movimiento_posible_torre((1,1), (2,1)))
        self.assertTrue(es_movimiento_posible_torre((2,2), (2,3)))
        self.assertFalse(es_movimiento_posible_torre((3,3), (4,5)))
        self.assertFalse(es_movimiento_posible_torre((4,4), (5,6)))

# It tests the function es_movimiento_posible_reina.
class TestEsMovimientoPosibleReina(unittest.TestCase):

    def test_movimiento_diagonal(self):
        self.assertTrue(es_movimiento_posible_reina((2,2), (3,3)))

    def test_movimiento_horizontal(self):
        self.assertTrue(es_movimiento_posible_reina((2,2), (4,2)))

    def test_movimiento_vertical(self):
        self.assertTrue(es_movimiento_posible_reina((2,2), (2,4)))

    def test_movimiento_noValido(self):
        self.assertFalse(es_movimiento_posible_reina((2,2), (4,5)))

# TestEsMovimientoPosibleRey is a class that tests the function es_movimiento_posible_rey.
class TestEsMovimientoPosibleRey(unittest.TestCase):

    def test_movimiento_posible(self):
        self.assertTrue(es_movimiento_posible_rey((1,1), (2,2)))

    def test_movimiento_no_posible(self):
        self.assertFalse(es_movimiento_posible_rey((1,1), (3,3)))
        

# A way to make sure that the code in the main() function is only executed when the file is run as a
# script.
if __name__ == '__main__':
    unittest.main()
