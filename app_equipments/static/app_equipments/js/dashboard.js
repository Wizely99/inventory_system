icons = document.querySelectorAll('.icon')
console.log(icons)
icons.forEach((icon) => {
    icon.addEventListener('click', (e) => {
        console.log(e.currentTarget.parentNode.children[0].children[1].name)
           
    })
})