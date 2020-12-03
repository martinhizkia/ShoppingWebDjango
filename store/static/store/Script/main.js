var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productID: ', productId, 'action: ', action)
    updateUserOrder(productId, action)
  })
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, options);
  });

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, options);
  });

document.getElementById('payment-btn').addEventListener('click', function(e){
    submitFormData();
  }
);

var form = document.getElementById('form')
function submitFormData(){
  console.log('Paid!')

  var alamatPengiriman = {
    'province': null,
    'city' :null,
    'address': null
  }
  alamatPengiriman.province = form.province.value
  alamatPengiriman.city = form.city.value
  alamatPengiriman.address = form.address.value
  console.log(alamatPengiriman)

  var url = '/processorder/'
  fetch(url,{
    method:'POST',
    headers:{
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken},
    body:JSON.stringify({'alamatPengiriman':alamatPengiriman}),
  })
  .then(response =>{
    response.json()
  })
  .then(data =>{
    console.log("Success");
  })
}

function updateUserOrder(productId, action){
  console.log("User is Loggedin, data is being sent!")
  var url = '/updateitem/'
  fetch(url, {
    method: 'POST',
    headers:{
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken},
    body:JSON.stringify({
      'productId': productId,
      'action': action})})
  .then((response)=>{
    return response.json();
  })
  .then(data =>{
    console.log('data:', data)
    location.reload()
  })
}

M.AutoInit();