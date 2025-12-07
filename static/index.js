// Menu
const mainMenuTrigger = document.querySelector(".menu-trigger")
const mainMenuContainer = document.querySelector(".main-menu-container")

mainMenuTrigger.addEventListener("click", () => {
  mainMenuContainer.classList.toggle("main-menu-opened")
})

/* photo gallery */
let allComments = [
  "Цей кадр нереально крутий! :)",
  "Ти вмієш дивувати! Кожен кадр - поєднання життєлюбності і краси",
  "Спинися мить, прекрасна ти!",
  "Просто супер! Як тобі це вдається?",
  "Це прото шедевр мистецтва",
  "В цьому штучному світі так приємно знайти щось натуральне))",
  "Клас!!!))",
  "Нереально чудово!",
  "А ти вмієш дивувати ;)",
  "Це фото так і проситься в рамочку на стіну",
]

let allDescriptions = [
  "Коли радості немає меж",
  "Любов в кожному пікселі",
  "Фото заряджене позитивом",
  "Зловив дзен",
  "Як мало потрібно для щастя",
  "Знали б ви що в мене на умі! ;)",
  "Show must go on",
  "Good vibes only",
  "My inspiration",
  "On my way to paradise",
  "Що це, якщо не любов? Х)",
]

function generateRandomElement(array) {
  const randomIndex = Math.floor(Math.random() * (array.length - 1))
  return array[randomIndex]
}

function generatePicturesDB(number) {
  let pictures = []
  for (let i = 0; i < number; i++) {
    let comments = []

    for (let j = 0; j < Math.floor(Math.random() * 10); j++) {
      comments.push(generateRandomElement(allComments))
    }

    let pictureExample = {
      src: `../static/img/photos/${i}.jpg`,
      likes: Math.floor(Math.random() * 200),
      effect: "none",
      description: generateRandomElement(allDescriptions),
      comments: comments,
      commentsNumber: comments.length,
    }

    pictures.push(pictureExample)
  }

  return pictures
}

let picturesDB = generatePicturesDB(25)
console.log(picturesDB)

function showPictures(photosArray) {
  let picturesTemplate = document.querySelector("#templatePictureExample")
  let pictureExample = picturesTemplate.content.querySelector(".pictureExample")
  let pictureContainer = document.querySelector(".pictureContainer")
  for (let i = 0; i < photosArray.length; i++) {
    let photoBlock = pictureExample.cloneNode(true)
    const currentPhoto = photosArray[i]
    photoBlock.querySelector(".pictureImg").src = currentPhoto.src
    photoBlock.querySelector(".pictureImg").style.filter = currentPhoto.filter
    photoBlock.querySelector(".pictureComments").innerText = currentPhoto.commentsNumber
    photoBlock.querySelector(".pictureLike").innerText = currentPhoto.likes
    pictureContainer.append(photoBlock)
  }
}

showPictures(picturesDB)

function showCheckedPicture(picture) {
  let openedPictureContainer = document.querySelector(".openedPictureContainer")
  openedPictureContainer.querySelector(".openedPictureImg").src = picture.src
  openedPictureContainer.querySelector(".openedPictureImg").style.filter = picture.effect
  openedPictureContainer.querySelector(".descriptionText").innerText = picture.description
  openedPictureContainer.querySelector(".pictureComments").innerText = picture.commentsNumber
  openedPictureContainer.querySelector(".pictureLike").innerText = picture.likes
  let commentsContainer = document.querySelector(".pictureCommentsContainer")
  let commentsTemplate = document.querySelector("#commentsTemplate").content.querySelector(".commentBlock")
  for (let i = 0; picture.comments.lenght; i++) {
    let comment = commentsTemplate.cloneNode(true)
    comment.querySelector(".commentText").innerText = picture.comments[i]
    commentsContainer.append(comment)
  }
  openedPictureContainer.classList.remove("hidden")
}

// showCheckedPicture(picturesDB[3])

const pictureContainer = document.querySelector(".pictureContainer")
pictureContainer.addEventListener("click", (event) => {
  let checkedElement = event.target
  if (checkedElement.classList.contains("pictureImg")) {
    const pictureSrc = checkedElement.getAttribute("src")
    for (let i = 0; i < picturesDB.length; i++) {
      if (picturesDB[i].src === pictureSrc) {
        showCheckedPicture(picturesDB[i])
        break
      }
    }
  }
})

const closeButton = document.querySelector(".closeButton")
closeButton.addEventListener("click", (event) => {
  document.querySelector(".openedPictureContainer").classList.add("hidden")
  commentsContainer.innerHTML = ""
})

/* Upload image form */
const inputUploadFile = document.querySelector("#inputUploadFile")
inputUploadFile.addEventListener("change", function () {
  if (inputUploadFile.files[0].type.includes("image")) {
    let reader = new FileReader()
    reader.readAsDataURL(inputUploadFile.files[0])

    reader.addEventListener("load", function () {
      let uploadImage = document.querySelector(".uploadImage")
      uploadImage.src = reader.result
      let labelsEffectsSettings = document.querySelectorAll(".uploadEffectPreview")
      for (let i = 0; i < labelsEffectsSettings.length; i++) {
        labelsEffectsSettings[i].style.backgroundImage = `url(${reader.result})`
      }
      let settingsContainer = document.querySelector(".uploadImageOverlay")
      settingsContainer.classList.remove("hidden")
    })
  }
})

let buttonCloseUpload = document.querySelector("#uploadCancel")
buttonCloseUpload.addEventListener("click", function () {
  document.querySelector(".uploadImageOverlay").classList.add("hidden")
})

let uploadEffectFieldset = document.querySelector(".uploadEffectFieldset")
uploadEffectFieldset.addEventListener("change", function (event) {
  document.querySelector(".inputActive").classList.remove("inputActive")
  document.querySelector(`[for="${event.target.id}"]`).classList.add("inputActive")
})
