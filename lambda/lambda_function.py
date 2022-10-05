"""
Omar A Omar
This function returns a static page from a Lambda function
"""

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
        "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = """
    <html>
        <head>
            <title>Lambda URL</title>
            <style>
                html, body {
                background-color:rgb(22, 30, 43);
                margin: 10; padding: 10;
                # font-family: arial; font-weight: 10; font-size: 1em;
                # text-align: center;
                }
                html, h1 {
                color: white;
                text-align: center;
                font-family: verdana; font-weight: 10; font-size: 1em;
                font-size: 200%;
                }
                html, p {
                color: white;
                text-align: center;
                font-family: verdana; font-weight: 10; font-size: 3em;
                font-size: 120%;
                }
                .responsive {
                width: 100%;
                max-width: 600px;
                height: auto;
                }
            </style>
        </head>
        <body>

            <h1>Hello AWS Community Builders</h1>
            <p>I'm a static web page running on a Lambda function. Thank you CDK for Terraform for letting me do my moves.</p>
            <img src="https://acegif.com/wp-content/gifs/banana-82.gif" class="responsive" width="600" height="auto">
        </body>
    </html>
    """

    return response