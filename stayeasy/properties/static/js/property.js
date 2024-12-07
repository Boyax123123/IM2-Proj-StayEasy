
// document.addEventListener("DOMContentLoaded", function () {
//     const checkInInput = document.getElementById("check-in");
//     const checkOutInput = document.getElementById("check-out");
//     const totalPriceElement = document.getElementById("total-price");
//     const bookingButton = document.getElementById("booking-button");
//     const bookingStatusElement = document.getElementById("booking-status");

//     const modal = document.getElementById("modalBooking");
//     const modalDates = document.getElementById("modalBookingDates");
//     const modalTotal = document.getElementById("modalBookingTotal");
//     const cancelBookingButton = document.getElementById("cancel-booking");
//     const confirmBookingButton = document.getElementById("confirm-booking");

//     const pricePerNight = parseFloat('{{ property.price }}'); // Pass property price dynamically
//     const userId = parseInt('{{ user.id }}'); // Pass user ID dynamically
//     const unavailableDates = JSON.parse('{{ unavailable_dates_json|safe }}'); // Pass unavailable dates dynamically

//     // Utility function to format price
//     function formatPrice(amount) {
//         return `₱ ${amount.toLocaleString("en-US", {
//             minimumFractionDigits: 2,
//         })}`;
//     }

//     // Update the calendar to disable unavailable dates
//     function updateCalendar() {
//         const today = new Date().toISOString().split("T")[0];
//         checkInInput.setAttribute("min", today);
//         checkOutInput.setAttribute("min", today);

//         unavailableDates.forEach((date) => {
//             const unavailableDateElement = document.createElement("style");
//             unavailableDateElement.innerHTML = `
//                 input[type="date"]::-webkit-calendar-picker-indicator[date="${date}"] {
//                     color: grey;
//                     pointer-events: none;
//                 }
//             `;
//             document.head.appendChild(unavailableDateElement);
//         });
//     }

//     // Calculate total price
//     function calculateTotal() {
//         const checkInDate = new Date(checkInInput.value);
//         const checkOutDate = new Date(checkOutInput.value);

//         if (checkInInput.value && checkOutInput.value && checkInDate <= checkOutDate) {
//             const diffTime = checkOutDate - checkInDate;
//             const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
//             const totalPrice = diffDays * pricePerNight;

//             totalPriceElement.textContent = formatPrice(totalPrice);
//             bookingButton.disabled = false;

//             // Pass the data to the modal
//             modalDates.textContent = `${checkInInput.value} - ${checkOutInput.value} (${diffDays} days)`;
//             modalTotal.textContent = formatPrice(totalPrice);
//         } else {
//             totalPriceElement.textContent = formatPrice(0);
//             bookingButton.disabled = true;
//         }
//     }

//     // Show modal on clicking "Book" button
//     bookingButton.addEventListener("click", function () {
//         modal.style.display = "flex";
//     });

//     // Close modal when "Cancel" is clicked
//     cancelBookingButton.addEventListener("click", function () {
//         modal.style.display = "none";
//     });

//     // Confirm booking
//     confirmBookingButton.addEventListener("click", async function () {
//         const formData = new FormData();
//         formData.append("checkin_date", checkInInput.value);
//         formData.append("checkout_date", checkOutInput.value);

//         const response = await fetch("{% url 'properties:booking_create' %}", {
//             method: "POST",
//             body: formData,
//             headers: {
//                 "X-CSRFToken": "{{ csrf_token }}",
//             },
//         });

//         if (response.ok) {
//             alert("Booking successfully created!");
//             modal.style.display = "none";
//             location.reload(); // Reload the page to reflect changes
//         } else {
//             alert("Failed to create booking. Please try again.");
//         }
//     });

//     // Check if the user has already booked this property
//     async function checkUserBookingStatus() {
//         const response = await fetch(
//             `{% url 'properties:check_booking_status' property.id user.id %}`
//         );
//         const data = await response.json();

//         if (data.status === "currently_booked") {
//             bookingStatusElement.textContent =
//                 "Currently Booked: Your stay is in progress.";
//         } else if (data.status === "future_booking") {
//             bookingStatusElement.textContent =
//                 "Future Booking: Confirmed and awaiting your stay.";
//         } else if (data.status === "pending_booking") {
//             bookingStatusElement.textContent =
//                 "Booked: Pending Host Approval.";
//         }
//     }

//     // Event listeners for date inputs
//     checkInInput.addEventListener("change", function () {
//         checkOutInput.setAttribute("min", checkInInput.value);
//         calculateTotal();
//     });

//     checkOutInput.addEventListener("change", calculateTotal);

//     // Initialize calendar and check booking status
//     updateCalendar();
//     checkUserBookingStatus();
// });
document.addEventListener("DOMContentLoaded", function () {
    const checkInInput = document.getElementById("check-in");
    const checkOutInput = document.getElementById("check-out");
    const totalAmountElement = document.querySelector("#total-price");
    const bookButton = document.getElementById("show-confirm-modal");
    const modal = document.getElementById("modalBooking");
    const closeModalButton = document.querySelector(".close-modal");
    const confirmBookingButton = document.getElementById("confirm-booking");
    const cancelBookingButton = document.getElementById("cancel-booking");
    const modalBookingDates = document.getElementById("modalBookingDates");
    const modalBookingTotal = document.getElementById("modalBookingTotal");

    const pricePerNight = parseFloat(document.querySelector(".amount").textContent.replace(/[^\d.]/g, ""));
    const unavailableDates = JSON.parse('{{ unavailable_dates_json|safe }}');
    const today = new Date().toISOString().split("T")[0];

    // Format price for display
    function formatPrice(amount) {
        return `₱ ${amount.toLocaleString("en-US", {
            minimumFractionDigits: 2,
        })}`;
    }

    // Disable unavailable dates in the calendar
    function disableUnavailableDates(input) {
        unavailableDates.forEach((date) => {
            const option = document.createElement("option");
            option.value = date;
            option.disabled = true;
            input.appendChild(option);
        });
    }

    // Calculate total price based on selected dates
    function calculateTotal() {
        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);

        if (checkInInput.value && checkOutInput.value && checkInDate <= checkOutDate) {
            const diffTime = checkOutDate - checkInDate;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            const totalPrice = diffDays * pricePerNight;

            totalAmountElement.textContent = formatPrice(totalPrice);
            bookButton.disabled = false;

            // Update modal details
            modalBookingDates.textContent = `${checkInInput.value} to ${checkOutInput.value} (${diffDays} nights)`;
            modalBookingTotal.textContent = formatPrice(totalPrice);
        } else {
            totalAmountElement.textContent = formatPrice(0);
            bookButton.disabled = true;
        }
    }

    // Open booking confirmation modal
    bookButton.addEventListener("click", function () {
        modal.showModal();
    });

    // Close the modal
    closeModalButton.addEventListener("click", function () {
        modal.close();
    });

    cancelBookingButton.addEventListener("click", function () {
        modal.close();
    });

    // Confirm booking
    confirmBookingButton.addEventListener("click", async function () {
        const formData = new FormData(document.getElementById("booking-form"));
        const response = await fetch("{% url 'properties:booking_create' %}", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": "{{ csrf_token }}",
            },
        });

        if (response.ok) {
            alert("Booking successfully created!");
            modal.close();
            location.reload(); // Refresh the page to reflect changes
        } else {
            alert("Failed to create booking. Please try again.");
        }
    });

    // Event listeners for date inputs
    checkInInput.addEventListener("change", function () {
        checkOutInput.min = checkInInput.value; // Ensure checkout is after check-in
        calculateTotal();
    });

    checkOutInput.addEventListener("change", calculateTotal);

    // Initialize unavailable dates and total calculation
    checkInInput.min = today;
    checkOutInput.min = today;
    disableUnavailableDates(checkInInput);
    disableUnavailableDates(checkOutInput);
});
