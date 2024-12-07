document.addEventListener('DOMContentLoaded', () => {
    window.modalManager = new ModalManager();
});

// When a user tries to perform an action without being logged in
function checkBookingEligibility() {
    if (!isUserLoggedIn) {  // Assuming you have some way of checking user login status
        window.modalManager.showLoginRequired();
    }
}

// Logout confirmation
document.getElementById('logoutLink').addEventListener('click', (e) => {
    e.preventDefault();
    window.modalManager.showLogoutConfirmation();
});

// Wishlist deletion
document.querySelector('.delete-wishlist-btn').addEventListener('click', () => {
    window.modalManager.showDeleteWishlistConfirmation();
});

// Booking confirmation
document.querySelector('.book-property-btn').addEventListener('click', () => {
    checkBookingEligibility(); // Check if the user is logged in before booking
});

// Show a success notification
window.modalManager.showNotification('Booking confirmed successfully!');

// Show an error notification
window.modalManager.showNotification('Failed to delete item', 'error');

// Modal Utility Functions
class ModalManager {
    constructor() {
        this.initializeModals();
    }

    initializeModals() {
        // Close modal buttons for all modals
        document.querySelectorAll('.close-modal').forEach(closeBtn => {
            closeBtn.addEventListener('click', () => {
                const modal = closeBtn.closest('dialog');
                modal.close();
            });
        });

        // Login Required Modal
        const loginRedirectBtn = document.getElementById('loginRedirectBtn');
        const cancelLoginModal = document.getElementById('cancelLoginModal');
        const loginRequiredModal = document.getElementById('loginRequiredModal');

        if (loginRedirectBtn) {
            loginRedirectBtn.addEventListener('click', () => {
                window.location.href = '/accounts/login/'; // Adjust this URL as needed
            });
        }

        if (cancelLoginModal) {
            cancelLoginModal.addEventListener('click', () => {
                loginRequiredModal.close();
            });
        }

        // Logout Confirmation Modal
        const confirmLogoutBtn = document.getElementById('confirmLogoutBtn');
        const cancelLogoutBtn = document.getElementById('cancelLogoutBtn');
        const logoutConfirmModal = document.getElementById('logoutConfirmModal');

        if (confirmLogoutBtn) {
            confirmLogoutBtn.addEventListener('click', () => {
                window.location.href = '/accounts/logout/'; // Adjust this URL as needed
            });
        }

        if (cancelLogoutBtn) {
            cancelLogoutBtn.addEventListener('click', () => {
                logoutConfirmModal.close();
            });
        }

        // Wishlist Delete Modal
        const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
        const cancelDeleteBtn = document.getElementById('cancelDeleteBtn');
        const deleteWishlistModal = document.getElementById('deleteWishlistModal');

        if (confirmDeleteBtn) {
            confirmDeleteBtn.addEventListener('click', () => {
                // Add your wishlist delete logic here
                deleteWishlistModal.close();
                this.showNotification('Removed from wishlist successfully');
            });
        }

        if (cancelDeleteBtn) {
            cancelDeleteBtn.addEventListener('click', () => {
                deleteWishlistModal.close();
            });
        }

        // Booking Confirmation Modal
        const confirmBookingBtn = document.getElementById('confirmBookingBtn');
        const cancelBookingBtn = document.getElementById('cancelBookingBtn');
        const bookingConfirmModal = document.getElementById('bookingConfirmModal');

        if (confirmBookingBtn) {
            confirmBookingBtn.addEventListener('click', () => {
                // Add your booking confirmation logic here
                bookingConfirmModal.close();
            });
        }

        if (cancelBookingBtn) {
            cancelBookingBtn.addEventListener('click', () => {
                bookingConfirmModal.close();
            });
        }

        // Cancel Booking Modal
        const confirmCancelBookingBtn = document.getElementById('confirmCancelBookingBtn');
        const closeCancelBookingBtn = document.getElementById('closeCancelBookingBtn');
        const cancelBookingModal = document.getElementById('cancelBookingModal');

        if (confirmCancelBookingBtn) {
            confirmCancelBookingBtn.addEventListener('click', () => {
                // Add your booking cancellation logic here
                cancelBookingModal.close();
            });
        }

        if (closeCancelBookingBtn) {
            closeCancelBookingBtn.addEventListener('click', () => {
                cancelBookingModal.close();
            });
        }
    }

    // Method to show login required modal
    showLoginRequired() {
        const loginRequiredModal = document.getElementById('loginRequiredModal');
        if (loginRequiredModal) {
            loginRequiredModal.showModal();
        }
    }

    // Method to show logout confirmation modal
    showLogoutConfirmation() {
        const logoutConfirmModal = document.getElementById('logoutConfirmModal');
        if (logoutConfirmModal) {
            logoutConfirmModal.showModal();
        }
    }

    // Method to show delete wishlist confirmation modal
    showDeleteWishlistConfirmation() {
        const deleteWishlistModal = document.getElementById('deleteWishlistModal');
        if (deleteWishlistModal) {
            deleteWishlistModal.showModal();
        }
    }

    // Method to show booking confirmation modal
    showBookingConfirmation() {
        const bookingConfirmModal = document.getElementById('bookingConfirmModal');
        if (bookingConfirmModal) {
            bookingConfirmModal.showModal();
        }
    }

    // Method to show cancel booking modal
    showCancelBookingConfirmation() {
        const cancelBookingModal = document.getElementById('cancelBookingModal');
        if (cancelBookingModal) {
            cancelBookingModal.showModal();
        }
    }

    // Optional: Method to show a simple notification
    showNotification(message, type = 'success') {
        // Create a notification element
        const notification = document.createElement('div');
        notification.classList.add('notification', type);
        notification.textContent = message;
        
        // Append to body
        document.body.appendChild(notification);

        // Remove after 3 seconds
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
}


