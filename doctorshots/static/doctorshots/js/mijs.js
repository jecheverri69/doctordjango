/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

// este metodo me carga el contenido de el formulario editar empleado a la ventana modal
function editarEmpleado(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('modaleditar').innerHTML = respuesta;
        },
        error: function() {
            console.log("No se a podido tener la informacion");
        }
    })


}