function showRemoveWishlistModal(button) {
    const propertyId = button.dataset.propertyId;
    const propertyName = button.dataset.propertyName;

    // Set modal values
    document.getElementById("propertyId").value = propertyId;
    document.getElementById("propertyName").textContent = propertyName;

    // Dynamically set the form's action to the current page URL
    const currentUrl = window.location.href;
    document.getElementById("removeWishlistForm").action = currentUrl;

    // Show modal
    document.getElementById("removeWishlistModal").showModal();
}

function closeRemoveWishlistModal() {
    document.getElementById("removeWishlistModal").close();
}

function closeRemoveWishlistModal() {
    document.getElementById('removeWishlistModal').close();
}
