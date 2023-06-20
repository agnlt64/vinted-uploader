const allDropdowns = document.querySelectorAll('.dropdown-button')
const allOptions = document.querySelectorAll('.dropdown-options')

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
                }
            }
        }
    }
}))