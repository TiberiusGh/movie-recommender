const userSelect = document.getElementById('user-select')
const resultCountInput = document.getElementById('result-count')
const searchForm = document.getElementById('search-form')
const searchButton = searchForm.querySelector('button[type="submit"]')
const statusText = document.getElementById('status')
const resultsSection = document.getElementById('results')
const similarUsersBody = document.getElementById('similar-users-body')
const recommendationsBody = document.getElementById('recommendations-body')

async function fetchJson(url) {
  const response = await fetch(url)
  if (!response.ok)
    throw new Error(`Request to ${url} failed with ${response.status}`)
  return response.json()
}

function tableRow(cells) {
  const row = document.createElement('tr')
  for (const { text, isNumber } of cells) {
    const cell = document.createElement('td')
    cell.textContent = text
    if (isNumber) cell.classList.add('number')
    row.append(cell)
  }
  return row
}

function showStatus(message, isError = false) {
  statusText.textContent = message
  statusText.classList.toggle('error', isError)
}

async function loadUsers() {
  const users = await fetchJson('/api/users')
  for (const user of users) {
    userSelect.append(new Option(`${user.name} (${user.id})`, user.id))
  }
}

function renderSimilarUsers(similarUsers) {
  const rows = similarUsers.map((user) =>
    tableRow([
      { text: user.user_id },
      { text: user.user_name },
      { text: user.similarity_score.toFixed(4), isNumber: true }
    ])
  )
  similarUsersBody.replaceChildren(...rows)
}

function renderRecommendations(recommendations) {
  const rows = recommendations.map((movie) =>
    tableRow([
      { text: movie.movie_id },
      { text: movie.movie_name },
      { text: movie.estimated_score.toFixed(4), isNumber: true }
    ])
  )
  recommendationsBody.replaceChildren(...rows)
}

async function search(event) {
  event.preventDefault()
  const userId = userSelect.value
  const resultCount = Number(resultCountInput.value)

  searchButton.disabled = true
  showStatus('Loading…')

  try {
    const [similarUsers, recommendations] = await Promise.all([
      fetchJson(`/api/users/${userId}/similarusers`),
      fetchJson(`/api/users/${userId}/recommendations`)
    ])
    renderSimilarUsers(similarUsers.slice(0, resultCount))
    renderRecommendations(recommendations.slice(0, resultCount))
    resultsSection.classList.remove('hidden')
    showStatus('')
  } catch (error) {
    showStatus(error.message, true)
  } finally {
    searchButton.disabled = false
  }
}

searchForm.addEventListener('submit', search)
loadUsers().catch((error) => showStatus(error.message, true))
