# ajedrez

# Juego en Python 3.9

Este código se utiliza para validar si un movimiento es posible en el juego de ajedrez. Se tienen diferentes funciones para diferentes piezas de ajedrez, que toman como argumento la posición actual de la pieza y la posición a la que se quiere mover. Estas funciones devuelven True si el movimiento es posible y False en caso contrario.

## Explicación del código

La función main() es la función principal que toma como entrada dos tuplas que representan la posición de dos casillas del tablero y la pieza de ajedrez que se quiere utilizar. Luego, la función determina si es posible mover la pieza de la posición actual a la posición deseada llamando a la función correspondiente. Si es posible, la función devuelve "Es posible realizar el movimiento"; de lo contrario, devuelve "No es posible realizar el movimiento".

La clase TestEsMovimientoPosibleCaballo es una clase de prueba que prueba la función es_movimiento_posible_caballo. Esta clase tiene dos métodos: test_movimiento_posible y test_movimiento_no_posible. El primero verifica si la función es_movimiento_posible_caballo devuelve True para un movimiento posible y el segundo verifica si la función devuelve False para un movimiento no posible.

La clase TestEsMovimientoPosibleAlfil también es una clase de prueba que prueba la función es_movimiento_posible_alfil. Esta clase también tiene dos métodos: test_movimiento_posible_alfil y test_movimiento_no_posible_alfil. El primero verifica si la función es_movimiento_posible_alfil devuelve True para un movimiento posible y el segundo verifica si la función devuelve False para un movimiento no posible.

Hay otras tres funciones, es_movimiento_posible_torre, es_movimiento_posible_reina, y es_movimiento_posible_rey, que se utilizan para determinar si un movimiento es posible para la torre, la reina y el rey, respectivamente. Todas estas funciones siguen el mismo patrón que las funciones es_movimiento_posible_caballo y es_movimiento_posible_alfil, y se prueban de manera similar en diferentes clases de prueba que no se muestran aquí.

## Tiempo de codificación

Usando la tecnica de pomodoro para realizar este ejercicio el tiempo invertido fue de un total de 20 horas debido a su complejidad.

## Conclusión

El código proporciona funciones para determinar si un movimiento es posible para diferentes piezas de ajedrez, y se incluyen pruebas unitarias para cada función.

***

Codigo del [Ajedrez](https://github.com/davig3t3/ajedrez/blob/main/ajedrez.py).

***

# Abstract
# Game in Python 3.9

This code is used to validate whether a move is possible in the game of chess. Different functions are available for different chess pieces, which take the current position of the piece and the desired position to move to as arguments. These functions return True if the move is possible and False otherwise.

## Code Explenation

The main() function is the main function that takes two tuples representing the positions of two squares on the board and the chess piece to be used as input. The function then determines if it is possible to move the piece from the current position to the desired position by calling the corresponding function. If possible, the function returns "The move is possible"; otherwise, it returns "The move is not possible".

The TestEsMovimientoPosibleCaballo class is a test class that tests the es_movimiento_posible_caballo function. This class has two methods: test_movimiento_posible and test_movimiento_no_posible. The first verifies if the es_movimiento_posible_caballo function returns True for a possible move and the second verifies if the function returns False for an impossible move.

The TestEsMovimientoPosibleAlfil class is also a test class that tests the es_movimiento_posible_alfil function. This class also has two methods: test_movimiento_posible_alfil and test_movimiento_no_posible_alfil. The first verifies if the es_movimiento_posible_alfil function returns True for a possible move and the second verifies if the function returns False for an impossible move.

There are three other functions, es_movimiento_posible_torre, es_movimiento_posible_reina, and es_movimiento_posible_rey, which are used to determine if a move is possible for the rook, queen, and king, respectively. All these functions follow the same pattern as the es_movimiento_posible_caballo and es_movimiento_posible_alfil functions, and are similarly tested in different test classes that are not shown here.
## Coding time

Using the Pomodoro technique to complete this exercise, the total time invested was 20 hours due to its complexity.

## Conclusion

The code provides functions to determine if a move is possible for different chess pieces, and includes unit tests for each function.

***

Code of [Ajedrez](https://github.com/davig3t3/ajedrez/blob/main/ajedrez.py).

***
