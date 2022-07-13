$(document).ready(function () {
  checkCookie();
});

function checkCookie() {
  const loginStatus = document.cookie.split("; ").find((x) => x.startsWith("mytoken"));

  if (loginStatus) {
    // 로그인 상태 //
    console.log("main js logged in status");
    let loginBtn = document.querySelector("#btn-login");
    loginBtn.innerHTML = "LogOut";
    loginBtn.addEventListener("click", logOut);
  } else {
    console.log("main js logged out status");
  }
}

function logOut() {
  document.cookie = "mytoken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  document.cookie = "name=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  window.location.href = "/";
}

function add() {
  const loginStatus = document.cookie.split("; ").find((x) => x.startsWith("mytoken"));
  if (loginStatus) {
    // 로그인 상태 //
    console.log("main js logged in status");
    window.location.href = "/detail";
  } else {
    alert("로그인이 필요합니다.");
    window.location.href = "/login";
  }
}


function delete_card(index){
  $.ajax({
      type: "POST",
      url: "/api/delete_card",
      data: {index_give:index},
      success: function (response) {
          alert(response["msg"])
          window.location.reload()
      }
  });

}