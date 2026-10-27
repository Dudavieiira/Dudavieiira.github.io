// Capturar textos do HTML

// Fazer fetch para a API FastAPI

// Receber o JSON de resposta

// Atualizar o HTML com o resultado

async function compararTextos() {
  const texto1 = document.getElementById("texto1").value;
  const texto2 = document.getElementById("texto2").value;

  if (!texto1 || !texto2) {
    alert("Preencha os dois textos!");
    return;
  }

  const response = await fetch("http://127.0.0.1:8000/similaridade", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      texto1: texto1,
      texto2: texto2,
    }),
  });

  const data = await response.json();

  document.getElementById(
    "resultado"
  ).innerText = `Similaridade: ${data.similaridade_percentual}%`;
}
