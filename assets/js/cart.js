var btns = document.getElementsByClassName('cart')

function updateUserOrder(id,action){
    var url="/shop/update_item";
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'id':id,'action':action})
    })
    .then((response)=>{ return response.json()})
    .then((data)=>{console.log(data);window.location.replace("/shop/cart");})

}
for (var i = 0; i<btns.length; i++){
    btns[i].addEventListener('click', function(){
         console.log(this.dataset.product);
         console.log(user);
         if (user == 'AnonymousUser'){
            window.location.replace("/shop/login");
         }
         else{
             updateUserOrder(this.dataset.product,this.dataset.action);
             
         }
    });
}

