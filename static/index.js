const countries = [
  { title: "Іспанія", flag: "Flag_of_Spain.svg", background: "spain.webp" },
  { title: "Португалія", flag: "", background: "" },
  { title: "Греція", flag: "", background: "" },
  { title: "Ізраїль", flag: "", background: "" },
  { title: "Туреччина", flag: "", background: "" },
  { title: "Єгипет", flag: "", background: "" },
  { title: "Туніс", flag: "", background: "" },
  { title: "Таїланд", flag: "", background: "" },
  { title: "ОАЕ", flag: "", background: "" },
  { title: "Шрі Ланка", flag: "", background: "" },
  { title: "Індія", flag: "", background: "" },
  { title: "Домініканська р.", flag: "", background: "" },
]

/* tabs */

const adminTourTab = document.querySelector(".admin-tour-tab")
const adminCountryTab = document.querySelector(".admin-country-tab")
const tourForm = document.querySelector(".tour-form")
const countryForm = document.querySelector(".country-form")

const onAdminTabClick = (e) => {
  if (e.target.classList.contains("admin-tour-tab")) {
    adminTourTab.classList.add("active")
    adminCountryTab.classList.remove("active")

    tourForm.classList.add("active")
    countryForm.classList.remove("active")
  }
  if (e.target.classList.contains("admin-country-tab")) {
    adminCountryTab.classList.add("active")
    adminTourTab.classList.remove("active")

    countryForm.classList.add("active")
    tourForm.classList.remove("active")
  }
}

if (adminTourTab && adminCountryTab) {
  adminTourTab.addEventListener("click", onAdminTabClick)
  adminCountryTab.addEventListener("click", onAdminTabClick)
}

/* modal */

const modalCloseButtons = document.querySelectorAll(".modal-close")

const onModalClose = (e) => {
  const modalLayout = e.target.closest(".modal-layout")
  modalLayout.classList.add("hidden")
}

modalCloseButtons.forEach((button) => {
  button.addEventListener("click", onModalClose)
})


const toursModal = document.querySelector("#tours-modal")
const tourDetailsModal = document.querySelector("#tour-details-modal")
const openTourModalButton = document.querySelector("#open-tour-modal")
const modalTourButtons = document.querySelectorAll('.modal-tour-button')

openTourModalButton.addEventListener('click', () => {
  toursModal.classList.remove('hidden')
})

modalTourButtons.forEach((el) => {
  el.addEventListener('click', (e) => {
    toursModal.classList.add('hidden')
    tourDetailsModal.classList.remove('hidden')
    const id = e.target.getAttribute('id')
    console.log(id)
  })
})

