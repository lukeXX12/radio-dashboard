let bandChart = null;

async function loadData() {
  const res = await fetch("data/metrics.json");
  const data = await res.json();

  document.getElementById("active15").textContent = data.active_last_15_min;

  renderBandChart(data.spots_by_band);
}

function renderBandChart(bandData) {
  const ctx = document.getElementById("bandChart");

  const labels = bandData.map((b) => b.band);
  const values = bandData.map((b) => b.count);

  if (bandChart) {
    bandChart.destroy();
  }

  bandChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          data: values,
        },
      ],
    },
    options: {
      plugins: {
        legend: { display: false },
      },
    },
  });
}

// load immediately
loadData();

// auto-refresh every minute
setInterval(loadData, 60000);
