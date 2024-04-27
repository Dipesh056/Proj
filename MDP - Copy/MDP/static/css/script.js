function goToRegister() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
  
    loginForm.classList.remove('active');
    registerForm.classList.add('active');
  }
  
  function goToLogin() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
  
    loginForm.classList.add('active');
    registerForm.classList.remove('active');
  }
  