let registerForm = document.getElementById('submitBtnId');

// Student Name 
let studentName = document.getElementById('studentName');
studentName.addEventListener('input', function checkName() {
    let studentNameAlert = document.getElementById('studentNameAlert');
    if ((studentName.value.length <= 2) || (studentName.value.length >= 40)) {
        let msg = `Name should be of <strong> 2 to *40 characters </strong>`
        let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
        studentNameAlert.innerHTML = alertMsg
        registerForm.disabled = true
    } else {
        let msg = `<strong>Success</strong>`
        let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
        studentNameAlert.innerHTML = alertMsg
        registerForm.disabled = false
    }
})

// Phone Number Validation 
let phoneNumber = document.getElementById('phoneNumber');
phoneNumber.addEventListener('input', function phoneNumAuthen() {
    let phoneNumberAlert = document.getElementById('phoneNumberAlert');
    if (phoneNumber.value.length != 10) {
        let msg = `Phoe number should be <strong> 10 digits </strong>`
        let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
        phoneNumberAlert.innerHTML = alertMsg
        registerForm.disabled = true
    } else {
        let msg = `<strong>Success</strong>`
        let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
        phoneNumberAlert.innerHTML = alertMsg
        registerForm.disabled = false
    }
})

// emailName Validation 
let emailName = document.getElementById('emailName');
emailName.addEventListener('input', function mailAuthen() {
    let emailNameAlert = document.getElementById('emailNameAlert')
    let mailLogicRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (emailName.value.match(mailLogicRegex)) {
        let msg = `<strong>Success</strong>`
        let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
        emailNameAlert.innerHTML = alertMsg
        registerForm.disabled = false
    } else {
        let msg = `Enter valid <strong> email address </strong>`
        let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
        emailNameAlert.innerHTML = alertMsg
        registerForm.disabled = true
    }
})

// Address Verification 
// let inputAddress = document.getElementById('inputAddress');
// inputAddress.addEventListener('input', function checkAdd() {
//     let inputAddressAlert = document.getElementById('inputAddressAlert');
//     if ((inputAddress.value.length <= 8) || (inputAddress.value.length >= 100)) {
//         let msg = `Address should be of <strong> 8 to *100 characters </strong>`
//         let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
//         inputAddressAlert.innerHTML = alertMsg
//         registerForm.disabled = true
//     } else {
//         let msg = `<strong>Success</strong>`
//         let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
//         inputAddressAlert.innerHTML = alertMsg
//         registerForm.disabled = false
//     }
// })

// https://api.postalpincode.in/pincode/801105
let inputZip = document.getElementById("inputZip")
inputZip.addEventListener('input', function fill(){
        let inputZipAlert = document.getElementById('inputZipAlert')
        let state = document.getElementById('inputState')
        let district = document.getElementById('inputCity')
        if(inputZip.value.length==6){
            let api_key = `https://api.postalpincode.in/pincode/${inputZip.value}`
            async function getdata(){
                let response = await fetch(api_key)
                let data = await response.json()
                return data;
            }
            getdata().then(function(data){
                let stateval = data[0].PostOffice[0].State
                let distval = data[0].PostOffice[0].District
                state.value = `${stateval}`
                district.value = `${distval}`
            })
            let msg = `<strong>Success </strong>`
            let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
            inputZipAlert.innerHTML = alertMsg
            registerForm.disabled = true
        }else{
            let msg = `PIN Code should be of <strong>6 digits </strong>`
            let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
            inputZipAlert.innerHTML = alertMsg
            registerForm.disabled = true
        }
    })

// // City Name 
// let inputCity = document.getElementById('inputCity');
//     let inputCityAlert = document.getElementById('inputCityAlert');
//     if ((inputCity.value.length <= 2) || (inputCity.value.length >= 40)) {
//         let msg = `City name should be of <strong> 2 to *40 characters </strong>`
//         let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
//         inputCityAlert.innerHTML = alertMsg
//         registerForm.disabled = true
//     } else {
//         let msg = `<strong>Success</strong>`
//         let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
//         inputCityAlert.innerHTML = alertMsg
//         registerForm.disabled = false
//     }

// // State Name 
// let inputState = document.getElementById('inputState');
// inputState.addEventListener('input', function checkName() {
//     let inputStateAlert = document.getElementById('inputStateAlert');
//     if ((inputState.value.length <= 2) || (inputState.value.length >= 40)) {
//         let msg = `State name should be of <strong> 2 to *40 characters </strong>`
//         let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
//         inputStateAlert.innerHTML = alertMsg
//         registerForm.disabled = true
//     } else {
//         let msg = `<strong>Success</strong>`
//         let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
//         inputStateAlert.innerHTML = alertMsg
//         registerForm.disabled = false
//     }
// })
