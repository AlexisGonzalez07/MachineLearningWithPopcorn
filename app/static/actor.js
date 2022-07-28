function titleCase(str) {
  return str
    .split(' ')
    .map((word) => word[0].toUpperCase() + word.slice(1).toLowerCase())
    .join(' ')
}

async function searchHandler(e) {
  e.preventDefault()
  const search = titleCase(document.querySelector('input').value.trim())
  // console.log(search)

  if (search) {
    const res = await fetch(`/api/actor/${search}`, {
      method: 'post',
      actor: JSON.stringify(search),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.ok) {
      const r = await res.json()
      // console.log(r)
      new Chart(document.getElementById('chart'), {
        type: 'doughnut',
        data: {
          labels: r.labels,
          datasets: [
            {
              label: 'Movies',
              backgroundColor: r.colors,
              data: r.values,
              hoverOffset: 10,
            },
          ],
        },
        options: {
          responsive: false,
          plugins: {
            legend: {
              position: 'bottom',
            },
            title: {
              display: true,
              text: `${search}'s Movies Ratio by Genre`,
              fullSize: true,
              padding: 25,
              font: {
                size: 20,
              },
            },
          },
        },
      })
    } else {
      alert(res.status)
    }
  }
  document.querySelector('input').value = ''
}
document.querySelector('form').addEventListener('submit', searchHandler)
