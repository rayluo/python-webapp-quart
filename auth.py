import os

from identity.quart import Auth


# We initialize the auth helper as a global variable,
# so that your other modules or blueprints (if any) can import it and use it.
auth = Auth(
    # If your app object is globally available, you may pass it in here.
    # But if you are using Application Factory pattern
    # https://flask.palletsprojects.com/en/latest/patterns/appfactories/
    # your app is not available globally, so you need to pass None here,
    # and call auth.init_app(app) later, inside or after your app factory function.
    app=None,

    authority=os.getenv("AUTHORITY"),
    client_id=os.getenv("CLIENT_ID"),
    client_credential=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    oidc_authority=os.getenv("OIDC_AUTHORITY"),
    b2c_tenant_name=os.getenv('B2C_TENANT_NAME'),
    b2c_signup_signin_user_flow=os.getenv('SIGNUPSIGNIN_USER_FLOW'),
    b2c_edit_profile_user_flow=os.getenv('EDITPROFILE_USER_FLOW'),
    b2c_reset_password_user_flow=os.getenv('RESETPASSWORD_USER_FLOW'),
)
