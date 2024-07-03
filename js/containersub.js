function toggleContainerColor() {
    var container = document.querySelector('.containersub');
    container.classList.toggle('clicked');

    var containerText = document.querySelector('.container-text');
    containerText.style.display = container.classList.contains('clicked') ? 'block' : 'none'; // Buton açık olduğunda metni göster
}