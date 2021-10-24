// Get the modal
var cadastrarMatriz = document.getElementById("cadastrarMatriz");
var span1 = document.getElementsByClassName("fechar")[0];

// When the user clicks on the button, open the modal
function mostrarModal() {
    cadastrarMatriz.style.display = "block";
}

span1.onclick = function() {
    cadastrarMatriz.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modalCadastrar) {
//     modalCadastrar.style.display = "none";
//   }
// }