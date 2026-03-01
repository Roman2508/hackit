const layout = document.querySelector(".layout")
const modalClose = document.querySelector(".modal-close")
const excursionLink = document.getElementById("excursion-link")

if (excursionLink) {
  excursionLink.addEventListener("click", (e) => {
    e.preventDefault()
    layout.classList.remove("hidden")
  })
}

if (modalClose) {
  modalClose.addEventListener("click", () => {
    layout.classList.add("hidden")
  })
}

// Admin Tabs Logic
const tabButtons = document.querySelectorAll(".tab-btn")
const tabContents = document.querySelectorAll(".admin-tab-content")

tabButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const tabId = btn.getAttribute("data-tab")

    tabButtons.forEach((b) => b.classList.remove("active"))
    tabContents.forEach((c) => c.classList.remove("active"))

    btn.classList.add("active")
    document.getElementById(tabId).classList.add("active")
  })
})

// Tour Page Request Button (scroll to form)
const requestBtn = document.getElementById("request-btn")
if (requestBtn) {
  requestBtn.addEventListener("click", () => {
    document.querySelector(".send-application").scrollIntoView({ behavior: "smooth" })
  })
}
