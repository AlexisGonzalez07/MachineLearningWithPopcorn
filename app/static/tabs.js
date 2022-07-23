const tab = (e) => {
  document.location.replace(e.target.href)
}

document.querySelector('.tabs').addEventListener('click', tab)
