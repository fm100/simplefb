# simplefb
A simplefb is the simple facebook graph api library.

## Usage
### import module
    >>> import simplefb

### me function
A simplefb module provides function for facebook me api, and it simply requires access token only.
    >>> simplefb.me('my-access-token')

### fb_exchange_token function
To get a long-lived access token from facebook, you can use a fb_exchange_token function. It requires app-id, app-secret, and short-lived access token.
    >>> simplefb.me('my-app-id', 'my-app-secret', 'my-short-lived-token')

### api function
You may also call api to the any of endpoints via "api" function.
    >>> simplefb.api('/me', 'GET', {'access_token': 'my-access-token'})
It only supports api which returns JSON objects. Almost every facebook api returns response as the JSON object but some does not, for example, fb_exchange_token.

### specifying api version
You can specify api version by passing version string to the functions as the last argument. The default value is "v2.4".
    >>> simplefb.me('my-app-id', 'my-app-secret', 'my-short-lived-token', ver='v2.0')
    >>> simplefb.api('/me', 'GET', {'access_token': 'my-access-token'}, ver='v2.0')
