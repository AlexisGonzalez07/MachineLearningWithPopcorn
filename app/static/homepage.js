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
  // console.log(m_info)
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
      id: 545187,
      title: 'Bill Burr: Live at Red Rocks',
      year: 2022,
      imdb_id: 'tt21106500',
      tmdb_id: 991115,
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
      id: 1686587,
      title: 'Under the Amalfi Sun',
      year: 2022,
      imdb_id: 'tt15311262',
      tmdb_id: 873127,
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
      id: 1677314,
      title: 'Prizefighter: The Life of Jem Belcher',
      year: 2022,
      imdb_id: 'tt4471908',
      tmdb_id: 943822,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 1686819,
      title: 'For Jojo',
      year: 2022,
      imdb_id: 'tt21044524',
      tmdb_id: 968572,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 1587954,
      title: 'Valley of the Dead',
      year: 2022,
      imdb_id: 'tt10127708',
      tmdb_id: 613093,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 1685368,
      title:
        'The Day the Music Died: The Story of Don McLean\'s "American Pie"',
      year: 2022,
      imdb_id: 'tt12992162',
      tmdb_id: 985709,
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
    {
      id: 1622320,
      title: '1Up',
      year: 2022,
      imdb_id: 'tt13487922',
      tmdb_id: 767401,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 3165380,
      title: 'Prehistoric Planet',
      year: 2022,
      imdb_id: 'tt10324164',
      tmdb_id: 95171,
      tmdb_type: 'tv',
      type: 'movie',
    },
    {
      id: 1601485,
      title: 'Elvis',
      year: 2022,
      imdb_id: 'tt3704428',
      tmdb_id: 614934,
      tmdb_type: 'movie',
      type: 'movie',
    },
    {
      id: 1584304,
      title: 'Thor: Love and Thunder',
      year: 2022,
      imdb_id: 'tt10648342',
      tmdb_id: 616037,
      tmdb_type: 'movie',
      type: 'movie',
    },
  ]

  res.forEach((item) => imdb(item))
}

document.onload = fetchPosters
