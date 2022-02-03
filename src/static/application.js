$(document).ready(function() {
    $.ajaxSetup({
        type: "GET",
        data: {},
        dataType: 'json',
        xhrFields: {
           withCredentials: true
        },
        crossDomain: true,
        contentType: 'application/json; charset=utf-8'
    });

    $("#hello").click(function(event){
        alert('Hallo')
    });
    
});


async function doSomeThing() {
    console.log('some thing will be doing');
    const res = await fetch('http://127.0.0.1:5000/api/user', {
        mode: 'cors',
        headers: {
          'Access-Control-Allow-Origin':'*'
        }
      });
    const json = await res.json();
    console.log('user: ', json);
}