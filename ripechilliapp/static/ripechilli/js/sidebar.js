let openSidebarTrigger = document.getElementById('openSidebarTrigger');
let sidebar = document.getElementById('sidebar');

openSidebarTrigger.addEventListener('click', function triggerNav() {

    if (screen.width <= 578) {

        document.getElementById('sidebar').style.width = "300px";

    } else if (screen.width <= 992) {

        document.getElementById('sidebar').style.width = "300px";

    } else {

        document.getElementById('sidebar').style.width = "300px";

    }

})

let CloseBtnId = document.getElementById('CloseBtnId')
CloseBtnId.addEventListener('click', function closeNav() {
    document.getElementById('sidebar').style.width = "0";
})

let BodytoTrigger = document.getElementById('BodytoTrigger')
if(BodytoTrigger){
    BodytoTrigger.addEventListener('click', closeNav)
}

let getStartedProdId = document.getElementById('getStartedProdId')
if(getStartedProdId){
    getStartedProdId.addEventListener('click',closeNav)
}

let webpricelistsecId = document.getElementById('webpricelistsecId')
if(webpricelistsecId){
    webpricelistsecId.addEventListener('click',closeNav)
}

let logopricelistsec = document.getElementById('logopricelistsec')
if(logopricelistsec){
    logopricelistsec.addEventListener('click',closeNav)
}

let wkowwmID = document.getElementById('wkowwmID')
if(wkowwmID){
    wkowwmID.addEventListener('click',closeNav)
}

let formContactID = document.getElementById('formContactID')
if(formContactID){
    formContactID.addEventListener('click',closeNav)
}
let webPlansheadTitle = document.getElementById('webPlansheadTitle')
if(webPlansheadTitle){
    webPlansheadTitle.addEventListener('click',closeNav)
}
let headTitleGetStarted = document.getElementById('headTitleGetStarted')
if(headTitleGetStarted){
    headTitleGetStarted.addEventListener('click',closeNav)
}
let logoPlansheadTitle = document.getElementById('logoPlansheadTitle')
if(logoPlansheadTitle){
    logoPlansheadTitle.addEventListener('click',closeNav)
}

function closeNav() {
    document.getElementById('sidebar').style.width = "0";
}

