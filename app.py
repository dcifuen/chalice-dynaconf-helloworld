from chalice import Chalice
from dynaconf import settings

app = Chalice(app_name='chalice-dynaconf-helloworld')

settings.configure(ENVVAR_PREFIX_FOR_DYNACONF=False)


@app.route('/')
def index():
    return {'hello': settings.APP_NAME}
