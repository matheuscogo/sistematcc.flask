// var xValues = [100,200,300,400,500,600,700,800,900,1000];

// new Chart("myChart", {
//   type: "line",
//   data: {
//     labels: xValues,
//     datasets: [{
//       data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
//       borderColor: "red",
//       fill: false
//     },{
//       data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
//       borderColor: "green",
//       fill: false
//     },{
//       data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
//       borderColor: "blue",
//       fill: false
//     }]
//   },
//   options: {
//     legend: {display: false}
//   }
// });

// function setDias(dias)
//   var xValues = dias;
//   return xValues

// function setQuantidade(quantidade)
//   var data = quantidade;
//   return data;
  
// new Chart("myChart", {
//   type: "line",
//   data: {
//     labels: [setDias],
//     datasets: [{
//       data: setQuantidade,
//       borderColor: "red",
//       fill: false
//     }]
//   },
//   options: {
//     legend: {display: false}
//   }
// });

var xValues = ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5","Dia 6","Dia 7","Dia 8","Dia 9","Dia 10",];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      data: [2000, 2000, 2000, 2000, 3000, 3000, 3000, 2000, 3500, 3500],
      borderColor: "red",
      fill: false
    }]
  },
  options: {
    legend: {display: false}
  }
});