allDropdowns = document.querySelectorAll('.dropdown-button')
allOptions = document.querySelectorAll('.dropdown-options')
generatedFolderInput = document.getElementById('generated-folder-name')

allOptions.forEach(options => {
    for (const p of options.children) {
        const refersTo = p.parentElement.getAttribute('data-refers-to')
        p.addEventListener('click', () => {
            document.getElementById(refersTo).setAttribute('value', p.innerHTML)
            // change the value of the button
            const previousElements = p.parentElement.parentElement.children
            for (const elt of previousElements) {
                if (elt.getAttribute('type') === 'button') {
                    const buttonValue = elt.getElementsByTagName('span')[0]
                    buttonValue.innerHTML = p.innerHTML
                }
                if (elt.getAttribute('class') === 'dropdown-options') {
                    elt.style.display = 'none'
                    const icon = elt.parentElement.children[0].children[1]
                    icon.className = 'bx bxs-down-arrow'
                }
            }
            generatedFolderInput.value = p.innerHTML
        })
    }
})

allDropdowns.forEach(dropdown => dropdown.addEventListener('click', () => {
    for (const elt of dropdown.parentElement.children) {
        if (elt.classList.contains('dropdown-options')) {
            if (elt.style.display !== 'block') {
                elt.style.display = 'block'
            }
            else {
                elt.style.display = 'none'
            }
            for (const elts of dropdown.parentElement.children) {
                for (const attribute of elts.children) {
                    if (attribute.classList.contains('bxs-down-arrow')) {
                        attribute.className = 'bx bxs-up-arrow'
                    }
                    else if (attribute.classList.contains('bxs-up-arrow')) {
                        attribute.className = 'bx bxs-down-arrow'
                    }
                }
            }
        }
    }
}))