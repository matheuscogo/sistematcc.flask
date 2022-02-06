window.addEventListener("load", function () {
  var ajax = new XMLHttpRequest();
  var id = document.getElementById("id").value;

  ajax.open("GET", "consultarQuantidade?id=" + id);
  ajax.responseType = "json";
  ajax.send();
  ajax.addEventListener("readystatechange", function () {
    if (ajax.readyState === 4 && ajax.status === 200) {
      var resposta = ajax.response;
      //var xValues = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7", "Dia 8", "Dia 9", "Dia 10", "Dia 11", "Dia 12", "Dia 13", "Dia 14", "Dia 15", "Dia 16", "Dia 17", "Dia 18", "Dia 19", "Dia 20", "Dia 11", "Dia 21", "Dia 22", "Dia 23", "Dia 24", "Dia 25", "Dia 26", "Dia 27", "Dia 28", "Dia 29", "Dia 30", "Dia 31", "Dia 32", "Dia 33", "Dia 34", "Dia 35", "Dia 36", "Dia 37", "Dia 38", "Dia 39", "Dia 40",];

      new Chart("myChart", {
        type: "line",
        data: {
          label: "1 - 114 dias",
          datasets: [{
            data: resposta,
            borderColor: "red",
            fill: false
          }]
        },
        options: {
          legend: { display: false },
          responsive: true,
        }
      }).resize();
    }
  });

});


// new Chart(ctx, {
//   type: "line",
//   data: {
//     labels: ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7", "Dia 8", "Dia 9", "Dia 10"],
//     datasets:[{
//       label: "Quantidade de comida em miligramas",
//       data: [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000],
//       borderWidth: 6,
//       boderColor: 'rgab(77,166,253,0.85)',
//       backgroudColor: 'transparent'
//     }]
//   }
// });