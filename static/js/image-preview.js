function chooseImg(){
    $("#userInput").click();
}
function previewImg(input){
    if (input.files && input.files[0])
     {
        var reader = new FileReader();

        reader.onload = function (e) {
           $('#prevImage').attr('src', e.target.result);
           $('#prevImage').removeAttr('hidden');
           $('#uploadButton').attr('disabled', false);
        }
       reader.readAsDataURL(input.files[0]);
    }
}