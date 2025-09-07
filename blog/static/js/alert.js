document.addEventListener("DOMContentLoaded", function () {
    const flashes = document.querySelectorAll(".flash-message");
    flashes.forEach(flash => {
        // закрити по кліку
        flash.querySelector(".close-btn").addEventListener("click", () => {
            flash.style.display = "none";
        });

        // автоматично ховати через 5 секунд
        setTimeout(() => {
            flash.style.opacity = "0";
            setTimeout(() => flash.remove(), 500);
        }, 5000);
    });
});


function openModal(postId, title) {
  document.getElementById("globalModal").style.display = "flex";
  document.getElementById("modalTitle").textContent = `Delete "${title}"?`;
  document.getElementById("deleteForm").action = `/post/${postId}/delete`;
}

function closeModal() {
  document.getElementById("globalModal").style.display = "none";
}
