const passwordField = document.querySelector(".passwordField1");
const passwordField2 = document.querySelector(".passwordField2");
toggleBtn = document.querySelector(".input-group .password");
ctoggleBtn = document.querySelector(".input-group .confirm");

toggleBtn.onclick=()=>{
    if (passwordField.type=='password'){
        passwordField.type ='text';
        toggleBtn.classList.add('active');

    }

    else{
        passwordField.type='password';
        toggleBtn.classList.remove('active');
    }
}
ctoggleBtn.onclick=()=>{
    if (passwordField2.type=='password'){
        passwordField2.type ='text';
        toggleBtn.classList.add('active');

    }

    else{
        passwordField2.type='password';
        toggleBtn.classList.remove('active');
    }
}