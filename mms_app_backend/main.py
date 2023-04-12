# Import FastAPI and RedirectResponse classes
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Import the authentication router
from mms_app_backend.mms_app_backend.api.authentication.route import router as auth_router

# Instantiate the FastAPI application
app = FastAPI()

# Include the authentication router in the FastAPI app
app.include_router(auth_router)

# Create shortcuts for app.get and app.post decorators
get = app.get
post = app.post

# Define the root endpoint, which redirects to the API documentation
@get('/')
def homepage():
    """
    This is the API's home page.
    :return: A RedirectResponse to the API documentation
    """
    return RedirectResponse('/redoc')

# Run the Uvicorn server if this script is executed as the main module
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
