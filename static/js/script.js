let items = document.querySelectorAll(".skills-conent span")
let startWidth = 0
// start count

window.onload = function () {
    items.forEach((el) => startcount(el))
}

function startcount(el) {
    let goal = el.dataset.goal
    let count = setInterval(() => {
        if (startWidth >= goal) {
            clearInterval(count)
        }
        el.style.width = `${startWidth}%`
        startWidth++;
    }, 2000 / goal)
}