# simplefb
A simplefb is the simple facebook graph api library.

## Usage
### import module
    >>> import simplefb

### me function
    >>> simplefb.me('my-access-token')
A simplefb module provides function for facebook me api, and it simply requires access token only.

### fb_exchange_token function
    >>> simplefb.me('my-app-id', 'my-app-secret', 'my-short-lived-token')
To get a long-lived access token from facebook, you can use a fb_exchange_token function. It requires app-id, app-secret, and short-lived access token.


### api function
    >>> simplefb.api('/me', 'GET', {'access_token': 'my-access-token'})
You may also call api to the any of endpoints via "api" function.
It only supports api which returns JSON objects. Almost every facebook api returns response as the JSON object but some does not, for example, fb_exchange_token.

### specifying api version
    >>> simplefb.me('my-app-id', 'my-app-secret', 'my-short-lived-token', ver='v2.0')
    >>> simplefb.api('/me', 'GET', {'access_token': 'my-access-token'}, ver='v2.0')
You can specify api version by passing version string to the functions as the last argument. The default value is "v2.4".
