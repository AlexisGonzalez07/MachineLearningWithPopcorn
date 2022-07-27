async function searchHandler(e) {
  e.preventDefault()
  const search = document.querySelector('input').value.trim()
  console.log(search)
  if (search) {
    const res = await fetch(`/api/actor/${search}`, {
      method: 'post',
      actor: JSON.stringify(search),
      headers: { 'Content-Type': 'application/json' },
    })
    if (res.ok) {
      const r = await res.json()
      console.log(r)

      // let pieData = []
      // let iteration = r[0].length
      // let values = r.length
      // for (let i = 0; i < iteration; i++) {
      //   let item = { value: 0, label: '', color: '' }
      //   for (let j = 0; j < values; j++) {
      //     if (j === 0) {
      //       item.value = r[j][i]
      //     } else if (j === 1) {
      //       item.genre = r[j][i]
      //     } else {
      //       item.color = r[j][i]
      //     }
      //   }
      //   pieData.push(item)

      new Chart(document.getElementById('chart'), {
        type: 'pie',
        data: {
          labels: r.labels,
          datasets: [
            {
              label: 'Population (millions)',
              backgroundColor: r.colors,
              data: r.values,
            },
          ],
        },
        options: {
          title: {
            display: true,
            text: `${search}'s Movie Genre  `,
          },
        },
      })

      // r.map(
      //   (item) => {
      //     console.log(item)
      //   },
      //   // pieData.push({
      //   //   value: item.value,
      //   //   label: label,
      //   //   color: colors,
      //   // }),
      // )
      // console.log(pieData)
      // window.location.replace(`/actor/${search}`)
    } else {
      alert(res.status)
    }
  }
  // window.location.replace(`/actor/${search}`)
  document.querySelector('input').value = ''
}
document.querySelector('form').addEventListener('submit', searchHandler)
