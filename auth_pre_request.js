const login_url=pm.variables.get("login_url");
const email=pm.variables.get("email");
const password=pm.variables.get("password");
// set these before  currentAccessToken  , accessTokenExpiry
const echoPostRequest = {

  url: login_url,
  method: 'POST',
  header: 'Content-Type:application/json',
  body: {
    mode: 'application/json',
    raw: JSON.stringify(
        {
        	'email':email,
            'password':password
        })
  }
};

var getToken = true;

if (!pm.environment.get('accessTokenExpiry') || 
    !pm.environment.get('currentAccessToken')) {
    console.log('Token or expiry date are missing')
} else if (pm.environment.get('accessTokenExpiry') <= (new Date()).getTime()) {
    console.log('Token is expired')
} else {
    getToken = false;
    console.log('Token and expiry date are all good');
}

if (getToken === true) {
    pm.sendRequest(echoPostRequest, function (err, res) {
    console.log(err ? err : res.json());
        if (err === null) {
            console.log('Saving the token and expiry date')
            var responseJson = res.json();
            pm.environment.set('currentAccessToken', responseJson.access)
    
            var expiryDate = new Date();
            expiryDate.setSeconds(expiryDate.getSeconds() + responseJson.expires_in);
            pm.environment.set('accessTokenExpiry', expiryDate.getTime());
        }
    });
}

