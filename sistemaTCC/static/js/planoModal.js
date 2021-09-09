// Get the modal
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
function showmodal(id) {
  modal.style.display = "block";
  document.getElementById('detalhes').src = "detalhesPlano.html" + "?id=" + id;
}

span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal || event.target == cadastrarPlanoCadastrar) {
    modal.style.display = "none";
    cadastrarPlanoCadastrar.style.display = "none";
  }
}