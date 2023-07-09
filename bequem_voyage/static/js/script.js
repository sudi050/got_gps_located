window.addEventListener('DOMContentLoaded', function() {
    var priceButton = document.getElementById('price-button');
    var priceBreakdown = document.getElementById('price-breakdown');

    priceButton.addEventListener('click', function() {
        if (priceBreakdown.style.display === 'none') {
            priceBreakdown.style.display = 'block';
        } else {
            priceBreakdown.style.display = 'none';
        }
    });
});

// Set the receipt details
var date = new Date().toLocaleDateString();
var distance = 275;
var rate = 20;
var firstKilometerCharge = 30;
var maintenanceFeePerKm = 1000 / 150;
var petrolCharge = 106 * (distance / 15);
var totalFare = firstKilometerCharge + (distance - 1) * rate + (Math.floor(distance / 150) * maintenanceFeePerKm) + petrolCharge;

// Update the HTML elements with the receipt details
document.getElementById("date").textContent = date;
document.getElementById("fare").textContent = "Rs " + totalFare.toFixed(2);
document.getElementById("distance-fare").textContent = ((distance - 1) * rate).toFixed(2);
document.getElementById("petrol-charge").textContent = petrolCharge.toFixed(2);
