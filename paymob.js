const API = ''        // your api here
// const integrationID = 2627644;

async function firstStep () {
    let data = {
        "api_key": ""
    }

    let request = await fetch('https://accept.paymob.com/api/auth/tokens' , {
        method : 'post',
        headers : {'Content-Type' : 'application/json'} ,
        body : JSON.stringify(data)
    })

    let response = await request.json()

    let token = response.token

    secondStep(token)
}

async function secondStep (token) {
    let data = {
        "auth_token":  token,
        "delivery_needed": "false",
        "amount_cents": "100",
        "currency": "EGP",
        "items": [],
    }

    let request = await fetch('https://accept.paymob.com/api/ecommerce/orders' , {
        method : 'post',
        headers : {'Content-Type' : 'application/json'} ,
        body : JSON.stringify(data)
    })

    let response = await request.json()

    let id = response.id
    // let id=""
    thirdStep(token , id)
}

async function thirdStep (token , id) {
    let data = {
        "auth_token": token,
        "amount_cents": "10000", 
        "expiration": 3600, 
        "order_id": id,
        "billing_data": {
            "apartment": "803", 
            "email": "claudette09@exa.com", 
            "floor": "42", 
            "first_name": "Clifford", 
            "street": "Ethan Land", 
            "building": "8028", 
            "phone_number": "+86(8)9135210487", 
            "shipping_method": "PKG", 
            "postal_code": "01898", 
            "city": "Jaskolskiburgh", 
            "country": "CR", 
            "last_name": "Nicolas", 
            "state": "Utah"
        }, 
        "currency": "EGP", 
        "integration_id": "4538217"
    }

    let request = await fetch('https://accept.paymob.com/api/acceptance/payment_keys' , {
        method : 'post',
        headers : {'Content-Type' : 'application/json'} ,
        body : JSON.stringify(data)
    })

    let response = await request.json()
        console.log(response)
    let TheToken = response.token
  

    cardPayment(TheToken)
}


async function cardPayment (token) {
    let iframURL = `https://accept.paymob.com/api/acceptance/iframes/831751?payment_token=${token}`
    console.log(iframURL)
    // location.href = iframURL
}

firstStep()
