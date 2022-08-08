<h1>Tips para mejorar la velocidad de programación con VSCode</h1>

<h2>Consejo: es la práctica lo que naturaliza los procesos.</h2>

-------------
<br />

<!-- 1 -->
<p style= "font-size:1.5rem;">1. Arrastre vertical de lineas</p>

Apretando la fecha del teclado hacia arriba y hacia abajo, movemos el cursor.
Si apretamos la tecla Alt y movemos las flechas, conseguimos el movimiento de la linea hacia esa dirección.
<div class="code" style="background: gray;">Alt + flecha arriba/abajo</div><br />

También se consigue el mismo resultado partiendo de la selección de multiples lineas. En ese caso se arrastrara todo el bloque seleccionado.
<div class="code" style="background: gray;">Seleccionar bloque de texto + Alt + flecha arriba/abajo</div><br />

<!-- 2 -->
<p style= "font-size:1.5rem;">2. Arrastre horizontal de lineas - Tab</p>

Si queremos manejar la tabulación (o identación) en el bloque de código, debemos seleccionar parcial o totalmente las líneas que se desean desplazar, y luego el botón Tab para desplazarse hacia la derecha, y Shift + Tab para la izquierda.
<div class="code" style="background: gray;">Tab: hacia la derecha <br /> Shift + Tab: hacia la izquierda</div><br />

<!-- 3 -->
<p style= "font-size:1.5rem;">3. Clonar lineas</p>

En vez de seleccionar el bloque de código y apretar ctrl c, ctrl v, podemos copiar una linea, o un bloque completo haciendo Alt + Shift + flecha arriba/abajo
<div class="code" style="background: gray;">Alt + Shift + flecha arriba/abajo</div><br />

<!-- 4 -->
<p style= "font-size:1.5rem;">4. Multicursor Parte 1</p>

Sirve para crear multiples cursores en las lineas adyacentes.
<div class="code" style="background: gray;">Alt + Ctrl + flecha arriba/abajo</div><br />

También puede utilizarse manteniendo apretado el botón Alt y haciendo doble click en la palabras que quieras seleccionar simultáneamente y si es más de una palabra, arrastrar el cursor del mouse con el click apretado junto con la tecla Alt. Sino con Alt + click se crean independientemente. Luego se cierra con la tecla Esc.
<div class="code" style="background: gray;">Alt + mouse</div><br />

<!-- 5 -->
<p style= "font-size:1.5rem;">5. Atajo para acceder a la configuración de atajos</p>

Apretar una vez y Ctrl + K y luego Ctrl + S se ingresa a "Métodos abreviados de teclado"
<div class="code" style="background: gray;">( Ctrl + K ) + ( Ctrl + S )</div><br />

<!-- 6 -->
<p style= "font-size:1.5rem;">6. Comentar parte de codigo</p>

Ingresando a la configuración de atajos, buscar "Agregar comentario de linea" y se sugiere utilizar la configuración "Ctrl + /"
<div class="code" style="background: gray;">( Ctrl + K ) + ( Ctrl + S )
<br />Escribir en el buscador "comentarios" y seleccionar "Agregar comentario de linea"
<br />Cambiar la configuración predeterminada</div>
<br />

<!-- 7 -->
<p style= "font-size:1.5rem;">7. Multicursor Parte 2</p>

Se puede seleccionar todas las coincidencias seleccionadas, es decir, si se selecciona una "hola", se pueden seleccionar en simultáneo todas las veces que "hola" aparece en el código. Para ello se debe apretar Ctrl + F12.
<div class="code" style="background: gray;">Ctrl + F12</div><br />

En cambio si se quiere seleccionar de a una todas las coincidencias encontradas debajo de la selección se debe apretar Ctrl + D, se puede repetir hasta seleccionar las coincidencias necesarias.
<div class="code" style="background: gray;">Ctrl + D (repetidas veces)</div><br />

<!-- 8 -->
<p style= "font-size:1.5rem;">8. Borrar lineas</p>

Manteniendo el cursor sobre la linea, o multiples lineas que se desean borrar, apretar Ctrl + Shift + K, para eliminar toda la linea completamente y arrastrar de abajo una linea hacia arriba.
<div class="code" style="background: gray;">Ctrl + Shift + K</div><br />

<!-- 9 -->
<p style= "font-size:1.5rem;">9. Deshacer y Rehacer</p>

Esto ya es conocido por todos.
<div class="code" style="background: gray;">Ctrl + Z: Deshacer<br />Ctrl + Shift + Z: Rehacer</div><br />

<!-- 10 -->
<!-- Eliminado creacion rápida de archivos -->
<p style= "font-size:1.5rem;">10. Emmet Wrap</p>

Con esta herramienta de VSCode podemos colocar al comienzo y al final de un bloque de texto seleccionado las correspondientes Tags "<>" de apertura y cierre. Luego escribiendo el nombre de la etiqueta se completa, y presionando la tecla Enter queda establecido.<br /> Este atajo permite encerrar el bloque en múltiples etiquetas escribiendo por ejemplo "div>p" va a crear un padre div y un hijo p. Se sugiere la configuración "Alt + W".

<code class="code" style="background: gray;">( Ctrl + K ) + ( Ctrl + S )
<br />Escribir en el buscador "Wrap with abbreviation"
<br />Cambiar la configuración predeterminada</code>
<br />

<p style= "font-size:1.5rem;">12. Ir a la definicion</p>

Cuando estamos trabajando con un código que tiene variables definidas en una parte del archivo o en otro archivo, y nosotros inspeccionamos la parte donde se implementa, no donde se crea la definición, podemos acceder a ella, ya sea, a través de un display en pantalla sin movernos de donde estamos, o dirigirse a la sección del código donde se encuentra la definición, y sino abrira el archivo donde se encuentre almacenada la definición.
<div class="code" style="background: gray;">Alt + F12: en pantalla & Esc (para cerrar)
<br />Alt + clic: te lleva al archivo</div>
<br />

<!-- 13 -->
<p style= "font-size:1.5rem;">13. Manejo de tabs</p>

Si se desea manejar los pestallas de archivos abiertas dentro de VSCode se hace como se menciona a continuación.
<div class="code" style="background: gray;">
Ctrl + Tab: cambio de ventana por solapa
<br />Ctrl + W: cerrar
<br />Ctrl + Shift + T: abrir anterior
<br />( Ctrl K ) + ( Ctrl + W ): cerrar todas
</div>











<!-- (ejercicio 23 multiple cursor) -->

















