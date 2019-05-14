$(document).ready(function(){
$('#addheaders').click(
    function () {
        $('.headerParams').toggle()
    }
)


$('.addHeader').click(
    function () {
    var $addInput=$('<div class="headerParams">\n' +
    '                    <input name="headKey" type="text" class="form-control" placeholder="key" />\n' +
    '                    <input name="headValue" type="text" class="form-control" placeholder="value" />' +
    '                     ')
    $('.opt').append($addInput);
    }
)
$('input:radio[name="bodyType"]').click(function () {
     var radioValue=$('input:radio[name="bodyType"]:checked').val();
     console.log(radioValue)
     if(radioValue=='raw'){
         $('.bodyinfo1').append(
             '<textarea  id="bodyinfo" class="form-control" name="about"></textarea>'
         )

     }
      else if (radioValue='form-data'){
             var $addInput=$('<div class="bodyParams">\n' +
    '                    <input name="bodyKey" type="text" class="form-control" placeholder="key" />\n' +
    '                    <input name="bodyValue" type="text" class="form-control" placeholder="value" />' +
    '                     ')
          $('#bodyinfo').remove()
          $('#bodyinfo').append($addInput)
     }
})

})
