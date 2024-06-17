import os
import httpx
from quart import Quart, render_template
from auth import auth


__version__ = "0.2.0"  # The version of this sample, for troubleshooting purpose

def create_app():
    app = Quart(__name__)
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_URI'] = 'redis://localhost:6379'  # Assuming your Redis server is here
        # In production, your web servers shall share one centralized session storage
    auth.init_app(app)

    ## You could also register a blueprint here
    #app.register_blueprint(my_module.bp)

    return app

app = create_app()

@app.route("/")
@auth.login_required
async def index(*, context):
    return await render_template(
        'index.html',
        user=context['user'],
        edit_profile_url=auth.get_edit_profile_url(),
        api_endpoint=os.getenv("ENDPOINT"),
        title=f"Quart Web App Sample v{__version__}",
    )

@app.route("/call_api")
@auth.login_required(scopes=os.getenv("SCOPE", "").split())
async def call_api(*, context):
    async with httpx.AsyncClient() as client:
        api_result = (await client.get(  # Use access token to call a web api
            os.getenv("ENDPOINT"),
            headers={'Authorization': 'Bearer ' + context['access_token']},
        )).json() if context.get('access_token') else "Did you forget to set the SCOPE environment variable?"
    return await render_template('display.html', title="API Response", result=api_result)

