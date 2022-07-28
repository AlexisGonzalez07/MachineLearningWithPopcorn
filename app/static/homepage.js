// movie titles
const carousel = document.querySelector('.carousel-inner')

const imdb = async (el, i) => {
  const posterArr = [
    'https://m.media-amazon.com/images/M/MV5BOWY4MmFiY2QtMzE1YS00NTg1LWIwOTQtYTI4ZGUzNWIxNTVmXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg',
    'https://i.ebayimg.com/images/g/uhsAAOSw-Cti1Mxu/s-l500.jpg',
    'https://m.media-amazon.com/images/M/MV5BNzBjZGFkNTUtYTFlNS00Yjg4LWExNjEtODAxMjFmZTY0OGIyXkEyXkFqcGdeQXVyMjAwNzczNTU@._V1_FMjpg_UX1000_.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/81Xo-x5AT0L.__AC_SX300_SY300_QL70_FMwebp_.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/81zWZ6aB74L.__AC_SX300_SY300_QL70_FMwebp_.jpg',
  ]
  // const url = `https://movie-details1.p.rapidapi.com/imdb_api/movie?id=${el.imdb_id}`
  // const m_info = await fetch(url, {
  //   method: 'GET',
  //   headers: {
  //     'X-RapidAPI-Key': '7c400c61c9msh218a2ea93c6f1abp10adbajsn17a8bf4634c4',
  //     'X-RapidAPI-Host': 'movie-details1.p.rapidapi.com',
  //   },
  // })
  // console.log(m_info)
  // if (m_info.ok) {
  // const poster = await m_info.json()
  const innerDiv = document.createElement('div')
  innerDiv.classList = 'carousel-item'
  const carouselImg = document.createElement('img')
  carouselImg.classList = 'd-block img-fluid mx-auto'
  carouselImg.setAttribute('src', posterArr[i])
  innerDiv.appendChild(carouselImg)
  carousel.appendChild(innerDiv)
  // }
}

const fetchPosters = async () => {
  // const t_url =
  //   'https://watchmode.p.rapidapi.com/list-titles/?types=movie&page=1&limit=15&sort_by=relevance_desc&release_date_start=20220101&release_date_end=20220715'

  // const movieTitles = await fetch(t_url, {
  //   method: 'GET',
  //   headers: {
  //     'X-RapidAPI-Key': '7c400c61c9msh218a2ea93c6f1abp10adbajsn17a8bf4634c4',
  //     'X-RapidAPI-Host': 'watchmode.p.rapidapi.com',
  //   },
  // })
  // const m_titles = await movieTitles.json()
  // console.log(m_titles)
  // const res = m_titles.titles

  const res = [
    {
      id: 1616014,
      title: 'The Gray Man',
      year: 2022,
      imdb_id: 'tt1649418',
      tmdb_id: 725201,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 1679274,
      title: 'Persuasion',
      year: 2022,
      imdb_id: 'tt13456318',
      tmdb_id: 820912,
      tmdb_type: 'movie',
      type: 'movie',
    },

    {
      id: 1686554,
      title: "My Daughter's Killer",
      year: 2022,
      imdb_id: 'tt21049266',
      tmdb_id: 992536,
      tmdb_type: 'movie',
      type: 'movie',
    },

    {
      id: 1632034,
      title: 'Z-O-M-B-I-E-S 3',
      year: 2022,
      imdb_id: 'tt14301252',
      tmdb_id: 809107,
      tmdb_type: 'movie',
      type: 'movie',
    },

    {
      id: 1255914,
      title: 'Minions: The Rise of Gru',
      year: 2022,
      imdb_id: 'tt5113044',
      tmdb_id: 438148,
      tmdb_type: 'movie',
      type: 'movie',
    },
  ]

  res.forEach((item, i) => imdb(item, i))
}

window.onload = fetchPosters
