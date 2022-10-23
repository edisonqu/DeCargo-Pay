
function takeValue(event) {
    event.preventDefault()
        window.open("http://localhost:3000/");

    var vendor = document.getElementById("vendor").value
    var invoice = document.getElementById("invoice").value
    var type = document.getElementById("type").value
    var number = document.getElementById("number").value
    var totalAmount = document.getElementById("totalAmount").value
    var item = document.getElementById("item").value
    var payer = document.getElementById("payer").value
    var dataInfo;

    window.open("http://localhost:3000/");


    fetch('http://127.0.0.1:5000/createInvoice', {method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "vendor": vendor,
        "type": type,
        "number": number,
        "totalAmount": totalAmount,
          "item": item,
          "invoice": invoice,
          "payer": payer
      }),
    })
        .then((data )=>{
            data.text().then((data) => {
                dataInfo = data
        console.log('Success:', data);
        document.write("https://gateway.pinata.cloud/ipfs/"+data)
      })
      .catch((error) => {
        console.error('Error:', error);
      });})


}