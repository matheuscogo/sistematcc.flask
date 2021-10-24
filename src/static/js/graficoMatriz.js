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