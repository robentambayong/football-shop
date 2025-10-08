// A global variable to manage the timeout, preventing multiple toasts from overlapping badly
let toastTimeout;

function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    const toastProgress = document.getElementById('toast-progress');
    
    if (!toastComponent) return;

    // Clear any existing toast timeout
    clearTimeout(toastTimeout);

    // Reset progress bar
    toastProgress.style.width = '100%';
    toastProgress.style.transition = 'none';

    // Remove old styling classes
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-blue-50', 'border-blue-500', 'text-blue-600'
    );
    toastProgress.classList.remove('bg-red-300', 'bg-green-300', 'bg-blue-300');

    // Apply new styles and icon based on type
    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
        toastProgress.classList.add('bg-green-300');
        toastIcon.innerHTML = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastProgress.classList.add('bg-red-300');
        toastIcon.innerHTML = '❌';
    } else { // 'normal' or any other type
        toastComponent.classList.add('bg-blue-50', 'border-blue-500', 'text-blue-600');
        toastProgress.classList.add('bg-blue-300');
        toastIcon.innerHTML = 'ℹ️';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Show the toast with slide-down animation
    toastComponent.classList.remove('opacity-0', '-translate-y-full');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Start the progress bar animation after a short delay
    setTimeout(() => {
        toastProgress.style.transition = `width ${duration}ms linear`;
        toastProgress.style.width = '0%';
    }, 50);

    // Set timeout to hide the toast
    toastTimeout = setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', '-translate-y-full');
    }, duration);
}