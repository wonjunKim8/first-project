function id_verify() {
  if ($("#id").val().length > 5) {
    let id = $("#id").val();

    $.ajax({
      type: "POST",
      url: "/api/user_check",
      data: {
        username_give: id,
      },
      success: function (response) {
        if (response["exist"]) {
          alert("이미 등록된 아이디입니다.");
          $("#id").focus();
        } else {
          alert("사용가능한 아이디입니다. ");
        }
      },
    });
  } else {
    alert("ID를 6자 이상 입력해주세요.");
  }
}

function signup_success() {
  if ($("#id").val().length > 5) {
    let id = $("#id").val();
    let pw = $("#pw").val();
    let pw2 = $("#pw2").val();
    if (pw == pw2) {
      if ($("#name").val().length > 2) {
        let name = $("#name").val();

        $.ajax({
          type: "POST",
          url: "/signup",
          data: { id_give: id, pw_give: pw, name_give: name },
          success: function (response) {
            alert("회원가입에 완료하였습니다,로그인화면으로 이동합니다.");
            window.location.href = "/login";
          },
        });
      } else {
        alert("닉네임을 3자 이상 입력해주세요.");
      }
    } else {
      alert("비밀번호가 서로 일치하지 않습니다.");
    }
  } else {
    alert("ID를 6자 이상 입력해주세요.");
  }
}

function signup_cancel() {
  alert("홈 화면으로 돌아갑니다.");
  window.location.href = "/";
  //    메인페이지 입력
}
