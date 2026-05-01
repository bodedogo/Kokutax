let addBtn = document.getElementById("addgastoBtn");
let gastosArea = document.getElementById("detalhar-gastos-area");


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

// ===== ELEMENTOS =====
let lista = document.getElementById("lista-gastos");
let submitGasto = document.getElementById("submitGasto");

// ===== ESTADO =====
let gastos = JSON.parse(localStorage.getItem("gastos")) || [];

// ===== SALVAR =====
function salvarGastos() {
  localStorage.setItem("gastos", JSON.stringify(gastos));
}

// ===== RENDER LISTA =====
function renderizarGastos() {
  lista.innerHTML = "";

  gastos.forEach((gasto) => {
    let li = document.createElement("li");

    li.innerHTML = `
      ${gasto.nome} 
      <span>R$ ${gasto.valor}</span>
      <button class="remove-btn" data-id="${gasto.id}">-</button>
    `;

    lista.appendChild(li);
  });
}

// ===== GRÁFICO =====
let ctx = document.getElementById("myChart");

let chart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "Gráfico de Gastos",
        data: [],
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

// ===== ATUALIZAR GRÁFICO =====
function atualizarGrafico() {
  let labels = gastos.map((g) => g.nome);
  let valores = gastos.map((g) => g.valor);

  chart.data.labels = labels;
  chart.data.datasets[0].data = valores;

  chart.update();
}

// ===== ADICIONAR GASTO =====
submitGasto.addEventListener("click", () => {
  let nomeGasto = document.getElementById("nome-gasto").value;
  let valorGasto = document.getElementById("valorGastoInput").value;

  if (!nomeGasto || !valorGasto) return;

  let novoGasto = {
    id: Date.now(),
    nome: nomeGasto,
    valor: Number(valorGasto),
  };

  gastos.push(novoGasto);

  salvarGastos();
  renderizarGastos();
  atualizarGrafico();

  // limpa inputs
  document.getElementById("nome-gasto").value = "";
  document.getElementById("valorGastoInput").value = "";
});

// ===== REMOVER GASTO =====
lista.addEventListener("click", (event) => {
  if (event.target.classList.contains("remove-btn")) {
    let id = event.target.dataset.id;

    gastos = gastos.filter((g) => g.id != id);

    salvarGastos();
    renderizarGastos();
    atualizarGrafico();
  }
});

// ===== INICIALIZAÇÃO =====
renderizarGastos();
atualizarGrafico();