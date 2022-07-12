

$(document).ready(function () {
    checkCookie();
});

function checkCookie() {
    const test = document.cookie
        .split('; ')
        .find(x => x.startsWith('mytoken'))

    if (test) { // 로그인 상태 //
        console.log('main js logged in status')

    } else {

        console.log('main js logged out status')

    }

}





function logOut() {
    document.cookie = "mytoken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "name=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.href = "/"
}



