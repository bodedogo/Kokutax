let addBtn = document.getElementById("addgastoBtn");
let gastosArea = document.getElementById("detalhar-gastos-area");
let submitGasto = document.getElementById("submitGasto");

addBtn.addEventListener("click", () => {
  // PARTE DE FAZER ELE APARECER E DESAPERECER (E FICAR COM O FUNDO TRANSPARENTE)
  gastosArea.style.display = "block";
  gastosArea.style.opacity = "1";
  document.querySelector("header").classList.toggle("fade");
  document.getElementById("content").classList.toggle("fade");

  // Parte de Fazer a Lista Funcionar
});

let close = document.getElementById("fecha-area");
close.addEventListener("click", () => {
  gastosArea.style.display = "none";
  document.querySelector("header").classList.toggle("fade");
  document.getElementById("content").classList.toggle("fade");
});

submitGasto.addEventListener("click", () => {
    let nomeGasto = document.getElementById("nome-gasto").value;
    let valorGasto = document.getElementById("valorGastoInput").value;
    
    console.log(nomeGasto, valorGasto)


});

const ctx = document.getElementById("myChart");
new Chart(ctx, {
  type: "bar",
  data: {
    // labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],

    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
