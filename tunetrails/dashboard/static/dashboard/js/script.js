// Toggle password visibility
document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordInput = document.getElementById('password');
    const icon = this.querySelector('i');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        icon.classList.replace('fa-eye-slash', 'fa-eye');
    }
});

// Form validation & submission
document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();
    e.stopPropagation();

    if (this.checkValidity()) {
        const loginBtn = this.querySelector('.btn-login');
        const originalHTML = loginBtn.innerHTML;

        loginBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Signing In...';
        loginBtn.disabled = true;

        setTimeout(() => {
            alert('Login successful! Welcome to Tunetrails 🎵');
            loginBtn.innerHTML = originalHTML;
            loginBtn.disabled = false;
        }, 1200);
    }

    this.classList.add('was-validated');
});

// Social login placeholders
document.querySelector('.btn-google').addEventListener('click', () => {
    alert('Redirecting to Google authentication...');
});

document.querySelector('.btn-github').addEventListener('click', () => {
    alert('Redirecting to GitHub authentication...');
});

// Prevent background scroll when card is scrolled to edge
document.addEventListener('wheel', function (e) {
    const card = document.querySelector('.login-card');
    const atTop = card.scrollTop === 0;
    const atBottom = card.scrollHeight - card.clientHeight <= card.scrollTop + 1;

    if ((atTop && e.deltaY < 0) || (atBottom && e.deltaY > 0)) {
        e.preventDefault();
    }
}, { passive: false });