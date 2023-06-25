allEditButtons = document.querySelectorAll('.edit-price')

allEditButtons.forEach(editButton => editButton.addEventListener('click', () => {
    for (const node of editButton.parentElement.children) {
        const submitButton = editButton.parentElement.children[2]
        if (node.classList.contains('item-price')) {
            node.classList.add('enabled')
        }
        if (node.classList.contains('edit-price')) {
            node.className = 'hidden'
            submitButton.style.display = 'block'
        }
    }
}))

