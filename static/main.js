function imgToBase64ByFileReader(url) {
  return new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest();
    xhr.onload = () => {
      let reader = new FileReader();
      reader.onloadend = function () {
        resolve(reader.result);
        document.getElementById("cafe-image").setAttribute("src", reader.result);
      };
      reader.readAsDataURL(xhr.response); //Base64형식으로 인코딩
    };
    xhr.open("GET", url);
    xhr.responseType = "blob";
    xhr.send();
  });
}
function loadFile(input) {
  let file = input.files[0]; //선택된 파일 가져오기

  let newImage = document.createElement("img"); //새 이미지 추가
  newImage.src = URL.createObjectURL(file); //이미지 source 가져오기
  newImage.id = "cafe-image";
  newImage.style.width = "100%";
  newImage.style.height = "100%";
  newImage.style.objectFit = "cover";

  //이미지를 image-show div에 추가
  let container = document.getElementById("image-show");
  container.appendChild(newImage);

  //이미지를 서버에 저장하기 위해 base64 형태로 변환
  imgToBase64ByFileReader(document.getElementById("cafe-image").getAttribute("src"));
}

function save_order() {
  let img = $("#cafe-image").attr("src");
  let region = $("#region").val();
  let content = $("#content").val();
  let checker = document.cookie.split(";").find((x) => x.startsWith("name"));

  let name = decodeURI(checker);
  console.log(name);

  $.ajax({
    type: "POST",
    url: "/travel",
    data: { image_give: img, region_give: region, content_give: content, names_give: name },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload("/");
    },
  });
}
