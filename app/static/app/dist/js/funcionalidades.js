function confirmarDelete(id){
    Swal.fire({
        title: '¿Estas Seguro?',
        text: "No podrás revertir los cambios",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'Cancelar',
        confirmButtonText: 'Si, Borrar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            '¡Borrado!',
            'Tu archivo ya no se encuentra en el sistema',
            'Realizado'
          ).then(function(){
            window.location.href = "/eliminar_producto/"+ id +"/";
          })
        }
      })
}

function confirmarModificar(){
  Swal.fire({
    icon: 'success',
    title: 'Se ha modificado el producto',
    showConfirmButton: false,
    timer: 800
  })
}

