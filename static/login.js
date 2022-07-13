function login() {
  // 로그인하기 버튼 클릭시 실행
  let id = $("#id").val();
  let pw = $("#pw").val();

  if (id == "") {
    alert("아이디를 입력해주세요");
    $("#id").focus(); // id 칸을 입력하지 않을시 아이디 박스 강조
    return;
  }
  if (pw == "") {
    alert("비밀번호를 입력해주세요.");
    $("#pw").focus(); // pw 칸을 입력하지 않을시 아이디 박스 강조
    return;
  }
  $.ajax({
    //POST방식으로 /api/login url창구로 data 리스트 전송
    type: "POST",
    url: "/api/login",
    data: {
      username_give: id,
      password_give: pw,
    },
    success: function (response) {
      //서버에서 처리 후 결과 받아옴
      let name = response["name"];
      $.cookie("name", name, { path: "/" });

      if (response["result"] == "success") {
        $.cookie("mytoken", response["token"], { path: "/" });

        alert("로그인 성공!");
        window.location.href = "/";
      } else {
        alert("로그인에 실패하였습니다.");
      }
    },
  });
}
