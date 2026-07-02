const login_tab = document.getElementById('login-tab');
const register_tab = document.getElementById('register-tab');

const login_form = document.getElementById('login-form');
const register_form = document.getElementById('register-form');

const login_sc = document.getElementById('login-sc');
const register_sc = document.getElementById('register-sc');

function showLoginForm(e) {
    if (e) e.preventDefault(); 
    login_tab.classList.add('tab_is_active');     
    register_tab.classList.remove('tab_is_active'); 
    login_form.classList.remove('is-hidden');
    register_form.classList.add('is-hidden');
}

function showRegisterForm(e) {
    if (e) e.preventDefault(); 
    register_tab.classList.add('tab_is_active');   
    login_tab.classList.remove('tab_is_active');  
    register_form.classList.remove('is-hidden');
    login_form.classList.add('is-hidden');
}

login_tab.addEventListener('click', showLoginForm);  
register_tab.addEventListener('click', showRegisterForm);

login_sc.addEventListener('click', showLoginForm);
register_sc.addEventListener('click', showRegisterForm);