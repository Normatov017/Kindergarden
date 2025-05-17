document.addEventListener("DOMContentLoaded", () => {
    console.log("Global JS yuklandi");

    // alertlarni avtomatik tarzda yashirish
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 4000);
    });
});
