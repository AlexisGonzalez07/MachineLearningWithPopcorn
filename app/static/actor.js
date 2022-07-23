async function searchHandler(e) {
  e.preventDefault()
  const search = document.querySelector('input').value.trim()
  console.log(search)
  // if (search) {
  //   const res = await fetch(`/api/actor/${search}`)
  //   if (res.ok) {
  //     console.log(res)
  //     // window.location.replace(`/actor/${search}`)
  //   } else {
  //     alert(res.status)
  //   }
  // }
  document.querySelector('input').value = ''
}
document.querySelector('form').addEventListener('submit', searchHandler)
