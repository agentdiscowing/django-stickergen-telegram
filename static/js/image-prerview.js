function previewImg(input) {
    alert("Function");
    if(input.files && input.files[0]){
        alert("condition");
        let reader = new FileReader();
        reader.onload = function(e){
            alert(e.target.result);
            $("#prevImage").attr("src", e.target.result);
            $("#prevImage").removeAttr('hidden');
            $("#uploadButton").attr("disabled", false);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
function chooseImg(){
    $("#userInput").click();
}
$("#userInput").onchange = function () {
    previewImg(this);
}
