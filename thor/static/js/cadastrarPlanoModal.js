// Get the modal
var cadastrarPlanoCadastrar = document.getElementById("cadastrarPlano");
var span1 = document.getElementsByClassName("fechar")[0];

// When the user clicks on the button, open the modal
function mostrarModal() {
  cadastrarPlanoCadastrar.style.display = "block";
}

span1.onclick = function() {
  cadastrarPlanoCadastrar.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modalCadastrar) {
//     modalCadastrar.style.display = "none";
//   }
// }