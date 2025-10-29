Preguntas LM's

1ª Pregunta: ¿Por qué uso self._Matriz con guión bajo? ¿Qué significa eso?

- Es una buena practica de programación para la encapsulación e indica de solo se debe usar dentro de la clase.

2ª Pregunta: En el método SumarMatrices, ¿por qué uso .shape y no comparo las filas y columnas por separado?

- Usar .shape es más seguro que comparar las filas y columnas por separado y además devuele una tupla con las dimensiones de la matriz.

3ª Pregunta: ¿Por qué CrearMatriz1D llama a CrearMatriz2D(1, nElementos) en lugar de crear un array 1D directamente?

- Es para reutilizar el código y no necesitar duplicar la logica de crear arrays.

4ª Pregunta: En operaciones_menu, ¿por qué creo matriz2 con las mismas dimensiones que matriz1? ¿No podría dejar que el usuario elija?

- Se hace así para que se simplifiquen las operaciones, ya que solo se puede operar con matrices con las mismas dimensiones.

5ª Pregunta: En el método SumarMatrices, ¿por qué retorno self._Matriz + otra_matriz._Matriz directamente? ¿No debería crear un nuevo objeto CMatFloat con el resultado?

- De esta forma retorna el array de Numpy que en este caso es más cómodo ya que es más simple y solo necesito mostrar el resultado ya que no voy ha hacer más operaciones con el.

6ª Pregunta. 

- Al compilar me daba error la llamada a numpy, la solución era que tenia que tener instalada la libreria en visual studio.
aparte para poder instalar numpy tenia que tener instalado python para windows.

7ª Pregunta. ¿Porque para las practicas anteriores no necesitaba tener instalado python?

- Antes no necesitaba python porque usaba una extensión que ya tenia python integrado
