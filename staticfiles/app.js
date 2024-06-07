setTimeout(() => {
    let alerts = document.querySelectorAll(".alert_warning, .alert_success");
    alerts.forEach((alert) => {
        alert.remove();
    });
},3000);