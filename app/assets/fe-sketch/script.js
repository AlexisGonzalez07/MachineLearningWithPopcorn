// movie titles
const carousel = document.querySelector('.carousel-inner')

const imdb = async (el) => {
  const url = `https://movie-details1.p.rapidapi.com/imdb_api/movie?id=${el.imdb_id}`
  const m_info = await fetch(url, {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': '7c400c61c9msh218a2ea93c6f1abp10adbajsn17a8bf4634c4',
      'X-RapidAPI-Host': 'movie-details1.p.rapidapi.com',
    },
  })
  if (m_info.ok) {
    const poster = await m_info.json()
    const innerDiv = document.createElement('div')
    innerDiv.classList = 'carousel-item'
    const carouselImg = document.createElement('img')
    carouselImg.classList = 'd-block img-fluid mx-auto'
    carouselImg.setAttribute('src', poster.image)
    innerDiv.appendChild(carouselImg)
    carousel.appendChild(innerDiv)
  }
}

const fetchPosters = async () => {
  const t_url =
    'https://watchmode.p.rapidapi.com/list-titles/?types=movie&page=1&limit=15&sort_by=relevance_desc&release_date_start=20220101&release_date_end=20220715'

  const movieTitles = await fetch(t_url, {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': '7c400c61c9msh218a2ea93c6f1abp10adbajsn17a8bf4634c4',
      'X-RapidAPI-Host': 'watchmode.p.rapidapi.com',
    },
  })
  const m_titles = await movieTitles.json()
  const res = m_titles.titles

  res.forEach((item) => imdb(item))
}

// window.onload = fetchPosters

// const tab = (e) => {
//   console.log(e.target.href)
//   document.location.replace(e.target.href)
// }

// document.addEventListener('click', tab)
// ================================================

function searchHandler(e) {
  e.preventDefault()
  const search = document.querySelector('input').value.trim()
  console.log(search)
  document.querySelector('input').value = ''
}
document.querySelector('#search').addEventListener('submit', searchHandler)
